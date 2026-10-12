# Senaryoların yürütülmesi

Senaryolar aynı `roller.md`, `akis.md`, `veri.md` ve `ekranlar.md` kurallarını kullanır. İsimler görev belgesinden, tarihler/istekler örnektir. Bu bir masa başı tasarım kontrolüdür; uygulama testi değildir.

## 1. Arda açar, Hakkı ve Eren aynı anda talip olur

1. Arda kaptan rolüyle İstek Aç'ta Görev seçer; başlık “Üç dakikalık tanıtım videosu”, takım amacı “Proje sunumu”, gelecek bir son tarih ve açıklama girer. `requests.status=acik`; açılış olayı yazılır.
2. Hakkı ve Eren üye olarak aynı anda detaydan talip olur. İki ayrı `applications` satırı bekler; istek hâlâ açık ve üstlenen boştur. Arda iki adaylığı görür; Hakkı ve Eren yalnız kendi adaylığını görür. Diğer üyeler adayların adlarını ve sayısını görmez.
3. Arda adayları değerlendirir; Hakkı'yı “Çekim saatine uygunluğu nedeniyle” kabul eder; bu seçim notu adayları karşılaştıran ortak yorum olarak yayımlanmaz. Tek işlemde Hakkı kabul, Eren seçilmedi; istek üstlenildi, üstlenen Hakkı olur.
4. Arda'nın başka sekmesinden Eren için aynı anda kabul gelse bile eski sürüm/açık durum geçersizdir. İkinci işlem 409 gösterir; Eren üstlenen olamaz. Eren hiçbir sıra veya puan kaybetmez. Eren’e “Bu görev için bir kişi belirlendi. İlginiz için teşekkür ederiz; diğer görevlere aday olabilirsiniz” anlamında nazik bildirim gelir. Eren Hakkı’nın özel teklif notunu görmez.
5. Hakkı işi yapar, sonuç notuyla Yapıldı bildirir. Durum onay bekliyor olur. Arda videonun beklenen sonucu sağladığını ortak yorum ve sonucu görerek onaylar.
6. İstek arşive girer; tek onay olayı Hakkı'yı hedef kişi olarak kaydeder. Bu haftanın görev toplamı bir artar, yardım toplamı değişmez. Hakkı'nın görev katkısı yalnız danışman kişi özetinde artar.

**Son durum:** tek üstlenen, tek onay, açıkta bekleyen aday yok; takım katkısı ile yardım ayrıdır.

## 2. Derin talep açar, Furkan karşılar, Derin onaylar

1. Derin üye rolüyle Yardım Talebi açar: “Arduino servo motor desteği”; beklenen yardım açıklanır, takım amacı/fotoğraf yoktur. Son tarih isteğe bağlıdır.
2. Furkan detaydan “Yardım teklif et” ile kısa not bırakır. Bu adım otomatik üstlenme değildir; istek açık, teklif bekliyordur.
3. Derin Furkan'ı kabul eder; durum üstlenildi olur. Birlikte uygun zamanı ortak yorumlarda konuşurlar; Batu dahil takım üyeleri bu yorumları görebilir.
4. Furkan yardım sonrası “Servo bağlantısı düzeltildi, örnek hareket çalıştı” sonuç notuyla Yapıldı bildirir. Durum onay bekliyor olur.
5. Derin “Yardım aldım, sorun çözüldü” diyerek onaylar. İstek arşivlenir.
6. Takım yardım toplamı bir artar; görev toplamı değişmez. Danışman özetinde Furkan'ın onaylanmış yardım sütunu bir artar; puan, kredi veya rozet çıkmaz.

**Son durum:** talep sahibinin kabulü ve tamamlanma onayı alınmış kişisel yardım.

## 3. Selim açar, üstlenen iki gün sonra bırakır

1. Selim kaptan olarak sunum slaytlarının hazırlanması görevini takım amacı ve son tarihle açar.
2. Ayaz talip olur; Selim gerekçeyle kabul eder. İstek üstlenildi olur.
3. İki gün sonra Ayaz detaydan Bırak seçer, “Bu hafta yetiştiremeyeceğim” gerekçesini ve “İlk üç slaydın metni hazır; görseller eksik” devam notunu yazar. Not takımın görebildiği hareket kaydında kalır. Durum tekrar açık olur; aktif üstlenen temizlenir. Ayaz'ın bırakma olayı kalır, görev tamamlanmış sayılmaz.
4. Eski adaylar otomatik atanmaz. Ayaz veya başka üye yeniden aday olabilir. Son tarih geçtiyse gecikme etiketi oluşur; örnekte tarih henüz geçmemiştir.
5. Batu yeniden açılan göreve aday olur; Selim kabul eder. Batu işi yapar, Yapıldı bildirir; Selim sonucu onaylar.
6. Arşiv tek onay taşır; hedef kişi Batu'dur. Ayaz'ın önceki kabulü/bırakması bağlam olarak danışmana görünür, bitirmiş gibi sayılmaz. Görev toplamı yalnız bir artar.

**Son durum:** bırakma sonrası görev kaybolmadan tekrar üstlenilmiş ve onaylanmıştır.

## 4. Kaptan kişisel işini görev olarak açmaya çalışır

1. Selim Görev formuna “Kendi odam için poster tasarla” yazar. Form görevlerin takım amacı taşıması gerektiğini açıklar ve takım amacı alanını ister.
2. Selim doğru ayrımı yaparsa Talep seçer; açıklamayı kişisel yardım olarak yayımlar. Sistem bu seçimde kişisel işi takım katkısı saymaz.
3. Kuralı zorlayan dalda Selim ilgisiz bir takım gerekçesi yazıp görev yayımlar. Form tek başına niyeti kesin tespit edemez; istek açık olur.
4. Batu detaydan Danışmana Bildir ile “Bu poster takım projesi için değil” gerekçesini gönderir. Özgür yalnız danışmana açık kuyruktan kaydı inceler ve ortak yorumda Selim'in açıklamasını ister.
5. Özgür kişisel ihtiyaç olduğunu doğrulayıp gerekçeli iptal eder. İstek iptal arşivine gider, üstlenen varsa serbest kalır; görev ve yardım toplamları değişmez. Başlamış emek varsa olay/yorum izi kaybolmaz.
6. Selim yeni bir Yardım Talebi açabilir. Örnekte Efe teklif eder, Selim kabul eder, Efe yardım eder ve Selim onaylar. Yeni kayıt yalnız yardım toplamına bir ekler.

**Son durum:** uygunsuz görev takım katkısına dönüşmemiş, kişisel ihtiyaç ayrı talep olarak tamamlanmıştır. Otomatik kusursuz niyet tespiti iddia edilmez.

## 5. Yapıldı bildirimi 48 saat onaysız kalır (tek eşik)

1. Hakkı üstlendiği görevi pazartesi 10:00 İstanbul saatinde Yapıldı bildirir; saat UTC olay kaydına yazılır.
2. Arda ilgili detayı açana kadar bir şey olmaz; iş panoda “Onay bekliyor” olarak görünür. Ayrı hatırlatma yoktur.
3. Çarşamba 10:00'da 48 saat olur; görev danışman inceleme kuyruğuna girer. Hâlâ onay bekliyor ve takım sayımı değişmemiştir.
4. Özgür sonuç notunu ve tarafların ortak yorumunu inceler; işi yeterli bulursa “48 saatlik bekleme sonrası sonucu inceledim” gerekçesiyle onaylar. Alternatif olarak düzeltme, yeniden açma veya iptal kararı verebilir.
5. Onay dalında arşiv ve tek görev sayımı oluşur. Sonradan Arda'nın eski onay butonuna basması ikinci onay üretmez.

**Son durum:** süre işin başarıyla bitmesini otomatik varsaymamıştır; son söz gerekçeli danışman kararıdır.

## 6. Kaptanlığı değişir veya takım üyesi ayrılır

1. Danışman Arda'yı kaptandan üyeye çevirir; olayda eski/yeni rol tutulur. Yeni görev açamaz, eski görevin sahibi olarak sonucu onaylayabilir.
2. Üstlenen Hakkı ayrılırsa hesabı pasifleştirilir ve oturumları iptal edilir. Üstlendiği iş gerekçeli bırakma olayıyla açığa döner; tamamlanmış sayılmaz.
3. İsteğin sahibi de ayrılmışsa sahiplik danışmana devredilir. Yeni adayın seçimi ve sonucu onaylama devredilen sahibe aittir.
4. Yeni aday Eren seçilip işi tamamlar; danışman sonucu onaylar ve arşive geçilir. Eski üyelerin önceki hareketleri saklama süresi boyunca kalır.

**Son durum:** rol/üyelik değişikliğinde aktif iş sahipsiz veya erişilemeyen bir hesapta kilitli değildir.

## Ek masa başı kontrolleri — kayıt ve görünürlük

- Danışman kod üretir; Batu ad/kullanıcı adı/kod ve kendi parolasıyla kaydolur. Üye olur, “Hoş geldin, Batu” görür. Aynı kod ikinci kayıtta geçersizdir; 7 günlük/iptal edilmiş kod da reddedilir.
- Eren yalnız kendi adaylığını ve nazik seçilmeme bilgisini görür; Arda kendi görevinde tüm adayları görür. Özgür bildirilen sorunu incelerken ilgili adaylık notuna erişebilir. Ortak yorumları Batu da görür; kutular görünürlüğü ayrı açıklar.
- Parolasını unutan Batu danışmana başvurur; kimliği doğrulanır. Hedef hesaba özel kodla 24 saat içinde yeni parola belirler; eski oturumlar kapanır, hesap/geçmiş kalır. Kod ikinci kez çalışmaz. İlk danışmanın aynı kurtarmasını Batu bakım erişimiyle yürütür.

Bunlar tasarım senaryolarıdır; gerçek kayıt, güvenlik veya uygulama testi yapıldığı iddiası değildir.
