# Doğrulanmış Açık Kaynak OSINT Araçları

> Son inceleme: **2026-08-24** · Türkçe · [English](open-source-tools.md) · [العربية](open-source-tools.ar.md)

Bu sayfada **Open Source** etiketi yalnızca güncel upstream proje ve lisans doğrulandıktan sonra kullanılır. Kaynak kodunun herkese açık olması, açık bir lisans yoksa bu projede açık kaynak olarak işaretlenmesi için yeterli değildir.

## Keşif, arşivleme ve kimlik

| Araç | Lisans | Pratik rol | Temel sınırlama |
| --- | --- | --- | --- |
| [Bellingcat Auto Archiver](https://github.com/bellingcat/auto-archiver) | MIT | Genel bağlantı, medya ve sosyal gönderileri otomatik koruma | Arşiv kaynağı ve yakalama zamanı ayrıca kaydedilmelidir |
| [Browsertrix](https://github.com/webrecorder/browsertrix) | AGPL-3.0 | Tarayıcı tabanlı yüksek doğrulukta web arşivleme | Crawl kapsamı ve erişim kısıtları gözetilmelidir |
| [ReplayWeb.page](https://github.com/webrecorder/replayweb.page) | AGPL-3.0 | WARC/WACZ arşivlerini yeniden oynatma | Replay tek başına yakalama zamanını veya özgünlüğü kanıtlamaz |
| [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) | GPL-3.0 | Genel telefon numarası araştırmasını ve arama pivotlarını yapılandırma | Numara metadatası abone kimliğini kanıtlamaz |
| [GHunt](https://github.com/mxrch/GHunt) | AGPL-3.0 | Genel Google hesabı/nesnesi OSINT araştırması | Bazı modüller Google oturumu ister; hesap maruziyetini azaltın |

## Altyapı ve CTI

| Araç | Lisans | Pratik rol | Temel sınırlama |
| --- | --- | --- | --- |
| [theHarvester](https://github.com/laramies/theHarvester) | GPL-2.0 | Genel pasif altyapı kaynaklarını birleştirme | Kaynak kapsamı, kota ve API anahtarı gereksinimleri değişir |
| [OWASP Amass](https://github.com/owasp-amass/amass) | Apache-2.0 | Harici varlık keşfi ve ilişki haritalama | Aktif teknikler açık yetki gerektirir |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | MIT | Pasif subdomain numaralandırma | Upstream sağlayıcılar değişebilir veya API anahtarı isteyebilir |
| [OpenCTI Community Edition](https://github.com/OpenCTI-Platform/opencti) | Apache-2.0 (CE) | CTI bilgisini yapılandırma ve ilişkilendirme | Kaynak güveni analistin sorumluluğunda kalır |
| [MISP](https://github.com/MISP/MISP) | AGPL-3.0 | Yapılandırılmış tehdit istihbaratı paylaşımı | Topluluk verisi ve paylaşım politikaları yönetişim gerektirir |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | AGPL-3.0 | IOC ve dosya enrichment işlemlerini orkestre etme | Harici analiz sağlayıcıları gönderilen gösterge veya örnekleri alabilir |
| [YETI](https://github.com/yeti-platform/yeti) | Apache-2.0 | Observable, varlık ve enrichment yönetimi | Bilgiyi düzenlemek her upstream iddiayı doğrulamaz |

## Görsel, medya ve GEOINT

| Araç | Lisans | Pratik rol | Temel sınırlama |
| --- | --- | --- | --- |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Apache-2.0 | Görsel ve taranmış belgelerde yerel OCR | OCR hataları kaynak görselle karşılaştırılmalıdır |
| [MediaInfo](https://github.com/MediaArea/MediaInfo) | BSD-2-Clause | Ses/video teknik metadatasını inceleme | Metadata silinebilir veya yeniden yazılabilir |
| [Sherloq](https://github.com/GuidoBartoli/sherloq) | GPL-3.0 | Dijital görüntü adli analizi | Anomaliler ipucudur, manipülasyon kanıtı değildir |
| [Overpass Turbo](https://github.com/tyrasd/overpass-turbo) | MIT | GEOINT için OpenStreetMap verisini sorgulama | OSM kapsamı ve güncelliği konuma göre değişir |
| [kepler.gl](https://github.com/keplergl/kepler.gl) | MIT | Büyük coğrafi veri setlerini görselleştirme | Görsel korelasyon nedensellik kanıtı değildir |
| [OpenAerialMap](https://github.com/hotosm/openaerialmap) | AGPL-3.0 | Açık lisanslı hava görüntülerini keşfetme | Kapsam, tarih ve çözünürlük önemli ölçüde değişir |

## Analiz ve çalışma alanları

| Araç | Lisans | Pratik rol | Temel sınırlama |
| --- | --- | --- | --- |
| [Datasette](https://github.com/simonw/datasette) | Apache-2.0 | Yapılandırılmış yerel veriyi keşfetme ve sorgulama | Hassas araştırma verisini yanlışlıkla yayınlamayın |
| [Timesketch](https://github.com/google/timesketch) | Apache-2.0 | Ortak olay/zaman çizelgesi analizi | Parser, saat ve zaman dilimi hataları analize taşınır |
| [GraphSense](https://github.com/graphsense/graphsense-dashboard) | MIT | Açık kripto-varlık grafik analizi | Kümeleme ve etiketler bağımsız doğrulama gerektiren hipotezlerdir |

## Güvenli kullanım kuralı

Açık kaynak; yetkilendirme, gizlilik, sağlayıcı şartları veya veri işleme sorumluluğunu ortadan kaldırmaz. Altyapı araştırmasında hedef size ait değilse veya açık izin yoksa pasif toplama tercih edilmelidir. Kimlik, telefon ve hesap araştırmasında kişisel veri toplamayı azaltın. Dosya, URL veya IOC'leri üçüncü taraf analiz servislerine göndermeden önce saklama ve yeniden paylaşım politikasını kontrol edin.

Araç çıktısı otomatik sonuç değil, bir **bulgu adayı veya gözlemdir**. Raporda kullanmadan önce kaynak, zaman, sorgu, güven düzeyi ve sınırlamayı kaydedin.

İpucuna göre hem açık kaynak hem resmi veri kaynaklarını seçmek için [OSINT Araştırmacı Araç Seti](investigator-stack.tr.md) sayfasını kullanın.
