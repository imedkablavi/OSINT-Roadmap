# OSINT Profesyonel Uzmanlaşma Yolları

Arama, doğrulama ve raporlama temeli oturduktan sonra amaç daha fazla araç toplamak değil; belirli bir alanda savunulabilir araştırma çıktısı üretebilmektir.

Bu sayfa ileri uzmanlık yollarını Türkçe olarak özetler ve her yol için beklenen becerileri açıklar.

## 1. Cyber Threat Intelligence - CTI

### Amaç

Açık teknik göstergeleri anlamlı tehdit bağlamına dönüştürmek; zayıf ilişkilerden aktör attribution'ı üretmemek.

### Beceriler

- Priority Intelligence Requirement yazma
- domain / IP / URL / hash için pasif enrichment
- indicator, infrastructure ve actor ayrımını koruma
- kampanya/activity timeline oluşturma
- altyapı ilişkilerini inceleme
- MITRE ATT&CK'i davranışı tanımlamak için kullanma
- confidence statement yazma

### Uygulama çıktısı

```text
Question
Indicators
Passive enrichment
Timeline
Observed relationships
Alternative explanations
Confidence
Limitations
```

**Kural:** iki aktivitenin aynı altyapı veya aracı paylaşması aynı aktör olduklarını tek başına kanıtlamaz.

Teknik detay: [CTI Track](../../tracks/cti.md)

---

## 2. Digital Footprint Investigation

### Amaç

Kamuya açık dijital izleri değerlendirirken gereksiz kişisel veri toplamadan ve zayıf eşleşmeleri kimlik kanıtına dönüştürmeden çalışmak.

### Beceriler

- kullanıcı adı araştırması
- archive history
- kamuya açık stable identifiers
- açık profil, görsel ve link karşılaştırması
- attribution ladder
- çelişkili kanıtlarla çalışma
- veri minimizasyonu

### Önerilen attribution seviyeleri

| Seviye | Anlam |
| --- | --- |
| Zayıf | Tek benzerlik; örneğin yalnızca username |
| Orta | Birden fazla uyumlu fakat tamamen bağımsız olmayan gösterge |
| Güçlü | Birden fazla bağımsız ve bağlamla uyumlu gösterge |
| Doğrulanmış | İki varlığı doğrudan bağlayan doğrulanabilir açık kanıt |

**Kural:** aynı username aynı kişi demek değildir.

Teknik detay: [Digital Footprint Track](../../tracks/digital-footprint.md)

---

## 3. Company Investigation

### Amaç

Bir şirketi yalnızca kendi web sitesi veya arama sonuçlarıyla değil, kamu kayıtları ve filings üzerinden doğru tüzel kişi olarak incelemek.

### Önce Entity Resolution

- legal name
- trade name
- registration number
- jurisdiction
- registered address
- previous names

### Beceriler

- resmi şirket kayıtları
- filings ve kamuya açık raporlar
- directors / officers
- kamuya açık ownership bilgisi
- sanctions screening
- corporate timeline
- şirketler, markalar ve domain ilişkileri
- legal ownership ile operational control ayrımı

### Uygulama çıktısı

```text
Legal entity
Jurisdiction
Registry identifiers
Key filings
Directors/officers
Ownership evidence
Related entities
Timeline
Sanctions checks
Unresolved questions
```

Teknik detay: [Company Investigation Track](../../tracks/company-investigation.md)

---

## 4. GEOINT ve Görsel Araştırma

### Amaç

Bir fotoğraf veya videonun yer/zaman iddiasını yeniden kontrol edilebilir görsel kanıtla değerlendirmek.

### İş akışı

1. Görsel ipuçlarını ayrı ayrı çıkar.
2. Dil, yol, arazi ve landmark gibi yüksek değerli ipuçlarını belirle.
3. Birden fazla konum hipotezi oluştur.
4. Harita ve kamu görüntüleriyle hipotezleri test et.
5. Gölge, güneş ve hava bilgisini destekleyici kanıt olarak kullan.
6. Uyuşan ve uyuşmayan noktaları kaydet.
7. Confidence ve limitations yaz.

Kullan:

- [Türkçe geolocation field guide](geolocation-field-guide.md)
- [Advanced GEOINT Challenges](../../challenges/advanced-geoint.md)

---

## 5. Investigation Playbooks

Elinde tek bir seed varsa rastgele araç açma. Önce seed türünü tanımla:

| Elindeki veri | İlk sorular |
| --- | --- |
| Domain | geçmişi nedir, hangi açık kaynaklar bahsediyor, hangi public records var? |
| Username | nerelerde görünüyor, hangi bağımsız göstergeler var? |
| Image | daha önce nerede yayımlandı, içindeki görsel ipuçları ne? |
| Video | keyframe'ler ne söylüyor, ilk yayın nerede? |
| Company | doğru legal entity ve jurisdiction hangisi? |
| IP | hangi pasif veriler var, tarihsel ownership olay tarihiyle uyumlu mu? |
| Document | kim yayımladı, metadata ne söylüyor, asıl kopya var mı? |
| Claim | ilk kaynak ne, gerçekten bağımsız doğrulama var mı? |

[Investigation Playbooks](../../playbooks/README.md) ile [Araştırma yöntemlerini](research-methods.md) birlikte kullan.

---

## 6. Gerçek bir OSINT portföyü oluşturma

CV'ye yalnızca “OSINT biliyorum” yazmak yerine incelenebilir çıktılar üret:

- kamuya açık bir iddia doğrulama raporu
- kaynaklı timeline
- eğitim amaçlı geolocation
- pasif domain footprint
- public registry tabanlı company profile
- CTI intelligence note
- reddedilmiş bir hipotezin neden reddedildiğini gösteren rapor

İlerlemeni [Skill Matrix](../skill-matrix.md) ile takip et.

## Bir üst seviyeye ne zaman geçmelisin?

Şunları yapabiliyorsan:

- her kaynağı neden seçtiğini açıklamak;
- primary source ile republisher'ı ayırmak;
- source dependency tespit etmek;
- alternative hypothesis üretmek;
- limitations açıkça yazmak;
- haftalar sonra yalnızca notlarından araştırmayı yeniden kurmak.

---

Profesyonel seviye “gizli bir araç” bulmak değildir. Sonucun başkaları tarafından incelenebilmesi ve savunulabilmesidir.