# Askıda Görev Panosu — 19 Ekim sunum çalışması

Bu belge AI destekli **çalışma taslağıdır**. Batu'nun Django, aday seçimi ve sonuç onayı açıklamaları alındı; gerçek prova sonucu henüz alınmadı; bugünün sunum işi tamamlandı sayılmaz. Teslim 22 Ekim 2026; gerçek sunum günü ayrıca doğrulanacak. Hazırlık takvimi 19–21 Ekim'dir.

## Bugüne kadar nerede kaldık?

| İş | 19 Ekim durumu |
|---|---|
| Sekiz zorunlu tasarım belgesi ve Django ana site | Mevcut; 19 Ekim belgeler ve teknik akışlar tekrar kontrol edildi. |
| Son teknik doğrulama | 19 Ekim: 40 Django testi, 43 Chrome akış kontrolü ve tema/menü için 12 ek kontrol geçti; gerçek kullanıcı/telefon denemesi değildir. |
| Beş dakikalık anlatım akışı ve soru kartları | Bu belgede hazır taslak. Batu kendi sözleriyle düzenleyecek. |
| Batu'nun teknoloji/seçim/onay gerekçeleri | Üç kısa açıklama da 19 Ekim alındı; aşağıda kullanıcı yanıtları olarak kayıtlı. 12 Ekim beyanı teknoloji.md'de korunur. |
| İlk süreli prova | Yapılmadı / süre bildirilmedi. Aşağıya gerçek sonuç yazılacak. |
| Selim/Arda ihtiyaç denemesi | Batu 19 Ekim henüz yapmadığını söyledi; bekliyor. |
| Kaptanın göreve adaylığı için öğretmen yanıtı | Batu 19 Ekim henüz görüşmediğini bildirdi; pilot önerisi kesin öğretmen kararı değildir. |
| Fiziksel telefonda son sürüm | Gerçek cihaz denemesi ayrıca bekliyor. |
| İnternet yayını | Yapılmadı. Batu VDS veya hosting düşünüyor; sağlayıcı/paket seçilmedi. |

## Beş dakikalık konuşma kartları

Metni ezberlemek yerine her bölümün ana fikrini kendi cümlelerinle anlat. Süreler hedeftir; ölçülmüş konuşma süresi değildir.

### 0:00–0:45 — Sorun ve çözüm

- Takımda kimin hangi işi yaptığı, bir ihtiyacın karşılanıp karşılanmadığı ve sonucun kabul edilip edilmediği aynı yerde izlenebilsin.
- Takımın ihtiyacı **Görev**, kişinin yardım ihtiyacı **Yardım talebi** olarak ayrı tutulur.
- Telefon ve bilgisayardan kullanılan tek web panosu vardır. Örnek: takım tanıtım videosu bir görev; servo motor bağlantısı konusunda destek bir yardım talebidir.

### 0:45–1:45 — İki aday, bir üstlenen, sonuç onayı

- Arda kaptan olarak takım videosu görevini, takım amacı ve son tarihle açar.
- Hakkı ve Eren aday olur; ilk tıklayan otomatik üstlenmez. Arda adayları değerlendirip Hakkı'yı seçer.
- Arda bütün adaylıkları, adaylar yalnız kendi teklifini görür. Eren'e nazik bir seçilmeme bildirimi gider. Diğer üyeler seçilen kişiyi ve işin durumunu görür.
- Hakkı sonucu yazıp “Yapıldı” bildirir. Arda onaylarsa arşive geçer; eksikse gerekçeli düzeltme ister.
- **Batu’nun açıklaması:** Açan kişi uygun adayı seçebilsin. İş yarım kalmış veya yanlışlıkla bitti denmiş olabilir; isteyen kişi de sonucu kontrol edip onaylasın.

### 1:45–2:45 — Üç ekranı göster

- **Pano:** Görevler/Yardım Talepleri ayrımı, durum ve kendi işlerim filtreleri; ayrı takım toplamları.
- **Detay:** Takım amacı, seçilen kişi, ortak yorumlar, sonuç notu ve yetkiye bağlı işlemler.
- **Danışman özeti:** Kişi bazlı katkı ve yardım ayrı sütunlarda; yalnız danışman erişebilir. Herkese açık kişi sıralaması yoktur.
- Sunumda veri değiştirmek gerekmiyorsa bu üç ekranı gezmek yeterlidir. Hazır örnek senaryo için aşağıdaki demo yolunu kullan.

### 2:45–3:45 — Kurallar ve veri

- Kaptanın kişisel işi takım görevi sayılmaz; takım amacı ve danışmana bildirim yolu vardır.
- Görev ve yardım sayımları ayrıdır; sıralama, puan, kredi ve rozet yoktur.
- Yorumlar takımın ortak alanıdır; özel sohbet yoktur. Teklif notunun sınırlı görünürlüğü özel mesajlaşma değildir.
- Hesap ve işi izlemek için gereken bilgiler tutulur; fotoğraf, telefon, adres istenmez. Parola açık metin tutulmaz.
- Dönem kayıtlarının 90 günlük süresi tek tek görevlerden değil, danışmanın dönemi kapatmasından başlar; aktif hesaplar korunur.

### 3:45–5:00 — Teknoloji, istisnalar ve sınırlar

- İki seçenek karşılaştırıldı: Django + SQLite web uygulaması veya eski Python API/web panelini uyarlama. Güncel seçim Django'dur; ayrıntı teknoloji.md'de.
- **Batu'nun 19 Ekim kendi açıklaması (yazım düzeltilmiş):** “Django daha kullanışlı olduğu için.” Hangi özelliğini kullanışlı bulduğunu bir örnekle açıklama çalışması sürüyor.
- Giriş altyapısı hazır olsa da kimin hangi isteği seçip onaylayabileceği ayrıca uygulanır.
- Yapıldı bildirimi 48 saat onaysız kalırsa danışman inceler; otomatik onay olmaz. İşi bırakan gerekçe ve devam notu bırakır, istek yeniden açılır.
- Yerel gerçek hesaplı site ile örnek demo ayrıdır. Site henüz internette yayımlanmadı. Yayın VDS/hosting seçimiyle ilerleyecek; bakım Batu'dadır.
- AI desteği kullanıldı; kararları kendi sözlerinle açıklaman ve savunman gerekir. Öğretmen ve kullanıcı görüşmelerini gerçekleşmiş gibi anlatma.

## Veri değiştirmeden örnek gösterim

Proje klasöründeki **index.html** üç ekranlık örnek demodur. Gerçek hesaplı site için **baslat.bat** kullanılır. Demo gerçek oturum/izin güvenliğini veya ortak veritabanını kanıtlamaz.

1. Demoda Arda'yı seç; tanıtım videosu görevini aç veya mevcut örneği incele.
2. Hakkı/Eren tekliflerini ve Arda'nın birini seçmesini göster.
3. Eren'e geç; yalnız kendi teklifini ve seçilmeme bilgisini göster.
4. Hakkı olarak Yapıldı, Arda olarak onay/düzeltme akışını göster.
5. Gerçek sitenin pano/detay/danışman özeti görünümünü yetkili mevcut hesapla gez. Gerçek kaydı sırf prova için kapatma; hesapları sıfırlama.

Bu adımlar **prova önerisidir**; bugün uygulanmış deneme kaydı değildir. Örnek demoda sıfırlama yalnız tarayıcıdaki demo verisini etkiler.

## Soru kartları

| Soru | Yanıtı kurarken hatırlanacak nokta |
|---|---|
| Görev ile yardım talebi niye ayrı? | Takım ihtiyacı ve kişisel yardımın amacı/sayımı farklı. Somut bir örnek ver. |
| Neden ilk aday doğrudan üstlenmiyor? | İstek sahibinin uygun kişiyi seçmesi; adaylık ve üstlenme ayrı işlemler. Kendi nedenini anlat. |
| Seçilmeyen kişi ne görüyor? | Kendi teklifini, nazik bildirimi ve seçilen kişiyi; başkasının teklifini değil. |
| Sonuç yetersizse? | Açan kişi gerekçeli düzeltme ister; aynı üstlenen devam eder. |
| Onay unutulursa veya iş bırakılırsa? | 48 saat danışman incelemesi; bırakmada gerekçeli yeniden açılma. |
| Herkes kişi toplamlarını görebilir mi? | Hayır; kişi özeti danışmana, ayrı takım toplamları herkese. |
| Yanlış takım amacı yazılmasını sistem çözer mi? | Metinden niyeti kesin bilemez; bildirim ve gerekçeli danışman incelemesi var. |
| Django her izni otomatik çözüyor mu? | Giriş/oturum temeli sağlar; sahiplik ve durum kuralları ayrıca yazılır. |
| Nerede çalışacak, kim bakacak? | Yerelde çalışıyor. Yayın yönü VDS/hosting; paket seçilmedi. Bakım Batu'da. |
| Kaptan göreve aday olabilir mi? | Pilot uygulamada öneriliyor; öğretmenden kesin yanıt bekleniyor. |
| AI kullanıldı mı? | Taslak/kod/kontrolde destek kullanıldı; kendi gerekçelerini açıklama sorumluluğun sürüyor. |

## İlk prova kaydı — Batu dolduracak

- Tarih/saat: **henüz yok**
- Gerçek toplam süre: **ölçülmedi**
- Django seçimi — Batu, 19 Ekim (yazım düzeltilmiş): **“Django daha kullanışlı olduğu için.”** Bu kişisel değerlendirmedir; alternatiflerin ölçülmüş karşılaştırması değildir.
- Aday seçimi — Batu, 19 Ekim (anlamı korunarak yazım düzenlendi): **“Görevi açan kişi, uygun kişiye verebilmek için bir kişi seçecek.”**
- Sonuç onayı — Batu, 19 Ekim (anlamı korunarak yazım düzenlendi): **“İş henüz bitmemiş veya yarım kalmış olabilir; yapan kişi yanlışlıkla bitti diyebilir. İşi isteyen kişi de sonucu kontrol edip onaylarsa iki tarafın da işin bittiği konusunda anlaşması daha uygun olur.”** Bu normal tamamlama akışının gerekçesidir; mevcut 48 saatlik danışman inceleme istisnasını kaldırmaz.
- Takıldığım bölüm / yanıtlayamadığım soru: **henüz bildirilmedi**
- Bir sonraki provada değiştireceğim şey: **henüz belirlenmedi**

Kronometreyi başlat, beş bölümü sesli anlat, bitince gerçek süreyi yaz. Beş dakikayı aşıyorsa aynı bilgiyi tekrarlayan cümleleri azalt. Kısa sürüyorsa yeni özellik anlatmak yerine seçim/onay örneğini açıklığa kavuştur. 20 Ekim ikinci prova ve soru-cevap; 21 Ekim son prova/erişim kontrolü; 22 Ekim teslim kontrolü.

## Kaynaklar

Bu belge mevcut proje belgelerinin çalışma özetidir; yeni ürün kuralı veya görüşme sonucu eklemez. Proje içindeki kaynaklar: README.md (13 Ekim güncel planı ve 18 Ekim kontrolü), roller.md, akis.md, veri.md, ekranlar.md, kurallar.md, senaryolar.md, teknoloji.md ve ANA-SITE.md. Asıl görev belgesi: Özgür Girgin, GOREV-TANIMI.pdf; bu çalışma sırasında yeniden okunmadı. Öğrenci gerekçesi ve beş dakikalık anlatım koşulu önceki kaynaklı inceleme kaydından doğrulandı.
