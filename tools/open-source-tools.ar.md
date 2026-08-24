# أدوات OSINT مفتوحة المصدر الموثقة

> آخر مراجعة: **2026-08-24** · العربية · [English](open-source-tools.md) · [Türkçe](open-source-tools.tr.md)

تضم هذه الصفحة الأدوات التي تم التحقق من مشروعها الأصلي وترخيصها الحالي قبل وضع وسم **Open Source** عليها. وجود كود عام بدون ترخيص واضح لا يكفي لاعتبار المشروع مفتوح المصدر في هذه الخارطة.

## الاكتشاف والأرشفة والهوية

| الأداة | الترخيص | الدور العملي | أهم قيد |
| --- | --- | --- | --- |
| [Bellingcat Auto Archiver](https://github.com/bellingcat/auto-archiver) | MIT | أتمتة حفظ الروابط العامة والوسائط والمنشورات | يجب حفظ مصدر الأرشيف ووقت الالتقاط |
| [Browsertrix](https://github.com/webrecorder/browsertrix) | AGPL-3.0 | أرشفة ويب عالية الدقة عبر متصفح فعلي | يجب ضبط نطاق الزحف واحترام قيود الوصول |
| [ReplayWeb.page](https://github.com/webrecorder/replayweb.page) | AGPL-3.0 | إعادة تشغيل أرشيفات WARC/WACZ | إعادة العرض لا تثبت وحدها وقت الالتقاط أو الأصالة |
| [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) | GPL-3.0 | تنظيم البحث العام حول أرقام الهاتف ومحاور البحث | بيانات الرقم لا تثبت هوية المشترك |
| [GHunt](https://github.com/mxrch/GHunt) | AGPL-3.0 | بحث OSINT حول معلومات Google العامة | بعض الوحدات تحتاج جلسة Google؛ قلل تعريض الحساب |

## البنية التحتية وCTI

| الأداة | الترخيص | الدور العملي | أهم قيد |
| --- | --- | --- | --- |
| [theHarvester](https://github.com/laramies/theHarvester) | GPL-2.0 | تجميع مصادر بنية تحتية عامة وسلبية | المصادر والحصص ومفاتيح API تتغير |
| [OWASP Amass](https://github.com/owasp-amass/amass) | Apache-2.0 | اكتشاف الأصول الخارجية ورسم العلاقات | التقنيات النشطة تحتاج تفويضًا صريحًا |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | MIT | تعداد النطاقات الفرعية بشكل سلبي | بعض المصادر تتغير أو تحتاج API keys |
| [OpenCTI Community Edition](https://github.com/OpenCTI-Platform/opencti) | Apache-2.0 (CE) | تنظيم وربط معرفة CTI | تقييم المصدر والثقة يبقى مسؤولية المحلل |
| [MISP](https://github.com/MISP/MISP) | AGPL-3.0 | مشاركة معلومات التهديدات بشكل منظم | جودة بيانات المجتمع وقواعد المشاركة تحتاج حوكمة |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | AGPL-3.0 | تنسيق enrichment للمؤشرات والملفات | المحللات الخارجية قد تستقبل الملفات أو المؤشرات المرسلة |
| [YETI](https://github.com/yeti-platform/yeti) | Apache-2.0 | إدارة observables والكيانات والإثراء | تنظيم المعلومة لا يثبت صحة كل مصدر خارجي |

## الصور والوسائط وGEOINT

| الأداة | الترخيص | الدور العملي | أهم قيد |
| --- | --- | --- | --- |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Apache-2.0 | OCR محلي للصور والمستندات الممسوحة | يجب مقارنة النص المستخرج بالصورة الأصلية |
| [MediaInfo](https://github.com/MediaArea/MediaInfo) | BSD-2-Clause | قراءة metadata التقنية للصوت والفيديو | metadata قد تكون محذوفة أو معدلة |
| [Sherloq](https://github.com/GuidoBartoli/sherloq) | GPL-3.0 | تحليل جنائي رقمي للصور | الشذوذ إشارة للفحص وليس إثبات تلاعب |
| [Overpass Turbo](https://github.com/tyrasd/overpass-turbo) | MIT | استعلام بيانات OpenStreetMap لـGEOINT | اكتمال وتحديث OSM يختلفان جغرافيًا |
| [kepler.gl](https://github.com/keplergl/kepler.gl) | MIT | عرض وتحليل مجموعات بيانات جغرافية كبيرة | الارتباط البصري لا يثبت السببية |
| [OpenAerialMap](https://github.com/hotosm/openaerialmap) | AGPL-3.0 | اكتشاف صور جوية مفتوحة الترخيص | التغطية والتواريخ والدقة تختلف كثيرًا |

## التحليل ومساحات العمل

| الأداة | الترخيص | الدور العملي | أهم قيد |
| --- | --- | --- | --- |
| [Datasette](https://github.com/simonw/datasette) | Apache-2.0 | استكشاف واستعلام البيانات المحلية المنظمة | تجنب نشر بيانات التحقيق الحساسة بدون قصد |
| [Timesketch](https://github.com/google/timesketch) | Apache-2.0 | تحليل تعاوني للأحداث والخط الزمني | أخطاء parser والساعة والمنطقة الزمنية تنتقل للتحليل |
| [GraphSense](https://github.com/graphsense/graphsense-dashboard) | MIT | تحليل شبكات العملات الرقمية بشكل مفتوح | التجميع والـlabels فرضيات تحتاج تأكيدًا مستقلًا |

## قاعدة الاستخدام الآمن

كون الأداة مفتوحة المصدر لا يلغي التفويض أو الخصوصية أو شروط مزودي البيانات. في البنية التحتية، ابقَ على الجمع السلبي إلا ضمن هدف تملكه أو لديك إذن صريح لاختباره. في بحث الهوية والهاتف والحسابات، قلل جمع البيانات الشخصية. وقبل إرسال ملفات أو URLs أو IOCs إلى محللات خارجية، افحص سياسة الاحتفاظ وإعادة المشاركة.

مخرجات الأداة **إشارة أو ملاحظة** وليست نتيجة نهائية تلقائيًا. احفظ المصدر والوقت والاستعلام ومستوى الثقة والقيود قبل استخدامها في التقرير.

للاختيار حسب نوع المعلومة الموجودة لديك، راجع [حزمة أدوات الباحث في OSINT](investigator-stack.ar.md).
