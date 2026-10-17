# Teknoloji karşılaştırması ve öneri

Bu belge iki seçeneği karşılaştırır. Batu 12 Ekim’de gerçek uygulama için A seçeneği Django’yu seçti; proje .venv içinde kurulum kaydı mevcut. Üç ekranlık geri bildirim demosu bağımlılıksız HTML/CSS/JavaScript’tir; gerçek giriş ve paylaşılan veritabanı sunmaz.

| Seçenek | Artıları | Eksileri / gerekli çalışma |
|---|---|---|
| A — Django + SQLite + HTML/CSS, az JavaScript | Python tabanı; framework giriş/oturum/izin araçları; tek web arayüzüyle telefon ve bilgisayar; model ve şema değişikliklerini düzenli yönetme imkânı | Django öğrenme ve ilk kurulum; mevcut tek dosyalı API'nin iş kuralları taşınmalı; sahiplik, akış ve nesne düzeyindeki izinler ayrıca yazılmalı |
| B — Mevcut Python standart kütüphane + SQLite API ve HTML/CSS/JavaScript web panelini uyarlama | Mevcut giriş, teklif, onay akışları ve web panelinden yararlanma; az yeni bağımlılık | Roller/veri/erişim/akış geniş ölçüde değişecek; oturum ve yetki altyapısının bakımı elde kalacak; fotoğraf, özel yorum görünürlüğü ve eski mobil/web kısıtları temizlenmeli |

## Seçim: A, sade web pilotu

Batu gerçek uygulama için Django ve SQLite ile tek web panosu tercih etti. Gerekçe: bu pilotun asıl zorluğu çok ekran değil, rol/sahiplik ve durum kurallarının doğru uygulanmasıdır. Framework'ün giriş ve izin temeli tekrarlanan altyapı işini azaltabilir. Bunun iki haftada tamamlanacağı garanti değildir; tasarım ve uygulama süreleri birbirine karıştırılmaz. Takımın Django deneyimi yoksa ve ilk kullanım tarihi çok yakınsa B seçeneği tekrar değerlendirilir.

Django'nun kullanıcı, oturum ve grup/izin araçları bulunduğu resmi belgede doğrulandı. Ancak bunlar “isteğin sahibi mi?” veya “onay bekliyor mu?” kurallarını kendiliğinden çözmez; açık iş kuralları şarttır. Kaynak: [Django kimlik doğrulama ve izinler](https://docs.djangoproject.com/en/5.2/topics/auth/default/) (2026-10-08 erişimi; sürüm numarası burada kurulum taahhüdü değildir).

SQLite için eşzamanlı yazma kapasitesi sınırlıdır; kabul işlemleri kısa veritabanı işlemleriyle yapılmalı, kilit/çakışma hataları kullanıcıya anlaşılır gösterilmelidir. Seçilen işlem kayıt sürümüyle koşullu güncelleme yapar; iki adayı aynı anda atamaz. Takım ölçeği büyür veya kilit sorunları görülürse PostgreSQL'e geçiş değerlendirilebilir. Kaynak: [Django SQLite notları](https://docs.djangoproject.com/en/5.2/ref/databases/#sqlite-notes). Python standart kütüphanesinde SQLite erişimi mevcut olduğundan B seçeneği yeni veritabanı sürücüsü gerektirmez: [Python sqlite3](https://docs.python.org/3/library/sqlite3.html).

## Basit uygulama yerleşimi

```text
Telefon / PC tarayıcı
        |
        v
Web sunucusu + tek uygulama
  - oturum ve aktif üyelik
  - rol / sahiplik izinleri
  - görev / talep geçişleri
  - ortak yorumlar
  - takım ve danışman görünümleri
        |
        v
SQLite: kullanıcı + istek + adaylık + yorum + olay + bildirim
```

Her ekran aynı kaynağı okur. Danışman verisi istemciye gönderilip CSS ile saklanmaz; sunucu yetkisiz isteği reddeder. Arayüz düzenli yeniden yükleme ile güncellenebilir; ilk pilot için gerçek zamanlı bağlantı, mağaza dağıtımı veya push şart değildir. 48 saatlik danışman kuyruğu olay zamanlarından hesaplanır; sayfa açıldığında ve günlük kontrolde görünür. İnternet yayınına geçilirse HTTPS ve güvenli oturum çerezleri gerekir; geliştirme sunucusu doğrudan yayınlanmaz. Üç ekranlık demo GitHub Pages planındadır; gerçek Django uygulaması için ücretsiz PythonAnywhere başlangıç planıyla ilerlenir. Hesap açılışı/yayın henüz yapılmış sayılmaz.

## Dayanışma Ağı ile ilişki

Mevcut proje okul geneli onarım/ders yardımıdır; yeni pano takım içi görev/talep pilotudur. İlk tasarım ayrı klasör ve kendi GitHub reposunda tutulur. Mevcut proje yerinde korunur.

Sonraki uygulamada yeniden değerlendirilebilecekler: giriş deneyimi, aday teklif/seçme, işi bırakma, yapıldı/onaylama mantığı ve testlerdeki senaryo yaklaşımı. Doğrudan taşınmayacaklar: onarımda ilk tıklayana atama, öğrenci/öğretmen/yönetici rolleri, öğrenci web yasağı, fotoğraf yükleme, beceri/konum profilleri, yalnız katılımcılara görünen yorumlar ve teşekkür sayacı.

Görev/Talep adları eski Onarım/Ders alanlarının yalnız yeniden adlandırılmasıyla çözülmez. Eski çalışma DB'si yeni modele bağlanmaz. Birleştirme kararı seçilen tasarımın kapsamı netleşince verilir; tek takım pilotunda öğrenilen süreç büyük okul projesine aktarılabilir.

## Uygulamaya geçildiğinde kabul ölçütleri

Rol/sahiplik izinleri, iki eşzamanlı kabulde tek kazanan, tekrar tıklamada tek onay, bırakma sonrası yeniden adaylık, geciken onay kuyruğu, pasifleştirmenin oturum/iş etkisi, tüm takıma açık yorumlar, kişi özetine üye/kaptanın erişememesi ve fotoğraf/puan alanlarının reddi doğrulanır. Bunlar mevcut taslağın kodla doğrulandığı iddiası değildir.

## Batu’nun seçim nedeni ve öğrenme sınırı

Batu’nun 12 Ekim kendi beyanı: “senin önerin ile daha kolay erişebilirlik yüzünden seçtim.” Asistan önerisi ve kendisine erişilebilir gelmesi seçimin nedenidir. Bu beyan Django’da deneyim veya alternatiflere göre ölçülmüş kolaylık iddiası değildir. Batu Python’da değişkenler aşamasında; HTML/CSS/JavaScript’e sıfırdan başlıyor. Gerekli parçalar proje içinde açıklanacak; gerekçeyi sunumda kendi cümleleriyle savunması gereklidir.

Kurulum kaydına göre .venv içinde Django 5.2.18 kurulmuştur; requirements.txt paketleri sabitler. Global Python değiştirilmez. Uygulama, demo, GitHub yayını ve gerçek hesap kurulumu birbirinden ayrı sonuçlardır.

## Yayın ve bakım

Demo: GitHub Pages’te HTML/CSS/JavaScript. Gerçek uygulama: PythonAnywhere ücretsiz başlangıç planı; bakım Batu’da, Codex oturumlarda yardımcı. Ücretsiz planda bir web uygulaması, 512 MiB toplam hesap alanı ve bir aylık süre uzatma takibi vardır (12 Ekim resmî belge kontrolü). Kurulum boyutu/kullanımı yayın sırasında ölçülür; yedekler PC’de tutulacak şekilde planlanır. Otomatik kota izleme, yedekleme veya sürekli bakım henüz kurulmadı.

Kaynaklar: [Ücretsiz plan](https://help.pythonanywhere.com/pages/FreeAccountsFeatures/), [süre uzatma](https://blog.pythonanywhere.com/129/), [Django yayını](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/), [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## 17 Ekim — yayın planı ve öğrenci gerekçesi kontrolü

PythonAnywhere resmî ücretsiz planı 17 Ekim’de tekrar kontrol edildi: 1 web uygulaması/1 worker, 512 MiB alan ve 1 aylık uzatma takibi var. Yeni ücretsiz hesapta zamanlanmış görev yok; bu nedenle otomatik günlük temizlik/yedek çalışacağı varsayılamaz. Bakım sahibi Batu, teknik_temizle ve donem_temizle komutlarının takibini ANA-SITE.md üzerinden yapmalı; otomatik zamanlayıcı ayrıca kurulmadan işletilmiş sayılmaz. Kaynak: [güncel ücretsiz hesap özellikleri](https://help.pythonanywhere.com/pages/FreeAccountsFeatures/), [2026 değişikliği](https://blog.pythonanywhere.com/221/). Hesap açılışı ve internet yayını henüz yapılmadı.

Batu’nun 17 Ekim kendi açıklaması henüz alınmadı. README’deki kısa gerekçe soruları bunun için var; yukarıdaki asistan açıklaması öğrenci cevabının yerini tutmaz.
