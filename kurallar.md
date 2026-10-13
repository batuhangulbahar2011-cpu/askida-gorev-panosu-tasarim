# Altı değişmez kuralın uygulanması

| Belge kuralı | Ekran ve veri karşılığı | Sunucu/işleyiş karşılığı | Kabul kontrolü |
|---|---|---|---|
| 1. Hiyerarşi kalkanı | İstek açta Görev/Talep açıklaması; görevde `team_purpose`; detayda danışmana bildir | Görevi yalnız kaptan/danışman açar; görevde takım amacı zorunlu. Uygunsuz görev danışman kararıyla iptal; kişisel ihtiyaç yeni talep olarak açılır | Selim kişisel işini görev diye açarsa form uyarısı ve gerekçe sorusu; yayımlarsa bildirim ve gerekçeli iptal; görev katkısı sayılmaz |
| 2. Görev iyilik değildir | Ayrı sekmeler ve tür etiketleri; danışman tablosunda ayrı sütunlar | `kind` yayın sonrası değişmez. Yalnız onay olayları sayılır, görev ile yardım toplama veya puana çevirme yok | Bir görev ve bir talep onaylanınca ayrı toplamlar birer artar |
| 3. Sıralama yok | Pano yalnız takım toplamı; danışman özeti alfabetik | Kişi toplamı yalnız danışmana sunulur; kaptan dahil diğer rollere veri uçlarında 403. Kişiye göre herkese açık rapor yok | Üye/kaptan URL ve ağ isteğiyle kişi tablosuna ulaşamaz; toplamlar erişilebilir |
| 4. Özel mesaj yok | Detayda tek ortak yorum alanı; alıcı seçimi yok | Yorumlar tüm aktif takım üyelerine görünür. DM tablosu/uç noktası yok; teklif notu yalnız adaylık açıklamasıdır, istek sahibi ve ilgili aday görür; danışman bildirilen sorunu inceleyebilir. Danışmana bildirim tek gerekçeli işlem kaydıdır, sohbet kanalı değildir | Derin ve Furkan'ın detay yorumunu Batu da görür; gizli konuşma başlatılamaz |
| 5. Asgari veri | Fotoğraf/telefon/adres/doğum tarihi alanları ve yükleme butonu yok | `veri.md` her alanın gerekçesini tanımlar. Bilinmeyen ek alan reddedilir; fotoğraf kabul edilmez. Hassas veri yorumdan gerekçeli temizlenir | Form/API fazladan `photo`/`phone` verisi gönderirse kayıt oluşmaz; parola/log kontrolünde açık sır bulunmaz |
| 6. Kredi yok | Puan, rozet, teşekkür puanı ve ödül görünümü yok | Sadece hareket izi ve ayrı faaliyet adetleri hesaplanır; puan/kredi kolonları yok | İşi bitiren kullanıcıya onay bilgisi gelir; puan/rozet üretilmez |

Bu kontroller uygulama geliştirilirken yapılacak kabul ölçütleridir; şu an çalışan uygulamada test edilmiş sonuçlar değildir.

## Otomatik kontrolün sınırı

Takım amacı alanı kişisel amacın olmadığını kanıtlamaz. Örneğin bir kaptan açıklamaya yanlış takım gerekçesi yazabilir. Tasarım, metni yapay zekâya sınıflandırıp kesin hüküm vermez; görünür gerekçe, üyelerin bildirimi ve danışmanın son sözüyle kuralı uygular. Bildirim gerekçesi yalnız danışmana, karar ise isteğin ortak hareketlerine görünür.

Takım üyeleri ham isteklerde kim ne yaptı görebilir. Kuralın korunması, bu açık kayıtların sistem tarafından kişi sıralamasına/başarı tablosuna dönüştürülmemesidir; bir kişinin kendi sayımını yapmasını teknik olarak tamamen engellemek vaat edilmez.

## Uygulamada karar sırası

Önce oturum ve aktif üyelik, sonra güncel rol, sonra sahiplik/üstlenen ilişkisi, sonra geçerli durum ve kayıt sürümü denetlenir. Gizlenmiş buton güvenlik değildir. İşlem ve olay kaydı aynı veritabanı işlemiyle yazılır. Hata olursa yarım geçiş veya yarım sayım kalmaz.

## Görünürlük kabul kontrolü

Adayların birbirini görmemesi yalnız kartları gizlemekle sağlanmaz: gerçek uygulamada adaylık/not/olay uçları ve bildirim alıcıları denetlenir. Seçilmeyen adları ve aday sayılarını ortak pano/hareket akışına sızdırmama kontrol edilir. Danışman inceleme erişimi teklif kutusunda açıklanır. Üç ekranlık demo yalnız örnek verilerle görünür davranışı gösterir; tarayıcıdaki rol seçici gerçek oturum/yetkilendirme değildir.


## 13 Ekim uygulama kontrolü

Ana Django sitesinde üyelerin görev açamaması, görevde amaç/son tarih zorunluluğu, ek kişisel veri ve rol alanının reddi, sıradan kullanıcıya danışman özetinin 403 olması, gizli teklif/olay/bildirim alıcısı, ortak yorumdaki HTML'nin kaçışlanması ve iptalin tamamlanmış sayılmaması ayrı testlerle kontrol edildi. Sonuç: 30 Django testi, 32 ayrı gerçek Chrome kontrolü geçti. Bu sonuç her gelecekteki güvenlik açığını veya kötü niyet tespitini garanti etmez; kaptanın yanlış takım amacı yazması hâlâ ortak bildirim/danışman kararını gerektirir. Kullanıcı geri bildirimi ve fiziksel telefon denemesi ayrı açık işlerdir. Önceki bölümdeki genel ölçütler korunur; burada yalnız gerçekleştirilen kapsam kaydedilir.
