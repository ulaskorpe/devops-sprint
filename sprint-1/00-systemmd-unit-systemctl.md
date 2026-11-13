systemd
systemd, birçok Linux dağıtımında sistemi başlatan ve sistem çalışırken çeşitli bileşenleri yöneten temel yazılımdır. Bilgisayar açılırken gerekli servisleri başlatır; çalışan servislerin durumunu takip eder ve servisler arası başlama sırasını yönetebilir.

Örneğin ağ servisi, zaman senkronizasyonu veya web sunucusu gibi arka planda çalışan programlar systemd tarafından yönetilebilir.

systemctl
systemctl, systemd ile iletişim kurmak ve yönetilen birimleri kontrol etmek için kullanılan komut satırı aracıdır. Servislerin durumunu görüntüleme, başlatma, durdurma ve açılışta otomatik başlatılmasını ayarlama gibi işlemleri yapar.

Örnekler:

bash
Kopyala
systemctl status ssh
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh
Deneyin:
|
Burada ssh servis adıdır. Dağıtıma göre servis adı değişebilir; örneğin bazı sistemlerde SSH servisi sshd olarak adlandırılır.

Unit
Unit, systemd’nin yönettiği bir kaynak veya işi tarif eden yapılandırma birimidir. Unit dosyaları, systemd’ye ilgili kaynağın ne olduğunu ve nasıl yönetileceğini bildirir.

Yaygın unit türleri:

.service — arka plan servisi
.socket — ağ veya yerel soket
.timer — belirli zamanda ya da aralıklarla çalışacak iş
.mount — dosya sistemi bağlama işlemi
.target — bir grup unit’i veya sistemin belirli çalışma aşamasını temsil eder
Bir servis unit’i genellikle .service uzantılıdır. Örneğin cron.service veya nginx.service. Komutlarda çoğu zaman uzantı yazmadan da kullanılabilir:

bash
Kopyala
systemctl status nginx
Deneyin:
|
Birbirleriyle ilişkileri
Kısaca:

systemd: Servisleri ve diğer birimleri yöneten sistem
unit: Yönetilecek servisin ya da kaynağın tanımı
systemctl: Bu tanımları sorgulayıp yönetmek için kullandığın komut
Bunu şöyle düşünebilirsin: systemd yöneticidir, unit yönetilecek işin tanımıdır, systemctl ise yöneticiye verdiğin komut arayüzüdür.

Önemli ayrım: çalışıyor olmak ve açılışta etkin olmak
Bir servisin şu anda çalışıyor olması, bilgisayar her açıldığında otomatik başlayacağı anlamına gelmez. Benzer şekilde, açılışta başlaması etkinleştirilmiş bir servis o anda çalışmıyor olabilir.

active: Servis şu anda çalışıyor.
enabled: Servisin sistem açılışında başlatılması ayarlanmış.
Bunları ayrı ayrı kontrol edebilirsin:

bash
 
systemctl is-active nginx
systemctl is-enabled nginx


systemd nasıl görüntülenir ve yönetilir?
systemd ile servisleri ve diğer unit’leri genellikle systemctl komutuyla yönetirsin. Görüntüleme komutları çoğunlukla normal kullanıcıyla çalışır; sistem servislerini değiştiren işlemler için genellikle sudo gerekir.

Genel sistem bilgisi
bash

systemctl --version
systemctl is-system-running


sudo systemctl start <servis-adı>
sudo systemctl stop <servis-adı>
sudo systemctl restart <servis-adı>
sudo systemctl reload <servis-adı>


start: Çalıştırır.
stop: Durdurur.
restart: Durdurup yeniden başlatır.
reload: Servisin desteklemesi hâlinde, servisi kapatmadan yapılandırmasını yeniden okutmaya çalışır.