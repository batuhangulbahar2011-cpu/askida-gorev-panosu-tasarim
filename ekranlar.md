# Ekran taslakları

Tüm ekranlar giriş yapmış aktif takım üyelerine açıktır; danışman özeti ve takım yönetimi yalnız danışmana. Girişte kullanıcı adı/parola, ilk girişte parola değişimi vardır. Mobilde tek sütun, bilgisayarda geniş liste kullanılır. Türkçe etiketler, klavyeyle erişilebilir butonlar ve renk yanında yazılı durum etiketleri bulunur. Taslak çizimlerdeki örnekler gerçek faaliyet kaydı değildir.

## 1. Pano — açık istekler

```text
+----------------------------------------------------+
| ASKIDA GÖREV PANOSU                 Batu · Üye      |
| Pano | Arşiv | [Danışman özeti]* | Çıkış             |
| Bu hafta: 12 görev onaylandı · 5 talep karşılandı     |
| [Görevler] [Yardım Talepleri]           [İstek aç]   |
| Durum: Tüm aktifler v   [Benim açtıklarım]           |
| [Benim üstlendiklerim] [Başlıkta ara]                |
|----------------------------------------------------|
| GÖREV · Tanıtım videosu · Açık                      |
| Açan: Arda · Son tarih: 15 Ekim                     |
| Takım amacı: Proje tanıtımı                 [Detay] |
|----------------------------------------------------|
| TALEP · Servo motor desteği · Üstlenildi             |
| Açan: Derin · Yardım eden: Furkan           [Detay]  |
+----------------------------------------------------+
* Yalnız danışmana görünür; sunucu da yetkiyi denetler.
```

Sekme seçilince yalnız ilgili tür görünür; çizim iki kartın biçimini birlikte gösterir. Kaptan/üye için kişi sıralaması ve başkasına göre kişi filtresi yoktur. Kendi açtıkları/üstlendikleri filtreleri yalnız iş takibi içindir, kişisel başarı toplamı göstermez. Durum seçenekleri Açık/Üstlenildi/Onay bekliyor; arşiv ayrı ekrandadır. Boş liste “Bu filtrede istek yok” gösterir. Geciken görev “Gecikti” metni taşır.

## 2. İstek aç

```text
+----------------------------------------------------+
| Yeni istek                              [Geri]     |
| Tür: ( ) Görev    (o) Yardım Talebi                  |
| Görev takım içindir; kişisel yardım talep edilir.    |
| Başlık       [Servo motoru döndüremiyorum         ]  |
| Açıklama     [Beklenen yardımı anlat              ]  |
| Takım amacı  [Yalnız görevde gösterilir           ]  |
| Son tarih    [Talepte isteğe bağlı                ]  |
| Telefon, adres veya kişisel bilgi yazmayın.          |
|                                     [Yayımla]      |
+----------------------------------------------------+
```

Üye rolünde Görev seçeneği “Yalnız kaptan/danışman açabilir” metniyle devre dışıdır. Görevde takım amacı ve son tarih zorunlu; talepte takım amacı alanı yoktur. Fotoğraf/ek yükleme ve ödül alanları yoktur. Eksik alan hatası alanın yanında gösterilir, yazılan metin korunur. Yayın başarıyla bitince detay ekranı açılır. Kişisel amaç fark eden kaptan yayımlamadan Talep seçer; otomatik amaç tespiti vaat edilmez.

## 3. İstek detayı — adaylık ve ortak konuşma

```text
+----------------------------------------------------+
| GÖREV #42 · Tanıtım videosu             [Panoya dön]|
| Açık · Açan Arda · Son tarih 15 Ekim                |
| Amaç: Takım projesinin tanıtımı                     |
| Açıklama: Üç dakikalık video hazırlanacak.          |
| [Talip ol]* [Adaylıktan vazgeç]* [Geri çek]**        |
| Adaylar (yalnız sahibi bütün adayları görür)        |
| Hakkı · Çekimi yapabilirim      [Kabul et]**         |
| Eren · Kurguya yardımcı olurum [Kabul et]**          |
|----------------------------------------------------|
| Hareketler: Arda açtı; seçilen kişi üstlendi         |
| Ortak yorumlar (takım görebilir)                    |
| Eren: Çekim için okulda uygun saat var mı?          |
| [Yorum yaz......................................]  |
| [Gönder]                [Danışmana bildir]          |
+----------------------------------------------------+
* Sahibine görünmez. ** Yalnız sahibine görünür.
```

Kabul sırasında kısa gerekçe istenir; sahibi olan kişi aday olamaz. Kabul sonrası aday butonları kapanır. Üstlenene “Yapıldı bildir” ve “Bırak”; onay beklerken sahibine “Onayla” ve “Düzeltme iste” gösterilir. Yapıldı formu sonuç notu ister, dosya eki istemez. Ortak yorumlarda kişiye gizli gönderme seçeneği yoktur. Arşiv/iptal detayları okunabilir; sıradan yeni yorum kapalıdır, danışmana itiraz bildirimi yapılabilir. Danışman kararını olay akışında yazar.

Bırak formu kısa neden ve varsa yarım kalan iş notunu ister; “İstek yeniden adaylara açılacak, yeni kişiyi açan seçecek” açıklamasını gösterir. Not ortak hareketlerde korunur.

İstek geri çekme formu neden ister ve “Bu iş tamamlanmış sayılmayacak; geçmiş hareketler korunacak” der. Uyuşmazlık bildirimi kısa gerekçe formudur; gönderen kendi bildirim sonucunu görür, özel mesaj dizisi açılmaz.

## 4. Arşiv

```text
+----------------------------------------------------+
| Arşiv                                   [Panoya dön]|
| [Onaylanan] [İptal edilen]                          |
| Tür: Hepsi v   Tarih aralığı: Bu hafta v            |
| GÖREV · Tanıtım videosu · Onaylandı · 11 Ekim       |
| Arda açtı · Hakkı tamamladı                [Detay]  |
| TALEP · Servo motor desteği · Onaylandı · 12 Ekim   |
| Derin açtı · Furkan yardım etti            [Detay]  |
+----------------------------------------------------+
```

Onaylanan ve iptal edilen ayrılır; iptal edilen başarı sayılmaz. Başkasına göre kişisel faaliyet filtresi veya kişi toplamı yoktur. Kayıtlar herkese görünür, toplu bireysel performans sunulmaz. Boş arşiv “Henüz bu aralıkta kayıt yok” gösterir. Kayıt “sil” veya “puan ver” eylemi taşımaz.

## 5. Danışman özeti

```text
+----------------------------------------------------+
| Danışman özeti · Özgür                   [Panoya dön]|
| Dönem: Bu hafta v                                  |
| Takım: 12 görev · 5 yardım onaylandı                |
| İnceleme: 48 saati aşan 2 onay; 1 uygunsuz görev    |
| [İnceleme kuyruğu]                                 |
| İsim (alfabetik) | Görev adaylığı | Görev | Yardım  |
| Ayaz             | 2             | 1     | 0       |
| Batu             | 1             | 0     | 1       |
| ...                                                |
| [Görev kabulleri / Yardım teklifleri ayrıntısı]     |
| Sayılar bağlamdır; puan veya sıralama değildir.     |
+----------------------------------------------------+
```

Tam kişi tablosu: ad, ayrı görev adaylığı, görev kabulü, onaylanmış görev, yardım teklifi, yardım kabulü, onaylanmış yardım sütunları. Mobilde kişi başına kart; sütunlar gizlenmez. Alfabetik sıralama sabittir. Kaptana da bu ekran ve veri uçları kapalıdır. URL elle açılırsa 403 görünür, hiçbir kişi verisi gönderilmez.

Kuyrukta geciken onay, geciken son tarih ve açık bildirim ayrı etiketlerdir. Danışman detaya geçer, gerekçeli karar verir. Otomatik “başarılı say” butonu yoktur; “İnceledim, onaylıyorum” açık karar eylemidir. Danışman kendi üstlendiği talebi bu eylemle onaylayamaz.

## 6. Takım yönetimi

```text
+----------------------------------------------------+
| Takım yönetimi · yalnız danışman                   |
| [Üye ekle]                                        |
| Selim  | Kaptan v | Aktif | [Kaydet]               |
| Batu   | Üye v    | Aktif | [Pasifleştir]          |
| Özgür  | Danışman | Aktif | Son danışman korunur   |
| [Parola sıfırla] [Dönemi kapat]                    |
+----------------------------------------------------+
```

Pasifleştirme öncesi devredilecek sahiplik ve tekrar açılacak işler listelenir. Parola sıfırlama yalnız kişinin yüz yüze talebi üzerine yapılır; geçici parola ilk girişte değişir. Dönemi kapatma yalnız aktif istek yokken kullanılabilir; 90 günlük silme zamanı önizlenir. Sistem ayarları takım toplamları veya kişi sıralaması içermez.

## Görünürlük

Aday listesi çizimi yalnız sahibi görünümüdür. Aday kendi kaydını görür; diğer üyeler seçilmeyenleri ve aday sayılarını görmez. Danışman bildirilen sorunu incelerken erişebilir. Teklif kutusu bu erişimi açıklar; ortak yorum kutusu tüm takımın göreceğini belirtir. Seçilmeyen kişiye nazik bildirim gösterilir.
