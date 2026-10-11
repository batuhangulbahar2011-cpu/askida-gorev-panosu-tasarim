# Askıda Görev Panosu — Batu'nun tasarım taslağı

Bu tasarım, Askıda İyilik takımının takım görevlerini ve kişisel yardım taleplerini ayrı izleyebilmesi için hazırlanmıştır. Açan kişi adayları değerlendirir, birini seçer ve sonucu onaylar. Takım toplamları herkes tarafından, kişi bazlı özet yalnız danışman tarafından görülür. Pilot, telefon ve bilgisayardan kullanılan sade bir web panosu olarak önerilmiştir. Bu depo sistem tasarımı içerir; uygulama değildir.

**Durum:** 2026-10-09 tarihinde akış kararları güncellendi. Belgedeki zorunlu kurallar uygulanmıştır; gerekçeli bırakma Batu tarafından kabul edildi. 10 Ekim öğretmen geri bildirimiyle onay takibi sadeleştirildi: 12 saatlik hatırlatma kaldırıldı, yalnız 48 saat danışman eşiği kaldı; saklanan durumlar beşten dörde indi. Son tarih kararı Batu tarafından Codex'e bırakıldı: görevde zorunlu, talepte isteğe bağlı. Dönem sonrası 90 günlük kayıt saklama Batu tarafından kabul edildi; teknoloji seçimi hâlâ öneridir. Bu metin AI desteğiyle hazırlanmıştır; Batu gerekçeleri anlayıp kendi görüşüne göre düzenlemeden nihai teslim sayılmaz.

## Dosyalar

| Dosya | İçerik |
|---|---|
| [roller.md](roller.md) | Roller, sahiplik, izinler ve üyelik değişiklikleri |
| [akis.md](akis.md) | Durumlar, geçişler, süreler, eşzamanlılık ve istisnalar |
| [veri.md](veri.md) | Alanlar, örnekler, gerekçeler, erişim ve saklama |
| [ekranlar.md](ekranlar.md) | Altı ekranın çizimi ve davranışı |
| [kurallar.md](kurallar.md) | Altı değişmez kuralın somut uygulaması |
| [senaryolar.md](senaryolar.md) | Dört zorunlu ve iki ek senaryonun yürütülmesi |
| [teknoloji.md](teknoloji.md) | İki seçenek, gerekçeli öneri ve Dayanışma Ağı ilişkisi |

## Tasarımın kısa gerekçesi

- Görev ve talep ayrı kanallardır: takım katkısı ile kişisel yardımı karıştırmamak için.
- İlk aday otomatik atanmaz: açan kişinin işin ihtiyacına göre seçim yapabilmesi için.
- Tek istek, tek aktif üstlenen: pilotu sade tutmak için.
- Tamamlama açanın onayına bağlıdır: yapılan iş ile kabul edilen sonucu ayırmak için.
- Geciken onay danışmana gider: emeğin belirsiz süre beklememesi için.
- Web önceliklidir: takım üyelerinin uygulama kurmadan aynı panoya ulaşabilmesi için.

## Günlük çalışma ve teslim planı

**Teslim: 22 Ekim 2026 Perşembe** (Batu'nun 9 Ekim tarihli doğrudan beyanı). Hedef: sekiz tasarım dosyasını **18 Ekim Pazar** günü tamamlamak; 19–21 Ekim'i sunuma, 22 Ekim'i teslim kontrolüne ayırmak. Bu bir çalışma planıdır; tarihlerdeki işler henüz yapılmış sayılmaz. İlk taslak 8 Ekim'de hazırlanmıştır.

### 1. hafta — 9–15 Ekim: kararları ve tasarımı netleştirme

| Tarih | Yapılacak iş | Gün sonunda beklenen çıktı |
|---|---|---|
| 9 Ekim Cuma — bugün | Onay, son tarih, bırakma, gecikme ve düzeltme akışlarını netleştir; hesap ve saklama sorularını tamamla | Anlaşılmış akış kararları; güncel taslağın ilk gerçek GitHub kaydı (repo/yükleme doğrulanacak) |
| 10 Ekim Cumartesi | Rol tablosu, sahiplik ve hesap açılışını gözden geçir; kaptanın aday olması belirsizliğini öğretmene sorulacak soru olarak kaydet | Tutarlı roller.md; açık yetki sorusu |
| 11 Ekim Pazar | Görev ve kişisel yardım akışlarını baştan sona anlat; eşzamanlı aday, bırakma ve geciken onayı kontrol et | Savunulabilir akis.md; bulunan boşlukların düzeltmesi |
| 12 Ekim Pazartesi | Her veri alanının neden gerekli olduğunu ve kimlerin göreceğini incele; saklama kararını işle | Gerekçeli veri.md |
| 13 Ekim Salı | Pano, istek açma ve detay ekranlarını akışla eşleştir | İlk üç ekranın tutarlı taslağı |
| 14 Ekim Çarşamba | Arşiv, danışman özeti ve takım yönetimini tamamla; mümkünse Selim/Arda'dan ihtiyaç geri bildirimi al | Altı ekranın tamamı; alınan geri bildirimin gerçek kaydı |
| 15 Ekim Perşembe | Altı değişmez kuralı dosyalarda izle; ilk haftanın yapılan işlerini ve açıklarını özetle | kurallar.md kontrolü; birinci hafta ilerleme özeti |

### 2. hafta — 16–22 Ekim: son kontrol ve sunum

| Tarih | Yapılacak iş | Gün sonunda beklenen çıktı |
|---|---|---|
| 16 Ekim Cuma | Dört zorunlu ve iki ek senaryoyu adım adım yürüt; boşluk çıkarsa ilgili dosyayı düzelt | Çelişkisiz senaryolar.md |
| 17 Ekim Cumartesi | İki teknoloji seçeneğini anlayıp seçimin gerekçesini kendi cümlelerinle yaz; açık öğretmen sorusunu takip et | Gerekçeli teknoloji.md; yanıt gelmezse belirsizlik açıkça korunur |
| 18 Ekim Pazar | Sekiz dosyayı çapraz kontrol et: roller, süreler, ekranlar, alanlar ve kurallar; bağlantıları ve GitHub görünümünü denetle | Tam tasarım; eksiklerin kapanması ve teslim öncesi sürüm |
| 19 Ekim Pazartesi | Beş dakikalık anlatımı hazırla; neden bu kararları verdiğini kendi cümlelerinle çalış | Kısa konuşma notları ve ilk süreli prova |
| 20 Ekim Salı | Süreli sunum yap; rol, aday seçimi, onay ve veri sorularına cevap çalış | Beş dakikaya sığan anlatım ve soru-cevap provası |
| 21 Ekim Çarşamba | Son prova; ikinci hafta ilerleme özeti, repo erişimi ve dosya kontrolü | Hazır sunum ve hocayla paylaşılacak repo bağlantısı |
| 22 Ekim Perşembe | Teslim saatini doğrula; bağlantıyı ve dosyaları son kez açıp kontrol et; teslimi yap | Teslim teyidi; gerekiyorsa sunum |

19 Ekim'den itibaren yeni özellik eklenmez; yalnız bulunan önemli çelişki veya eksikler düzeltilir. Bir gün aksarsa öncelik sekiz zorunlu dosyadadır; sunum günleri ek özellikler için kullanılmaz. Çalışma blokları için başlangıç önerisi günlük 45–60 dakikadır; Batu'nun zamanına göre ayarlanabilir.

GitHub'a yalnız gerçekten yapılan değişiklikler açıklayıcı commit mesajlarıyla yüklenir. Bugünkü yükleme günün kararları tamamlandığında yapılacaktır. Haftalık özetler o günkü gerçek çalışma üzerinden hazırlanır; şu an yazılmış rapor değildir. Rapor istenirse sekiz zorunlu dosya korunur, ek raporlar ayrı tutulur. Commit tarihleri geriye çekilmez; boş veya sahte commitlerle düzenli çalışma görüntüsü oluşturulmaz. Azra'nın tasarımına teslimden önce bakılmaz; Selim ve Arda ile ihtiyaç konuşulabilir.

## Beş dakikalık sunum

1. 0:00–0:45 — Sorun ve görev/talep ayrımı.
2. 0:45–1:45 — Arda'nın görevine iki aday; seçim ve onay akışı.
3. 1:45–2:45 — Pano, detay ve danışman özeti.
4. 2:45–3:45 — Asgari veri ve altı kuralın uygulanması.
5. 3:45–5:00 — Teknoloji tercihi, geciken onay ve tasarımın sınırları.

## Kaynak ve açık kararlar

Kaynak: Özgür Girgin, **GOREV-TANIMI.pdf**, Bölüm 1–10; Batu'nun sağladığı dört sayfalık görev belgesi. Yerel kaynak: `C:\Users\Batuhann\Desktop\GOREV-TANIMI.pdf`. Belgenin kendisi bu depoya kopyalanmadı.

2026-10-09 kararları (10 Ekim'de sadeleştirildi): Yapıldı bildiriminden 48 saat sonra danışman incelemesi; 12 saatlik hatırlatma kaldırıldı; otomatik onay yoktur. Görevde son tarih zorunlu, talepte isteğe bağlıdır; takım işlerini planlamak ve kişisel yardımı gereksiz tarihle sınırlamamak amaçlanır. Üstlenen kısa gerekçe ve varsa yarım kalan iş notuyla bırakabilir; istek yeniden adaylara açılır, yeni üstleneni açan kişi seçer. Geciken görev kapanmaz; “Gecikti” etiketiyle danışman inceleme kuyruğuna girer. Sonuç eksikse açan kişi gerekçeli düzeltme ister; iş aynı üstlenende kalır ve yeniden Yapıldı bildirimiyle onaya sunulur. Bu iki akış Batu tarafından kabul edildi. Hesapları danışman açar; kullanıcı adı ve geçici parola verir, kullanıcı ilk girişte parolasını değiştirir. Bu hesap açılışı Batu tarafından kabul edildi. Dönem kayıtları danışman dönemi kapattıktan sonra 90 gün tutulur, ardından silinir; süre tek tek görevlerin tamamlanmasından başlamaz. Aktif kullanıcı hesapları korunur. Batu, eski görevleri sonraki yıl görmeye ihtiyaç duymadığını söyleyerek bu saklama kararını kabul etti. Kalan teknoloji önerisi Django tercihidir. Danışman görevi üstlenmez; kaptanın üye gibi göreve aday olmasına izin verilmesi belge tablosundaki belirsizlik için pilot önerisidir ve Özgür öğretmene doğrulatılmalıdır. Teslim tarihi 22 Ekim 2026 Perşembe olarak Batu tarafından bildirildi; tasarım 18 Ekim'de bitecek şekilde planlandı. Öğretmenin tasarım seçimi, GitHub repo/yükleme doğrulaması ve sunum henüz tamamlanmadı.
