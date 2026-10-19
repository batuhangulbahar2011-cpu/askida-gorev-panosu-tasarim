# Görev ve Talep akışları

## İstek ve adaylık

Görevde kaptan/danışman takım ihtiyacını açar; üye veya kaptan aday olur; **açan kişi kabul etmeden üstlenme başlamaz**. Talepte herhangi bir aktif kişi yardım ihtiyacını açar; başka biri teklif eder; talep sahibi kabul eder. Kendi isteğine aday olunamaz. İki türde de tek aktif üstlenen vardır.

Adaylık, isteğin durumundan ayrıdır: `bekliyor`, `kabul`, `seçilmedi`, `geri_çekildi`. Aynı kişinin bir istek için tek adaylık satırı olur; istek yeniden açılınca kişi yeni kısa notla tekrar aday olur. Eski hareketler olay kaydında korunur. Birden çok aday olması isteği açık durumdan çıkarmaz.

```mermaid
stateDiagram-v2
    [*] --> acik: İstek yayımla
    acik --> ustlenildi: Sahip bir adayı kabul eder
    ustlenildi --> onay_bekliyor: Üstlenen yapıldı bildirir
    onay_bekliyor --> ustlenildi: Sahip düzeltme ister
    onay_bekliyor --> onaylandi: Sahip sonucu onaylar
    onaylandi --> kapandi: Aynı işlemde kapat
    ustlenildi --> acik: Üstlenen bırakır
    onay_bekliyor --> acik: Üstlenen bırakır
    acik --> kapandi: Sahip geri çeker
    ustlenildi --> kapandi: Sahip geri çeker
    onay_bekliyor --> kapandi: Sahip geri çeker
```

`onaylandi` kabul olayını temsil eder, bekleyen ayrı bir veritabanı durumu değildir. İşlem sonunda durum `kapandi` olur ve `onaylandi` olayı yazılır. Geri çekme de aynı `kapandi` durumuna gider; fark olaydadır (`onaylandi` veya `geri_cekildi`). Arşiv ekranı bu olaya bakarak onaylananları ve iptal edilenleri ayrı filtrede gösterir; iptal tamamlanmış sayılmaz. Saklanan durumlar dörttür: `acik`, `ustlenildi`, `onay_bekliyor`, `kapandi`.

## Geçiş sözleşmesi

| İşlem | Ön koşul ve yetki | Sonuç / görünür geri bildirim |
|---|---|---|
| Yayınla | Tür yetkisi; başlık ve açıklama; görevde takım amacı/son tarih | Açık; açılış olayı |
| Aday ol | Açık, aktif hesap, sahibi değil | Bekleyen adaylık; pano durumu değişmez |
| Adaylıktan vazgeç | Kendi bekleyen adaylığı | Geri çekildi; istek açık kalır |
| Kabul et | Sahip; açık; bekleyen aktif aday | Üstlenildi; seçilen kabul, diğer bekleyenler seçilmedi |
| Yapıldı | Üstlenen; üstlenildi; sonuç notu | Onay bekliyor; 48 saat sayacı başlar |
| Düzeltme iste | Sahip; onay bekliyor; açıklama zorunlu | Üstlenildi; üstlenen korunur, sayaç sıfırlanır |
| Onayla | Sahip; onay bekliyor | Kapandı (arşivde görünür); tek onay olayı, türe göre bir tamamlanma sayılır |
| Bırak | Üstlenen; üstlenildi/onay bekliyor; neden zorunlu | Açık; üstlenen/sayaç temizlenir, eski adaylıklar tekrar canlanmaz |
| Geri çek | Sahip; aktif üç durumdan biri; neden zorunlu | Kapandı (geri çekildi olayı); adaylıklar kapanır; onay/katkı sayılmaz |
| Danışman kararı | Uyuşmazlık veya 48 saat aşımı; açıklama zorunlu | Onay, düzeltme, yeniden açma veya iptal; ilgili geçişin aynı kuralları |

Sahip isteği yalnız açıkken düzenler; tür sonradan değiştirilmez. Yeniden açılmış istek düzenlenebilir, önceki adaylar yeniden başvurmalıdır. Kapandı terminaldir; aynı ihtiyaç tekrar doğarsa yeni istek açılır. Yayımlanmış yorum ve olaylar sonradan değiştirilemez. Yanlış yorum için yeni düzeltme yorumu eklenir.

## Belgedeki beş sorunun cevabı

1. **İki kişi aynı göreve talip olursa:** açan kişi iki adaylığı da görür; adaylar birbirini görmez. Danışman yalnız bildirilen sorunu incelemek için ilgili adaylıkları görebilir. Açan kişi gerekçeli seçim yapar; erken tıklamak öncelik hakkı değildir. Aynı anda iki kabul gelirse veritabanındaki tek işlem açık durum ve kayıt sürümünü kontrol eder; biri kazanır, diğeri “Bu istek güncellendi, yenileyin” görür. Üstlenen asla iki kişi olmaz.
2. **Üstlenen yapamazsa:** detayda “Bırak” seçer, kısa neden ve varsa yarım kalan işin nerede kaldığını yazar, sonra onaylar. Bu not takımın görebildiği hareket kaydında kalır. Üstlenen temizlenir, istek tekrar açık olur. Eski adaylar otomatik atanmaz; yeniden başvurabilir. Bırakmak puan/ceza üretmez.
3. **Yapıldı hiç onaylanmazsa:** tek eşik vardır: Yapıldı bildirilmesinden 48 saat sonra iş danışmanın inceleme kuyruğuna girer. (10 Ekim öğretmen geri bildirimiyle sadeleştirildi: önceki 12 saatlik ayrı hatırlatma kaldırıldı; neden aşağıda.) Süre takvim saatiyle ölçülür; hafta sonu durmaz. Otomatik başarı/onay yoktur. Danışman tarafların ortak yorumlarını inceleyerek gerekçeli karar verir. Eşik sayfa açıldığında veya yenilendiğinde olay zamanından hesaplanır. Pilot için danışmanın kuyruğu günde bir kez kontrol etmesi önerilir; 48 saat incelemeye açılma eşiğidir, kararın aynı anda verileceği garantisi değildir. Hakem de üstlenen ise otomatik çözüm yok; sahip onayı gerekir.

   *Neden 12 saat çıkarıldı:* iki ayrı eşik, küçük bir takım için iki ayrı kural ve iki ayrı ekran metni demekti; sahibin zaten onay bekleyen işi panoda "Onay bekliyor" olarak görünüyor. Tek eşik daha kolay anlatılır ve sınanır.
4. **Son tarih:** görevde zorunlu, talepte isteğe bağlı. Geçmiş tarihli yeni istek açılamaz. Tarih, İstanbul saatine göre gün sonudur. Süre geçince “Gecikti” etiketi ve danışman kuyruğu oluşur; görev iptal edilmez. Açık isteğin sahibi gerekçeyle tarihi değiştirebilir; üstlenilmiş işte danışman gecikme/uyuşmazlık incelemesinde gerekçeyle yeniden adaylara açar. İstek açık olduktan sonra sahibi gerekçeyle tarihi düzenler ve yeniden aday seçer; sürmekte olan işin tarihi sessizce değiştirilmez.
5. **Açan geri çekebilir mi:** arşivlenmeden önce evet, neden yazar; üstlenen varsa form yapılan emeğin kayıtta kalacağını açıklar. Üstlenen buna ortak yorumla itiraz edebilir ve danışmana bildirebilir. İptal sonucu onaylanmış iş toplamına girmez. İptalin amacı işi kapatmaktır; işi görünmez silmek değildir.

## Hiyerarşi kalkanı

Görev formu “Takım için beklenen çıktı nedir?” açıklamasını zorunlu ister. Kişisel ihtiyaç bildiren kişi Talep sekmesine yönlendirilir. Sözcük kontrolü kişisel amaç tespitinde kesin karar vermez. Yanlış yayımlanmış görev için herkes gerekçeli bildirim oluşturabilir. Bildirimin kimin tarafından yapıldığı ve gerekçesi danışman tarafından görülür; bu, özel sohbet değil tek işlem kaydıdır. Danışman ortak alanda karar gerekçesini yazar; uygunsuz görev iptal edilir. Sahip isterse yeni bir talep açar. Tür değiştirilerek önceki görev izi silinmez.

## Yarışlar ve hatalar

Kabul, bırakma, yapıldı, onay ve iptal; durum/sürüm kontrolü ve olay yazımıyla tek veritabanı işlemidir. Çift tıklama ikinci kez olay veya sayım üretmez. Eşzamanlı iptal/onayda ilk geçerli işlem tamamlanır, ikincisi çakışma görür. İnternet kopunca buton sonuç gelene kadar kilitlenir; tekrar gönderimde eski sürüm ve güncel durum kontrol edilir. Sayfa yenilenip son durum görülmeden başarı gösterilmez. 403 yetkisiz, 409 güncel olmayan işlem, alan hatası ilgili form alanında Türkçe görünür.

İstek listesi: aktifler önce; son tarih artan, son tarihsizler en sonda; eşitlikte oluşturma zamanı artan ve kimlik artan. Arşiv: onay olayı tarihi azalan. Sayaçlar istek adedidir, aday/yorum adedi değildir.

## Seçilmeyen aday ve bildirimler — 12 Ekim kararı

Kabulden sonra seçilen kişiye kabul bildirimi, seçilmeyene “Bu istek için yardım ayarlandı. Teklifiniz için teşekkür ederiz; başka bir isteğe teklif verebilirsiniz” anlamında nazik, resmî bildirim gösterilir. Görevde yardım yerine görev için kişi belirlendi ifadesi kullanılır. Seçilmeyen kişi puan/öncelik kaybetmez; seçilen kişinin teklif notunu veya diğer adayları görmez. Seçim gerekçesi adayları karşılaştıran ortak bir değerlendirme olarak yayımlanmaz.

Site içi bildirim simgesi yalnız kişinin kendi bildirimlerini gösterir; tıklama ilgili detaya açar. Yeni teklif isteği açana, kabul/seçilmeme adaylara, Yapıldı sahibine, onay/düzeltme üstlenene gider. Ortak yorumlar herkese açıktır; teklif notu özel sohbet değildir. Teklif, geri çekilme ve seçilmeme olayları da adaylık görünürlüğüne tabidir; ortak hareket listesi seçilmeyen adları sızdırmaz. Push/e-posta ilk kapsamda yoktur.

## 17 Ekim uygulama netleştirmesi

Kapalı istekte yeni ortak yorum sunucuda reddedilir; geçmiş okunur ve danışmana gerekçeli itiraz bildirilebilir. Çözülmüş eski bildirim tek başına yeni danışman müdahalesi yetkisi vermez; açık bildirim, güncel gecikme veya 48 saat aşımı gerekir. Kişisel veri içeren yorumu temizlemek diğer şikâyet konularını kendiliğinden çözmez; danışman incelemeyi ayrıca tamamlar.


## 19 Ekim — Batu’nun sonuç onayı gerekçesi

Batu’nun kendi açıklaması, anlamı korunarak yazım düzenlendi: “İş henüz bitmemiş veya yarım kalmış olabilir; yapan kişi yanlışlıkla bitti diyebilir. İşi isteyen kişi de sonucu kontrol edip onaylarsa iki tarafın da işin bittiği konusunda anlaşması daha uygun olur.”

Bu, mevcut Yapıldı → onay bekliyor → sahip onayı akışının kullanıcı gerekçesidir. Yeni bir üçüncü onay adımı eklemez; 48 saat sonra gerekçeli danışman incelemesi ve düzeltme/bırakma yolları korunur.
