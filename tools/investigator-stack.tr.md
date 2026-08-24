# OSINT Araştırmacı Araç Seti

> Son inceleme: **2026-08-24** · Türkçe · [English](investigator-stack.md) · [العربية](investigator-stack.ar.md)

Bu sayfa her aracı çalıştırmanız gereken bir kontrol listesi değil, bir **seçim haritasıdır**. Elinizde gerçekten bulunan ipucuyla başlayın, soruyu cevaplayan en küçük kaynağı kullanın, kaynağı ve zamanı kaydedin ve önemli bulguları bağımsız biçimde doğrulayın.

## Elinizdeki ipucundan başlayın

| Elinizde ne var? | İyi başlangıç araçları | Gerektiğinde ekleyin | Temel sınırlama |
| --- | --- | --- | --- |
| Kullanıcı adı | WhatsMyName, Sherlock, Maigret | GitHub Search, GHunt | Aynı kullanıcı adının kullanılması tek başına kimlik eşleştirmesi değildir |
| E-posta | Have I Been Pwned, Epieos | GHunt | Yalnızca hukuka uygun/yetkili tanımlayıcılar kullanın; ihlal kaydı güncel ele geçirmeyi kanıtlamaz |
| Telefon | PhoneInfoga, Epieos | Arama motorları ve resmi numaralandırma kaynakları | Numara metadatası kullanıcı kimliğini kanıtlamaz |
| Alan adı / URL | ICANN Lookup, crt.sh, Internet Archive, urlscan.io | Common Crawl, SecurityTrails, DNSViz, Subfinder, Amass | Pasif kanıtı tercih edin; aktif teknikler açık yetki gerektirir |
| IP / ASN | RIPEstat, BGP.tools, GreyNoise | Censys, Shodan, IntelOwl | Gözlem zamanı ve tarama verisinin yaşı önemlidir |
| Görsel | Google Lens, TinEye, Yandex Images | ExifTool, Sherloq, Tesseract OCR | Adli görüntü anomalileri ipucudur, manipülasyon kanıtı değildir |
| Video / ses | InVID & WeVerify, FFmpeg, MediaInfo | ExifTool ve kare bazlı kontroller | Kapsayıcı ve etiket metadatası yeniden yazılabilir |
| Konum | OpenStreetMap, Google Maps/Earth, SunCalc | Overpass Turbo, OpenAerialMap, Mapillary, kepler.gl, QGIS | Harita ve görüntü kapsamı bölgeye ve tarihe göre değişir |
| Tarihsel hava / zaman iddiası | NOAA Climate Data Online | NASA FIRMS ve yerel resmi meteoroloji kaynakları | İddiayı kayıtla karşılaştırmadan önce istasyon, saat dilimi, gözlem türü ve veri boşluklarını eşleştirin |
| Şirket | Resmi sicil, OpenCorporates, GLEIF | SEC EDGAR, Companies House, OpenSanctions, ICIJ, USAspending, TED | Kayıtları bağlamadan önce doğru tüzel kişiyi çözümleyin |
| Yaptırım adı/kuruluşu/gemisi | OFAC Sanctions Search, UK Sanctions List, UN Consolidated List | OpenSanctions ve rejime özel resmi listeler | Yaklaşık/ad eşleşmesi kimlik doğrulaması değildir; alias, doğum tarihi/ID ve yaptırım rejimini doğrulayın |
| Lobicilik / politika etkisi | LDA.gov, EU Transparency Register | Yabancı temsil ilişkisi varsa DOJ FARA | Beyanlar bildirilen faaliyeti gösterir; usulsüzlüğü veya gerçek politika etkisini kanıtlamaz |
| ABD'de yabancı müvekkil temsili | DOJ FARA Filings Search | LDA.gov ve birincil dosyalar | Kayıt bir hukuki bildirim statüsüdür, yanlış davranış kanıtı değildir |
| Kamu alımları / sözleşmeler | USAspending.gov, TED | Open Contracting Data Registry ve ulusal ihale portalı | Süreç aşaması, değişiklikler, alt sözleşmeler ve yayıncı veri kalitesi eşleşmenin anlamını değiştirebilir |
| Gerçek faydalanıcı sicili | Ulusal resmi sicil | Yetki alanındaki kaynağı bulmak için Open Ownership Map | Erişim ve kapsam değişir; eski ulusötesi Open Ownership Register kullanımdan kaldırıldı |
| ABD kâr amacı gütmeyen kuruluşu | ProPublica Nonprofit Explorer | Kaynak IRS dosyaları, USAspending | Dosyalama dönemlerini ve işlem gecikmelerini karşılaştırın |
| ABD mahkeme davası/kişi/şirket | CourtListener / RECAP | Dava uyarıları ve birincil mahkeme kaynakları | Yargı alanı ve usul aşaması bağlamı gerekir |
| IOC / hash | VirusTotal, CIRCL hashlookup, abuse.ch | IntelOwl, YETI, MISP, OpenCTI | Bulut servisine gönderilen gösterge veya dosya üçüncü tarafla paylaşılabilir |
| Uçuş / uçak | Flightradar24, ADS-B Exchange, OpenSky | Harita ve hava durumu bağlamı | Kapsama alıcıların konumuna göre değişir |
| Gemi | MarineTraffic, VesselFinder | Global Fishing Watch | AIS kesintileri veya spoofing yanlış sonuca yol açabilir |
| Demiryolu altyapısı | OpenRailwayMap, OpenStreetMap | Overpass Turbo | Topluluk verisinin tamamlığı bölgeye göre değişir |
| Kripto adresi / işlem | Blockchair, Etherscan/Tronscan | GraphSense, Breadcrumbs | Kümeleme ve etiketler hipotezdir, kimlik kanıtı değildir |
| PDF / taranmış belge | ExifTool, Apache Tika, OCRmyPDF | Tesseract, Tabula, CyberChef | Dönüştürmeden önce orijinali koruyun |
| Büyük yapılandırılmış veri | OpenRefine, jq | Datasette, QGIS, kepler.gl | Sonucun tekrar üretilebilmesi için her dönüşümü kaydedin |
| Zaman çizelgesi / olay seti | Timesketch | İlişki karmaşıklaşırsa Gephi | Saat dilimi, saat ve parser hataları analize taşınır |
| Araştırmacı / makale / DOI | OpenAlex, Crossref | ORCID Search | İsim eşleştirmesi ve kullanıcı tarafından yönetilen profiller hatalı olabilir |
| Tarihsel web sayfası | Internet Archive, Archive.today | Common Crawl, Browsertrix, ReplayWeb.page | Yakalama tarihi ve arşiv kaynağı kanıtın parçasıdır |
| Web kanıtını koruma | SingleFile, Bellingcat Auto Archiver | Browsertrix, ArchiveBox, ReplayWeb.page | Arşiv oluşturmak bağımsız doğrulama değildir |

## Pratik minimum set

Çoğu araştırma yüz araç gerektirmez. Savunulabilir temel akış genellikle şudur:

1. **Keşif:** iki bağımsız arama veya indeks kaynağı.
2. **Birincil kaynak:** resmi sicil, dosya, orijinal gönderi, harita verisi veya resmi kayıt.
3. **Koruma:** hukuka uygun olduğunda URL, zaman, kaynak ve tekrar incelenebilir kopyayı kaydedin.
4. **Zenginleştirme:** yalnızca tanımlı bir soruyu cevaplayan uzman aracı ekleyin.
5. **Doğrulama:** sonucu bağımsız kaynak veya yöntemle doğrulayın.
6. **Analiz:** güven düzeyi, alternatifler ve bilinmeyenleri not edin; grafik/zaman çizelgesini yalnızca karmaşıklık gerektiriyorsa kullanın.
7. **Raporlama:** gözlenen gerçek, araç çıktısı, çıkarım ve bilinmeyeni açıkça ayırın.

## Gizlilik ve yetkilendirme

- Bir bilginin herkese açık olması her sorgu veya işlemi otomatik olarak uygun yapmaz.
- Telefon, e-posta ve hesap araştırmasında kişisel veri toplamayı azaltın ve yetkili/hukuka uygun tanımlayıcılar kullanın.
- Altyapıda pasif gözlemi tercih edin; probing/scanning için hedefin size ait olması veya açık izin gerekir.
- Dosya, URL veya IOC'leri CTI/bulut servislerine göndermeden önce saklama ve yeniden paylaşım politikasını kontrol edin.
- Yaptırım, lobicilik, FARA, mahkeme ve kamu ihale kayıtları kimlik, tarih, yetki alanı ve usul bağlamı gerektirir; bir kayıt eşleşmesi yanlış davranış kararı değildir.
- İhlal kaydı, kullanıcı adı tekrar kullanımı, kripto kümelemesi, metadata, görüntü adli sinyalleri veya otomatik enrichment sonuçlarını kimlik kanıtı olarak kabul etmeyin.

## Açık kaynak tercihi

Benzer işi yapan iki araç arasında bu yol haritası; bakımı süren upstream'i, açık lisansı, incelenebilir davranışı ve yerel/self-hosted seçeneği olan aracı tercih eder. Bkz. [Doğrulanmış Açık Kaynak OSINT Araçları](open-source-tools.tr.md).