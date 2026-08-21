# 🕵️ OSINT Yol Haritası

## Açık Kaynak İstihbaratı için pratik, etik ve kanıta dayalı öğrenme yolu

> Bu depo, OSINT'i araç ezberleyerek değil; doğru soruyu kurarak, açık kaynakları araştırarak, bulguları doğrulayarak ve sonucu savunulabilir biçimde raporlayarak öğrenmek isteyenler için hazırlanmıştır.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Seviye](https://img.shields.io/badge/seviye-başlangıçtan%20ileri%20seviyeye-blue)
![Odak](https://img.shields.io/badge/odak-etik%20OSINT-lightgrey)

## 🌐 Diller

- [English](README.en.md)
- [العربية](README.ar.md)
- [Türkçe](README.tr.md)

## Hızlı başlangıç

OSINT'e yeni başlıyorsan şu sırayı kullan:

```text
1. Araştırma sorusunu tanımla
2. Kapsamı ve sınırları belirle
3. Açık kaynaklardan aday bulguları topla
4. Önemli iddiaları bağımsız kaynaklarla doğrula
5. Kaynak, tarih ve bağlamı kaydet
6. Alternatif açıklamaları test et
7. Sonucu güven düzeyi ve sınırlamalarla raporla
```

Araçları öğrenmek faydalıdır; fakat iyi bir araştırma, aracın çıktısını doğrudan gerçek kabul etmez.

## Bu depoda ne var?

| Bölüm | İçerik |
| --- | --- |
| [Türkçe öğrenme merkezi](docs/tr/README.md) | Türkçe tüm pratik rehberler |
| [Araştırma yöntemleri](docs/tr/research-methods.md) | Tekrarlanabilir araştırma yöntemleri |
| [Araç matrisi](docs/tr/tool-matrix.md) | Araç, kullanım amacı, zorluk ve sınırlamalar |
| [Pratik laboratuvarları](docs/tr/practice-labs.md) | Güvenli ve uygulanabilir OSINT alıştırmaları |
| [Kaynak doğrulama kontrol listesi](docs/tr/source-verification-checklist.md) | Bir kaynağa güvenmeden önce sorulacak sorular |
| [Coğrafi doğrulama saha rehberi](docs/tr/geolocation-field-guide.md) | Görsel konum doğrulama iş akışı |
| [Rapor şablonu](docs/tr/report-template.md) | Bulguları düzenli raporlama yapısı |

---

## 🔍 OSINT nedir?

**OSINT (Open Source Intelligence)**; kamuya açık kaynaklardan bilgi toplama, doğrulama, analiz etme ve belirli bir soruyu yanıtlayacak şekilde raporlama sürecidir.

OSINT yalnızca internette arama yapmak değildir. Bir araştırmanın istihbarat değerine sahip olması için:

- sorunun açık olması,
- kullanılan kaynakların izlenebilir olması,
- önemli iddiaların doğrulanması,
- varsayımların olgulardan ayrılması,
- belirsizliğin açıkça yazılması gerekir.

Açık kaynaklara örnekler:

- web siteleri ve arşivlenmiş sayfalar,
- haberler ve basın açıklamaları,
- kamuya açık sosyal medya içerikleri,
- resmi kayıtlar ve şirket sicilleri,
- haritalar ve uydu görüntüleri,
- fotoğraf ve videolar,
- alan adı, DNS ve sertifika kayıtları,
- akademik yayınlar,
- açık veri setleri.

## ⚖️ OSINT ve izinsiz erişim arasındaki sınır

OSINT, erişim kontrolünü aşmayı gerektirmez.

Bu yol haritasının kapsamı:

- açık web araştırması,
- kamuya açık kayıtların incelenmesi,
- arşiv ve kaynak karşılaştırması,
- görsel doğrulama,
- pasif altyapı araştırması,
- açık sosyal medya içeriğinin analizi,
- kanıt ve raporlama yöntemleri.

Kapsam dışı olanlar:

- parola tahmini,
- hesap ele geçirme,
- yetkisiz erişim,
- erişim kontrollerini aşma,
- aldatıcı sosyal mühendislik,
- kimliğe bürünme,
- taciz veya doxxing,
- izinsiz aktif tarama.

Basit kural:

```text
Bir sonraki adım özel erişim, aldatma veya güvenlik kontrolünü aşmayı gerektiriyorsa dur.
```

---

# 🧭 Öğrenme yol haritası

## 1 — Temeller

Önce araştırma disiplinini geliştir.

Öğrenilecekler:

- bilgi ile istihbarat arasındaki fark,
- açık ve özel veri farkı,
- araştırma sorusu yazma,
- kapsam belirleme,
- kaynak güvenilirliği,
- bilişsel önyargılar,
- temel araştırmacı OPSEC'i,
- not alma ve kanıt düzeni.

### İlk alışkanlıklar

Her araştırmada şu beş soruyu yaz:

```text
Ne doğrulamaya çalışıyorum?
Hangi kaynaklar bu soruyu cevaplayabilir?
Hangi kaynaklar birbirinden gerçekten bağımsız?
Hangi bulgular yalnızca gösterge, hangileri kanıt?
Mevcut verilerle neyi söyleyemem?
```

## 2 — Arama ve keşif

Arama motorlarını yalnızca anahtar kelime kutusu olarak görme.

Çalışılacak konular:

- Boolean arama,
- tırnak içinde tam ifade araması,
- `site:` ve `filetype:` kullanımı,
- tarih filtreleme,
- farklı arama motorlarının sonuç farkları,
- web arşivleri,
- çok dilli arama ve transliterasyon,
- kullanıcı adı ve profil keşfi,
- şirket ve kamu kayıtları.

Örnekler:

```text
site:example.com filetype:pdf "annual report"
"exact phrase" -facebook -pinterest
intitle:"incident report" company
```

Arama operatörleri tek başına yöntem değildir. Amaç, hipotezi test edecek kaynaklara ulaşmaktır.

## 3 — Kaynak doğrulama

Bir sonucu bulmak ile bir iddiayı doğrulamak aynı şey değildir.

Kontrol et:

- Kaynağı kim yayımladı?
- İçerik ilk nerede yayımlandı?
- Yayın tarihi ile olay tarihi aynı mı?
- Kaynak başka bir kaynağı kopyalıyor olabilir mi?
- İddia bağımsız bir kaynakta doğrulanıyor mu?
- İçerik sonradan düzenlenmiş olabilir mi?
- Kaynak iddiayı gerçekten söylüyor mu, yoksa yalnızca benzer bir şeyi mi?

Detaylı kontrol listesi: [Kaynak Doğrulama](docs/tr/source-verification-checklist.md)

## 4 — Görsel ve video doğrulama

Ana teknikler:

- tersine görsel arama,
- videodan kare çıkarma,
- ilk yayın tarihini bulma,
- tabela ve yazıları inceleme,
- yol çizgileri ve trafik yönü,
- mimari ve arazi karşılaştırması,
- hava durumu ve ışık koşulları,
- gölge yönü,
- harita ve uydu görüntüsü karşılaştırması,
- metadata'yı dikkatli yorumlama.

Metadata'nın olmaması sahtecilik kanıtı değildir. Sosyal platformlar metadata'yı sıklıkla kaldırır.

## 5 — GEOINT / Coğrafi doğrulama

Amaç, bir fotoğraf veya videonun iddia edilen konumla uyumlu olup olmadığını açık kaynaklarla değerlendirmektir.

İyi ipuçları:

- yol geometrisi,
- bina cepheleri,
- dağ ve kıyı şekilleri,
- elektrik direkleri,
- yol işaretleri,
- toplu taşıma unsurları,
- işletme tabelaları,
- güneş ve gölge,
- bitki örtüsü,
- hava ve mevsim koşulları.

Adım adım rehber: [Geolocation Field Guide](docs/tr/geolocation-field-guide.md)

## 6 — SOCMINT

SOCMINT, kamuya açık sosyal medya faaliyetinin sistematik analizidir.

Kullanılabilecek sinyaller:

- kullanıcı adı,
- biyografi değişiklikleri,
- açık gönderiler,
- zaman çizelgesi,
- halka açık görsel ve videolar,
- açık bağlantılar,
- tekrar eden kamuya açık davranış örüntüleri.

Önemli:

```text
Aynı kullanıcı adı = aynı kişi değildir.
```

Atıf için birden fazla bağımsız gösterge gerekir.

## 7 — WEBINT ve altyapı araştırması

Pasif web araştırmasında kullanılabilecek kaynaklar:

- WHOIS/RDAP,
- DNS kayıtları,
- Certificate Transparency,
- web arşivleri,
- teknoloji tespiti,
- halka açık alt alan adı kayıtları,
- URL ve sayfa metadata'sı,
- üçüncü taraf pasif tarama veri tabanları.

Amaç bir sistemi zorlamak değil, zaten kamuya açık olan kayıtları yorumlamaktır.

## 8 — Zaman çizelgesi analizi

Zaman çizelgesi özellikle olay doğrulamada güçlüdür.

Her kayıtta tut:

| Alan | Örnek |
| --- | --- |
| Zaman | 2026-08-21 12:30 UTC |
| Olay | İlk basın açıklaması |
| Kaynak | Resmi URL |
| Kaynak türü | Birincil |
| Güven | Yüksek |
| Not | Sayfa daha sonra güncellendi |

Saat dilimlerini normalize et. “Dün”, “bu sabah” gibi göreli ifadeleri mutlak zamana çevirmeden karşılaştırma yapma.

## 9 — Analiz ve hipotez testi

İyi OSINT yalnızca destekleyici kanıt aramaz.

En az iki alternatif açıklama yaz:

| Hipotez | Destekleyen kanıt | Çelişen kanıt | Eksik bilgi |
| --- | --- | --- | --- |
| H1 | ... | ... | ... |
| H2 | ... | ... | ... |
| H3 | ... | ... | ... |

Bu yöntem confirmation bias riskini azaltır.

## 10 — Raporlama

Bir başkasının sonucu nasıl elde ettiğini anlayabilmesi gerekir.

Minimum rapor yapısı:

```text
1. Araştırma sorusu
2. Kapsam
3. Yönetici özeti
4. Bulgular
5. Kanıtlar ve kaynaklar
6. Analiz
7. Alternatif açıklamalar
8. Güven düzeyi
9. Sınırlamalar
10. Kaynak günlüğü
```

Kullanıma hazır şablon: [Türkçe OSINT Rapor Şablonu](docs/tr/report-template.md)

---

# 🧰 Araçlar

Araç seçerken “hangi araç popüler?” yerine “hangi soruyu cevaplamam gerekiyor?” diye sor.

Başlangıç kategorileri:

### Arama ve arşiv

- Google / Bing / Brave / DuckDuckGo
- Internet Archive
- Archive.today

### Görsel doğrulama

- Google Lens / Google Images
- Yandex Images
- TinEye
- InVID
- ExifTool

### Harita ve coğrafi araştırma

- Google Earth
- OpenStreetMap
- SunCalc
- Mapillary / mevcut olduğu yerlerde sokak görüntüleri

### Alan adı ve web altyapısı

- RDAP / WHOIS
- crt.sh
- Censys
- Shodan'ın pasif verileri
- urlscan.io
- BuiltWith / Wappalyzer

### Şirket ve kamu kayıtları

- OpenCorporates
- OpenSanctions
- OCCRP Aleph
- GLEIF
- SEC EDGAR

Her aracın hangi durumda işe yaradığını ve neyi **kanıtlamadığını** görmek için [Araç Matrisi](docs/tr/tool-matrix.md) dosyasına bak.

---

# 🧪 Pratik

Pasif okumak yerine küçük dosyalar üret.

Önerilen başlangıç görevleri:

1. Bir haber iddiasının en eski açık kaynağını bul.
2. Değişmiş bir web sayfasını arşivlerden yeniden oluştur.
3. Kamuya açık bir görselin iddia edilen bağlamını doğrula.
4. Yalnızca pasif kaynaklarla bir alan adının açık web ayak izini çıkar.
5. Bir kullanıcı adı eşleşmesinin gerçekten aynı kişiye ait olup olmadığını test et.
6. Bir olay için saat dilimi normalize edilmiş zaman çizelgesi oluştur.
7. Eğitim amaçlı bir görseli coğrafi ipuçlarıyla doğrula.
8. Bulguları tek sayfalık istihbarat notuna dönüştür.

Detaylar ve puanlama: [Pratik Laboratuvarları](docs/tr/practice-labs.md)

---

# 🤖 AI destekli OSINT

Yapay zekâ şu işlerde yardımcı olabilir:

- arama sorgusu varyasyonları üretme,
- yabancı dil terimleri ve transliterasyon seçenekleri önerme,
- kendi topladığın notları sınıflandırma,
- uzun belgelerde aday kişi/kurum/tarih isimlerini çıkarma,
- alternatif hipotezler önermede,
- tablo veya metin verisini düzenlemede.

Ama model çıktısı kaynak değildir.

```text
AI bir sonraki soruyu önerebilir.
Cevabı kanıtlayan şey doğrulanabilir kaynaktır.
```

İsim, tarih, alıntı, URL, ilişki ve sonuçları her zaman asıl kaynakla doğrula.

---

# 🎓 Uzmanlaşma yolları

Temel iş akışı oturduktan sonra şunlardan birine odaklanabilirsin:

- Cyber Threat Intelligence (CTI)
- görsel araştırma ve geolocation
- şirket ve risk araştırması
- kamuya açık sosyal ağ analizi
- gazetecilik ve fact-checking
- fraud ve brand protection
- web altyapısı araştırması
- olay doğrulama ve incident support

Uzmanlık değişir; kanıt standardı değişmez.

---

# ✅ İyi bir araştırmacının kontrol listesi

- [ ] Araştırma sorusu tek cümlede açık mı?
- [ ] Kapsam ve sınırlar yazılı mı?
- [ ] Kaynakların URL ve zaman bilgisi kaydedildi mi?
- [ ] Birincil kaynak arandı mı?
- [ ] Kritik bulgular bağımsız kaynaklarla doğrulandı mı?
- [ ] Kaynakların birbirini kopyalayıp kopyalamadığı kontrol edildi mi?
- [ ] Alternatif açıklamalar test edildi mi?
- [ ] Varsayımlar olgulardan ayrıldı mı?
- [ ] Güven düzeyi gerekçelendirildi mi?
- [ ] Sınırlamalar açıkça yazıldı mı?

---

# 🤝 Katkıda bulunma

Katkılar özellikle şu alanlarda değerlidir:

- güncel ve güvenilir kaynaklar,
- bozuk bağlantı düzeltmeleri,
- yeni güvenli pratik laboratuvarları,
- bölgesel kamu kayıtları rehberleri,
- daha iyi çeviriler,
- görsel doğrulama yöntemleri,
- raporlama örnekleri,
- araçların sınırlamalarının belgelenmesi.

Katkı yapmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını incele.

## Lisans

MIT License © Imed Kablavi

---

Bu yol haritası işine yaradıysa projeye yıldız vermen, depoyu diğer öğrencilerin ve araştırmacıların bulmasını kolaylaştırır.
