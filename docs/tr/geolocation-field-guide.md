# Geolocation Saha Rehberi

Bu rehber, açık veya eğitim amaçlı görsellerde konum doğrulaması yaparken kullanılabilecek savunulabilir bir iş akışı sunar.

## 1. Görseli parçalara ayır

İlk bakışta ülke veya şehir tahmin etmeye çalışma. İpuçlarını sınıflandır:

- dil ve alfabe,
- yol çizgileri,
- trafik yönü,
- tabela biçimi,
- mimari,
- dağ/kıyı/ova şekli,
- elektrik altyapısı,
- toplu taşıma,
- işletme isimleri,
- gölge,
- hava durumu,
- bitki örtüsü.

## 2. Güçlü ve zayıf ipuçlarını ayır

**Güçlü:** benzersiz bina, açık işletme adı, yol numarası, belirgin dağ silueti.

**Orta:** tabela standardı, yol işaretleri, plaka biçimi, mimari grup.

**Zayıf:** hava, bitki örtüsü, genel bina tarzı.

Tek zayıf ipucundan konum çıkarma.

## 3. Metni çıkar

Görünen yazıları manuel olarak oku. Gerekirse farklı olası harflerle ara.

Örnek:

```text
"Cafe Mavi" + şehir
"Mavi Market" + cadde
```

Yabancı alfabelerde transliterasyon varyasyonlarını dene.

## 4. Haritada doğrula

Bir aday konum bulunca şu sırayla karşılaştır:

1. yol geometrisi,
2. bina yerleşimi,
3. kavşak açısı,
4. topoğrafya,
5. sabit sokak nesneleri,
6. görünür işletmeler.

Bir işletme eşleşmesi tek başına yeterli değildir; zincir olabilir veya taşınmış olabilir.

## 5. Zaman faktörü

Görsel eski olabilir.

- arşivlenmiş harita/işletme sayfalarını kontrol et,
- kapanmış işletmeleri araştır,
- sokak görüntüsünün çekim tarihine bak,
- bina veya yol değişikliklerini zaman çizelgesine koy.

## 6. Gölge ve güneş

Gölge analizi destekleyici kanıttır.

- gölgenin yönünü belirle,
- yaklaşık kamera yönünü tahmin et,
- aday konumdaki güneş yönü ile karşılaştır,
- tarih iddiası varsa mevsimsel uyumu kontrol et.

Perspektif hataları nedeniyle yalnızca gölgeden kesin zaman vermekten kaçın.

## 7. Hava durumu

İddia belirli bir tarihe bağlıysa:

- yağış,
- kar,
- bulutluluk,
- görüş mesafesi,
- sıcaklıkla uyumlu çevresel işaretler

gibi unsurları tarihsel hava kayıtlarıyla karşılaştır.

## 8. Sonucu derecelendir

### Olası
Bazı özellikler uyuşuyor fakat benzersiz doğrulama yok.

### Muhtemel
Birden fazla bağımsız coğrafi ipucu aynı aday konumu destekliyor.

### Yüksek güven
Benzersiz veya çok güçlü sabit özellikler harita/sokak görüntüsü ile doğrudan eşleşiyor ve önemli çelişki bulunmuyor.

## 9. Kanıt tablosu

| İpucu | Gözlem | Kaynak | Güç | Çelişki |
| --- | --- | --- | --- | --- |
| Tabela | X adı görünüyor | Görsel | Güçlü | Yok |
| Yol | T kavşağı | OSM | Orta | Yok |
| Dağ | Kuzeyde sırt | Uydu | Orta | Yok |

## 10. Raporlama dili

Kötü:

> Fotoğraf kesin olarak X'te çekildi.

Daha iyi:

> Görüntüdeki yol geometrisi, işletme tabelası ve kuzeydeki dağ silueti X konumuyla eşleşiyor. İncelenen açık kaynaklarda önemli bir çelişki bulunmadığı için konum değerlendirmesi yüksek güven düzeyindedir.
