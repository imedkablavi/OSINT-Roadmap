# Araç Matrisi

Bu tablo “en iyi araçlar” listesi değildir. Her aracın hangi soruya yardımcı olduğu ve çıktısının neyi **kanıtlamadığı** önemlidir.

| Kategori | Araç | Kullanım | Seviye | Maliyet | Sınırlama |
| --- | --- | --- | --- | --- | --- |
| Arama | Google / Bing / Brave | Açık web keşfi | Başlangıç | Ücretsiz | Sonuç sıralaması kanıt değildir |
| Arşiv | Wayback Machine | Eski sayfa sürümleri | Başlangıç | Ücretsiz | Her sayfa/tarih arşivlenmez |
| Arşiv | Archive.today | Sayfa snapshot'ı | Başlangıç | Ücretsiz | Kapsama düzensiz olabilir |
| Kullanıcı adı | WhatsMyName | Platformlarda kullanıcı adı kontrolü | Başlangıç | Ücretsiz | Eşleşme = kimlik kanıtı değildir |
| Kullanıcı adı | Sherlock | Çoklu site username keşfi | Orta | Ücretsiz | False positive üretilebilir |
| Görsel | Google Lens | Benzer görsel ve nesne araması | Başlangıç | Ücretsiz | En eski kaynağı garanti etmez |
| Görsel | TinEye | Görsel eşleşme ve geçmiş | Başlangıç | Freemium | Veri tabanı kapsamı sınırlıdır |
| Video | InVID | Frame extraction ve doğrulama desteği | Orta | Ücretsiz | Araç sonucu manuel kontrol ister |
| Metadata | ExifTool | Dosya metadata inceleme | Orta | Ücretsiz | Metadata silinebilir veya değiştirilebilir |
| Harita | Google Earth | Uydu ve tarihsel görüntü karşılaştırması | Başlangıç | Ücretsiz | Görüntü tarihi bölgeye göre değişir |
| Harita | OpenStreetMap | Yol, bina, POI karşılaştırması | Başlangıç | Ücretsiz | Topluluk verisi eksik/eski olabilir |
| Güneş | SunCalc | Güneş/gölge hipotezini test etme | Orta | Ücretsiz | Kamera açısı bilinmezse kesin sonuç vermez |
| Domain | RDAP / WHOIS | Kayıt bilgileri | Başlangıç | Ücretsiz | Privacy proxy gerçek sahibi gizleyebilir |
| Sertifika | crt.sh | Certificate Transparency geçmişi | Orta | Ücretsiz | Host ilişkisi sahiplik kanıtı değildir |
| Pasif internet | Censys | Kamuya açık tarama verisi | Orta | Freemium | Veri güncelliği değişebilir |
| Pasif internet | Shodan | İnternet servis görünürlüğü | Orta | Freemium | Sonuçlar gecikmeli olabilir |
| URL | urlscan.io | Açık URL tarama kayıtları | Orta | Freemium | Hassas URL'leri göndermek uygun olmayabilir |
| Teknoloji | Wappalyzer / BuiltWith | Web teknoloji izi | Başlangıç | Freemium | Teknoloji tespiti yanlış/eskimiş olabilir |
| Şirket | OpenCorporates | Şirket kayıt keşfi | Başlangıç | Freemium | Resmi sicilin yerine geçmez |
| Yaptırım | OpenSanctions | Yaptırım/PEP veri agregasyonu | Orta | Açık/Freemium | Kaynak kayıtla doğrulanmalıdır |
| Araştırma | OCCRP Aleph | Belgeler ve şirket ilişkileri | Orta | Değişken | Eşleşmeler manuel doğrulanmalıdır |
| LEI | GLEIF | Tüzel kişi LEI doğrulaması | Başlangıç | Ücretsiz | LEI tüm kuruluşlarda bulunmaz |

## Araç seçme kuralı

Bir aracı açmadan önce dört soruya cevap ver:

```text
1. Hangi soruyu cevaplamaya çalışıyorum?
2. Hangi veri bu soruyu destekler?
3. Araç bu veriyi nereden alıyor?
4. Sonucu bağımsız olarak nasıl doğrulayacağım?
```

## Yanlış kullanım örneği

**Bulgu:** Sherlock aynı kullanıcı adını 12 sitede buldu.

**Yanlış sonuç:** “Bu 12 hesap aynı kişiye ait.”

**Doğru yaklaşım:** Username eşleşmelerini aday ilişki olarak tut; profil tarihi, benzersiz içerik, bağlantılar, biyografi, zaman çizelgesi ve başka bağımsız göstergelerle test et.
