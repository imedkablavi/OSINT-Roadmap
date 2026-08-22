# مكتبة أدوات OSINT

> آخر مراجعة: **2026-08-22** · [English](tool-library.md) · العربية · [Türkçe](tool-library.tr.md)

هذه **مكتبة تعليمية منتقاة** وليست تجميعاً عشوائياً لكل رابط يحمل اسم OSINT. نضيف الأداة عندما تحل مشكلة واضحة في البحث بالمصادر العامة ويمكن وضع نتيجتها داخل سير عمل قابل للتوثيق والمراجعة.

نتيجة الأداة هي **مؤشر أو ملاحظة** وليست إثباتاً تلقائياً. النتائج المهمة يجب الرجوع فيها إلى المصدر الأصلي والتحقق منها بشكل مستقل متى أمكن.

## كيف تقرأ المكتبة؟

| الحقل | معناه |
| --- | --- |
| Input | الشيء الذي تبدأ منه عادةً |
| الكلفة | مجاني، Freemium، مدفوع، أو Self-hosted |
| المستوى | مبتدئ، متوسط، متقدم |
| الأفضل لـ | السؤال الذي تساعدك الأداة على الإجابة عنه |
| أهم قيد | الشيء الذي لا تثبته النتيجة أو المكان الذي قد يسبب استنتاجاً خاطئاً |

## مجموعات بداية مقترحة

### الأساسيات للمبتدئ

Google Search · Internet Archive · SingleFile · Google Lens · TinEye · Google Earth · OpenStreetMap · ExifTool

### GEOINT

Google Earth · OpenStreetMap · Mapillary · SunCalc · PeakVisor · Copernicus Browser · NASA Worldview · QGIS

### CTI والبنية التحتية

VirusTotal · urlscan.io · Shodan · Censys · GreyNoise · ThreatFox · RIPEstat · crt.sh

### التحقيق في الشركات

OpenCorporates · GLEIF LEI Search · OpenSanctions · OCCRP Aleph · ICIJ Offshore Leaks · SEC EDGAR · Companies House

### المراقبة والأرشفة

Internet Archive · Archive.today · changedetection.io · GDELT · Hunchly · SingleFile · OpenRefine

---

# 1. البحث والاكتشاف والأرشفة

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Google Search](https://www.google.com/) | كلمات، أسماء، Domains | مجاني | مبتدئ | البحث العام، العبارات الدقيقة، `site:` والملفات | الترتيب والتخصيص قد يخفيان نتائج |
| [Bing](https://www.bing.com/) | كلمات، صور | مجاني | مبتدئ | فهرس بحث ثانٍ وبحث بصري | التغطية تختلف عن Google |
| [Brave Search](https://search.brave.com/) | كلمات | مجاني / مدفوع | مبتدئ | منظور بحث إضافي أكثر استقلالية | بعض المجالات الصغيرة أقل تغطية |
| [Kagi](https://kagi.com/) | كلمات | مدفوع | مبتدئ | بحث أقل ضجيجاً وسير عمل بحثي | يحتاج اشتراكاً |
| [SearXNG](https://searxng.org/) | كلمات | مجاني / Self-hosted | متوسط | Meta-search عبر عدة محركات | الجودة تعتمد على الـinstance والمحركات المفعلة |
| [GDELT](https://www.gdeltproject.org/) | موضوع، كيان، مكان | مجاني | متوسط | اكتشاف الأخبار والأحداث وتحليل الاتجاهات | استخراج الأحداث يحتاج تحققاً سياقياً |
| [Google Scholar](https://scholar.google.com/) | موضوع أكاديمي، مؤلف | مجاني | مبتدئ | أبحاث، citations، ومصادر أكاديمية | ليس كل محتوى مفهرس peer-reviewed |
| [Internet Archive](https://web.archive.org/) | URL | مجاني | مبتدئ | نسخ تاريخية من صفحات عامة | غياب النسخة لا يثبت أن الصفحة لم توجد |
| [Archive.today](https://archive.ph/) | URL | مجاني | مبتدئ | Snapshot لنقطة زمنية | التغطية والتوفر متفاوتان |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | صفحة ويب | مجاني | مبتدئ | حفظ الصفحة محلياً في HTML واحد | يحفظ ما عرضه المتصفح وليس تاريخ الخادم |
| [ArchiveBox](https://archivebox.io/) | URLs | مجاني / Self-hosted | متوسط | إنشاء أرشيف بحثي محلي | يحتاج تخزيناً وصيانة |
| [changedetection.io](https://changedetection.io/) | URL | مجاني / مدفوع / Self-hosted | متوسط | متابعة تغير صفحات الويب | الصفحات الديناميكية قد تولد تنبيهات كثيرة |

# 2. أسماء المستخدمين والهوية العامة

استخدم أدوات الهوية لسؤال بحثي مشروع ومحدد. تطابق Username أو Avatar أو Display Name لا يثبت أن حسابين يعودان للشخص نفسه.

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | Username | مجاني | مبتدئ | فحص اسم مستخدم عبر خدمات عامة كثيرة | False positives وإعادة استخدام الأسماء |
| [Sherlock](https://github.com/sherlock-project/sherlock) | Username | مجاني | متوسط | فحص CLI عبر مواقع متعددة | النتيجة تثبت وجود handle فقط |
| [Maigret](https://github.com/soxoj/maigret) | Username | مجاني | متوسط | Username enumeration وتقارير | تغييرات المنصات تكسر بعض الفحوصات |
| [Epieos](https://epieos.com/) | Email / Phone ضمن القانون | Freemium | متوسط | قرائن حسابات عامة وعمليات pivot | النتائج قد تكون حساسة؛ اجمع الحد الأدنى وتحقق مستقلاً |
| [GitHub Search](https://github.com/search) | Username، Code، Organization | مجاني | مبتدئ | Profiles وRepositories وCommits عامة | هوية GitHub لا تثبت الهوية الواقعية وحدها |

# 3. التحقق من الصور والفيديو

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Google Lens](https://lens.google/) | صورة | مجاني | مبتدئ | Visual matches والنصوص والعناصر الظاهرة | التشابه لا يثبت المصدر الأصلي |
| [TinEye](https://tineye.com/) | صورة | مجاني / مدفوع | مبتدئ | العثور على نسخ مطابقة أو معدلة | فهرسه أصغر من محركات البحث العامة |
| [Yandex Images](https://yandex.com/images/) | صورة | مجاني | مبتدئ | بديل قوي للبحث البصري | كل نتيجة تحتاج تحقق مصدر |
| [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | فيديو / صورة / URL | مجاني | متوسط | Keyframes وأدوات تحقق | يساعد التحليل ولا يتحقق من الادعاء تلقائياً |
| [ExifTool](https://exiftool.org/) | ملف محلي | مجاني | متوسط | قراءة Metadata لأنواع ملفات كثيرة | Metadata قد تُحذف أو تُعدل |
| [FotoForensics](https://fotoforensics.com/) | صورة | مجاني | متوسط | تعلم إشارات Forensics والضغط | ELA وحده لا يثبت التلاعب |
| [FFmpeg](https://ffmpeg.org/) | Video / Audio | مجاني | متوسط | استخراج Frames وصوت وتجهيز نسخة للتحليل | احتفظ بالأصل لأن المعالجة تغير الملف |

# 4. GEOINT والخرائط والأقمار الصناعية

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Google Maps](https://maps.google.com/) | Location / Coordinates | مجاني | مبتدئ | طرق، شركات، معالم، Street View | الصور والبيانات التجارية قد تكون قديمة |
| [Google Earth](https://earth.google.com/) | Location | مجاني | مبتدئ | Terrain و3D وصور تاريخية حيث تتوفر | التاريخ المتوفر يختلف حسب المنطقة |
| [OpenStreetMap](https://www.openstreetmap.org/) | Location / Feature | مجاني | مبتدئ | بيانات خرائط مفتوحة وطرق ومعالم | التغطية المجتمعية غير متساوية |
| [Mapillary](https://www.mapillary.com/) | Location | مجاني | متوسط | صور Street-level من المستخدمين | التاريخ والتغطية متفاوتان جداً |
| [SunCalc](https://www.suncalc.org/) | Location + Time | مجاني | متوسط | اختبار اتجاه الشمس والظل | يحتاج فرضية مكان/وقت معقولة |
| [PeakVisor](https://peakvisor.com/) | Landscape / Location | Freemium | متوسط | التعرف على الجبال والـskyline | التضاريس المتشابهة قد تسبب Match خاطئ |
| [Copernicus Browser](https://dataspace.copernicus.eu/browser/) | Area + Date | حساب مجاني | متوسط | Sentinel imagery والمقارنة والتحميل | السحب والدقة المكانية تحدان بعض التحقيقات |
| [NASA Worldview](https://worldview.earthdata.nasa.gov/) | Area + Date | مجاني | متوسط | طبقات Earth observation وأحداث بيئية شبه فورية | كثير من الطبقات أقل دقة من الصور التجارية |
| [QGIS](https://qgis.org/) | Geospatial files | مجاني | متقدم | دمج وتحليل وقياس طبقات مكانية | يحتاج معرفة GIS وأنظمة الإحداثيات |

# 5. Domains وIPs والبنية التحتية

هذه الأدوات هنا للبحث **السلبي في السجلات العامة والبيانات التي جُمعت مسبقاً**. الفحص النشط قد يحتاج تفويضاً صريحاً.

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [ICANN Lookup](https://lookup.icann.org/) | Domain | مجاني | مبتدئ | بيانات RDAP/Registration العامة الحالية | Privacy redaction شائع |
| [crt.sh](https://crt.sh/) | Domain / Organization | مجاني | متوسط | Certificate Transparency history | إصدار شهادة لا يثبت الملكية الحالية |
| [SecurityTrails](https://securitytrails.com/) | Domain / IP | Freemium | متوسط | DNS history والسياق البنيوي | العمق حسب التغطية والخطة |
| [DNSDumpster](https://dnsdumpster.com/) | Domain | مجاني | مبتدئ | DNS discovery بصري | العلاقات المكتشفة Leads وليست Attribution |
| [BuiltWith](https://builtwith.com/) | Domain | Freemium | مبتدئ | Technologies المستخدمة بالموقع | الكشف قد يكون ناقصاً أو قديماً |
| [Wappalyzer](https://www.wappalyzer.com/) | Webpage / Domain | Freemium | مبتدئ | Technologies في صفحات الويب | Client-side detection ليس دائماً صحيحاً |
| [RIPEstat](https://stat.ripe.net/) | IP / ASN | مجاني | متوسط | Routing وAllocation وASN context | الـallocation لا يثبت المشغل الفعلي في وقت محدد |
| [BGP.tools](https://bgp.tools/) | ASN / Prefix | مجاني | متوسط | BGP routing والسياق الشبكي | علاقات routing تتغير |
| [Cloudflare Radar](https://radar.cloudflare.com/) | Domain / ASN / Trend | مجاني | متوسط | Internet trends وrouting وtechnology | بيانات مجمعة وليست رؤية كاملة للإنترنت |

# 6. CTI وإثراء المؤشرات العامة

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [VirusTotal](https://www.virustotal.com/) | Hash، URL، Domain، IP، File | Freemium | مبتدئ | Multi-source enrichment وسياق تاريخي | Public uploads قد تكشف مواد حساسة |
| [urlscan.io](https://urlscan.io/) | URL / Domain | Freemium | متوسط | Requests وDOM وScreenshot والبنية المرصودة | راجع Visibility قبل إرسال URL حساس |
| [Shodan](https://www.shodan.io/) | IP / Domain / Query | Freemium | متوسط | خدمات Internet-facing مرصودة سابقاً | البيانات قد تكون قديمة |
| [Censys](https://search.censys.io/) | IP / Domain / Certificate | Freemium | متوسط | Hosts وServices وCertificates | النتيجة مرتبطة بزمن المسح والتغطية |
| [GreyNoise](https://viz.greynoise.io/) | IP | Freemium | متوسط | فهم Internet noise/scanning | التصنيف سياقي وليس إثبات نية |
| [AlienVault OTX](https://otx.alienvault.com/) | IOC | مجاني | متوسط | Community threat pulses | جودة المصادر المجتمعية متفاوتة |
| [Pulsedive](https://pulsedive.com/) | Domain / IP / URL | Freemium | مبتدئ | Threat-intel enrichment سريع | Score يحتاج مراجعة المصدر |
| [ThreatFox](https://threatfox.abuse.ch/) | IOC | مجاني | متوسط | Indicators مرتبطة بMalware | المؤشرات تتقادم بسرعة |
| [URLhaus](https://urlhaus.abuse.ch/) | URL / Host | مجاني | متوسط | Malware distribution URLs | الغياب لا يعني أن الرابط آمن |
| [MalwareBazaar](https://bazaar.abuse.ch/) | Hash / Sample metadata | مجاني | متوسط | Malware intelligence والـhashes | التعامل مع Samples حية يحتاج ضوابط متخصصة |
| [AbuseIPDB](https://www.abuseipdb.com/) | IP | Freemium | مبتدئ | Community abuse reports | التقارير قديمة أو خاطئة أحياناً |

# 7. الشركات والملكية والسجلات العامة

قبل الاستنتاج، تأكد من Legal Entity باستخدام Jurisdiction وIdentifiers والتواريخ والعناوين، وليس الاسم فقط.

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [OpenCorporates](https://opencorporates.com/) | Company / Officer | Freemium | مبتدئ | اكتشاف الشركات عبر عدة jurisdictions | التغطية تختلف حسب السجل |
| [GLEIF LEI Search](https://search.gleif.org/) | Legal Name / LEI | مجاني | متوسط | معرفات قانونية موحدة وعلاقات Parent عندما تكون مبلغاً عنها | يغطي الكيانات التي لديها LEI فقط |
| [OpenSanctions](https://www.opensanctions.org/) | Person / Organization | مجاني لغير التجاري / مدفوع | متوسط | Sanctions وPEP وEntity datasets بمصادر واضحة | Name match وحده لا يثبت الهوية |
| [OCCRP Aleph](https://aleph.occrp.org/) | Person / Company / Document | حساب مجاني / وصول حسب البيانات | متوسط | وثائق وتحقيقات وStructured entities | الوصول يعتمد على مجموعة البيانات |
| [ICIJ Offshore Leaks](https://offshoreleaks.icij.org/) | Name / Company / Address | مجاني | متوسط | علاقات Offshore من تحقيقات كبرى | الظهور لا يعني سلوكاً غير قانوني ويجب تثبيت الهوية |
| [SEC EDGAR](https://www.sec.gov/search-filings) | US Company / Ticker / CIK | مجاني | متوسط | Filings رسمية للشركات العامة الأمريكية | النطاق أساساً كيانات تخضع للـSEC |
| [UK Companies House](https://find-and-update.company-information.service.gov.uk/) | UK Company / Officer | مجاني | مبتدئ | Filings وضباط شركات بريطانية رسمية | بعض البيانات قديمة أو Self-reported |

# 8. الطيران والبحر والنقل

منصات التتبع فيها Coverage gaps وتأخير وTargets مخفية. استخدم أكثر من مصدر وسجل Timestamp.

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Flightradar24](https://www.flightradar24.com/) | Flight / Aircraft / Location | Freemium | مبتدئ | سياق Live وHistorical للطيران | التغطية والتاريخ حسب Receivers والخطة |
| [ADS-B Exchange](https://www.adsbexchange.com/) | Aircraft / Location | Freemium | متوسط | ADS-B observations | ليس كل Aircraft يبث بيانات كاملة |
| [OpenSky Network](https://opensky-network.org/) | Aircraft / Time / Area | مجاني / Research | متوسط | Aviation datasets وأبحاث | API/History لها حدود |
| [MarineTraffic](https://www.marinetraffic.com/) | Vessel / IMO / MMSI | Freemium | مبتدئ | AIS positions ونشاط الموانئ | AIS قد يغيب أو يتأخر أو يكون خاطئاً |
| [VesselFinder](https://www.vesselfinder.com/) | Vessel / IMO / MMSI | Freemium | مبتدئ | بديل لتتبع AIS | نفس قيود AIS العامة |

# 9. المستندات والبيانات المنظمة والتنظيف

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Apache Tika](https://tika.apache.org/) | Documents / Files | مجاني | متقدم | استخراج Text وMetadata من أنواع ملفات كثيرة | النص المستخرج قد يفقد Layout والسياق |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/) | Scanned PDF | مجاني | متوسط | إضافة OCR قابل للبحث | أخطاء OCR يجب مراجعتها مقابل الصورة |
| [Tabula](https://tabula.technology/) | PDF Tables | مجاني | مبتدئ | استخراج جداول من PDF | Layout المعقد يحتاج Cleanup يدوي |
| [OpenRefine](https://openrefine.org/) | CSV / Tabular Data | مجاني | متوسط | تنظيف وNormalization وReconciliation | التحويلات غير الموثقة قد تخفي أخطاء |
| [CyberChef](https://gchq.github.io/CyberChef/) | Text / Encoded Data / Files | مجاني | متوسط | فك وتحويل بيانات تقنية | التحويل ليس تفسيراً أو Attribution |
| [jq](https://jqlang.org/) | JSON | مجاني | متوسط | Query وTransform لبيانات JSON | يحتاج راحة مع CLI |

# 10. مساحة العمل وتحليل العلاقات

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Hunchly](https://www.hunch.ly/) | Browsing Session | مدفوع | مبتدئ | حفظ الصفحات وسياق جلسة البحث | الحفظ لا يتحقق من صحة الادعاءات |
| [Vortimo](https://www.vortimo.com/) | Web Research | Freemium / مدفوع | متوسط | تنظيم مواد البحث العام | القيمة تعتمد على Notes وTagging منظم |
| [Maltego](https://www.maltego.com/) | Entities / Indicators | Freemium / مدفوع | متوسط | Relationship graphs وPivots | الرسم الجميل قد يخفي علاقة ضعيفة |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | Domain / IP / Name وغيره | مجاني / خيارات تجارية | متقدم | أتمتة Modules OSINT عديدة | Automation تولد Noise وتحتاج Validation |
| [Gephi](https://gephi.org/) | Graph Data | مجاني | متقدم | Visualizing شبكات كبيرة | القرب البصري لا يساوي علاقة سببية حقيقية |

# 11. Blockchain وCryptocurrency

| الأداة | Input | الكلفة | المستوى | الأفضل لـ | أهم قيد |
| --- | --- | --- | --- | --- | --- |
| [Etherscan](https://etherscan.io/) | Ethereum Address / TX / Contract | مجاني / API مدفوع | مبتدئ | معاملات وعقود Ethereum | Attribution للعنوان يحتاج دليلاً خارج السلسلة |
| [Tronscan](https://tronscan.org/) | TRON Address / TX | مجاني | مبتدئ | نشاط TRON وعقوده | On-chain activity لا يحدد الإنسان وحده |
| [Blockchair](https://blockchair.com/) | Address / TX / Block | Freemium | مبتدئ | Multi-chain explorer | الخصائص والتغطية تختلف حسب الشبكة |
| [Breadcrumbs](https://www.breadcrumbs.app/) | Crypto Address | Freemium | متوسط | Transaction graphing | Labels وClusters تحتاج Provenance |
| [Arkham](https://intel.arkm.com/) | Address / Entity Label | Freemium | متوسط | Labels وعلاقات Blockchain | Label المنصة Lead وليس إثبات هوية تلقائياً |

---

# مصادر تعلم تستحق الحفظ

| المصدر | لماذا يفيد؟ |
| --- | --- |
| [Bellingcat Online Investigations Toolkit](https://bellingcat.gitbook.io/toolkit) | أدوات منتقاة مع الاستخدام والكلفة والصعوبة والمتطلبات والقيود |
| [OSINT Dojo](https://www.osintdojo.com/) | Challenges متدرجة ومستويات للمبتدئين |
| [GIJN Resource Center](https://gijn.org/resource/) | أدلة تحقيق، قواعد بيانات، Verification، شركات، أقمار صناعية ومحتوى بعدة لغات |
| [Verification Handbook](https://verificationhandbook.com/) | منهجيات منظمة للتحقق من المحتوى الرقمي |
| [OSINT Framework](https://osintframework.com/) | اكتشاف سريع لفئات وأدوات البحث العام |
| [IntelTechniques Tools](https://inteltechniques.com/tools/) | Utilities ومراجع عملية للبحث |
| [Awesome OSINT](https://github.com/jivoi/awesome-osint) | دليل واسع عندما تحتاج شيئاً خارج القائمة المنتقاة |
| [OSINT Tools Library](https://github.com/The-OSINT-Newsletter/OSINT-Tools-Library) | دليل يركز على أدوات تستخدم في تحقيقات حقيقية والصيانة المستمرة |

# طريقة اختيار الأداة

```text
ابدأ بالسؤال البحثي
        ↓
حدد الـInput الحقيقي الذي تملكه
        ↓
اختر أصغر أداة تجيب عن سؤال واحد
        ↓
سجل المصدر + الوقت + Query
        ↓
تحقق من النتيجة في المصدر الأصلي
        ↓
أكد الادعاءات المهمة بمصدر مستقل
        ↓
وثق عدم اليقين وStop Conditions
```

# سياسة صيانة المكتبة

نخفض تقييم الأداة أو نحذفها عندما:

- يتوقف المشروع الرسمي وتصبح البدائل أفضل؛
- تصبح الخدمة غير موثوقة أو مضللة؛
- تسوء صلاحياتها أو سياسة الخصوصية بشكل مهم؛
- تعتمد أساساً على بيانات خاصة تم الحصول عليها بشكل غير مشروع؛
- لا يمكن شرح أو التحقق من مخرجاتها؛
- يتغير الرابط الرسمي ولا يمكن التحقق من البديل.

إذا لاحظت تغيراً استخدم Issue Template الخاص بـ **Resource suggestion** أو **Broken link**.
