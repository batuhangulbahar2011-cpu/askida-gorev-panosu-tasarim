# Askıda Görev Panosu — Batu'nun tasarım taslağı

Bu tasarım, Askıda İyilik takımının takım görevlerini ve kişisel yardım taleplerini ayrı izleyebilmesi için hazırlanmıştır. Açan kişi adayları değerlendirir, birini seçer ve sonucu onaylar. Takım toplamları herkes tarafından, kişi bazlı özet yalnız danışman tarafından görülür. Pilot, telefon ve bilgisayardan kullanılan sade bir web panosu olarak önerilmiştir. Bu depo sistem tasarımı ve üç ekranlık örnek web demosu içerir. Gerçek hesaplı Django uygulamasının yerel ilk sürümü 13 Ekim’de başlatıldı; [ana site rehberi](ANA-SITE.md). İnternet yayını ayrıca yapılacaktır.

**Karar geçmişi (9–12 Ekim):** 2026-10-09 tarihinde akış kararları güncellendi. Belgedeki zorunlu kurallar uygulanmıştır; gerekçeli bırakma Batu tarafından kabul edildi. 10 Ekim öğretmen geri bildirimiyle onay takibi sadeleştirildi: 12 saatlik hatırlatma kaldırıldı, yalnız 48 saat danışman eşiği kaldı; saklanan durumlar beşten dörde indi. Son tarih kararı Batu tarafından Codex'e bırakıldı: görevde zorunlu, talepte isteğe bağlı. Dönem sonrası 90 günlük kayıt saklama Batu tarafından kabul edildi; 12 Ekim’de Batu gerçek uygulama için Django’yu seçti. Bu metin AI desteğiyle hazırlanmıştır; Batu gerekçeleri anlayıp kendi görüşüne göre düzenlemeden nihai teslim sayılmaz.

## 19 Ekim — sunum hazırlığı

[Beş dakikalık çalışma notları ve prova formu](SUNUM-HAZIRLIK-19-EKIM.md) hazırlandı: süre hedefli anlatım, örnek demo yolu, soru kartları ve gerçek prova kaydı alanı. Bu AI destekli hazırlık taslağıdır; Batu'nun kendi gerekçeleri veya yapılmış prova olarak gösterilmez.

19 Ekim tam tekrar kontrolde 40 Django testi ve ayrı örnek veritabanında 43 Chrome akış kontrolü geçti. `manage.py check`, şema değişikliği kontrolü, paket tutarlılığı ve iki JavaScript dosyasının sözdizimi sorunsuz. Sekiz zorunlu belge ve yerel Markdown bağlantıları yeniden kontrol edildi. Kod/bildirim alanlarının tek tek gerekçeleri veri.md'de tamamlandı. Uygulama kodu ve gerçek kullanıcı verileri değiştirilmedi. Tema ve mobil menü için 12 ek odaklı Chrome kontrolü de geçti; açık/koyu görüntüler incelendi. Bu gerçek telefon/kullanıcı denemesi değildir. Görev PDF’si kayıtlı Masaüstü konumunda bulunamadığından kapsam önceki kaynaklı inceleme notuna göre karşılaştırıldı; asıl PDF bugün yeniden doğrulanamadı. Güncel öğrenci gerekçeleri/sunum belgeleri yerelde kaydedildi; GitHub’daki son doğrulanan sürüm hâlâ 18 Ekim f662acd, yeni gönderim yapılmadı.

**Batu'nun 19 Ekim yanıtı:** Django kendisine daha kullanışlı geldiği için seçti; görevi açan kişi uygun kişiyi seçebilmek için bir aday belirlemeli. Bunlar kullanıcının kısa açıklamalarıdır, ölçülmüş teknoloji karşılaştırması değildir. Batu sonuç onayını da açıkladı: iş yarım kalmış veya yapan kişi yanlışlıkla bitti demiş olabilir; isteyen kişinin de kontrolü iki tarafın sonuçta anlaşmasını sağlar. Üç kısa gerekçe alındı; ilk sesli prova süresi bekliyor. Batu Selim/Arda denemesi ve öğretmen görüşmesini henüz yapmadığını bildirdi; bekliyor. Fiziksel telefon son sürüm teyidi ayrı açık iş. 20–21 Ekim prova, 22 Ekim teslim planı sürüyor. Site geliştirme bir sonraki çalışma olarak ele alınacak; bu hazırlıkta yeni özellik, hesap değişikliği veya internet yayını yapılmadı.

## 18 Ekim — teslim öncesi son kontrol

Teknik dosya ve uygulama kontrolü tamamlandı; aşağıdaki açık öğrenci/görüşme işleri nedeniyle bütün teslim koşulları bitmiş sayılmıyor. Alt bölümler önceki aşamaların o günkü kayıtlarını korur.

| Kontrol | 18 Ekim sonucu |
|---|---|
| Sekiz zorunlu tasarım dosyası | Mevcut ve dolu; 11 yerel Markdown bağlantısı kontrol edildi, eksik yok. |
| Roller, sahiplik, dört durum, 48 saat ve 90 gün | Dosyalar arası karşılaştırıldı; görev/talep ayrımı, sahip onayı ve tek üstlenen korunuyor. |
| Dört zorunlu ve iki ek senaryo / beş akış sorusu | Senaryolar, geçişler ve 17 Ekim test eşlemesi karşılaştırıldı; yeni akış değişikliği gerekmedi. |
| Veri alanları ve altı değişmez kural | Gerekçeler/erişim/saklama karşılaştırıldı; puan, özel sohbet veya ek kişisel veri eklenmedi. |
| Son uygulama testleri | Ayrı test veritabanında 40 Django testi ve ayrı Chrome oturumlarında 43 uçtan uca kontrol geçti. |
| Mobil görünüm / tema / logolar | Kompakt ikonlu menü, antrasit açık-koyu düzeni ve özgün logolar mevcut; ilgili 57 menü/28 logo kontrolleri aşamalarında geçti. Bunlar kullanıcı sayısı veya tek test toplamı değildir. |
| Git kapsamı | Çalışma DB’si, yerel gizli anahtar ve .venv Git dışında; örnek test hesapları gerçek DB’ye eklenmedi. |
| Yayın ve bakım kararı | Batu 18 Ekim’de bakımını kendisinin yapacağını, VDS veya hosting üzerinde çalıştıracağını söyledi. Sağlayıcı/paket seçilmedi; satın alma ve internet yayını yapılmadı. |

**Açık kalanlar:** Batu’nun Django tercihini ve temel tasarım nedenlerini kendi cümleleriyle açıklaması; Selim/Arda ihtiyaç denemesinin notları; kaptanın göreve adaylığına öğretmen yanıtı. Yeni görüşme sonucu bu oturumda bildirilmedi. Kullanıcının paylaştığı dar ekran görüntüleri geri bildirim olarak işlendi; fiziksel telefonun dokunmatik/gerçek sunucu son sürüm denemesi tamamlandı sayılmaz.

**Takvim:** 19–21 Ekim’de gerekçe ve beş dakikalık prova; 22 Ekim teslim. Yayın sağlayıcısı seçimi ve gerçek dağıtım ayrı işlerdir. [Proje deposu](https://github.com/batuhangulbahar2011-cpu/askida-gorev-panosu-tasarim), [çalıştırma/bakım](ANA-SITE.md).

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

## 18 Ekim — görünüm ve kullanım kolaylığı

Batu siteyi denerken hata görmediğini, daha geliştirilebileceğini söyledi; önceliği görünüm ve kullanım kolaylığı olarak seçti (kullanıcı beyanı; bütün olası hataların bulunmadığı anlamına gelmez).

Mevcut yeşil tema korunarak açık sayfayı gösteren gezinme, klavyede içeriğe geçiş, ayrı haftalık takım/yardım kartları, aktif istek sayısı, görev kartında takım amacı ve yazılı durum etiketleri düzenlendi. Mobilde arama tam satır, iki seçim yan yana; düğmeler en az 44px ve menü gerektiğinde kendi içinde kaydırılabilir. Sonuçsuz listeden filtreleri kaldırma ve yeni istek açma yolları belirginleştirildi.

Kontrol: yedi danışman sayfasını açan bir Django test metodu ve ayrı örnek DB/Chrome oturumlarında 43 tarayıcı kontrolü geçti. 320/390/1280px taşma, gerçek giriş/teklif/onay/filtre akışları, aktif gezinme ve klavye atlama bağlantısı kontrol edildi; JS hatası yok. Masaüstü ve mobil pano görüntüleri incelendi. Bu fiziksel cihaz testi değildir; 17 Ekim’deki 40 Django testinin tamamı bugün tekrar çalıştırılmadı. İş kuralları ve gerçek kullanıcı verileri değiştirilmedi.

Kendi gerekçeleri, Selim/Arda denemesi ve kaptan adaylığına öğretmen yanıtı hâlâ açık; 18 Ekim tasarım hedefi ve 19–21 prova/22 teslim takvimi bu görsel çalışmayla tamamlanmış sayılmaz. İnternet yayını yapılmadı.

### 18 Ekim — açık/koyu tema ve hafif shader

Batu üstte basıldığında koyu, tekrar basıldığında açık moda geçen düğme; hafif shader ve animasyon istedi. Asıl proje klasöründe uygulandı; yedeğe dokunulmadı.

Üst sağda güneş/ay düğmesi; ilk kullanım açık tema, seçim yalnız bu tarayıcıda hatırlanır. Sayfalar arasında ve yenilemede korunur. Küçük WebGL yüzeyinde 20 kare/saniye ışık/dalga efekti, kısa giriş ve kart geçişleri kullanılır. Sekme gizliyken çizim durur; azaltılmış hareket/veri tasarrufunda shader başlatılmaz. WebGL yoksa sabit zemin; depolama kapalıysa oturum içi tema geçişi çalışır. Yeni kütüphane veya dış servis yoktur.

Kontrol: yedi sayfayı açan bir Django render testi ve ayrı örnek DB/Chrome ile 70 tarayıcı kontrolü geçti. Açık-koyu geçiş, yenilemede saklama, klavye, 320/390/1280px, azaltılmış hareket, WebGL/depoya erişim yokluğu ve mevcut iş akışları kontrol edildi. WebGL test ortamında desteklendi; 427×300 çizim yüzeyinde GL hatası yoktu. Bu cihaz performans ölçümü veya fiziksel telefon testi değildir. Gerçek hesap/veri ve iş kuralları değiştirilmedi.

## 17 Ekim — önceki kontrol ve o günün açık işleri

17 Ekim’de mevcut Django sitesi üzerinden devam edildi. Panoya başlık araması ve durum filtresi; arşive tür/tarih filtresi eklendi. Kapalı kayda yorum yazma, çözülmüş şikâyetle danışman müdahalesi ve yorum temizlerken şikâyeti kendiliğinden kapatma açıkları düzeltildi. Ayrı veritabanında 40 Django testi geçti. Bu kontrol gerçek kullanıcı görüşmesi değildir.

| 17 Ekim’e kadar planlanan iş | Gerçek durum |
|---|---|
| Akış, roller, altı ekran ve altı değişmez kural | Dosyalar ve uygulama karşılaştırıldı; bulunan eksikler düzeltildi. |
| Dört zorunlu ve iki ek senaryo | senaryolar.md’deki yürütmeler ve ilgili otomatik testler karşılaştırıldı; 17 Ekim kontrol eşlemesi dosyanın sonunda. |
| Akıştaki beş soru | akis.md’de cevaplı; üstlenilmiş işte tarih değişimi yeniden açma kararı üzerinden netleştirildi. |
| Her veri alanının nedeni | veri.md kontrol edildi; tasarım/gerçek Django teknik alanları ayrımı korundu, görünürlük ifadesi düzeltildi. |
| Selim/Arda denemesi ve öğretmenin kaptan adaylığı yanıtı | Yeni bir sonuç bildirilmedi; bekliyor. Hocanın demoyu beğendiği önceki kullanıcı beyanı korunur. |
| Batu’nun kendi gerekçeleri | 12 Ekim’deki kısa beyan var; 17 Ekim açıklaması henüz alınmadı. AI metni Batu’nun cevabı sayılmaz. |
| Çalışan ana site | Yerel Django sitesi geliştirildi; internet yayını yapılmadı. |

**Batu’nun tamamlayacağı kısa çalışma:** Kendi cümlelerinle Django’yu neden seçtiğini, alternatifin hangi işini zorlaştıracağını, siteyi nerede çalıştıracağını ve bakımda hangi işleri üstleneceğini anlat. Ardından “neden ilk aday otomatik seçilmiyor?” ve “neden Yapıldı tek başına işi bitirmiyor?” sorularını cevapla. Bilinmeyen nokta öğrenilir; cevap kullanıcı adına uydurulmaz.

18 Ekim son tasarım kontrolü, 19–21 Ekim prova ve 22 Ekim teslim hedefleri korunur. Açık geri bildirim ve gerekçe işleri tamamlanmadan bütün plan bitmiş sayılmaz. Önceki plan aşağıda tarihsel kaydıyla korunmuştur.

## Önceki çalışma planı — 13 Ekim ilerleme değerlendirmesi

**Teslim: 22 Ekim 2026 Perşembe. Tasarımı tamamlama hedefi: 18 Ekim. Prova: 19–21 Ekim.** Gerçek sunum teslimden sonra; günü henüz doğrulanmadı. Bu plan, aşağıda korunan 9 Ekim takviminin kalan işler için yerini alır. Önceki commit tarihleri ve gerçekleşmiş işlerin tarihleri değiştirilmez.

### Geldiğimiz aşama

- Sekiz zorunlu tasarım dosyası güncellendi; sadeleştirme, gizli teklif/seçilmeyen kişi ve kayıt düzeni işlendi. Dosyaların hazır olması nihai tutarlılık ve öğrenci gerekçesi kontrolünün bittiği anlamına gelmez.
- Pano, İstek aç ve Detay demosu hazır. 12 Ekim kaydına göre 20 gerçek Chrome kontrolü geçti; bilgisayar ve 320/390px görüntüleri incelendi. Gerçek telefon ve kullanıcı geri bildirimi henüz tamamlanmadı.
- Beş değişiklik commit’i GitHub’a gönderildi; son demo commit’i `0590ecd`. 13 Ekim yerel kontrolünde çalışma alanı temizdi. GitHub Pages yayını henüz yapılmadı.
- Django ortamı kurulu; gerçek hesaplar/paylaşılan veritabanı ve PythonAnywhere yayını henüz yok. Görev belgesi sistem tasarımını ister; çalışan Django sitesi teslim şartı değildir. Önce tasarım teslimi ve kullanıcı geri bildirimi tamamlanır.

### Kalan günler

| Tarih | Çalışma | Gün sonunda beklenen çıktı |
|---|---|---|
| 13 Ekim Salı | Güncel planı kaydet; Batu mevcut demoyu denesin. GitHub Pages yayını için hazırlığı kontrol et; paylaşılacak linkin çalıştığını yayın yapılınca doğrula. | Güncel plan; Batu’nun gerçek deneme notları. Yayın gerçekleşmeden link hazır sayılmaz. |
| 14 Ekim Çarşamba | Demo yayımlandıysa Batu linki Selim/Arda’ya versin, yalnız “bir görev aç” desin; yönlendirmeden takıldıkları noktaları not et. Kaptanın göreve aday olma belirsizliğini Özgür öğretmene sor. | README’de kim/ne zaman/neye takıldı kaydı; varsa öğretmen yanıtı. Görüşme gerçekleşmezse bekliyor olarak bırak. |
| 15 Ekim Perşembe | Alınan geri bildirime göre yalnız gereken ekran/akış düzeltmelerini yap; altı ekran taslağını ve altı değişmez kuralı karşılaştır. | Gerekçeli gerçek düzeltme commitleri; gerçekleşen ilk hafta ilerlemesi. Geri bildirim yoksa belge kontrolünü tamamla. |
| 16 Ekim Cuma | Dört zorunlu ve iki ek senaryoyu roller/akış/ekranlarla sonuna kadar yürüt; akıştaki beş soruyu ve her veri alanının nedenini kontrol et. İlerlemeye göre kalan günleri yeniden değerlendir. | Bulunan boşlukların tasarımda düzeltilmesi; teslim kontrol listesi. |
| 17 Ekim Cumartesi | Batu iki teknoloji seçeneğini, Django’yu nerede çalıştıracağını ve kimin bakacağını anlayarak kendi cümleleriyle anlatsın; temel tasarım kararlarının nedenlerini de yazsın. | Batu’nun kendi gerekçeleri; yalnız AI önerisine dayanmayan açıklama. |
| 18 Ekim Pazar | Sekiz dosyayı çapraz kontrol et; açık öğretmen sorularını yanıtla veya belirsizlik olarak göster. Repo/link/son sürümü kontrol et. | Teslime hazır tasarım; kalan kritik eksikler açıkça listelenmiş. |
| 19 Ekim Pazartesi | Beş dakikalık anlatımı Batu’nun cümleleriyle hazırla; ilk süreli prova. | Kısa konuşma notları ve ölçülmüş prova süresi. |
| 20 Ekim Salı | Demo örneğiyle ikinci prova; rol, gizlilik, onay, veri ve teknoloji sorularına cevap çalış. | Beş dakikaya sığan anlatım; soru-cevap eksiklerinin giderilmesi. |
| 21 Ekim Çarşamba | Son prova; GitHub erişimi, sekiz dosya ve varsa demo linkini son kez denetle. | Hazır sunum ve gerçek çalışma özeti. |
| 22 Ekim Perşembe | Teslim saatini doğrula; repo bağlantısını ve zorunlu dosyaları kontrol edip teslim et. | Batu’nun teslim teyidi; gerçek sunum tarihi ayrıca takip edilir. |

Bu hız korunursa tasarım 18 Ekim’den önce hazır olabilir; kazanılan süre kullanıcı geri bildirimi ve gerekçeleri öğrenmek için kullanılır. Bu bir hedef, tamamlanma garantisi değildir. Geri bildirim gecikirse bağımsız belge/senaryo çalışması sürer, görüşme yapılmış gibi yazılmaz. Kritik düzeltmeler 18 Ekim’e kadar önceliklidir; 19 Ekim’den sonra yeni özellik eklenmez. 13 Ekim’de Batu, hocanın demoyu beğendiğini söyleyip ana siteye geçilmesini istedi. Ana Django sitesi tasarım teslimi/prova günlerini koruyarak paralel geliştirilir; tasarımın zorunlu kontrolleri önceliğini korur. Değişiklikler ayrı gerçek ve açıklayıcı commitlerle kaydedilir; tarihleri geriye çekilmez.

## Önceki günlük çalışma planı — 9 Ekim tarihli kayıt

**Teslim: 22 Ekim 2026 Perşembe** (Batu'nun 9 Ekim tarihli doğrudan beyanı). Hedef: sekiz tasarım dosyasını **18 Ekim Pazar** günü tamamlamak; 19–21 Ekim'i sunuma, 22 Ekim'i teslim kontrolüne ayırmak. Bu bir çalışma planıdır; tarihlerdeki işler henüz yapılmış sayılmaz. İlk taslak 8 Ekim'de hazırlanmıştır.

### 1. hafta — 9–15 Ekim: kararları ve tasarımı netleştirme

| Tarih               | Yapılacak iş                                                                                                                      | Gün sonunda beklenen çıktı                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 9 Ekim Cuma — bugün | Onay, son tarih, bırakma, gecikme ve düzeltme akışlarını netleştir; hesap ve saklama sorularını tamamla                           | Anlaşılmış akış kararları; güncel taslağın ilk gerçek GitHub kaydı (repo/yükleme doğrulanacak) |
| 10 Ekim Cumartesi   | Rol tablosu, sahiplik ve hesap açılışını gözden geçir; kaptanın aday olması belirsizliğini öğretmene sorulacak soru olarak kaydet | Tutarlı roller.md; açık yetki sorusu                                                           |
| 11 Ekim Pazar       | Görev ve kişisel yardım akışlarını baştan sona anlat; eşzamanlı aday, bırakma ve geciken onayı kontrol et                         | Savunulabilir akis.md; bulunan boşlukların düzeltmesi                                          |
| 12 Ekim Pazartesi   | Her veri alanının neden gerekli olduğunu ve kimlerin göreceğini incele; saklama kararını işle                                     | Gerekçeli veri.md                                                                              |
| 13 Ekim Salı        | Pano, istek açma ve detay ekranlarını akışla eşleştir                                                                             | İlk üç ekranın tutarlı taslağı                                                                 |
| 14 Ekim Çarşamba    | Arşiv, danışman özeti ve takım yönetimini tamamla; mümkünse Selim/Arda'dan ihtiyaç geri bildirimi al                              | Altı ekranın tamamı; alınan geri bildirimin gerçek kaydı                                       |
| 15 Ekim Perşembe    | Altı değişmez kuralı dosyalarda izle; ilk haftanın yapılan işlerini ve açıklarını özetle                                          | kurallar.md kontrolü; birinci hafta ilerleme özeti                                             |

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

GitHub'a yalnız gerçekten yapılan değişiklikler açıklayıcı commit mesajlarıyla yüklenir. İlk yükleme 9 Ekim’de, demo ve sonraki beş değişiklik commit’inin gönderimi 12 Ekim’de tamamlandı; yeni değişikliklerin gönderimi ayrıca doğrulanır. Haftalık özetler o günkü gerçek çalışma üzerinden hazırlanır; şu an yazılmış rapor değildir. Rapor istenirse sekiz zorunlu dosya korunur, ek raporlar ayrı tutulur. Commit tarihleri geriye çekilmez; boş veya sahte commitlerle düzenli çalışma görüntüsü oluşturulmaz. Azra'nın tasarımına teslimden önce bakılmaz; Selim ve Arda ile ihtiyaç konuşulabilir.

## Beş dakikalık sunum

1. 0:00–0:45 — Sorun ve görev/talep ayrımı.
2. 0:45–1:45 — Arda'nın görevine iki aday; seçim ve onay akışı.
3. 1:45–2:45 — Pano, detay ve danışman özeti.
4. 2:45–3:45 — Asgari veri ve altı kuralın uygulanması.
5. 3:45–5:00 — Teknoloji tercihi, geciken onay ve tasarımın sınırları.

## Kaynak ve açık kararlar

Kaynak: Özgür Girgin, **GOREV-TANIMI.pdf**, Bölüm 1–10; Batu'nun sağladığı dört sayfalık görev belgesi. Yerel kaynak: `C:\Users\Batuhann\Desktop\GOREV-TANIMI.pdf`. Belgenin kendisi bu depoya kopyalanmadı.

2026-10-09 kararları (10 Ekim'de sadeleştirildi): Yapıldı bildiriminden 48 saat sonra danışman incelemesi; 12 saatlik hatırlatma kaldırıldı; otomatik onay yoktur. Görevde son tarih zorunlu, talepte isteğe bağlıdır; takım işlerini planlamak ve kişisel yardımı gereksiz tarihle sınırlamamak amaçlanır. Üstlenen kısa gerekçe ve varsa yarım kalan iş notuyla bırakabilir; istek yeniden adaylara açılır, yeni üstleneni açan kişi seçer. Geciken görev kapanmaz; “Gecikti” etiketiyle danışman inceleme kuyruğuna girer. Sonuç eksikse açan kişi gerekçeli düzeltme ister; iş aynı üstlenende kalır ve yeniden Yapıldı bildirimiyle onaya sunulur. Bu iki akış Batu tarafından kabul edildi. 12 Ekim yeni hesap kararı önceki geçici parola düzeninin yerini alır: ilk danışman kurulumda kendi parolasını belirler; danışman tek kullanımlık kayıt kodu üretir. Kod 7 gün geçerli ve kullanılmadan iptal edilebilir. Kişi kendi parolasıyla üye kaydolur; rolü yalnız danışman değiştirir. Dönem kayıtları danışman dönemi kapattıktan sonra 90 gün tutulur, ardından silinir; süre tek tek görevlerin tamamlanmasından başlamaz. Aktif kullanıcı hesapları korunur. Batu, eski görevleri sonraki yıl görmeye ihtiyaç duymadığını söyleyerek bu saklama kararını kabul etti. Django tercih edilmiştir; 18 Ekim güncel yayın yönü Batu’nun seçimiyle VDS veya hosting, bakım sahibi Batu’dur; paket/sağlayıcı seçilmedi. Danışman görevi üstlenmez; kaptanın üye gibi göreve aday olmasına izin verilmesi belge tablosundaki belirsizlik için pilot önerisidir ve Özgür öğretmene doğrulatılmalıdır. Teslim tarihi 22 Ekim 2026 Perşembe olarak Batu tarafından bildirildi; tasarım 18 Ekim'de bitecek şekilde planlandı. İlk sekiz dosyanın GitHub yüklemesi 9 Ekim’de 2bba8aa commit’iyle doğrulandı; 11 Ekim sadeleştirmesi yerel 6e17d6d commit’idir. Yeni değişikliklerin gönderimi, öğretmen geri bildirimi ve sunum ayrıca takip edilir.

## 12 Ekim kararları ve sade web demo

- İstek sahibi bütün teklifleri, aday yalnız kendi teklifini görür. Diğer üyeler durum/seçilmiş kişiyi görür. Danışman bildirilen sorunu incelerken ilgili gizli kayda erişebilir; teklif kutusunda bu yazılır. Seçilmeyene nazik bildirim gösterilir; ortak yorumlar takımca görülür.
- Kayıt formu: ad, benzersiz kullanıcı adı, kayıt kodu, parola ve parola tekrarı. Üye parola yenilemesi danışman aracılığıyla; ilk danışman kurtarması bakım sorumlusu Batu aracılığıyla, kişiye özel tek kullanımlık 24 saatlik kodla yapılır.
- İsimli hoş geldin, iki ayrı pano sekmesi, kendi açtıkları/üstlendikleri filtreleri, yalnız kişiye ait site içi bildirimler. Puan/sıralama, fotoğraf veya özel sohbet yok.
- Bakıma Batu sahip; Codex oturumlarda yardımcı. Otomatik bakım başlatılmadı. Batu Django’yu asistan önerisiyle, daha kolay erişilebilir geldiği için seçtiğini söyledi; teknoloji öğrenimi ve sunumda gerekçeyi savunma çalışması sürer.
- Tema: açık arka plan, okunaklı yazı, az renk, belirgin düğmeler; telefonda tek sütun.

### Demoyu açma

[index.html](index.html) dosyasını tarayıcıda aç. Üç ekran: **Pano → İstek aç → İstek detayı**. Örnek kişi seçimiyle Batu, Arda, Hakkı, Eren, Derin ve danışmanın görünümünü deneyebilirsin. Örnek veriyi sıfırlamak için “Demoyu sıfırla”. Veriler yalnız bu tarayıcıda tutulur; site gerçek giriş/kayıt veya paylaşılan veritabanı sunmaz. Gerçek takım verisi girilmez.

Deneme: Arda olarak tanıtım videosu görevini aç, Hakkı’yı seç. Eren’e geçip nazik bildirimi ve yalnız kendi teklifini gör. Hakkı olarak Yapıldı bildir; Arda olarak onayla veya gerekçeyle düzeltme iste. Batu ile yardım talebi açmayı dene.

GitHub Pages için depo Settings → Pages → Deploy from a branch → main / root kullanılabilir. Önce gerçek commit/push gerekir; bu ayarın yapıldığı veya sitenin yayımlandığı varsayılmaz. Demo GitHub Pages içindir; gerçek Django sitesi 18 Ekim güncel kararına göre VDS veya hosting üzerinde ayrıca kurulacaktır; sağlayıcı/paket seçilmedi.

12 Ekim yeni sıra önce kararlar → tasarım güncellemesi → üç ekranlık demo → Selim/Arda geri bildirimi. 9 Ekim tarihli çalışma planı geçmiş plan olarak korunur; 13 Ekim güncel planı kalan işlerde esas alınır; işler geriye dönük yapılmış sayılmaz. Cuma sonraki hafta planlanır; 22 Ekim teslim tarihi değişmez.


## 13 Ekim — demo geri bildirimi ve ana siteye geçiş

Batu, demoyu hocaya gösterdiğini ve hocanın beğendiğini söyledi (13 Ekim, kullanıcı beyanı). Bu genel olumlu geri bildirimdir; belirli bir görevi açarken hangi noktada takıldığına dair kullanıcı deneme kaydı değildir. Ek öğretmen isteği ve Selim/Arda denemesi henüz bildirilmedi; yapılmış sayılmaz. Pages üzerinden yayın da henüz doğrulanmadı. Demo dosyaları korunur.

13–15 Ekim kalan kontrolü: Pano/İstek aç/Detay hazır; arşiv, danışman özeti ve takım yönetimi taslakları ekranlar.md’de mevcut. Altı değişmez kural; tür/amaç ayrımı, ayrı katkı-yardım sayımı, yalnız danışman kişi özeti, ortak yorumlar, asgari veri ve puan/kredi/rozet olmaması üzerinden ana siteye taşınır. Gerçek kullanıcı geri bildirimi gelirse gereken değişiklik ayrı commit yapılır. Kaptanın göreve adaylığı Özgür öğretmene doğrulatılacak açık sorudur; pilot önerisi henüz kesinleştirilmez.

Batu bugün ana site geliştirmesini açıkça istedi. Django sitesi yerelde gerçek giriş/kayıt, ortak veritabanı, panolar, teklif/onay, arşiv, bildirimler ve danışman yönetimiyle hazırlanır. [ANA-SITE.md](ANA-SITE.md) çalıştırma ve bakım adımlarını içerir. Başlangıç için `baslat.bat`; gerçek danışman hesabını ilk çalıştırmada kişi kendi parolasıyla oluşturur. Selim/Arda görüşmesi, Pages veya PythonAnywhere yayını bu metinle gerçekleşmiş sayılmaz. 18 Ekim tasarım hedefi, 19–21 Ekim prova ve 22 Ekim teslim korunur.


### Ana sitenin 13 Ekim doğrulaması

- `manage.py check` sorun bulmadı. Ayrı test veritabanında 30 Django testi geçti: oturum/rol/sahiplik, form ve ek veri reddi, tek kullanımlık kod, gizli teklif ve bildirim, durum/sürüm çakışması, düzeltme/bırakma/iptal/onay, üyelik devri ve dönem temizliği.
- Ayrı örnek veritabanı ve ayrı Chrome oturumlarıyla 32 gerçek tarayıcı kontrolü geçti: davetle kayıt, gerçek giriş, kaptanın görev açması, iki teklif/seçim, nazik seçilmeme, sonucun düzeltilmesi/onaylanması/arşiv, danışmana erişim engeli ve 320/390/1280px ana ekranlarda taşma kontrolü. Danışman ekranları 320px'de ayrıca kontrol edildi; JavaScript hatası çıkmadı. Bilgisayar panosu/mobil detay/mobil danışman özeti görüntüleri incelendi. Bu fiziksel telefon veya Selim/Arda kullanıcı testi değildir.
- Test hesapları gerçek çalışma veritabanında oluşturulmadı. Gerçek ilk danışman hesabı `baslat.bat` ilk açılışında kendi parolasıyla oluşturulur. GitHub gönderimi ve internet yayını ayrıca yapılır.


## 19 Ekim — adım 1: pano kartlarının görünümü

Batu görsel geliştirmeleri tek tek istedi ve ilk kart düzenlemesine “tamam yaparım devam et” diyerek devam onayı verdi. Kartlarda başlık/boşluk düzeni, daha yumuşak köşeler ve gölge; alt satırda açan/son tarih/üstlenen bilgisi ve belirgin inceleme bağlantısı uygulandı. Açık temada yeşil vurgu, koyu temada antrasit yüzey korunur. Var olan hafif yükselme hareketine bağlantı okunda küçük hareket eşlik eder; azaltılmış harekette kapanır. CSS sürüm bağlantısı yenilendi.

Ayrı örnek DB/Chrome’da 30 odaklı kontrol geçti: 320/390/1280px iki tema, üç iş durumu, kart alt satırlarının sığması, en az 44px dokunma alanı, detay bağlantısı, üstlenen adının korunması, hover ve azaltılmış hareket. Tek Django render testi yedi sayfayı açtı; kartın açık/koyu görüntüleri incelendi. Önceki tam 40/43/12 kontroller bu küçük görsel değişiklikten önceydi; tamamı tekrar çalıştırılmadı. Gerçek hesap/yedek/iş kuralları değişmedi; yeni push/yayın yok. Sonraki görsel adım kullanıcı değerlendirmesinden sonra düğmeler olabilir.
