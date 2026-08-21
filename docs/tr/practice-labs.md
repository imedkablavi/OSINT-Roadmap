# Pratik OSINT Laboratuvarları

Bu alıştırmalar kamuya açık, izinli veya eğitim için hazırlanmış içerikle yapılmalıdır.

## Lab 1 — Bir iddianın ilk kaynağını bul

**Amaç:** Bir haber veya duyurunun kaynak zincirini geriye doğru izlemek.

1. Kamuya açık bir iddia seç.
2. İddiayı paylaşan 3 farklı sayfayı bul.
3. Sayfaların birbirini kopyalayıp kopyalamadığını kontrol et.
4. En erken tarihli kaynağı bul.
5. Mümkünse birincil belge veya resmi duyuruya ulaş.
6. Bir paragrafta hangi kaynağın neden en güçlü olduğunu açıkla.

## Lab 2 — Değişmiş bir web sayfasını yeniden kur

**Amaç:** Web arşivlerini kanıt olarak dikkatli kullanmak.

1. Zaman içinde değişmiş kamuya açık bir sayfa seç.
2. Wayback Machine'de en az 3 tarih bul.
3. Başlık, metin, iletişim bilgisi veya ürün bilgisindeki değişiklikleri kaydet.
4. Değişiklik zamanını yaklaşık olarak daralt.
5. Arşivde olmayan dönemleri “bilinmiyor” olarak bırak.

## Lab 3 — Görsel bağlamını doğrula

**Amaç:** Görselin iddia edilen olay/tarih/yerle uyumunu test etmek.

1. Kamuya açık bir haber görseli seç.
2. Tersine görsel arama yap.
3. Daha eski kullanım bulmaya çalış.
4. Görseldeki yazı, bina veya arazi ipuçlarını kaydet.
5. Sonucu “doğrulandı / kısmen destekleniyor / doğrulanamadı” olarak yaz.

## Lab 4 — Pasif domain footprint

**Amaç:** Aktif tarama yapmadan bir alan adının açık kaynak izini çıkarmak.

Kullan:

- RDAP/WHOIS,
- DNS,
- crt.sh,
- Wayback Machine,
- BuiltWith/Wappalyzer,
- urlscan gibi mevcut üçüncü taraf kayıtları.

Çıktıda her bulgunun kaynağını ve tarihini göster.

## Lab 5 — Username hipotezini test et

**Amaç:** Aynı kullanıcı adının aynı kişi anlamına gelmediğini uygulamalı görmek.

1. Kendi kullanıcı adını veya eğitim için belirlenmiş bir hesabı kullan.
2. Açık platformlarda eşleşmeleri bul.
3. Her eşleşme için destekleyen ve çelişen göstergeleri yaz.
4. En az bir false positive örneği ara.
5. Kesin kimlik iddiası yapma.

## Lab 6 — Timeline oluştur ve boz

**Amaç:** Olay sırasını kaynaklarla kurmak ve çelişki aramak.

1. Kamuya açık bir etkinlik seç.
2. En az 6 zaman damgası topla.
3. Hepsini UTC'ye çevir.
4. Kaynak türünü belirt.
5. Zaman çizelgesinde çelişen bir kayıt olup olmadığını ara.

## Lab 7 — Eğitim görselini geolocate et

Kendi çektiğin veya eğitim için kullanılmasına izin verilen bir görsel seç.

- 5 görsel ipucu çıkar.
- Harita üzerinde en az 2 aday konum üret.
- Her adayı çürütecek kanıt ara.
- Son konumu güven düzeyiyle raporla.

## Lab 8 — Tek sayfalık intelligence note

Önceki lablardan birini seç ve tek sayfalık rapora dönüştür:

```text
Question
Scope
Key judgment
Evidence
Analysis
Confidence
Limitations
Sources
```

## Puanlama

Her lab için 0–2 puan ver:

| Kriter | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Kaynak kalitesi | Zayıf | Karışık | Güçlü/birincil |
| Doğrulama | Yok | Kısmi | Bağımsız |
| Dokümantasyon | Eksik | Temel | Tekrarlanabilir |
| Alternatif açıklama | Yok | Bahsedilmiş | Test edilmiş |
| Sonuç dili | Aşırı iddialı | Kısmen dikkatli | Kanıtla orantılı |

8+ iyi başlangıç, 10 ise güçlü çalışma demektir.
