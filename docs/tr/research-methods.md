# Araştırma Yöntemleri

Araçlardan bağımsız çalışan yöntemler, OSINT araştırmasının en değerli kısmıdır.

## 1. Discovery ve verification'ı ayır

**Discovery:** aday bilgi bulmak.

**Verification:** aday bilginin doğru olup olmadığını kanıtlamak.

Bu iki aşamayı karıştırma. Arama sonucu, username eşleşmesi veya araç çıktısı önce bir **lead** olarak kaydedilmelidir.

## 2. Provenance zinciri kur

Bir iddianın kaynağını geriye doğru izle:

```text
Paylaşım → Haber → Ajans → Resmi açıklama → Orijinal belge
```

Her adımda URL, tarih, yayıncı ve kaynak türünü kaydet.

## 3. Sideways search yap

Aynı cümleyi tekrar tekrar aramak yerine yanal geçişler dene:

- kuruluş adı + tarih,
- kişi adı + olay,
- belge başlığı + filetype,
- benzersiz ifade + arşiv,
- farklı dilde eşdeğer terim,
- şirket adı + sicil numarası.

Amaç algoritmanın sana sunduğu aynı kaynak kümesinden çıkmaktır.

## 4. Stable identifiers kullan

İsimler değişebilir. Daha kararlı tanımlayıcılar:

- alan adı,
- şirket sicil numarası,
- LEI,
- kullanıcı adı,
- belge numarası,
- sertifika fingerprint'i,
- kamu kayıt kimliği.

Bir tanımlayıcıyı yalnızca yasal ve açık kaynaklarda pivot olarak kullan.

## 5. Alternatif hipotez yaz

Ana sonucuna karşı en az iki alternatif açıklama üret.

```text
H1: Hesap gerçekten aynı kişiye ait.
H2: Kullanıcı adı tesadüfen aynı.
H3: Hesap başka biri tarafından kopyalanmış.
```

Her hipotez için destekleyen ve çürüten kanıt ara.

## 6. Kaynak bağımlılığını test et

Beş haber sitesi tek bir ajans haberini tekrar ediyorsa beş doğrulama yoktur.

Kaynak ağacını çiz:

```text
Ajans A
├─ Site 1
├─ Site 2
└─ Site 3

Resmi belge B
└─ Site 4
```

Burada iki gerçek kaynak hattı vardır.

## 7. Zamanı normalize et

Farklı saat dilimleri olay sırasını bozabilir.

Tüm kritik olayları tek saat dilimine çevir. Raporlarda UTC kullanmak çoğu durumda pratiktir.

## 8. Çok dilli araştırma yap

Aynı olay farklı dillerde farklı kelimelerle raporlanabilir.

Ara:

- yerel dilde isim,
- İngilizce karşılık,
- farklı transliterasyonlar,
- eski kurum adı,
- kısaltmalar.

Makine çevirisini başlangıç noktası olarak kullan; kritik ifadeyi mümkünse orijinal kaynakta doğrula.

## 9. Stop condition belirle

Araştırma sonsuza kadar sürmemeli.

Örnek durma kriterleri:

- iki bağımsız güçlü kaynak bulundu,
- kritik çelişki çözülemedi ve rapora sınırlama olarak eklendi,
- yeni aramalar yalnızca aynı kaynakları döndürüyor,
- sonraki adım yasal/etik sınırı aşıyor.

## 10. En güçlü bulgunu çürütmeye çalış

Raporu tamamlamadan önce şunu sor:

```text
Bu sonuç yanlışsa hangi kanıt beni fikrimden vazgeçirir?
```

Son bir aramayı özellikle o kanıtı bulmak için yap.
