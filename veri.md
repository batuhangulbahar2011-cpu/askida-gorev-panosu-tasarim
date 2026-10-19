# Veri modeli ve asgari veri

Bu model tek takım içindir. İleride çok takım gereksinimi çıkmadan okul, sınıf, konum veya çok takım tabloları eklenmez. Zamanlar UTC saklanır, İstanbul saatiyle gösterilir. Aşağıdaki her satır tek bir alanı tanımlar; yabancı anahtarlar mevcut kayda bağlanır.

## users — takım hesabı

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| id | 7 | İsim değişse de kişinin işlemlerini bağlamak |
| name | Derin | Takım içinde kişinin tanınması |
| username | derin | E-posta/telefon istemeden benzersiz giriş |
| password_hash | algoritma+tuz+özet | Parolayı açık metin saklamadan giriş doğrulamak |
| role | uye | Eylem izinlerini belirlemek; uye/kaptan/danisman |
| active | true | Ayrılan hesabı erişimden çıkarmak, geçmiş izi korumak |


Kullanıcı adı 3–30 karakter, harf/rakam/alt çizgi; ad 1–60 karakter. Aynı kullanıcı adı tekrar kullanılmaz. Tablodaki kimlikler sentetik örnektir; gerçek çalışma veritabanındaki hesap durumunu ifade etmez.

## requests — görev veya talep

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| id | 42 | İsteği ve bütün hareketlerini bağlamak |
| kind | gorev | Katkı ve yardımı ayrı akış/hesaplarda tutmak |
| title | Tanıtım videosu çekimi | Panoda ihtiyacı kısa anlatmak; 1–100 karakter |
| description | Üç dakikalık takım videosu hazırlanacak | Kapsamı ve beklenen sonucu açıklamak; 1–2000 karakter |
| team_purpose | Proje tanıtımında kullanılacak | Görevin takım amacı denetimi; görevde zorunlu, talepte boş |
| owner_id | 3 | Kabul, onay ve geri çekme yetkisini belirlemek |
| assignee_id | 8 veya boş | Tek aktif üstleneni göstermek |
| status | onay_bekliyor | Geçerli işlemleri belirlemek |
| due_date | 2026-10-15 veya boş | Son tarih/gecikme göstermek; görevde zorunlu |
| created_at | 2026-10-08T18:00:00Z | Açılış sırasını ve zamanı göstermek |
| version | 4 | Aynı anda gelen çelişkili değişiklikleri durdurmak |

Sonuç notu, onay saati, iptal nedeni, önceki üstlenenler ve ilk açan kişi olaylardan alınır; ikinci kopya alanlarda saklanmaz. Devredilen sahipliğin eski sahibi olay kaydında korunur.

## applications — adaylık

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| id | 19 | Adaylık kaydını tanımlamak |
| request_id | 42 | Hangi isteğe aday olduğunu bilmek |
| user_id | 8 | Talip olan veya yardım teklif eden kişi |
| note | Montaj kısmını yapabilirim | Açanın seçimini desteklemek; 0–300 karakter |
| state | bekliyor | Aktif/geri çekilmiş/seçilmiş adayları ayırmak |
| updated_at | 2026-10-08T18:05:00Z | Son başvurunun sırasını göstermek |

`request_id + user_id` benzersizdir. Eski not/hareket gerekli olduğunda yalnız yetkili kişiye events içindeki adaylık olayından okunur; tekrar adaylık yeni satır üretmez.

## comments — ortak yorumlar

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| id | 91 | Yorumu tanımlamak |
| request_id | 42 | Konuşmayı isteğin altında tutmak |
| author_id | 8 | Sözü kimin yazdığını göstermek |
| body | Videonun ilk kurgusu hazır | Ortak açıklama/koordinasyon; 1–1000 karakter |
| created_at | 2026-10-10T12:00:00Z | Konuşmayı sıraya koymak |

Aktif takım herkesin yorumunu görür. Özel mesaj, dosya/fotoğraf eki veya yorum alıcıları alanı yoktur. Kişisel veri yazılmaması formda hatırlatılır; ihlal danışmana bildirilir. Gerekirse danışman yorumu kişisel veriden arındırıp nedenini olay kaydına yazar; özgün hassas metin olay/lojlarda yeniden saklanmaz. Sıradan yazım düzeltmesi yeni yorumla yapılır.

## events — kim, ne, ne zaman

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| id | 114 | Hareketleri benzersiz ve sıralı tutmak |
| request_id | 42 veya boş | İstek hareketini bağlamak; rol değişikliğinde boş |
| subject_user_id | 8 veya boş | Adaylık/rol/üyelik gibi hareketin hedefini bağlamak |
| actor_id | 3 veya boş | İşlemi yapanı göstermek; otomatik saklama işleminde boş |
| action | onaylandi | Açıldı/adaylık/kabul/bırakma/onay/iptal/devir/rol değişimini ayırmak |
| note | Video takım sunumuna uygun | Sonuç, seçim, düzeltme veya istisna gerekçesi; 0–1000 karakter |
| created_at | 2026-10-11T08:00:00Z | Olay sırası ve süre hesabı |

Olaylar değiştirilemez; hata için yeni gerekçeli düzeltme olayı yazılır. Başvuru ve rol değişimi notunda gerekli önceki/yeni değerler bulunur, serbest teknik veri dump'ı bulunmaz. İstek onaylandığında hedef kişi `subject_user_id` ile üstlenen olarak kaydedilir. Onay tek terminal geçiştir; her istek en fazla bir onay olayı üretir.

## flags — danışmana işlem bildirimi

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| id | 6 | Bildirimi tanımlamak |
| request_id | 42 | İncelenecek isteği bağlamak |
| reporter_id | 7 | Danışmanın gerekçe kaynağını bilmesi |
| reason | Bu iş takım projesiyle ilişkili görünmüyor | Uygunsuz görev/uyuşmazlık gerekçesi; 1–500 karakter |
| state | acik | İncelenmemiş veya çözülmüş bildirimi ayırmak |
| created_at | 2026-10-08T19:00:00Z | Kuyruk sırası |

Karar ve karar veren events üzerinden okunur. Aynı kişi aynı istek için bir açık bildirim bırakabilir. Bildirim metni/kimliği danışmana görünür; gönderen kendi bildirimini ve durumunu da görür. Diğer üyeler görmez. Karar gerekçesi ortak olay akışına görünür. Danışman kendi üstlendiği talebin uyuşmazlığını kendi lehine kapatamaz.

## sessions — girişin teknik verisi

| Alan | Örnek | Neden tutulur? |
|---|---|---|
| key | rastgele oturum anahtarı | İsteklerde giriş yapan hesabı tanımak |
| user_id | 7 | Oturumu hesaba bağlamak |
| expires_at | girişten 12 saat sonra | Unutulmuş oturumları sonlandırmak |

Teknoloji bu tabloyu sağlayabilir; ayrıca paralel token sistemi kurulmaz. Çerezde yalnız rastgele anahtar bulunur. Açık parola, ham oturum anahtarı uygulama loguna yazılmaz. Parola değişiminde ve pasifleştirmede oturumlar iptal edilir. Aktif oturum süresi 12 saat önerisidir.

## Görünümler, saklama ve tutulmayacaklar

İlave teknik alanlar aşağıdadır; bunlar faaliyet veya kişi performansı değildir.

| Kayıt / alan | Örnek | Neden tutulur? |
|---|---|---|
| settings.period_closed_at | 2027-06-30T21:00:00Z veya boş | Dönemin kapanışını ve temizleme başlangıcını belirlemek |
| settings.purge_after | Kapanıştan 90 gün sonrası veya boş | Veriyi belirsiz süre saklamadan planlı silmek |
| error_log.code | DATABASE_BUSY | Kişisel veri taşımadan arıza türünü ayırmak |
| error_log.created_at | 2026-10-08T18:00:00Z | Arızanın ne zaman gerçekleştiğini belirlemek; 7 gün sonra silinir |

Hata kaydında bu iki alan dışında kullanıcı adı, IP, cihaz, gövde veya serbest açıklama bulunmaz. Ayarlar tek satırdır; birden fazla dönem modeli değildir.

- **Takım nabzı:** İstanbul saatine göre pazartesi 00:00'dan sonraki onay olayları; görev ve talep ayrı sayılır. İptal/bırakma/adaylık tamamlanma değildir.
- **Danışman kişi özeti:** aynı tarih aralığında adaylık, kabul, onaylanmış görev katkısı ve onaylanmış yardım ayrı sütunlar; isim alfabetik sıralıdır. Puan veya sıralama yoktur. Aynı istek için tekrar aday olan kişi aralıkta bir kez sayılır. Ham istekler herkesçe görülebilir; kişiler için toplu sayaç/filtre/rapor yalnız danışmana sunulur.
- Sayaçlar veriden hesaplanır; `puan`, `thanks`, `kredi`, `rozet`, `sıra` veya kalıcı performans tablosu tutulmaz.
- Batu'nun 2026-10-09 tarihinde kabul ettiği saklama politikası: dönem devam ederken kayıtlar kalır; danışman dönemin kapandığını kaydeder ve 90 gün sonra dönem istekleri, yorumları, adaylıkları, olayları ve bildirimleri silinir. `period_closed_at` ve `purge_after` adlı iki tekil yapılandırma zamanı bu takvim için tutulur; örnek `2027-06-30T21:00:00Z` ve bunun 90 gün sonrası. 90 günlük süre görev tamamlanınca değil, dönem kapatılınca başlar. Dönem kayıtlarının silinmesi aktif kullanıcı hesaplarını silmez. Açık istek varsa dönem kapatılamaz. Yeni döneme geçmeden eski dönem temizlenir; çok dönem özelliği pilotta yoktur.
- Ayrılan kişinin hesabı geçmiş işler bağlıyken pasif kalır; saklama süresi bitince referansı kalmayan pasif hesap silinir. Yedekler en çok 7 günlük döngüde tutulur; silinen veri en geç 7 gün sonra yedekten de çıkar. Yedek açılırsa aynı silme takvimi tekrar uygulanır.
- Telefon, adres, doğum tarihi, fotoğraf/avatar, konum, okul/sınıf, beceri profili, cihaz kimliği, reklam/analitik takibi ve kişi performans dışa aktarımı tutulmaz. E-posta istemeyen hesap modeli kullanılır. GitHub tasarım reposunda gerçek kullanıcı hesabı, parola, çalışma DB'si veya gerçek takım faaliyet kaydı bulunmaz.
- Altyapı erişim loglarında IP/cihaz takibi kapatılır; hata logları kimlik/parola/yorum gövdesi içermeyen teknik hata kodlarıyla, 7 gün süreyle tutulur. Bunlar pilotun ilave teknik saklama alanlarıdır; yalnız arıza bulmak içindir.

## Kodla kayıt, parola yenileme ve site içi bildirimler

| Kayıt | Asgari alanlar | Amaç / erişim |
|---|---|---|
| registration_codes | id, code_hash, created_by, created_at, expires_at, used_at, revoked_at | Tek kayıt; 7 gün; kullanılmadan iptal. Yönetimi yalnız danışman. Ham kod kalıcı saklanmaz/loglanmaz. |
| password_reset_codes | id, code_hash, user_id, created_by, created_at, expires_at, used_at | Yalnız hedef hesap için tek kullanım, 24 saat. Üye için danışman; ilk danışman için kimlik kontrolü sonrası Batu bakım erişimi. |
| notifications | id, recipient_id, request_id, kind, created_at, read_at | Yalnız alıcının bildirimleri; ilgili isteğe bağlantı. Seçim bildirimi başka adayın notunu taşımaz. |

Parola tekrarı veritabanına yazılmaz; yalnız formda eşleşme kontrolüdür. Kod tüketimi ve hesap/parola işlemi tek veritabanı işleminde gerçekleşir. Kullanılmış/süresi dolmuş/iptal edilmiş kod işlem yapamaz.

Adaylık satırı, notu ve olay geçmişi istek sahibi/ilgili aday için görünür; danışman bildirilen sorunu inceleyebilir. Ortak istek geçmişine tüm adaylık kayıtları gönderilmez. Parola yenileme/kayıt kodu alanları ortak yorum veya istek olayına yazılmaz. Dönem temizliği ilgili site içi bildirimleri de kapsar. Süresi dolan teknik kodlar temizlenir; şifre/oturum yenileme verileri arşiv veya Git deposuna konmaz.


## Kod ve bildirim alanlarının tek tek gerekçeleri — 19 Ekim

Üstteki toplu alan listesi aşağıda açılmıştır. Yeni kişisel veri veya ürün özelliği eklenmez. Ana sitede kayıt ve parola yenileme kodları ayrı tablo yerine aynı `Code` modelinde `kind` ile ayrılır.

| Uygulama alanı | Neden tutulur? / sınır |
|---|---|
| codes.id | Kodu ham değeriyle göstermeden iptal/temizlik işleminde tanımlamak. |
| codes.code_hash | Girilen kodu doğrulamak; ham kodu kalıcı saklamamak. |
| codes.kind | Kayıt kodunun parola yenilemek veya yenileme kodunun kayıt olmak için kullanılmasını önlemek. |
| codes.user_id | Parola yenilemesini yalnız hedef hesaba bağlamak; kayıt kodunda boştur. |
| codes.created_by_id | Kodu hangi yetkili hesabın ürettiğini izlemek; ilk danışmanın bakım kurtarmasında boş olabilir. |
| codes.created_at | Üretim zamanını ve teknik saklama süresini belirlemek. |
| codes.expires_at | Kayıt için 7 gün, parola yenileme için 24 saat sonrasını doğrulamak. |
| codes.used_at | Tek kullanımın tüketildiğini ve ne zaman olduğunu bilmek; aynı kodu tekrar reddetmek. |
| codes.revoked_at | Kullanılmadan iptal edilmiş kodu reddetmek; ortak Code modelinde iki kod türünde de alan vardır. |
| notifications.id | Alıcının belirli bir bildirimi açıp okundu işaretleyebilmesi. |
| notifications.recipient_id | Bildirimi yalnız doğru kişiye göstermek; başkasının bildirimine erişimi engellemek. |
| notifications.request_id | Bildirimi ilgili isteğin detayına bağlamak; dönem silinince bağlı bildirimi de temizlemek. |
| notifications.kind | Teklif, kabul, seçilmeme, sonuç veya düzeltme metnini belirlemek; serbest gizli teklif notu taşımamak. |
| notifications.created_at | Bildirimleri zamana göre sıralamak. |
| notifications.read_at | Okunmamış sayısını ve okundu durumunu belirlemek; kişi performansı ölçütü değildir. |

## Ana site — Django teknik alanları (13 Ekim)

Gerçek uygulamada tasarımdaki `users.name/role/active` Django özel kullanıcı modelindeki `name/role/is_active` alanlarıdır; parola özeti `password` alanında tutulur. İstek/adaylık/not alanları yukarıdaki modelle eşleşir. E-posta, first_name/last_name alanları kaldırılmıştır; yalnız ad istenir. Django'nun AbstractUser altyapısı aşağıdaki teknik alanları da sağlar; ürün rolü her zaman `role` alanından denetlenir, personel bayrağı site rolünü değiştirmez.

| Teknik alan | Neden / sınır |
|---|---|
| users.last_login | Django'nun başarılı girişin zamanını kaydetmesi; IP/cihaz içermez, kişi özeti ölçütü değildir. |
| users.date_joined | Hesabın açılış zamanını korumak; faaliyet/puan sayımı değildir. |
| users.is_staff, is_superuser | Django'nun standart teknik yetki bayrakları; web kayıt akışında kapalıdır. Ürün rolü bunlardan alınmaz; Django admin paneli açılmamıştır. |
| users.groups, user_permissions | Django standart izin ilişkileri; bu pilotta boş tutulur, ürün izinleri rol ve sahiplikten hesaplanır. |
| login_attempts.key | Kullanıcı adı özetine göre kısa süreli giriş denemelerini sınırlamak; kullanıcı adının kendisi veya IP tutulmaz. |
| login_attempts.count | 15 dakika içinde sekiz başarısız denemeden sonra bekletmek. |
| login_attempts.expires_at | Sayaç geçerliliği; süre dolunca tekrar girişe izin verilir, teknik_temizle komutu eski kayıtları siler. |

Django session tablosu `session_key/session_data/expire_date` adlarını kullanır: hesap kimliği ve oturum doğrulama bilgisi giriş için gereklidir. Cookie'de oturum anahtarı vardır; parola açık saklanmaz. Oturum ömrü 12 saattir, parola değişimi eski oturumun doğrulamasını geçersizleştirir. Framework tablo/alan adları bağımsız bir token sistemi eklemez.

Otomatik saklama/yedek işçisi bu yerel ilk sürümde kurulmadı. 90 günlük dönem temizliği ve teknik kayıt temizliği için ANA-SITE.md bakım komutları işletilir; yayın kurulurken çalıştırma takvimi ve sağlayıcı kayıtları ayrıca yapılandırılır. Gerçek çalışma DB'si ve yerel gizli anahtar repoya alınmaz.

## Tarayıcı tema tercihi — 18 Ekim

Tarayıcı localStorage içinde askida-theme anahtarı yalnız light veya dark değerini tutar; hesabı, parolayı veya faaliyet bilgisini içermez, sunucuya gönderilmez. Amaç aynı tarayıcıda yenileme ve sayfa değişiminde tema seçimini korumaktır. Kullanıcı tarayıcı site verilerini temizleyince varsayılan açık temaya dönülür. Depolamaya izin yoksa düğme yine çalışır, seçim yeniden açılışta saklanmaz. Shader için fare/cihaz kimliği veya takip verisi toplanmaz.
