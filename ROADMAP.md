# DevOps Yol Haritası

Hedef: günde 2 saat çalışmayla Linux ve DevOps uzmanlığı → remote iş, ardından AB'de relocate.
Kaynaklar: Udemy kursları (Linux, Docker, AWS, Terraform+AWS, Kubernetes) + resmi dokümanlar + YouTube.

Toplam: 21 sprint, 166 görev, ~506 saat (≈ 9–10 ay, haftada 6 gün × 2 saat).

Ayrıntılı görevler (kaynak, hedef, süre, kanıt) GitHub issue'larında. Sprint = Milestone.

**Aktif sprint: Sprint 01.** Sonraki sprintlerin detayları sırası geldikçe gözden geçirilir. Not: ortam CachyOS (Arch tabanlı); paket yönetimi görevleri `pacman` ile uyarlandı.

## Sprint 01 — Linux I — ortam, kabuk ve dosya sistemi
**Hedefler**
- Çalışan, yedekli bir Linux çalışma ortamı
- Kabuk, yardım sistemi ve dizin gezintisinde akıcılık
- Git/GitHub günlük akışı

- [ ] #13 CachyOS ortamını belgele ve güvenceye al — 2 sa
- [ ] #14 Sistem mimarisi ve kabuğun çalışma şekli — 3 sa
- [ ] #15 Kısayollar ve yardım sistemi — 3 sa
- [ ] #16 Dizinlerde gezinti — 4 sa
- [ ] #17 Joker karakterler ve kabuk genişletmeleri — 3 sa
- [ ] #18 Dosya işlemleri ve bağlantılar — 3 sa
- [ ] #19 Git temelleri ve GitHub akışı — 4 sa
- [ ] #166 Makineyi test sunucusuna çevir: Nginx + MariaDB — 4 sa
- [ ] #20 Sprint retro ve notlar — 1 sa

## Sprint 02 — Linux II — metin işleme, editör, arşiv ve sistem bilgisi
**Hedefler**
- Boru hattı (pipe) ile veri işleme: grep/sed/awk
- Vim ile rahat düzenleme
- Arşiv, yedek ve sistem bilgisi araçları

- [ ] #21 Metin verilerini işlemek — 3 sa
- [ ] #22 Metinleri filtrelemek: grep, regex, find — 4 sa
- [ ] #23 sed ve awk — 3 sa
- [ ] #24 Vim ve nano — 3 sa
- [ ] #25 Arşivleme, sıkıştırma ve rsync — 3 sa
- [ ] #26 Sistem bilgisi araçları — 3 sa
- [ ] #27 Bandit ile pratik: ağ ve SSH seviyeleri — 3 sa
- [ ] #28 Sprint retro ve notlar — 1 sa

## Sprint 03 — Linux III — sistem yönetimi
**Hedefler**
- Paket, kullanıcı, izin ve disk yönetimi
- Süreç ve systemd servis yönetimi
- Log okuma ve sorun giderme

- [ ] #29 Paket yönetimi: pacman (CachyOS) ve apt karşılaştırması — 4 sa
- [ ] #30 Kullanıcı ve grup yönetimi — 4 sa
- [ ] #31 Dosya izinleri, ACL ve özel bitler — 3 sa
- [ ] #32 Disk yönetimi: bölüm, dosya sistemi, mount, LVM — 4 sa
- [ ] #33 Süreç yönetimi — 3 sa
- [ ] #34 systemd: servis ve zamanlayıcı yazmak — 3 sa
- [ ] #35 Log yönetimi: journald, rsyslog, logrotate — 3 sa
- [ ] #36 Sprint retro ve notlar — 1 sa

## Sprint 04 — Ağ, güvenlik duvarı ve Bash scripting
**Hedefler**
- TCP/IP, DNS, HTTP/TLS temelleri
- Firewall ve SSH sertleştirme
- Güvenilir Bash script yazmak

- [ ] #37 Ağ temelleri: OSI, TCP/IP, IP ve alt ağlar — 4 sa
- [ ] #38 Ağ komutları — 4 sa
- [ ] #39 DNS, HTTP ve TLS derinlemesine — 3 sa
- [ ] #40 Güvenlik duvarı: ufw ve nftables — 3 sa
- [ ] #41 SSH'ı sertleştirmek ve tünelleme — 3 sa
- [ ] #42 Bash scripting I: temeller — 3 sa
- [ ] #43 Bash scripting II: gerçek bir operasyon script'i — 4 sa
- [ ] #44 Sprint retro ve notlar — 1 sa

## Sprint 05 — Docker derinlemesine
**Hedefler**
- Image katmanları, multi-stage build ve küçük imajlar
- Ağ, volume ve Compose üretim desenleri
- Konteyner güvenliği ve registry

- [ ] #45 Docker kursunu bitir — 3 sa
- [ ] #46 Image iç yapısı ve build cache — 3 sa
- [ ] #47 Multi-stage build ve küçük imaj — 4 sa
- [ ] #48 Ağ ve volume derinlemesine — 3 sa
- [ ] #49 Compose ile üretime yakın yığın — 4 sa
- [ ] #50 Konteyner güvenliği — 3 sa
- [ ] #51 Registry ve imaj dağıtımı — 3 sa
- [ ] #52 Sprint retro ve notlar — 1 sa

## Sprint 06 — Web sunucu yığını: Nginx, PHP-FPM, TLS ve veritabanı
**Hedefler**
- Nginx reverse proxy + TLS
- PHP-FPM ayarı ve Laravel üretim kurulumu
- Veritabanı yedek/geri yükleme

- [ ] #53 Nginx temelleri — 3 sa
- [ ] #54 Nginx: reverse proxy, load balancing, cache — 3 sa
- [ ] #55 TLS ve HTTPS — 3 sa
- [ ] #56 PHP-FPM ve Laravel üretim ayarları — 4 sa
- [ ] #57 MySQL/MariaDB operasyonu — 4 sa
- [ ] #58 Yedekleme ve geri yükleme tatbikatı — 3 sa
- [ ] #59 Laravel'i boş bir sunucuya elle üretime almak — 4 sa
- [ ] #60 Sprint retro ve notlar — 1 sa

## Sprint 07 — Redis derinlemesine
**Hedefler**
- Veri yapıları ve kullanım örüntüleri
- Kalıcılık, bellek ve eviction
- Replikasyon, Sentinel ve Cluster
- Laravel entegrasyonu

- [ ] #61 Redis veri yapıları I: string, hash, list, set — 3 sa
- [ ] #62 Redis veri yapıları II: sorted set, stream, pub/sub — 3 sa
- [ ] #63 Kalıcılık: RDB ve AOF — 3 sa
- [ ] #64 Bellek yönetimi ve eviction — 3 sa
- [ ] #65 Replikasyon ve Sentinel — 4 sa
- [ ] #66 Redis Cluster'a giriş — 3 sa
- [ ] #67 Laravel + Redis: cache, session, queue, Horizon, kilitler — 3 sa
- [ ] #68 Sprint retro ve notlar — 1 sa

## Sprint 08 — CI/CD — GitLab CI ve GitHub Actions
**Hedefler**
- Test→build→tara→deploy hattını uçtan uca kurmak
- Cache, artifact, ortam ve gizli değişken yönetimi
- İş yerindeki pipeline'a ölçülebilir katkı

- [ ] #69 CI/CD kavramları ve GitLab CI'a giriş — 3 sa
- [ ] #70 .gitlab-ci.yml derinlemesine — 4 sa
- [ ] #71 CI içinde Docker build — 3 sa
- [ ] #72 Laravel + Vue için tam CI — 3 sa
- [ ] #73 Deploy stratejileri — 4 sa
- [ ] #74 Pipeline güvenliği — 3 sa
- [ ] #75 GitHub Actions: aynı pipeline'ı taşı — 3 sa
- [ ] #76 İş yerinde pipeline iyileştirmesi — 2 sa
- [ ] #77 Sprint retro ve notlar — 1 sa

## Sprint 09 — Terraform — Infrastructure as Code
**Hedefler**
- HCL, state, modül ve workspace
- AWS'te güvenli hesap kurulumu
- Terraform için CI ve doğrulama

- [ ] #78 Terraform kurulumu ve temel kavramlar — 3 sa
- [ ] #79 HCL derinlemesine — 3 sa
- [ ] #80 State yönetimi — 3 sa
- [ ] #81 Modüller — 3 sa
- [ ] #82 AWS temelleri ve güvenli hesap kurulumu — 4 sa
- [ ] #83 Terraform ile AWS: EC2, SG, S3 — 3 sa
- [ ] #84 İleri konular ve kalite kapıları — 4 sa
- [ ] #85 Sprint retro ve notlar — 1 sa

## Sprint 10 — AWS çekirdek servisleri
**Hedefler**
- IAM, VPC, EC2/ASG/ALB, S3, RDS, CloudWatch
- Üç katmanlı mini ortamı Terraform ile kurmak
- Maliyet bilinci

- [ ] #86 IAM derinlemesine — 3 sa
- [ ] #87 VPC ve ağ tasarımı — 4 sa
- [ ] #88 EC2, EBS, ELB ve Auto Scaling — 4 sa
- [ ] #89 S3, CloudFront ve Route 53 — 3 sa
- [ ] #90 RDS ve ElastiCache — 3 sa
- [ ] #91 İzleme, denetim ve maliyet — 3 sa
- [ ] #92 Terraform ile 3 katmanlı mini ortam — 4 sa
- [ ] #93 Sprint retro ve notlar — 1 sa

## Sprint 11 — Ansible — yapılandırma yönetimi
**Hedefler**
- Inventory, playbook, role ve vault
- Laravel yığınını Ansible ile kurmak
- Sunucu sertleştirme role'ü

- [ ] #94 Ansible kavramları ve ad-hoc komutlar — 3 sa
- [ ] #95 Playbook ve temel modüller — 3 sa
- [ ] #96 Role'ler, Galaxy ve lint — 4 sa
- [ ] #97 Vault, değişken önceliği ve Jinja2 — 3 sa
- [ ] #98 Laravel yığınını Ansible ile kurmak — 4 sa
- [ ] #99 Terraform + Ansible birleşimi — 3 sa
- [ ] #100 Sunucu sertleştirme role'ü — 3 sa
- [ ] #101 Sprint retro ve notlar — 1 sa

## Sprint 12 — Kubernetes I — mimari, küme ve temel nesneler
**Hedefler**
- Mimariyi ve bileşenleri anlamak
- Yerel kümede Pod/Deployment/Service/Ingress
- ConfigMap, Secret, probe ve kaynak limitleri

- [ ] #102 Kubernetes mimarisi — 3 sa
- [ ] #103 Yerel küme kurulumu — 3 sa
- [ ] #104 Pod, ReplicaSet ve Deployment — 4 sa
- [ ] #105 Service ve Ingress — 4 sa
- [ ] #106 ConfigMap, Secret, probe ve kaynak limitleri — 3 sa
- [ ] #107 Namespace, label ve kubectl ustalığı — 3 sa
- [ ] #108 Killercoda ile ilk pratikler — 3 sa
- [ ] #109 Sprint retro ve notlar — 1 sa

## Sprint 13 — Kubernetes II — depolama, ağ, zamanlama ve güvenlik
**Hedefler**
- PV/PVC ve StatefulSet
- Zamanlama, ağ ve NetworkPolicy
- RBAC, HPA ve sorun giderme

- [ ] #110 Volume, PV, PVC ve StorageClass — 3 sa
- [ ] #111 StatefulSet: MySQL ve Redis — 4 sa
- [ ] #112 Zamanlama: affinity, taint ve PDB — 3 sa
- [ ] #113 Kubernetes ağı: CNI, CoreDNS, NetworkPolicy — 4 sa
- [ ] #114 RBAC ve ServiceAccount — 3 sa
- [ ] #115 Job, CronJob, DaemonSet ve HPA — 3 sa
- [ ] #116 Sorun giderme: bozuk manifestler — 3 sa
- [ ] #117 Sprint retro ve notlar — 1 sa

## Sprint 14 — Kubernetes III — Helm, Kustomize, GitOps ve ilk başvurular
**Hedefler**
- Helm ve Kustomize
- Argo CD ile GitOps
- Laravel+Vue+Redis+MySQL'i Kubernetes'e taşımak
- Başvuruya başlamak

- [ ] #118 Helm: kullanım ve chart yazma — 4 sa
- [ ] #119 Kustomize ile ortam katmanları — 3 sa
- [ ] #120 Argo CD ile GitOps — 4 sa
- [ ] #121 Proje: Laravel+Vue+Redis+MySQL'i Kubernetes'e taşı — 4 sa
- [ ] #122 GitOps boru hattı: CI → registry → Argo CD — 4 sa
- [ ] #123 KİLOMETRE TAŞI: CV v2 ve ilk başvurular — 3 sa
- [ ] #124 Sprint retro ve notlar — 1 sa

## Sprint 15 — Gözlemlenebilirlik — Prometheus, Grafana, Loki
**Hedefler**
- Metrik, log ve alarm hattı
- SLI/SLO ve runbook
- Kasıtlı arıza + postmortem

- [ ] #125 Prometheus mimarisi ve PromQL — 4 sa
- [ ] #126 Grafana panoları ve alarmlar — 3 sa
- [ ] #127 Uygulama ve altyapı exporter'ları — 4 sa
- [ ] #128 Loki ile merkezi log — 3 sa
- [ ] #129 Kubernetes'te kube-prometheus-stack — 4 sa
- [ ] #130 Alertmanager, SLI/SLO ve runbook — 3 sa
- [ ] #131 Arıza tatbikatı ve postmortem — 3 sa
- [ ] #132 Sprint retro ve notlar — 1 sa

## Sprint 16 — DevSecOps — Kali, sertleştirme, container ve K8s güvenliği
**Hedefler**
- İzole lab'da saldırı/savunma
- Linux, imaj ve K8s sertleştirme
- Secret yönetimi

- [ ] #133 Kali VM ve izole lab ağı — 3 sa
- [ ] #134 Zafiyetli hedef ve tarama (kendi lab'ında) — 4 sa
- [ ] #135 OWASP Top 10 ve Laravel güvenliği — 3 sa
- [ ] #136 Linux sertleştirme — 3 sa
- [ ] #137 Konteyner ve imaj güvenliği — 3 sa
- [ ] #138 Kubernetes güvenliği — 4 sa
- [ ] #139 Secret yönetimi — 3 sa
- [ ] #140 Sprint retro ve notlar — 1 sa

## Sprint 17 — AWS ileri — ECS/EKS, serverless ve SAA hazırlığı
**Hedefler**
- ECS/Fargate ve EKS'e giriş
- Serverless ve olay tabanlı mimari
- SAA sınavına hazır olmak

- [ ] #141 ECS ve Fargate — 4 sa
- [ ] #142 EKS'e giriş (maliyet dikkat) — 4 sa
- [ ] #143 Serverless ve olay tabanlı servisler — 3 sa
- [ ] #144 Well-Architected ve felaket kurtarma — 3 sa
- [ ] #145 Güncel SAA sınav kılavuzu ve deneme sınavı 1 — 3 sa
- [ ] #146 Zayıf alan çalışması ve deneme sınavı 2 — 4 sa
- [ ] #147 Sınav günü (opsiyonel) — 2 sa
- [ ] #148 Sprint retro ve notlar — 1 sa

## Sprint 18 — Capstone I — tasarım ve platformu kurmak
**Hedefler**
- Uçtan uca platformun mimarisi
- IaC + CI + GitOps + izleme + güvenlik

- [ ] #149 Mimari tasarım belgesi — 3 sa
- [ ] #150 Altyapıyı Terraform ile kodla — 4 sa
- [ ] #151 CI: build, test, tara, push — 4 sa
- [ ] #152 GitOps dağıtımı ve ortamlar — 4 sa
- [ ] #153 İzleme ve log entegrasyonu — 4 sa
- [ ] #154 Güvenlik katmanı — 3 sa
- [ ] #155 Sprint retro ve notlar — 1 sa

## Sprint 19 — Capstone II — dayanıklılık, tatbikat ve dokümantasyon
**Hedefler**
- Yük ve arıza testleri
- Yedekten kurtarma
- Portfolyoya hazır dokümantasyon

- [ ] #156 Yük testi ve otomatik ölçekleme — 3 sa
- [ ] #157 Arıza tatbikatları (chaos) — 4 sa
- [ ] #158 Yedekten kurtarma tatbikatı — 4 sa
- [ ] #159 Runbook'lar ve postmortem'ler — 3 sa
- [ ] #160 README, diyagramlar ve demo kaydı — 4 sa
- [ ] #161 Blog yazısı ve öğrenilenler — 3 sa
- [ ] #162 Sprint retro ve notlar — 1 sa

## Sprint 20 — Pazara çıkış — CV, mülakat ve AB hedefi
**Hedefler**
- Güçlü CV (EN/TR) ve profil
- Mülakat hazırlığı
- AB remote→relocate stratejisi

- [ ] #163 CV (EN) yeniden yazımı — 4 sa
- [ ] #164 CV (TR), LinkedIn ve GitHub profili — 3 sa
- [ ] (issue henüz açılmadı) Mülakat I: Linux ve ağ — 3 sa
- [ ] (issue henüz açılmadı) Mülakat II: Docker, Kubernetes, CI/CD, Terraform — 4 sa
- [ ] (issue henüz açılmadı) AB hedefi: remote şirketler ve relocate yolu — 3 sa
- [ ] (issue henüz açılmadı) Başvuru sistemi — 3 sa
- [ ] (issue henüz açılmadı) Davranışsal mülakat ve maaş müzakeresi — 3 sa
- [ ] (issue henüz açılmadı) Sprint retro ve notlar — 1 sa

## Sprint 21 — Yan hat — Node.js ve PHP ekosistemi (Symfony/Shopware)
**Hedefler**
- DevOps bağlamında Node.js akıcılığı
- Symfony ve Shopware'e güncel bakış

- [ ] (issue henüz açılmadı) Node.js temellerini tazele — 3 sa
- [ ] (issue henüz açılmadı) Express/Fastify API + Docker + CI — 4 sa
- [ ] (issue henüz açılmadı) Symfony 7 hızlı geçiş — 4 sa
- [ ] (issue henüz açılmadı) Symfony: Messenger ve Doctrine — 3 sa
- [ ] (issue henüz açılmadı) Shopware 6: eklenti mimarisi ve dev ortamı — 4 sa
- [ ] (issue henüz açılmadı) Symfony/Shopware için CI/CD ve konteyner — 3 sa
- [ ] (issue henüz açılmadı) Sprint retro ve notlar — 1 sa
