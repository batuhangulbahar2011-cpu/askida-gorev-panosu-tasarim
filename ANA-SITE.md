# Askıda Görev Panosu — ana Django sitesi

Bu klasördeki `index.html` üç ekranlık geri bildirim demosudur. Ana site `manage.py` ile çalışan Django uygulamasıdır; kayıtlar SQLite veritabanında ortak tutulur. Tasarım teslimi 22 Ekim'de; ana site geliştirmesi Batu'nun 13 Ekim isteğiyle paralel başlatıldı. Tasarımın gerekçe ve sunum çalışması devam eder.

## Bilgisayarda açma

1. `baslat.bat` dosyasına çift tıkla.
2. İlk açılışta danışmanın kullanıcı adı, adı ve kendi belirlediği parolası istenir. Parola yazarken ekranda görünmez. Önceden kurulmuş hesaplar değiştirilmez.
3. Pencere açıkken tarayıcıda **http://127.0.0.1:8000/** adresine git.
4. Danışman olarak giriş yap; **Takım → Kayıt kodu üret**. Kodu üye olacak kişiye ver. Kişi **Davetle kayıt** ekranından kendi parolasını belirler. Rolü başlangıçta Üye; yalnız danışman değiştirebilir.

Hazır/parolası herkese açık bir yönetici hesabı yoktur. İlk danışman kurulumu site üzerinden herkese açık değildir. Bu yerel adres bilgisayarda çalışır; internetten erişilebilir yayın yapılmış anlamına gelmez.

## Gerçekleşen kapsam

- Gerçek hesap/giriş/çıkış; 7 günlük tek kullanımlık kayıt ve 24 saatlik hedef hesaba özel parola yenileme kodu.
- Görev ve Talep panoları; sadece kendi açtıkları/üstlendikleri filtreleri; görevde amaç/son tarih ve rol denetimi.
- Teklif/kabul, sonuç bildirme, onay/düzeltme, gerekçeli bırakma/geri çekme, ortak yorum, danışmana bildirme.
- Sunucuda teklif gizliliği; kişisel bildirimler; ortak akışta seçilmeyen aday notu/kimliği sızdırılmaz.
- Arşiv; 48 saat/gecikme/bildirim incelemesi; danışmana alfabetik kişi özeti; son danışmanın korunması; rol/pasifleştirme/devretme.
- Dönem kapanışı ve 90 günlük silme bakım komutu. Aktif hesaplar korunur. Otomatik zamanlayıcı kurulmadı.

## Bakım ve veri

Parola, kod, SQLite veritabanı ve yerel gizli anahtar Git'e alınmaz. Ham kod yalnız üretildiğinde gösterilir; veritabanında özet saklanır. E-posta, telefon, adres, fotoğraf, özel sohbet, puan/kredi/rozet yoktur. Giriş deneme sayaçları kullanıcı adının özeti ve 15 dakikalık süre taşır; IP kaydetmez.

İlk danışman parolasını unutursa Batu kimlik doğrulamasından sonra:

```powershell
.venv\Scripts\python.exe manage.py danisman_kurtar kullanici_adi
```

Süresi dolmuş teknik kayıtlar:

```powershell
.venv\Scripts\python.exe manage.py teknik_temizle
```

Dönem kapanışından 90 gün sonra önce önizleme, ardından gerçek temizlik:

```powershell
.venv\Scripts\python.exe manage.py donem_temizle
.venv\Scripts\python.exe manage.py donem_temizle --uygula
```

Silme komutu yeni dönemi açar; zamanından önce dönem kayıtlarını silmez. Otomatik yedek/saklama zamanlayıcısı henüz kurulmadı. Yedek gerekiyorsa sunucu kapalıyken `db.sqlite3` dosyasını Git dışındaki güvenli yere kopyala; en fazla 7 gün tut. Yedek geri yüklenirse silme takvimi tekrar uygulanmalı. Bilgisayar açık kalmadan bakım komutları çalışmaz.

## Başka bilgisayarda kurulum

Python ve Git kurulu olmalı. Repoyu aldıktan sonra:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py kurulum
.venv\Scripts\python.exe manage.py runserver
```

## Kontrol ve yayın

```powershell
.venv\Scripts\python.exe manage.py check
.venv\Scripts\python.exe manage.py test pano
```

Gerçek yayın planı ücretsiz PythonAnywhere; hesap ve dağıtım bu adımda yapılmaz. Yayında `DJANGO_DEBUG=0`, güçlü `DJANGO_SECRET_KEY`, gerçek alan adıyla `DJANGO_ALLOWED_HOSTS`, HTTPS ve statik dosya sunumu gerekir. `collectstatic` ve `check --deploy` dağıtımdan önce çalıştırılır. WSGI uygulaması `config.wsgi.application`. Geliştirme sunucusu internette kullanılmaz. Sağlayıcı erişim logları ve yedek saklama ayarları ayrıca kontrol edilir; yerel uygulama altyapı sağlayıcısının kayıtlarını kontrol etmiş sayılmaz.

Başvuru kaynakları: [Django hesap modeli](https://docs.djangoproject.com/en/5.2/topics/auth/customizing/), [SQLite işlemleri](https://docs.djangoproject.com/en/5.2/ref/databases/#sqlite-notes), [yayın kontrol listesi](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/).

## 17 Ekim geliştirmesi

Pano: başlık araması, durum ve kendi açtıkları/üstlendikleri birlikte filtrelenebilir; sekme değişince seçimler korunur. Arşiv: görev/talep ve bütün dönem/bu hafta/bu ay filtreleri; sonuç sekmesi değişince filtreler korunur. Kapalı istekte yeni yorum yoktur, itiraz bildirimi devam eder. Çözülmüş şikâyet tek başına danışman müdahalesine yetmez; yorum temizleme açık şikâyeti kendiliğinden kapatmaz.

40 Django testi ayrı veritabanında geçti. Mevcut sunucu açıksa Ctrl+C, sonra baslat.bat ile yeniden başlat ve tarayıcıda Ctrl+F5 yap. Yeni hesap açman gerekmez. İnternet yayını ve gerçek telefon/takım denemesi ayrı açık işlerdir.

17 Ekim son tarayıcı kontrolü: ayrı örnek DB ve Chrome oturumlarında 40 kontrol geçti; 320/390/1280px taşma denetimleri, filtrelerin kullanımı, sekmede korunması, kapalı kayıt ve teklif gizliliği. JavaScript hatası yok. Masaüstü pano ve mobil detay görüntüleri incelendi. Fiziksel telefon testi değildir.
