# OSINT Tarayıcı Eklentileri ve Web Araçları

![OSINT Tarayıcı Eklentileri ve Web Araçları](../assets/osint-browser-tools.svg)

Bu sayfa rastgele eklenti kurmak için hazırlanmadı. Amaç **hangi aracı ne zaman kullanacağını, çıktının ne anlama geldiğini ve neyi kanıtlamadığını** anlamaktır.

> **Temel kural:** bir eklentinin veya web servisinin sonucu araştırma ipucudur. Önemli bulguları asıl kaynak üzerinden bağımsız olarak doğrula.

## Başlangıç için küçük araç seti

Yeni başlıyorsan onlarca eklenti kurma:

| İhtiyaç | Başlangıç aracı | Neden |
| --- | --- | --- |
| Sayfa kaydetme | [SingleFile](https://github.com/gildas-lormeau/SingleFile) | Sayfayı tek HTML dosyası olarak saklar |
| Eski web sayfası | [Wayback Machine](https://web.archive.org/) | Kamuya açık sayfaların geçmişini kontrol eder |
| Değişiklik takibi | [Distill](https://distill.io/) | Sayfadaki değişiklikleri izler |
| Tersine görsel arama | [TinEye](https://tineye.com/) + [Google Lens](https://lens.google/) | Görselin benzer/eski kopyalarını bulmaya yardımcı olur |
| Video doğrulama | [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | Keyframe ve doğrulama yardımcıları |
| IOC enrichment | [VirusTotal](https://www.virustotal.com/) + [urlscan.io](https://urlscan.io/) | URL, domain ve göstergeleri zenginleştirir |
| Pasif altyapı | [Shodan](https://www.shodan.io/) + [Censys](https://search.censys.io/) | Daha önce gözlemlenmiş internet verisini arar |
| Tam sayfa ekran görüntüsü | [GoFullPage](https://gofullpage.com/) / [FireShot](https://getfireshot.com/) | Sayfayı bağlamıyla belgelemeye yardımcı olur |
| Blockchain | [Etherscan](https://etherscan.io/) / [Blockchair](https://blockchair.com/) | Açık zincir verisini incelemek için |

## 1. Web capture ve arşivleme

### [Hunchly](https://www.hunch.ly/)
Araştırma sırasında ziyaret edilen açık web sayfalarını ve araştırma oturumunu belgelemeye yardımcı olur.

**Kanıtlamaz:** yakalanan sayfadaki iddianın doğru olduğunu.

### [Vortimo](https://www.vortimo.com/)
Web tabanlı OSINT araştırmasında karşılaşılan bilgileri düzenleme ve toplama iş akışları sunar.

### [Wayback Machine](https://web.archive.org/)
Web sayfalarının tarihsel kopyalarını incelemek için.

**Sınırlama:** bir sayfanın arşivde bulunmaması, hiç var olmadığı anlamına gelmez.

### [SingleFile](https://github.com/gildas-lormeau/SingleFile)
Sayfayı yerel olarak tek HTML dosyasına kaydeder.

### [Distill Web Monitor](https://distill.io/)
Duyuru, liste veya açıklama gibi değişen kamu sayfalarını takip etmek için.

## 2. Görsel ve video analizi

### [Google Lens](https://lens.google/)
Görsel arama, nesne ve metin ipuçlarını keşfetme.

### [TinEye](https://tineye.com/)
Aynı veya değiştirilmiş görsel kopyalarını bulmak için tersine arama.

### [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/)
Video keyframe çıkarma ve görsel doğrulama yardımcıları.

### [FotoForensics](https://fotoforensics.com/)
Görsel özelliklerini incelemek için eğitim/analiz servisi.

**Önemli:** sıkıştırma artefaktı veya ELA tek başına manipülasyon kanıtı değildir.

### [ExifTool](https://exiftool.org/)
Yerel dosyalardaki metadata'yı okumak için.

**Önemli:** sosyal platformlar metadata'yı sıkça siler. Metadata yokluğu sahtecilik kanıtı değildir.

## 3. Threat Intelligence ve IOC Lookup

### [Pulsedive](https://pulsedive.com/)
Açık tehdit istihbaratı göstergelerini zenginleştirmek için.

### [Mitaka](https://github.com/ninoseki/mitaka)
Seçilen indicator'ı birden fazla araştırma servisine hızlıca yönlendiren tarayıcı eklentisi.

### [VirusTotal](https://www.virustotal.com/)
Dosya, URL, domain ve IP hakkında çoklu veri kaynağı enrichment.

**Gizlilik:** gizli dosya veya hassas kurum içi URL'leri herkese açık analiz servislerine yükleme.

### [urlscan.io](https://urlscan.io/)
Web sayfalarıyla ilgili gözlem, network ve sayfa artefaktları sağlar.

**Gizlilik:** hassas bir URL göndermeden önce görünürlük ayarlarını kontrol et.

### [Shodan](https://www.shodan.io/)
Shodan tarafından daha önce gözlemlenmiş internete açık sistemleri arar.

### [Censys](https://search.censys.io/)
Host ve sertifika gözlemlerini aramak için.

> Bu roadmap pasif/açık kaynak araştırmasına odaklanır. Aktif probing için açık yetki gerekir.

## 4. Veri çıkarma ve scraping

### [Instant Data Scraper](https://webrobots.io/instantdata/)
Kamuya açık sayfalardaki tekrar eden verileri çıkarmaya yardımcı olur.

### [Web Scraper](https://webscraper.io/)
Yapısal sayfalardan düzenli veri çıkarma iş akışı.

### [Link Gopher](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/)
Bir sayfadaki linkleri toplu biçimde görüntülemek veya dışa aktarmak için.

**Sınırlar:** scraping; site koşulları, telif, gizlilik ve rate limit'lerle sınırlı olabilir. Araştırma sorusu için gereken minimum veriyi topla.

## 5. Ekran görüntüsü ve medya kaydı

### [GoFullPage](https://gofullpage.com/)
Tam sayfa ekran görüntüsü.

### [FireShot](https://getfireshot.com/)
Sayfa ekran görüntüsü ve export özellikleri.

### [Screenity](https://github.com/alyssaxuu/screenity)
Açık kaynak ekran kaydedici.

Kanıt kaydederken yalnızca görüntüyü saklama. Şunları da not et:

- URL
- erişim zamanı
- timezone
- görüntünün hangi bulguyu desteklediği
- sayfanın dinamik olup olmadığı

## 6. Download yardımcıları

### [DownThemAll!](https://www.downthemall.org/)
Tarayıcıdan erişilebilen dosyalar için toplu indirme yöneticisi.

### [Video DownloadHelper](https://www.downloadhelper.net/)
Desteklenen web medyasını indirmek için tarayıcı eklentisi.

**Sınır:** içeriğin herkese açık olması telif veya platform koşullarını ortadan kaldırmaz. Araştırma ve belgeleme amacıyla hukuka uygun kullan.

## 7. Blockchain ve kripto araştırması

### [Etherscan](https://etherscan.io/)
Ethereum blockchain explorer.

### [Tronscan](https://tronscan.org/)
TRON blockchain explorer.

### [Blockchair](https://blockchair.com/)
Birden fazla blockchain'i destekleyen explorer.

### [Breadcrumbs](https://www.breadcrumbs.app/)
Blockchain ilişkilerini analiz ve görselleştirme platformu.

### [Arkham](https://intel.arkm.com/)
Blockchain intelligence ve entity-labeling platformu.

**Attribution kuralı:** bir address label tek başına belirli bir kişinin adresi kontrol ettiğinin kanıtı değildir. Label kaynağını ve güven düzeyini kaydet.

## Eklenti kurmadan önce kontrol listesi

- [ ] Publisher/proje açıkça doğrulanabiliyor mu?
- [ ] Proje aktif olarak güncelleniyor mu?
- [ ] İstenen izinler özelliğe göre makul mü?
- [ ] Geniş browser izni vermek yerine web sürümü kullanılabilir mi?
- [ ] Ziyaret edilen URL veya sayfa içeriği üçüncü tarafa gönderiliyor mu?
- [ ] Gizlilik politikası anlaşılır mı?
- [ ] Eklentiyi ayrı bir araştırma browser profile'ında çalıştırabilir misin?

## Önerilen araştırma tarayıcısı düzeni

```text
Kişisel browser/profile
    └─ günlük kullanım ve kişisel hesaplar

Araştırma browser/profile
    ├─ minimum eklenti
    ├─ gereksiz kişisel login yok
    ├─ ayrı download klasörü
    ├─ evidence capture araçları
    └─ düzenli not ve kaynak sistemi
```

## İlgili içerik

- [Araç matrisi](../docs/tr/tool-matrix.md)
- [Araştırma yöntemleri](../docs/tr/research-methods.md)
- [Kaynak doğrulama checklist](../docs/tr/source-verification-checklist.md)
- [Pratik laboratuvarları](../docs/tr/practice-labs.md)
- [Rapor şablonu](../docs/tr/report-template.md)

---

Bu liste seçilmiş bir koleksiyondur; eksiksiz değildir. Eklentiler zamanla sahip değiştirebilir, izinlerini artırabilir veya bakımsız kalabilir. Kurmadan önce güncel durumu tekrar kontrol et.