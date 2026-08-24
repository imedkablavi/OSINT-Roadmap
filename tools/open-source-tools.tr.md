# Doğrulanmış Açık Kaynak OSINT Araçları

> Son inceleme: **2026-08-24** · Türkçe · [English](open-source-tools.md) · [العربية](open-source-tools.ar.md)

Bu sayfa, upstream projesi, lisansı ve güncel pratik rolü eklenmeden önce doğrulanmış açık kaynak araçları öne çıkarır. Açık kaynak olması; yetkilendirme, gizlilik, sağlayıcı şartları veya veri saklama sorumluluklarını ortadan kaldırmaz.

| Araç | Lisans | Girdi | En iyi kullanım | Önemli sınırlama |
| --- | --- | --- | --- | --- |
| [theHarvester](https://github.com/laramies/theHarvester) | GPL-2.0 | Domain, kurum | Domain, host ve ilişkili keşif için genel pasif kaynakları bir araya getirmek | Kaynak kapsamı, kotalar ve API anahtarı gereksinimleri değişir; bazı seçenekler ağ etkinliği oluşturur |
| [OWASP Amass](https://github.com/owasp-amass/amass) | Apache-2.0 | Domain, kurum, ASN | Harici varlık keşfi ve saldırı yüzeyi haritalama | Aktif teknikler yalnızca sahip olduğunuz veya açıkça yetkilendirildiğiniz hedeflerde kullanılmalıdır |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | MIT | Domain | Desteklenen kaynaklardan pasif subdomain keşfi | Yararlı birçok sağlayıcı API anahtarı ister ve upstream kaynaklar değişebilir veya kapanabilir |
| [OpenCTI Community Edition](https://github.com/OpenCTI-Platform/opencti) | Apache-2.0 (CE) | IOC, kurum, rapor | STIX2 ile CTI bilgisini yapılandırmak, ilişkilendirmek ve görselleştirmek | Platform bir doğruluk motoru değildir; kaynak ve güven düzeyi analist tarafından değerlendirilmelidir |
| [MISP](https://github.com/MISP/MISP) | AGPL-3.0 | IOC, olay, kurum | Tehdit istihbaratı paylaşımı, yapılandırılmış olaylar ve gösterge toplulukları | Topluluk verisinin kalitesi değişir; paylaşım ve hassas veri için yönetişim gerekir |

## Hangi durumda hangisi?

- **theHarvester:** Birden çok genel kaynağı tek tek sorgulamak yerine seçili kaynakları tekrarlanabilir bir akışta toplamak istediğinizde.
- **OWASP Amass:** Harici varlık keşfini daha derin yapmak istediğinizde; pasif ve aktif toplama adımlarını yetkili kapsam içinde açıkça ayırın.
- **Subfinder:** Otomasyona uygun, odaklı ve pasif bir subdomain numaralandırma aracı gerektiğinde.
- **OpenCTI Community Edition:** Sorun yeni IOC toplamaktan çok CTI bilgisini, ilişkileri, kaynakları ve güven seviyelerini yönetmek olduğunda.
- **MISP:** Bir ekip veya güvenilir topluluk içinde yapılandırılmış tehdit istihbaratı paylaşımı gerektiğinde.

## Güvenli kullanım kuralı

Bir hedefin internette açık olması tarama yetkisi vermez. Pasif sağlayıcılar bile sorgu terimlerini alabilir, kaydedebilir ve kendi şartları ile kotalarını uygular. Aktif DNS çözümleme, probing, scanning veya doğrulama yalnızca sahip olunan ya da açıkça yetkilendirilmiş kapsamla sınırlandırılmalıdır.

Araç çıktısı otomatik kanıt değil, bir **bulgu adayı veya gözlemdir**. Rapora girmeden önce kaynak, zaman, sorgu, güven düzeyi ve önemli sınırlamaları kaydedin.
