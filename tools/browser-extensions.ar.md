# إضافات المتصفح وأدوات الويب لـ OSINT

![إضافات المتصفح وأدوات الويب لـ OSINT](../assets/osint-browser-tools.svg)

هذه الصفحة ليست قائمة تثبيت عشوائية. الهدف هو معرفة **أي أداة تستخدم، ولماذا، وما الذي لا تستطيع نتيجتها إثباته**.

> **قاعدة مهمة:** نتيجة الإضافة أو الموقع هي مؤشر أو نقطة بداية. أي نتيجة مهمة يجب الرجوع فيها إلى المصدر الأصلي والتحقق منها مستقلاً.

## مجموعة بداية مقترحة

لا تثبت عشرات الإضافات من البداية. ابدأ بعدد صغير:

| الحاجة | أداة مناسبة للبداية | الاستخدام |
| --- | --- | --- |
| حفظ صفحة | [SingleFile](https://github.com/gildas-lormeau/SingleFile) | حفظ الصفحة محلياً كملف HTML واحد |
| نسخة قديمة من موقع | [Wayback Machine](https://web.archive.org/) | مراجعة تاريخ الصفحات العامة |
| مراقبة التغييرات | [Distill](https://distill.io/) | تنبيه عند تغير محتوى صفحة |
| البحث العكسي | [TinEye](https://tineye.com/) + [Google Lens](https://lens.google/) | العثور على نسخ مشابهة أو أقدم من الصورة |
| التحقق من الفيديو | [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | استخراج إطارات وأدوات تحقق مرئي |
| IOC / Threat Intel | [VirusTotal](https://www.virustotal.com/) + [urlscan.io](https://urlscan.io/) | إثراء نطاقات وروابط ومؤشرات عامة |
| بنية تحتية سلبية | [Shodan](https://www.shodan.io/) + [Censys](https://search.censys.io/) | البحث في بيانات تم رصدها مسبقاً |
| لقطة صفحة كاملة | [GoFullPage](https://gofullpage.com/) أو [FireShot](https://getfireshot.com/) | توثيق الصفحة مع سياقها |
| Blockchain | [Etherscan](https://etherscan.io/) / [Blockchair](https://blockchair.com/) | مراجعة بيانات السلاسل العامة |

## 1. حفظ وأرشفة الويب

### [Hunchly](https://www.hunch.ly/)
مفيد لتوثيق جلسة البحث والصفحات العامة التي تمت زيارتها.

**لا يثبت:** أن المعلومات الموجودة في الصفحة صحيحة؛ هو يساعدك على حفظ ما رأيته ومتى.

### [Vortimo](https://www.vortimo.com/)
أداة مساعدة لتنظيم وجمع المعلومات أثناء البحث عبر الويب.

### [Wayback Machine](https://web.archive.org/)
لمراجعة نسخ قديمة من المواقع والصفحات.

**تنبيه:** عدم وجود نسخة في الأرشيف لا يعني أن الصفحة لم تكن موجودة.

### [SingleFile](https://github.com/gildas-lormeau/SingleFile)
يحفظ الصفحة كملف HTML واحد للاحتفاظ بنسخة محلية.

### [Distill Web Monitor](https://distill.io/)
لمتابعة صفحات تتغير بمرور الوقت، مثل الإعلانات أو القوائم أو البيانات الرسمية.

## 2. تحليل الصور والفيديو

### [Google Lens](https://lens.google/)
بحث بصري واستخراج قرائن من الصورة.

### [TinEye](https://tineye.com/)
بحث عكسي للعثور على نسخ مطابقة أو معدلة من الصورة.

### [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/)
أدوات لاستخراج keyframes ومساعدة التحقق من الفيديو والصور.

### [FotoForensics](https://fotoforensics.com/)
أداة تعليمية لفحص خصائص الصور.

**مهم:** أنماط الضغط أو ELA وحدها ليست دليلاً قاطعاً على التلاعب.

### [ExifTool](https://exiftool.org/)
لفحص Metadata في الملفات المحلية.

**مهم:** غياب Metadata طبيعي بعد الرفع إلى كثير من المنصات، ولا يثبت أن الصورة مزيفة.

## 3. Threat Intelligence و IOC Lookup

### [Pulsedive](https://pulsedive.com/)
إثراء مؤشرات التهديد من مصادر عامة.

### [Mitaka](https://github.com/ninoseki/mitaka)
إضافة متصفح تساعد على فتح مؤشر محدد في عدة خدمات بحث وتحليل.

### [VirusTotal](https://www.virustotal.com/)
لفحص وإثراء الملفات والروابط والنطاقات وعناوين IP.

**خصوصية:** لا ترفع ملفات سرية أو روابط داخلية حساسة إلى خدمات تحليل عامة.

### [urlscan.io](https://urlscan.io/)
يعرض معلومات عن صفحات ومواقع تم فحصها أو يمكن إرسالها للفحص.

**خصوصية:** راجع مستوى ظهور الفحص قبل إرسال رابط حساس.

### [Shodan](https://www.shodan.io/)
بحث في أنظمة مكشوفة للإنترنت تم رصدها مسبقاً.

### [Censys](https://search.censys.io/)
بحث في hosts والشهادات والبيانات العامة التي تجمعها Censys.

> هذا الدليل يركز على البحث السلبي والمصادر العامة. الفحص النشط يحتاج تفويضاً واضحاً.

## 4. استخراج البيانات

### [Instant Data Scraper](https://webrobots.io/instantdata/)
لاستخراج بيانات متكررة من صفحات عامة.

### [Web Scraper](https://webscraper.io/)
لبناء عمليات استخراج منظمة من صفحات ذات بنية متكررة.

### [Link Gopher](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/)
لاستخراج الروابط الموجودة في الصفحة ومراجعتها أو تصديرها.

**حدود الاستخدام:** scraping قد يخضع لشروط الموقع، والخصوصية، وحقوق النشر، وحدود المعدل. اجمع فقط ما تحتاجه للسؤال البحثي.

## 5. Screenshots وتوثيق الوسائط

### [GoFullPage](https://gofullpage.com/)
لقطة كاملة لصفحة الويب.

### [FireShot](https://getfireshot.com/)
التقاط الصفحة وتصديرها بصيغ مختلفة.

### [Screenity](https://github.com/alyssaxuu/screenity)
مسجل شاشة مفتوح المصدر.

عند توثيق دليل، لا تحفظ الصورة وحدها. سجل معها:

- URL
- وقت الوصول
- المنطقة الزمنية
- ماذا تريد اللقطة أن تثبت
- إن كانت الصفحة ديناميكية أو قابلة للتغيير

## 6. أدوات التنزيل

### [DownThemAll!](https://www.downthemall.org/)
مدير لتنزيل ملفات عامة يمكن للمتصفح الوصول لها.

### [Video DownloadHelper](https://www.downloadhelper.net/)
يساعد في تنزيل وسائط مدعومة من المتصفح.

**تنبيه:** كون المحتوى عاماً لا يلغي حقوق النشر أو شروط المنصة. استخدم التنزيل لأغراض بحث وتوثيق مشروعة.

## 7. Blockchain و Crypto Investigation

### [Etherscan](https://etherscan.io/)
مستكشف Ethereum.

### [Tronscan](https://tronscan.org/)
مستكشف شبكة TRON.

### [Blockchair](https://blockchair.com/)
مستكشف يدعم عدة شبكات.

### [Breadcrumbs](https://www.breadcrumbs.app/)
تحليل وعرض العلاقات بين معاملات وعناوين blockchain.

### [Arkham](https://intel.arkm.com/)
منصة معلومات وتصنيفات لعناوين وكيانات blockchain.

**قاعدة Attribution:** وجود label على عنوان لا يثبت وحده أن شخصاً معيناً يتحكم به. وثق مصدر الـlabel ودرجة الثقة.

## قائمة تحقق قبل تثبيت أي إضافة

- [ ] هل الناشر أو المشروع معروف ويمكن التحقق منه؟
- [ ] هل ما زالت الإضافة محدثة؟
- [ ] هل الصلاحيات المطلوبة منطقية بالنسبة لوظيفتها؟
- [ ] هل يمكن استخدام نسخة Web بدلاً من منح صلاحيات واسعة للمتصفح؟
- [ ] هل ترسل URLs أو محتوى الصفحات إلى طرف ثالث؟
- [ ] هل سياسة الخصوصية واضحة؟
- [ ] هل يمكن تشغيلها في Browser Profile منفصل للبحث؟

## إعداد متصفح بحث أفضل

```text
ملف المتصفح الشخصي
    └─ حساباتك وتصفحك اليومي

ملف متصفح البحث
    ├─ أقل عدد ممكن من الإضافات
    ├─ بدون تسجيلات دخول شخصية غير ضرورية
    ├─ مجلد تنزيل منفصل
    ├─ أدوات توثيق
    └─ نظام ملاحظات وأدلة واضح
```

## مواد مرتبطة

- [مصفوفة الأدوات](../docs/ar/tool-matrix.md)
- [منهجيات البحث](../docs/ar/research-methods.md)
- [قائمة التحقق من المصادر](../docs/ar/source-verification-checklist.md)
- [المختبرات العملية](../docs/ar/practice-labs.md)
- [قالب التقرير](../docs/ar/report-template.md)

---

القائمة منتقاة وليست شاملة. الإضافات قد تتغير ملكيتها أو صلاحياتها أو تتوقف عن التحديث، لذلك افحص الأداة مجدداً قبل تثبيتها.