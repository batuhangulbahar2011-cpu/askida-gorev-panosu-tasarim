# Teknoloji karşılaştırması ve öneri

Bu aşamanın teslimi tasarımdır. Aşağıdaki seçenekler seçilen tasarımın sonraki uygulaması içindir; şu an kurulum veya sunucu yayını yapılmaz.

| Seçenek | Artıları | Eksileri / gerekli çalışma |
|---|---|---|
| A — Django + SQLite + HTML/CSS, az JavaScript | Python tabanı; framework giriş/oturum/izin araçları; tek web arayüzüyle telefon ve bilgisayar; model ve şema değişikliklerini düzenli yönetme imkânı | Django öğrenme ve ilk kurulum; mevcut tek dosyalı API'nin iş kuralları taşınmalı; sahiplik, akış ve nesne düzeyindeki izinler ayrıca yazılmalı |
| B — Mevcut Python standart kütüphane + SQLite API ve HTML/CSS/JavaScript web panelini uyarlama | Mevcut giriş, teklif, onay akışları ve web panelinden yararlanma; az yeni bağımlılık | Roller/veri/erişim/akış geniş ölçüde değişecek; oturum ve yetki altyapısının bakımı elde kalacak; fotoğraf, özel yorum görünürlüğü ve eski mobil/web kısıtları temizlenmeli |

## Öneri: A, sade web pilotu

Tasarım seçilirse küçük takım için Django ve SQLite ile tek web panosu öneriyorum. Gerekçe: bu pilotun asıl zorluğu çok ekran değil, rol/sahiplik ve durum kurallarının doğru uygulanmasıdır. Framework'ün giriş ve izin temeli tekrarlanan altyapı işini azaltabilir. Bunun iki haftada tamamlanacağı garanti değildir; tasarım ve uygulama süreleri birbirine karıştırılmaz. Takımın Django deneyimi yoksa ve ilk kullanım tarihi çok yakınsa B seçeneği tekrar değerlendirilir.

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

Her ekran aynı kaynağı okur. Danışman verisi istemciye gönderilip CSS ile saklanmaz; sunucu yetkisiz isteği reddeder. Arayüz düzenli yeniden yükleme ile güncellenebilir; ilk pilot için gerçek zamanlı bağlantı, mağaza dağıtımı veya push şart değildir. 48 saatlik danışman kuyruğu olay zamanlarından hesaplanır; sayfa açıldığında ve günlük kontrolde görünür. İnternet yayınına geçilirse HTTPS ve güvenli oturum çerezleri gerekir; geliştirme sunucusu doğrudan yayınlanmaz. Dağıtım sağlayıcısı bu taslakta seçilmedi.

## Dayanışma Ağı ile ilişki

Mevcut proje okul geneli onarım/ders yardımıdır; yeni pano takım içi görev/talep pilotudur. İlk tasarım ayrı klasör ve kendi GitHub reposunda tutulur. Mevcut proje yerinde korunur.

Sonraki uygulamada yeniden değerlendirilebilecekler: giriş deneyimi, aday teklif/seçme, işi bırakma, yapıldı/onaylama mantığı ve testlerdeki senaryo yaklaşımı. Doğrudan taşınmayacaklar: onarımda ilk tıklayana atama, öğrenci/öğretmen/yönetici rolleri, öğrenci web yasağı, fotoğraf yükleme, beceri/konum profilleri, yalnız katılımcılara görünen yorumlar ve teşekkür sayacı.

Görev/Talep adları eski Onarım/Ders alanlarının yalnız yeniden adlandırılmasıyla çözülmez. Eski çalışma DB'si yeni modele bağlanmaz. Birleştirme kararı seçilen tasarımın kapsamı netleşince verilir; tek takım pilotunda öğrenilen süreç büyük okul projesine aktarılabilir.

## Uygulamaya geçildiğinde kabul ölçütleri

Rol/sahiplik izinleri, iki eşzamanlı kabulde tek kazanan, tekrar tıklamada tek onay, bırakma sonrası yeniden adaylık, geciken onay kuyruğu, pasifleştirmenin oturum/iş etkisi, tüm takıma açık yorumlar, kişi özetine üye/kaptanın erişememesi ve fotoğraf/puan alanlarının reddi doğrulanır. Bunlar mevcut taslağın kodla doğrulandığı iddiası değildir.
