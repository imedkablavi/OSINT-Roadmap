# OSINT Araç Kütüphanesi

> Son inceleme: **2026-08-22** · [English](tool-library.md) · [العربية](tool-library.ar.md) · Türkçe

Bu sayfa internette OSINT etiketi taşıyan her bağlantıyı toplamak için hazırlanmadı. Amaç, açık kaynak araştırmasında belirli bir sorunu çözen ve çıktısı doğrulanabilir bir iş akışına yerleştirilebilen araçları **seçerek** sunmaktır.

Bir aracın çıktısı **ipucu veya gözlemdir**, otomatik kanıt değildir. Önemli bulgular asıl kaynaktan doğrulanmalı ve mümkün olduğunda bağımsız kaynaklarla desteklenmelidir.

## Kütüphane nasıl okunmalı?

| Alan | Anlamı |
| --- | --- |
| Input | Genellikle elinde bulunan başlangıç verisi |
| Maliyet | Ücretsiz, freemium, ücretli veya self-hosted |
| Seviye | Başlangıç, orta, ileri |
| En iyi kullanım | Aracın cevaplamaya yardımcı olduğu soru |
| Ana sınırlama | Sonucun neyi kanıtlamadığı veya nerede yanıltabileceği |

## Başlangıç setleri

### Temel başlangıç
Google Search · Internet Archive · SingleFile · Google Lens · TinEye · Google Earth · OpenStreetMap · ExifTool

### GEOINT
Google Earth · OpenStreetMap · Mapillary · SunCalc · PeakVisor · Copernicus Browser · NASA Worldview · QGIS

### CTI / altyapı
VirusTotal · urlscan.io · Shodan · Censys · GreyNoise · ThreatFox · RIPEstat · crt.sh

### Şirket araştırması
OpenCorporates · GLEIF LEI Search · OpenSanctions · OCCRP Aleph · ICIJ Offshore Leaks · SEC EDGAR · Companies House

### İzleme ve arşivleme
Internet Archive · Archive.today · changedetection.io · GDELT · Hunchly · SingleFile · OpenRefine

---

# 1. Arama, keşif ve arşivleme

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Google Search](https://www.google.com/) | kelime, isim, domain | Ücretsiz | Başlangıç | genel keşif, exact phrase, `site:` ve dosya aramaları | sıralama ve kişiselleştirme sonuç saklayabilir |
| [Bing](https://www.bing.com/) | kelime, görsel | Ücretsiz | Başlangıç | ikinci indeks ve görsel keşif | Google’dan farklı kapsama sahiptir |
| [Brave Search](https://search.brave.com/) | kelime | Ücretsiz / ücretli | Başlangıç | farklı ve daha bağımsız arama perspektifi | bazı niş konularda kapsama daha küçüktür |
| [Kagi](https://kagi.com/) | kelime | Ücretli | Başlangıç | düşük gürültülü araştırma | abonelik gerekir |
| [SearXNG](https://searxng.org/) | kelime | Ücretsiz / self-hosted | Orta | birden fazla motoru kullanan metasearch | kalite instance yapılandırmasına bağlıdır |
| [GDELT](https://www.gdeltproject.org/) | konu, entity, konum | Ücretsiz | Orta | haber/olay keşfi ve trend analizi | otomatik event çıkarımı bağlam doğrulaması ister |
| [Google Scholar](https://scholar.google.com/) | konu, yazar | Ücretsiz | Başlangıç | makale, citation ve akademik kaynak keşfi | her içerik peer-reviewed değildir |
| [Internet Archive](https://web.archive.org/) | URL | Ücretsiz | Başlangıç | geçmiş web sayfaları | arşivde olmaması sayfanın hiç var olmadığını göstermez |
| [Archive.today](https://archive.ph/) | URL | Ücretsiz | Başlangıç | belirli zamandaki sayfa snapshot’ı | kapsama ve erişilebilirlik değişir |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | web sayfası | Ücretsiz | Başlangıç | sayfayı tek HTML olarak saklama | yalnızca tarayıcıda render edilen sürümü korur |
| [ArchiveBox](https://archivebox.io/) | URL listesi | Ücretsiz / self-hosted | Orta | yerel araştırma arşivi oluşturma | depolama ve bakım gerekir |
| [changedetection.io](https://changedetection.io/) | URL | Ücretsiz / ücretli / self-hosted | Orta | web değişikliklerini izleme | dinamik sayfalar gürültülü değişiklikler üretir |

# 2. Kullanıcı adları ve kamuya açık kimlik ipuçları

Aynı username, avatar veya display name iki hesabın aynı kişiye ait olduğunu kanıtlamaz.

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | username | Ücretsiz | Başlangıç | aynı handle’ı birçok açık serviste arama | false positive ve yeniden kullanılan kullanıcı adları |
| [Sherlock](https://github.com/sherlock-project/sherlock) | username | Ücretsiz | Orta | komut satırıyla çoklu site kontrolü | hit yalnızca aynı handle’ın bulunduğunu gösterir |
| [Maigret](https://github.com/soxoj/maigret) | username | Ücretsiz | Orta | geniş username enumeration ve rapor | platform değişiklikleri kontrolleri bozabilir |
| [Epieos](https://epieos.com/) | email / telefon, hukuka uygun kapsamda | Freemium | Orta | kamuya açık hesap ipuçları ve pivot | hassas bilgi üretebilir; minimum toplama uygulanmalı |
| [GitHub Search](https://github.com/search) | username, code, organization | Ücretsiz | Başlangıç | açık profiller, repo, commit ve kod referansları | GitHub kimliği gerçek dünya kimliği değildir |

# 3. Görsel ve video doğrulama

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Google Lens](https://lens.google/) | görsel | Ücretsiz | Başlangıç | görsel eşleşmeler, nesne ve metin keşfi | benzerlik kaynak/provenance kanıtı değildir |
| [TinEye](https://tineye.com/) | görsel | Ücretsiz / ücretli | Başlangıç | aynı veya değiştirilmiş kopyaları bulma | genel arama motorlarından daha küçük indeks |
| [Yandex Images](https://yandex.com/images/) | görsel | Ücretsiz | Başlangıç | alternatif görsel benzerlik araması | sonuçların kaynağı ayrıca doğrulanmalı |
| [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | video / görsel / URL | Ücretsiz | Orta | keyframe ve doğrulama yardımcıları | iddiayı otomatik doğrulamaz |
| [ExifTool](https://exiftool.org/) | yerel dosya | Ücretsiz | Orta | metadata okuma | metadata silinebilir veya değiştirilebilir |
| [FotoForensics](https://fotoforensics.com/) | görsel | Ücretsiz | Orta | sıkıştırma ve forensic sinyalleri öğrenme | ELA tek başına manipülasyon kanıtı değildir |
| [FFmpeg](https://ffmpeg.org/) | video / ses | Ücretsiz | Orta | frame/ses çıkarma ve analiz kopyası oluşturma | işleme dosyayı değiştirir; orijinali ayrıca sakla |

# 4. GEOINT, haritalar ve uydu görüntüleri

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Google Maps](https://maps.google.com/) | konum / koordinat | Ücretsiz | Başlangıç | yol, işletme, landmark, Street View | görüntü ve işletme verisi eski olabilir |
| [Google Earth](https://earth.google.com/) | konum | Ücretsiz | Başlangıç | terrain, 3D ve mevcut yerlerde historical imagery | tarihsel kapsama konuma göre değişir |
| [OpenStreetMap](https://www.openstreetmap.org/) | konum / feature | Ücretsiz | Başlangıç | açık harita verisi ve yollar | topluluk kapsamı bölgelere göre değişir |
| [Mapillary](https://www.mapillary.com/) | konum | Ücretsiz | Orta | crowdsourced street-level görüntü | tarih ve kapsama çok değişkendir |
| [SunCalc](https://www.suncalc.org/) | konum + zaman hipotezi | Ücretsiz | Orta | güneş/gölge yönünü test etme | makul konum ve zaman tahmini gerekir |
| [PeakVisor](https://peakvisor.com/) | manzara / konum | Freemium | Orta | dağ ve skyline tanıma | benzer arazi yanlış eşleşme yaratabilir |
| [Copernicus Browser](https://dataspace.copernicus.eu/browser/) | bölge + tarih | Ücretsiz hesap | Orta | Sentinel imagery, karşılaştırma ve indirme | bulut ve mekânsal çözünürlük bazı soruları sınırlar |
| [NASA Worldview](https://worldview.earthdata.nasa.gov/) | bölge + tarih | Ücretsiz | Orta | near-real-time Earth observation katmanları | birçok katman ticari görüntülerden daha düşük çözünürlüktedir |
| [QGIS](https://qgis.org/) | geospatial dosyalar | Ücretsiz | İleri | harita/uydu katmanlarını birleştirme ve analiz | GIS ve koordinat sistemi bilgisi gerekir |

# 5. Domain, IP ve internet altyapısı

Bu bölüm **pasif açık kayıtlar ve önceden gözlemlenmiş veri** içindir. Aktif probing/scanning açık yetki gerektirebilir.

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [ICANN Lookup](https://lookup.icann.org/) | domain | Ücretsiz | Başlangıç | public RDAP/registration | privacy redaction yaygındır |
| [crt.sh](https://crt.sh/) | domain / organization | Ücretsiz | Orta | Certificate Transparency geçmişi | sertifika verilmesi güncel sahiplik kanıtı değildir |
| [SecurityTrails](https://securitytrails.com/) | domain / IP | Freemium | Orta | DNS geçmişi ve altyapı bağlamı | derinlik plana ve kapsama bağlıdır |
| [DNSDumpster](https://dnsdumpster.com/) | domain | Ücretsiz | Başlangıç | görsel DNS discovery | bulunan ilişkiler attribution değildir |
| [BuiltWith](https://builtwith.com/) | domain | Freemium | Başlangıç | web teknoloji sinyalleri | tespit eski veya eksik olabilir |
| [Wappalyzer](https://www.wappalyzer.com/) | sayfa / domain | Freemium | Başlangıç | web teknolojilerini belirleme | client-side tespit yanılabilir |
| [RIPEstat](https://stat.ripe.net/) | IP / ASN | Ücretsiz | Orta | routing, allocation, ASN bağlamı | tahsis kaydı belirli andaki operatörü kanıtlamaz |
| [BGP.tools](https://bgp.tools/) | ASN / prefix | Ücretsiz | Orta | BGP routing ve network context | routing ilişkileri değişir |
| [Cloudflare Radar](https://radar.cloudflare.com/) | domain / ASN / trend | Ücretsiz | Orta | internet trafik, routing ve teknoloji trendleri | aggregated veri tam internet görünümü değildir |

# 6. CTI ve public IOC enrichment

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [VirusTotal](https://www.virustotal.com/) | hash, URL, domain, IP, file | Freemium | Başlangıç | çoklu veri kaynağı enrichment | public upload hassas materyali açığa çıkarabilir |
| [urlscan.io](https://urlscan.io/) | URL / domain | Freemium | Orta | request, DOM, screenshot ve observed infra | hassas URL göndermeden visibility kontrol edilmeli |
| [Shodan](https://www.shodan.io/) | IP / domain / query | Freemium | Orta | önceden gözlemlenmiş internet-facing servisler | veri eski olabilir |
| [Censys](https://search.censys.io/) | IP / domain / certificate | Freemium | Orta | host, service ve certificate observations | sonuç scan zamanı ve kapsamına bağlıdır |
| [GreyNoise](https://viz.greynoise.io/) | IP | Freemium | Orta | internet noise/scanning bağlamı | sınıflandırma niyet kanıtı değildir |
| [AlienVault OTX](https://otx.alienvault.com/) | IOC | Ücretsiz | Orta | community threat pulses | kaynak kalitesi değişir |
| [Pulsedive](https://pulsedive.com/) | domain / IP / URL | Freemium | Başlangıç | hızlı threat enrichment | skorun kaynağı ayrıca kontrol edilmeli |
| [ThreatFox](https://threatfox.abuse.ch/) | IOC | Ücretsiz | Orta | malware ilişkili göstergeler | indicator’lar hızla eskir |
| [URLhaus](https://urlhaus.abuse.ch/) | URL / host | Ücretsiz | Orta | malware dağıtım URL’leri | bulunmaması güvenli olduğu anlamına gelmez |
| [MalwareBazaar](https://bazaar.abuse.ch/) | hash / sample metadata | Ücretsiz | Orta | malware sample intelligence | canlı sample işlemleri uzman güvenlik önlemi ister |
| [AbuseIPDB](https://www.abuseipdb.com/) | IP | Freemium | Başlangıç | community abuse report | raporlar yanlış veya eski olabilir |

# 7. Şirket, sahiplik ve kamu kayıtları

Legal entity’yi isimle değil; jurisdiction, identifier, tarih ve adres ile doğrula.

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [OpenCorporates](https://opencorporates.com/) | şirket / officer | Freemium | Başlangıç | farklı ülkelerde şirket keşfi | registry kapsamı ülkeye göre değişir |
| [GLEIF LEI Search](https://search.gleif.org/) | legal name / LEI | Ücretsiz | Orta | standart legal entity ID ve bildirilen parent ilişkileri | yalnızca LEI bulunan entity’ler |
| [OpenSanctions](https://www.opensanctions.org/) | kişi / kurum | non-commercial ücretsiz / ücretli | Orta | sanctions, PEP ve kaynaklı entity data | isim eşleşmesi kimlik kanıtı değildir |
| [OCCRP Aleph](https://aleph.occrp.org/) | kişi / şirket / belge | ücretsiz hesap / koleksiyona bağlı | Orta | investigative belge ve structured entity arama | veri erişimi koleksiyona göre değişir |
| [ICIJ Offshore Leaks](https://offshoreleaks.icij.org/) | isim / şirket / adres | Ücretsiz | Orta | büyük offshore araştırmalarındaki ilişkiler | veritabanında bulunmak yasa dışı davranış anlamına gelmez |
| [SEC EDGAR](https://www.sec.gov/search-filings) | US company / ticker / CIK | Ücretsiz | Orta | resmi ABD public-company filings | esas olarak SEC kapsamındaki kuruluşlar |
| [UK Companies House](https://find-and-update.company-information.service.gov.uk/) | UK company / officer | Ücretsiz | Başlangıç | resmi UK şirket kayıt ve filing’leri | kayıtlar eski veya self-reported olabilir |

# 8. Havacılık, deniz ve ulaşım

Tracking servislerinde coverage gap, gecikme ve filtrelenmiş hedefler olabilir. Birden fazla kaynak kullan ve timestamp kaydet.

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Flightradar24](https://www.flightradar24.com/) | flight / aircraft / location | Freemium | Başlangıç | canlı ve geçmiş flight context | kapsama receiver ve plana bağlıdır |
| [ADS-B Exchange](https://www.adsbexchange.com/) | aircraft / location | Freemium | Orta | ADS-B observations | her uçak tam veri yayınlamaz |
| [OpenSky Network](https://opensky-network.org/) | aircraft / time / area | Ücretsiz / research | Orta | aviation dataset ve research query | API/history sınırları vardır |
| [MarineTraffic](https://www.marinetraffic.com/) | vessel / IMO / MMSI | Freemium | Başlangıç | AIS vessel konumu ve liman aktivitesi | AIS yok, gecikmiş veya hatalı olabilir |
| [VesselFinder](https://www.vesselfinder.com/) | vessel / IMO / MMSI | Freemium | Başlangıç | alternatif AIS tracking | aynı AIS kapsam sınırlamaları geçerli |

# 9. Belgeler, structured data ve veri temizleme

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Apache Tika](https://tika.apache.org/) | belge / dosya | Ücretsiz | İleri | çok sayıda formatta text ve metadata çıkarma | layout ve bağlam kaybolabilir |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/) | taranmış PDF | Ücretsiz | Orta | searchable OCR katmanı ekleme | OCR hataları görselle kontrol edilmeli |
| [Tabula](https://tabula.technology/) | PDF table | Ücretsiz | Başlangıç | PDF tablosunu veri haline getirme | karmaşık layout elle temizleme ister |
| [OpenRefine](https://openrefine.org/) | CSV / tabular data | Ücretsiz | Orta | cleaning, normalization ve reconciliation | loglanmamış dönüşümler hata saklayabilir |
| [CyberChef](https://gchq.github.io/CyberChef/) | text / encoded data / file | Ücretsiz | Orta | teknik veri decode/transform | dönüşüm attribution veya yorum değildir |
| [jq](https://jqlang.org/) | JSON | Ücretsiz | Orta | JSON query ve transform | CLI öğrenme eğrisi vardır |

# 10. Araştırma workspace ve ilişki analizi

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Hunchly](https://www.hunch.ly/) | browsing session | Ücretli | Başlangıç | ziyaret edilen sayfa ve araştırma bağlamını koruma | capture iddiayı doğrulamaz |
| [Vortimo](https://www.vortimo.com/) | web research | Freemium / ücretli | Orta | kamu web araştırmasını organize etme | disiplinli tagging ve not gerekir |
| [Maltego](https://www.maltego.com/) | entity / indicator | Freemium / ücretli | Orta | relationship graph ve pivot | görsel graph zayıf bağlantıyı güçlü gösterebilir |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | domain / IP / name vb. | Ücretsiz / ticari seçenek | İleri | çok sayıda OSINT modülünü otomatik çalıştırma | automation ciddi noise üretir |
| [Gephi](https://gephi.org/) | graph data | Ücretsiz | İleri | büyük network visualization | görsel yakınlık gerçek ilişki/causation değildir |

# 11. Blockchain ve kripto araştırması

| Araç | Input | Maliyet | Seviye | En iyi kullanım | Ana sınırlama |
| --- | --- | --- | --- | --- | --- |
| [Etherscan](https://etherscan.io/) | Ethereum address / tx / contract | Ücretsiz / ücretli API | Başlangıç | Ethereum transaction ve contract | adres sahibini belirlemek için off-chain evidence gerekir |
| [Tronscan](https://tronscan.org/) | TRON address / tx | Ücretsiz | Başlangıç | TRON aktivitesi ve contract | zincir aktivitesi tek başına insan kimliği vermez |
| [Blockchair](https://blockchair.com/) | address / tx / block | Freemium | Başlangıç | multi-chain explorer | özellik/kapsama network’e göre değişir |
| [Breadcrumbs](https://www.breadcrumbs.app/) | crypto address | Freemium | Orta | transaction graphing | cluster ve label provenance kontrol edilmeli |
| [Arkham](https://intel.arkm.com/) | address / entity label | Freemium | Orta | entity label ve transaction ilişkileri | platform label’ı otomatik kimlik kanıtı değildir |

---

# Kaydetmeye değer öğrenme kaynakları

| Kaynak | Neden yararlı? |
| --- | --- |
| [Bellingcat Online Investigations Toolkit](https://bellingcat.gitbook.io/toolkit) | araç kullanım amacı, maliyet, zorluk, gereksinim ve sınırlamalar |
| [OSINT Dojo](https://www.osintdojo.com/) | kademeli challenge ve skill rank sistemi |
| [GIJN Resource Center](https://gijn.org/resource/) | araştırma, verification, company, satellite ve çok dilli rehberler |
| [Verification Handbook](https://verificationhandbook.com/) | dijital içerik doğrulama metodolojisi |
| [OSINT Framework](https://osintframework.com/) | kategori bazlı hızlı araç keşfi |
| [IntelTechniques Tools](https://inteltechniques.com/tools/) | pratik araştırma utilities ve referanslar |
| [Awesome OSINT](https://github.com/jivoi/awesome-osint) | bu seçilmiş listenin ötesinde geniş kaynak dizini |
| [OSINT Tools Library](https://github.com/The-OSINT-Newsletter/OSINT-Tools-Library) | gerçek araştırma kullanımına ve bakım durumuna odaklanan katalog |

# Araç seçme akışı

```text
Araştırma sorusunu yaz
        ↓
Elindeki gerçek input'u belirle
        ↓
Tek bir soruyu cevaplayan en küçük aracı seç
        ↓
Kaynak + zaman + query kaydet
        ↓
Sonucu asıl kaynaktan doğrula
        ↓
Önemli iddiaları bağımsız kaynakla destekle
        ↓
Belirsizlik ve stop condition'ı yaz
```

# Bakım politikası

Bir araç şu durumlarda listeden düşürülür veya statüsü azaltılır:

- resmi proje terk edilmişse ve daha iyi alternatif varsa;
- servis güvenilmez veya yanıltıcı hale geldiyse;
- izin veya gizlilik modeli belirgin biçimde kötüleştiyse;
- temel kullanım biçimi hukuka aykırı şekilde elde edilmiş özel veriye dayanıyorsa;
- çıktısı açıklanamıyor veya doğrulanamıyorsa;
- resmi URL değişmiş ve yeni adres doğrulanamıyorsa.

Bir değişiklik görürsen **Resource suggestion** veya **Broken link** issue template’ini kullan.
