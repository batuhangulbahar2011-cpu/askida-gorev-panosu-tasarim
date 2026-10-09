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
| must_change_password | true | Danışmanın verdiği geçici parolayı ilk girişte değiştirmek |

Kullanıcı adı 3–30 karakter, harf/rakam/alt çizgi; ad 1–60 karakter. Aynı kullanıcı adı tekrar kullanılmaz. Kimlikler sentetik örnektir, gerçek hesap kurulmamıştır.

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

`request_id + user_id` benzersizdir. Eski not/hareket gerekli olduğunda events içindeki adaylık olayından okunur; tekrar adaylık yeni satır üretmez.

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

Karar ve karar veren events üzerinden okunur. Aynı kişi aynı istek için bir açık bildirim bırakabilir. Bildirim metni/kimliği yalnız danışmana; karar gerekçesi ortak olay akışına görünür. Danışman kendi üstlendiği talebin uyuşmazlığını kendi lehine kapatamaz.

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
