# OSINT Yol Haritası

## Açık Kaynak İstihbaratı için pratik ve kanıta dayalı öğrenme yolu

[![GitHub Repo stars](https://img.shields.io/github/stars/imedkablavi/OSINT-Roadmap?style=plastic)](https://github.com/imedkablavi/OSINT-Roadmap/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/imedkablavi/OSINT-Roadmap?style=plastic)](https://github.com/imedkablavi/OSINT-Roadmap/network/members)
[![GitHub contributors](https://img.shields.io/github/contributors/imedkablavi/OSINT-Roadmap?style=plastic)](https://github.com/imedkablavi/OSINT-Roadmap/graphs/contributors)
[![Latest release](https://img.shields.io/github/v/release/imedkablavi/OSINT-Roadmap?style=plastic&label=latest)](https://github.com/imedkablavi/OSINT-Roadmap/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=plastic)](LICENSE)
[![Link Health](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/link-check.yml/badge.svg)](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/link-check.yml)
[![Tool Freshness](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/tool-freshness.yml/badge.svg)](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/tool-freshness.yml)

> Bu depo bir araç listesi değildir. Amaç; doğru soruyu kurmayı, açık kaynakları bulmayı, önemli bulguları doğrulamayı ve sonucu sınırlarıyla birlikte raporlamayı öğretmektir.

---

## Yol Haritası

![OSINT Roadmap — Research to Intelligence](assets/osint-roadmap.svg)

Sıralama özellikle böyledir. Araçlar değişebilir; araştırma disiplini daha uzun süre kullanılabilir.

~~~text
Soruyu tanımla
      ↓
Kapsamı belirle
      ↓
Kaynakları keşfet
      ↓
Önemli iddiaları doğrula
      ↓
Bulguları ve zaman çizelgelerini ilişkilendir
      ↓
Güveni ve alternatifleri değerlendir
      ↓
Sonucu raporla
      ↓
Bir uzmanlık alanı seç
~~~

### Yol haritasını nasıl kullanmalı?

Araştırma boyunca şu ayrımı koru:

| Katman | Soru |
| --- | --- |
| Soru | Tam olarak neyi öğrenmeye çalışıyorum? |
| Kanıt | Bu soruya cevap verebilecek hangi kamuya açık kaynaklar var? |
| Analiz | Kaynakları birlikte değerlendirdiğimde ne anlama geliyorlar? |
| Değerlendirme | Neyi savunabilirim, neyin belirsiz kaldığını açıkça söyleyebilir miyim? |

Bir arama sonucu yararlı olabilir ama tek başına kanıt değildir. Bir araç sonucu da doğrulanmadan gerçek kabul edilmemelidir.

> [!IMPORTANT]
> **Bir bulgu kanıtla aynı şey değildir. Aynı iddianın birçok yerde tekrar edilmesi de bağımsız doğrulama anlamına gelmez.**

---

## OSINT nedir?

OSINT, kamuya açık kaynaklardan bilgi toplama, doğrulama, ilişkilendirme, analiz etme ve belirli bir soruyu cevaplayacak şekilde raporlama sürecidir.

Buradaki önemli nokta yöntemdir. Araştırma sorusu olmadan yapılan arama gürültü üretir. Doğrulanmadan toplanan bilgi ise yanlış güven duygusu oluşturabilir.

Açık kaynaklara web siteleri, arşivler, haberler, kamu kayıtları, şirket sicilleri, haritalar, uydu görüntüleri, görseller, videolar, alan adı ve DNS kayıtları, akademik yayınlar ve açık veri setleri örnek verilebilir.

OSINT, yetkisiz erişim değildir. Bu yol haritası yasal ve gerçekten kamuya açık bilgiyle yapılan araştırmaya odaklanır.

---

## Nereden başlamalı?

Elindeki ipucunu seç ve küçük bir araştırmayı baştan sona tamamla.

| Başlangıç ipucu | İlk adım |
| --- | --- |
| Alan adı | [Alan adı playbook'u](playbooks/README.md#i-have-a-domain) |
| Kullanıcı adı | [Kullanıcı adı playbook'u](playbooks/README.md#i-have-a-username) |
| E-posta veya telefon | [Kimlik ve atıf çalışma akışı](playbooks/README.md#i-have-a-username) |
| Görsel | [Görsel playbook'u](playbooks/README.md#i-have-an-image) |
| Video | [Video playbook'u](playbooks/README.md#i-have-a-video) |
| Şirket | [Şirket playbook'u](playbooks/README.md#i-have-a-company-name) |
| IP adresi | [IP playbook'u](playbooks/README.md#i-have-an-ip-address) |
| Kamuya açık belge | [Belge playbook'u](playbooks/README.md#i-have-a-public-document) |
| Haber iddiası | [Haber doğrulama playbook'u](playbooks/README.md#i-have-a-news-claim) |
| Konum iddiası | [Konum doğrulama playbook'u](playbooks/README.md#i-have-a-location-claim) |

Araç isimlerini ezberlemekten önce bir araştırmayı soru, kaynak, doğrulama ve rapor aşamalarından geçirebilmek daha önemlidir.

---

## Temeller

Önce şu alışkanlıkları edin:

- araştırma sorusu yazma;
- kapsam ve durma koşulu belirleme;
- kaynak kökenini ve bağımlılığını değerlendirme;
- bağımsız doğrulama yapma;
- tarih ve saat dilimlerini doğru ele alma;
- varlıkları ve ilişkileri çözümleme;
- güven ve belirsizliği ifade etme;
- notları ve kanıtları düzenleme;
- araştırmacı OPSEC'ini koruma.

[Research Methods](docs/tr/research-methods.md)  
[Skill Matrix](docs/skill-matrix.md)  
[OSINT Quick Reference](cheatsheets/osint-quick-reference.md)

---

## Keşif

### Arama ve arşiv

Şunları öğren:

- Boolean ve tam ifade araması;
- site, filetype, başlık ve tarih filtreleri;
- web arşivlerinden eski sayfaları yeniden oluşturma;
- çok dilli arama ve transliterasyon;
- bir iddiayı mümkün olduğunca erken kaynağa kadar takip etme.

### Kimlik ve dijital ayak izi

Kamuya açık sinyallerle çalış:

- kullanıcı adları;
- e-posta adresleri;
- kamuya açık telefon numaraları;
- sabit tanımlayıcılar;
- hesapların kendi verdiği bağlantılar;
- arşivlenmiş profil geçmişi.

Aynı kullanıcı adının bulunması tek başına aynı kişiyi göstermez.

### Şirketler ve kamu kayıtları

Önce varlığı doğru çözümle:

- tüzel kişi kaydı;
- resmi dosyalar;
- sahiplik ve ilişkiler;
- kamu ihaleleri ve düzenleyici kayıtlar;
- şirket zaman çizelgesi.

Yanlış şirketi araştırıyorsan, sonraki analiz ne kadar ayrıntılı olursa olsun sonuç yanlış kalır.

---

## Doğrulama

### Görsel ve video

Çalış:

- tersine görsel arama;
- en erken kamuya açık görünüm;
- yeniden paylaşım ve kaynak zinciri;
- videodan kare çıkarma;
- tabela, yazı ve mimari ayrıntılar;
- yol, arazi ve çevre karşılaştırması;
- hava ve zaman tutarlılığı;
- metadata'yı dikkatli yorumlama.

[Tarayıcı Eklentileri ve Web Araçları](tools/browser-extensions.tr.md)

### Haber ve iddia doğrulama

Bir iddiayı yalnızca aynı cümleyi arayarak doğrulamaya çalışma.

Mümkün olduğunca:

1. ilk kaynağı bul;
2. birincil belge veya doğrudan açıklama ara;
3. bağımsız haberleri karşılaştır;
4. düzeltme ve güncellemeleri kontrol et;
5. gerekli olduğunda arşivlenmiş sürümleri incele.

### GEOINT

Konum araştırmasında genişten dara ilerle:

~~~text
Ülke veya bölge
      ↓
Şehir veya alan
      ↓
Yol, yapı, arazi veya belirgin işaret
      ↓
Kesin nokta, yalnızca kanıt izin veriyorsa
~~~

[İleri GEOINT Challenges](challenges/advanced-geoint.md)

---

## Analiz

Önemli bulgular doğrulandıktan sonra onları birbiriyle ilişkilendir.

Çalışılacak konular:

- varlık çözümleme;
- ilişki haritalama;
- zaman çizelgesi analizi;
- coğrafi korelasyon;
- alternatif hipotezler;
- güven düzeyi belirleme;
- eksik veri analizi.

Amaç mümkün olan en büyük grafiği üretmek değil, mevcut kanıtın taşıyabildiği en sade açıklamayı kurmaktır.

---

## Raporlama

Başka bir araştırmacı sonuca nasıl ulaştığını anlayabilmeli.

~~~text
Araştırma sorusu
Kapsam
Yöntem
Kaynaklar
Bulgular
Analiz
Güven düzeyi
Sınırlamalar
Sonuç
~~~

[Türkçe OSINT Rapor Şablonu](docs/tr/report-template.md)

---

## Uzmanlaşma

Temel iş akışı oturduktan sonra bir uzmanlık alanı seç:

| Alan | Odak |
| --- | --- |
| [Cyber Threat Intelligence](tracks/cti.md) | PIR, kamuya açık göstergeler, altyapı ilişkileri, ATT&CK, zaman çizelgeleri, atıf |
| [Digital Footprint Investigation](tracks/digital-footprint.md) | kamuya açık izler, tanımlayıcılar, atıf, arşiv, veri minimizasyonu |
| [Company Investigation](tracks/company-investigation.md) | tüzel kişi, kayıtlar, sahiplik, şirket zaman çizelgesi |
| [Advanced GEOINT](challenges/advanced-geoint.md) | geolocation, chronolocation, görüntü ve aday eleme |
| Gazetecilik ve fact-checking | kaynak takibi, medya kökeni, iddia doğrulama |
| Public Web Infrastructure | domain, DNS, sertifikalar ve pasif altyapı araştırması |

Alan değişir; kanıt standardı değişmez.

---

## Araç Kütüphanesi

Depo, internetteki bütün araçları listelemeye çalışmak yerine seçilmiş bir OSINT araç ve kaynak kütüphanesi tutar.

Kapsanan alanlar:

- arama ve arşiv;
- kullanıcı adı, e-posta ve telefon;
- görsel ve video doğrulama;
- GEOINT ve harita araştırması;
- domain, IP ve internet altyapısı;
- CTI ve kamuya açık IOC zenginleştirme;
- şirketler ve kamu kayıtları;
- havacılık, denizcilik ve demiryolu araştırması;
- belge işleme;
- ilişki ve zaman çizelgesi analizi;
- blockchain araştırması;
- akademik metadata.

Her araç için şu sorulara cevap arayın:

~~~text
Hangi girdiyi kullanıyor?
Nerede işe yarıyor?
Maliyeti nedir?
Neyi kanıtlamıyor?
~~~

[Türkçe Araç Kütüphanesi](tools/tool-library.tr.md)  
[Araştırmacı Araç Seti](tools/investigator-stack.tr.md)  
[Doğrulanmış Açık Kaynak Araçlar](tools/open-source-tools.tr.md)

---

## Uygulama

Bir videoyu izlemek veya bir aracı bir kez çalıştırmak beceriyi tamamlamaz.

~~~text
Öğren
  ↓
Pratik yap
  ↓
Üret
  ↓
Açıkla
  ↓
Savun
  ↓
Gözden geçir
~~~

Faydalı çıktılar arasında kaynak değerlendirmesi, zaman çizelgesi, görsel doğrulama raporu, GEOINT çalışması, atıf değerlendirmesi ve kısa istihbarat notu bulunabilir.

[Pratik Laboratuvarları](docs/tr/practice-labs.md)  
[Skill Matrix](docs/skill-matrix.md)  
[Case Studies](case-studies/README.md)

---

## Yapay Zekâ Destekli OSINT

Yapay zekâ şu tür yardımcı işlerde faydalı olabilir:

- arama sorgusu varyasyonları üretmek;
- çeviri ve transliterasyon seçenekleri önermek;
- kendi notlarından aday varlıkları çıkarmak;
- topladığın materyali düzenlemek;
- alternatif hipotezler önermek;
- yapılandırılmış veriyi temizlemek.

Fakat model çıktısı kaynak değildir.

~~~text
Yapay zekâ bir yol önerir
        ↓
Kaynağı sen incelersin
        ↓
İddiayı sen doğrularsın
        ↓
Sonucu sen belgelersin
~~~

Önemli isim, tarih, alıntı, URL, ilişki ve sonuçları mutlaka asıl kamuya açık kaynakla kontrol et.

---

## Kapsam, Etik ve Güvenli Kullanım

Bu yol haritası yasal ve gerçekten kamuya açık bilgilerle yapılan araştırmayla sınırlıdır.

Şunları kapsamaz:

- yetkisiz erişim;
- parola veya kimlik bilgisi saldırıları;
- hesap ele geçirme;
- erişim kontrollerini aşma;
- aldatıcı sosyal mühendislik;
- taciz veya doxxing;
- izinsiz aktif tarama;
- özel hesap veya özel içeriğe erişim.

Pratik durma kuralı:

~~~text
Bir sonraki adım saldırı,
aldatma, özel erişim
veya güvenlik kontrolünü
aşmayı gerektiriyorsa:
dur.
~~~

İyi OSINT ayrıca araştırma sorusuyla ilgisi olmayan kişisel bilgileri toplamamayı gerektirir.

---

## Bakım ve Güncellik

OSINT ekosistemi hızlı değişir.

Bir aracın sahibi, fiyatı, izinleri, arayüzü, kapsamı veya kullanım şartları değişebilir. Bu nedenle çalışan bir URL, katalog bilgisinin doğru veya güncel olduğunu tek başına göstermez.

[OSINT Tool Radar](updates/2026-08-tool-radar.md)  
[Güncellemeler Arşivi](updates/README.md)

Depo bağlantı sağlığı ile içerik güncelliğini ayrı ayrı kontrol eder.

---

## Katkıda bulunma

İyi katkılar genellikle küçük, açık ve doğrulanabilir olur.

Şunlarda yardımcı olabilirsin:

- kaynak veya bağlantı düzeltmek;
- eski bir kaynağı güncellemek;
- çeviriyi iyileştirmek;
- güvenli bir pratik laboratuvarı eklemek;
- daha iyi bir doğrulama yöntemi belgelemek;
- yeni bir playbook eklemek;
- bir aracın sınırlarını daha doğru açıklamak.

[Katkı Rehberi](CONTRIBUTING.md)

Tek bir doğru kaynak eklemek veya metodoloji hatasını düzeltmek bile sonraki araştırmacı için gerçek bir fark yaratabilir.

---

## Lisans

MIT License © Imed Kablavi
