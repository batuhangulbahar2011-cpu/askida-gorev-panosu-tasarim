from datetime import timedelta
from django.core.exceptions import PermissionDenied
from django.core.management import call_command
from django.db import transaction
from django.test import Client, TestCase
from django.utils import timezone
from .models import Application, Code, Event, Flag, Notification, Period, Request, User
from .services import Conflict, RuleError, act, change_member, close_period, consume_code, issue_code

class PanoTests(TestCase):
    def setUp(self):
        self.advisor = User.objects.create_user('ozgur', 'Secure-Sample-936!', name='Özgür', role='danisman')
        self.owner = User.objects.create_user('arda', 'Secure-Sample-936!', name='Arda', role='kaptan')
        self.a = User.objects.create_user('hakki', 'Secure-Sample-936!', name='Hakkı')
        self.b = User.objects.create_user('eren', 'Secure-Sample-936!', name='Eren')
        self.other = User.objects.create_user('batu', 'Secure-Sample-936!', name='Batu')
        self.item = Request.objects.create(kind='gorev', title='Takım videosu', description='Üç dakikalık video', team_purpose='Takım sunumu', owner=self.owner, due_date=timezone.localdate() + timedelta(days=2))
    def do(self, who, action, note='', target=None, item=None):
        item = item or self.item
        item.refresh_from_db()
        return act(who, item.pk, item.version, action, note, target)
    def accept(self):
        self.do(self.a, 'apply', 'Videoyu düzenlerim.')
        self.do(self.b, 'apply', 'Çekim yaparım.')
        row = Application.objects.get(request=self.item, user=self.a)
        return self.do(self.owner, 'accept', 'Montaj ihtiyacı için uygun.', row.pk)
    def test_member_cannot_open_task(self):
        self.client.force_login(self.a)
        response = self.client.post('/istek/yeni/', {'kind': 'gorev', 'title': 'Kişisel iş', 'description': 'test', 'team_purpose': 'test', 'due_date': timezone.localdate()})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Request.objects.count(), 1)
    def test_task_needs_purpose_and_date(self):
        self.client.force_login(self.owner)
        response = self.client.post('/istek/yeni/', {'kind': 'gorev', 'title': 'Video', 'description': 'Yeni video'})
        self.assertContains(response, 'zorunludur')
        self.assertEqual(Request.objects.count(), 1)
    def test_help_without_due_date(self):
        self.client.force_login(self.a)
        self.client.post('/istek/yeni/', {'kind': 'talep', 'title': 'Servo', 'description': 'Yardım', 'team_purpose': 'ignore'})
        item = Request.objects.get(title='Servo')
        self.assertEqual(item.team_purpose, '')
        self.assertIsNone(item.due_date)
    def test_owner_cannot_apply(self):
        with self.assertRaises(PermissionDenied):
            self.do(self.owner, 'apply')
    def test_advisor_cannot_apply_to_task(self):
        with self.assertRaises(PermissionDenied):
            self.do(self.advisor, 'apply')
    def test_two_candidates_single_assignee_and_private_notice(self):
        self.accept()
        self.item.refresh_from_db()
        self.assertEqual(self.item.assignee, self.a)
        self.assertEqual(Application.objects.get(request=self.item, user=self.b).state, 'secilmedi')
        self.assertTrue(Notification.objects.filter(recipient=self.b, kind='secilmedi').exists())
        self.assertEqual(Event.objects.filter(request=self.item, action='ustlenildi').count(), 1)
    def test_stale_double_accept_rolls_back(self):
        self.do(self.a, 'apply')
        self.do(self.b, 'apply')
        self.item.refresh_from_db()
        version = self.item.version
        act(self.owner, self.item.pk, version, 'accept', 'Uygun.', Application.objects.get(user=self.a).pk)
        with self.assertRaises(Conflict):
            act(self.owner, self.item.pk, version, 'accept', 'Diğeri.', Application.objects.get(user=self.b).pk)
        self.assertEqual(Event.objects.filter(action='ustlenildi').count(), 1)
    def test_wrong_owner_cannot_accept(self):
        self.do(self.a, 'apply')
        with self.assertRaises(PermissionDenied):
            self.do(self.other, 'accept', 'test', Application.objects.get(user=self.a).pk)
    def test_correction_retains_assignee(self):
        self.accept()
        self.do(self.a, 'done', 'İlk video hazır.')
        self.do(self.owner, 'correct', 'Ses eksik.')
        self.item.refresh_from_db()
        self.assertEqual(self.item.status, 'ustlenildi')
        self.assertEqual(self.item.assignee, self.a)
        self.assertIsNone(self.item.waiting_since)
    def test_approval_only_once(self):
        self.accept()
        self.do(self.a, 'done', 'Bitti.')
        self.do(self.owner, 'approve')
        with self.assertRaises(PermissionDenied):
            self.do(self.owner, 'approve')
        self.assertEqual(Event.objects.filter(action='onaylandi').count(), 1)
    def test_leave_reopens_without_auto_assignment(self):
        self.accept()
        self.do(self.a, 'leave', 'İki gün sonra yapamıyorum; kurgu yarıda.')
        self.item.refresh_from_db()
        self.assertEqual(self.item.status, 'acik')
        self.assertIsNone(self.item.assignee)
        self.assertFalse(Application.objects.filter(state='bekliyor').exists())
        self.do(self.b, 'apply', 'Devam edebilirim.')
        self.assertEqual(Application.objects.filter(user=self.b).count(), 1)
    def test_cancel_not_completion(self):
        self.accept()
        self.do(self.owner, 'cancel', 'Takımın ihtiyacı değişti.')
        self.assertFalse(Event.objects.filter(action='onaylandi').exists())
    def test_offer_note_and_identity_not_leaked(self):
        self.accept()
        self.client.force_login(self.other)
        html = self.client.get(f'/istek/{self.item.pk}/').content.decode()
        self.assertNotIn('Çekim yaparım.', html)
        self.assertNotIn('Eren', html)
        self.assertNotIn('Montaj ihtiyacı için uygun.', html)
        self.client.force_login(self.b)
        html = self.client.get(f'/istek/{self.item.pk}/').content.decode()
        self.assertIn('Çekim yaparım.', html)
        self.assertNotIn('Videoyu düzenlerim.', html)
    def test_advisor_offer_access_requires_report(self):
        self.do(self.a, 'apply', 'Gizli teklif.')
        self.client.force_login(self.advisor)
        self.assertNotContains(self.client.get(f'/istek/{self.item.pk}/'), 'Gizli teklif.')
        self.do(self.other, 'flag', 'İnceleme ihtiyacı.')
        self.assertContains(self.client.get(f'/istek/{self.item.pk}/'), 'Gizli teklif.')
    def test_48_hours_no_auto_approval(self):
        self.accept()
        self.do(self.a, 'done', 'Bitti.')
        Event.objects.filter(action='yapildi').update(created_at=timezone.now() - timedelta(hours=49))
        self.item.refresh_from_db()
        self.assertTrue(self.item.needs_review)
        self.assertEqual(self.item.status, 'onay_bekliyor')
        self.do(self.advisor, 'advisor_approve', 'Ortak yorum ve sonucu inceledim.')
        self.assertEqual(Event.objects.filter(action='onaylandi').count(), 1)
    def test_advisor_cannot_arbitrate_own_work(self):
        help_item = Request.objects.create(kind='talep', title='Yardım', description='test', owner=self.a)
        self.do(self.advisor, 'apply', item=help_item)
        row = Application.objects.get(request=help_item)
        self.do(self.a, 'accept', 'Uygun.', row.pk, help_item)
        self.do(self.advisor, 'done', 'Bitti.', item=help_item)
        Flag.objects.create(request=help_item, reporter=self.a, reason='İnceleyin')
        with self.assertRaises(PermissionDenied):
            self.do(self.advisor, 'advisor_approve', 'Ben yaptım.', item=help_item)
    def test_invite_single_use_and_forced_member(self):
        raw, code = issue_code(self.advisor)
        data = {'name': 'Yeni', 'username': 'yeni', 'code': raw, 'password': 'New-Safe-Password-735!', 'password_confirm': 'New-Safe-Password-735!'}
        self.client.post('/kayit/', data)
        self.assertEqual(User.objects.get(username='yeni').role, 'uye')
        data.update(username='ikinci', name='İkinci')
        Client().post('/kayit/', data)
        self.assertFalse(User.objects.filter(username='ikinci').exists())
    def test_expired_revoked_code_rejected(self):
        raw, code = issue_code(self.advisor)
        Code.objects.filter(pk=code.pk).update(expires_at=timezone.now() - timedelta(seconds=1))
        with self.assertRaises(RuleError), transaction.atomic():
            consume_code(raw, 'registration')
        raw, code = issue_code(self.advisor)
        Code.objects.filter(pk=code.pk).update(revoked_at=timezone.now())
        with self.assertRaises(RuleError), transaction.atomic():
            consume_code(raw, 'registration')
    def test_reset_target_only_and_password_hash(self):
        raw, _ = issue_code(self.advisor, self.a)
        with self.assertRaises(RuleError), transaction.atomic():
            consume_code(raw, 'reset', self.b)
        data = {'username': 'hakki', 'code': raw, 'password': 'New-Safe-Password-987!', 'password_confirm': 'New-Safe-Password-987!'}
        self.client.post('/parola-yenile/', data)
        self.a.refresh_from_db()
        self.assertTrue(self.a.check_password(data['password']))
        self.assertNotEqual(self.a.password, data['password'])
    def test_notification_belongs_to_recipient(self):
        self.accept()
        notice = Notification.objects.filter(recipient=self.b).first()
        self.client.force_login(self.a)
        self.assertEqual(self.client.post(f'/bildirim/{notice.pk}/oku/').status_code, 404)
        self.assertNotContains(self.client.get('/bildirimler/'), 'başka bir isteğe')
    def test_team_and_summary_forbidden_for_member(self):
        self.client.force_login(self.a)
        self.assertEqual(self.client.get('/takim/').status_code, 403)
        self.assertEqual(self.client.get('/danisman/').status_code, 403)
    def test_role_change_applies_to_open_session(self):
        self.client.force_login(self.owner)
        change_member(self.advisor, self.owner, 'uye', True)
        self.client.post('/istek/yeni/', {'kind': 'gorev', 'title': 'Yetkisiz', 'description': 'test', 'team_purpose': 'test', 'due_date': timezone.localdate()})
        self.assertFalse(Request.objects.filter(title='Yetkisiz').exists())
        self.accept()
        self.do(self.a, 'done', 'Bitti.')
        self.do(self.owner, 'approve')
    def test_last_advisor_protected(self):
        with self.assertRaises(RuleError):
            change_member(self.advisor, self.advisor, 'uye', True)
    def test_deactivation_reopens_and_transfers(self):
        self.accept()
        change_member(self.advisor, self.a, 'uye', False)
        self.item.refresh_from_db()
        self.assertEqual(self.item.status, 'acik')
        self.assertIsNone(self.item.assignee)
        change_member(self.advisor, self.owner, 'kaptan', False)
        self.item.refresh_from_db()
        self.assertEqual(self.item.owner, self.advisor)
    def test_csrf_and_logout_post_only(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.owner)
        self.assertEqual(client.post(f'/istek/{self.item.pk}/islem/', {'action': 'cancel', 'version': 1, 'note': 'test'}).status_code, 403)
        self.assertEqual(client.get('/cikis/').status_code, 405)
    def test_xss_is_escaped(self):
        self.do(self.a, 'comment', '<script>alert(1)</script>')
        self.client.force_login(self.b)
        response = self.client.get(f'/istek/{self.item.pk}/')
        self.assertContains(response, '&lt;script&gt;')
        self.assertNotContains(response, '<script>alert(1)</script>')
    def test_period_close_and_purge(self):
        with self.assertRaises(RuleError):
            close_period(self.advisor)
        self.do(self.owner, 'cancel', 'Bitti değil iptal.')
        close_period(self.advisor)
        with self.assertRaises(RuleError):
            self.do(self.a, 'comment', 'Yeni yorum')
        period = Period.objects.get(pk=1)
        Period.objects.filter(pk=1).update(purge_after=timezone.now() - timedelta(seconds=1))
        call_command('donem_temizle', uygula=True, verbosity=0)
        self.assertEqual(Request.objects.count(), 0)
        self.assertEqual(User.objects.filter(is_active=True).count(), 5)
    def test_all_pages_render_for_advisor(self):
        self.client.force_login(self.advisor)
        for url in ['/', '/arsiv/', '/bildirimler/', '/danisman/', '/takim/', '/istek/yeni/', f'/istek/{self.item.pk}/']:
            self.assertEqual(self.client.get(url).status_code, 200, url)
    def test_unknown_personal_fields_rejected(self):
        self.client.force_login(self.owner)
        self.client.post('/istek/yeni/', {'kind': 'talep', 'title': 'Ek veri', 'description': 'test', 'phone': '123'})
        self.assertFalse(Request.objects.filter(title='Ek veri').exists())
    def test_role_injection_registration_rejected(self):
        raw, _ = issue_code(self.advisor)
        data = {'name': 'Yetki', 'username': 'yetki', 'code': raw, 'password': 'New-Safe-Password-735!', 'password_confirm': 'New-Safe-Password-735!', 'role': 'danisman'}
        self.client.post('/kayit/', data)
        self.assertFalse(User.objects.filter(username='yetki').exists())
