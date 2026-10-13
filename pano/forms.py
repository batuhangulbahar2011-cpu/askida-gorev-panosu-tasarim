from django import forms
from django.contrib.auth import password_validation
from .models import Request, User

class StrictFields:
    def clean(self):
        data = super().clean()
        unknown = set(self.data) - set(self.fields) - {'csrfmiddlewaretoken'}
        if unknown:
            raise forms.ValidationError('Formda desteklenmeyen alanlar var. Kişisel ek veri göndermeyin.')
        return data

class RegisterForm(StrictFields, forms.Form):
    name = forms.CharField(label='Adınız', max_length=60)
    username = forms.RegexField(label='Kullanıcı adı', regex=r'^[a-zA-Z0-9_]{3,30}$', max_length=30, help_text='3–30 harf, rakam veya alt çizgi.')
    code = forms.CharField(label='Kayıt kodu', max_length=100)
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Parolayı tekrar yazın', widget=forms.PasswordInput)
    def clean_username(self):
        name = self.cleaned_data['username'].lower()
        if User.objects.filter(username=name).exists():
            raise forms.ValidationError('Bu kullanıcı adı kullanılıyor.')
        return name
    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirm'):
            self.add_error('password_confirm', 'Parolalar aynı olmalı.')
        if data.get('password'):
            user = User(username=data.get('username', ''), name=data.get('name', ''))
            password_validation.validate_password(data['password'], user)
        return data

class ResetForm(StrictFields, forms.Form):
    username = forms.CharField(label='Kullanıcı adı', max_length=30)
    code = forms.CharField(label='Parola yenileme kodu', max_length=100)
    password = forms.CharField(label='Yeni parola', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Yeni parola tekrar', widget=forms.PasswordInput)
    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirm'):
            self.add_error('password_confirm', 'Parolalar aynı olmalı.')
        if data.get('password'):
            user = User.objects.filter(username=data.get('username', '').lower()).first()
            password_validation.validate_password(data['password'], user)
        return data

class RequestForm(StrictFields, forms.ModelForm):
    version = forms.IntegerField(widget=forms.HiddenInput, required=False)
    date_reason = forms.CharField(label='Son tarih değişikliğinin nedeni', max_length=500, required=False)
    class Meta:
        model = Request
        fields = ['kind', 'title', 'description', 'team_purpose', 'due_date']
        widgets = {'description': forms.Textarea(attrs={'rows': 5}), 'due_date': forms.DateInput(attrs={'type': 'date'})}
    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        if not self.instance.pk and user.role == 'uye':
            self.fields['kind'].choices = [('talep', 'Yardım talebi')]
        if self.instance.pk:
            self.fields['kind'].disabled = True
            self.fields['version'].initial = self.instance.version
        else:
            self.fields.pop('date_reason')
        self.fields['team_purpose'].help_text = 'Görev yalnız takım işi içindir. Kişisel ihtiyacınız için Yardım talebi seçin.'
    def clean(self):
        data = super().clean()
        if data.get('kind') == 'gorev':
            if not self.instance.pk and self.user.role not in ['kaptan', 'danisman']:
                self.add_error('kind', 'Üyeler takım görevi açamaz.')
            if not data.get('team_purpose'):
                self.add_error('team_purpose', 'Takım için beklenen çıktıyı yazın.')
            if not data.get('due_date'):
                self.add_error('due_date', 'Takım görevinde son tarih zorunludur.')
        else:
            data['team_purpose'] = ''
        from django.utils import timezone
        if data.get('due_date') and data['due_date'] < timezone.localdate():
            self.add_error('due_date', 'Geçmiş bir tarih seçemezsiniz.')
        if self.instance.pk and data.get('due_date') != self.instance.due_date and not data.get('date_reason'):
            self.add_error('date_reason', 'Tarih değişikliğinin nedenini yazın.')
        return data

class ActionForm(StrictFields, forms.Form):
    version = forms.IntegerField(min_value=1, widget=forms.HiddenInput)
    action = forms.CharField(max_length=30, widget=forms.HiddenInput)
    target = forms.IntegerField(required=False, widget=forms.HiddenInput)
    note = forms.CharField(label='Not / gerekçe', max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}))
