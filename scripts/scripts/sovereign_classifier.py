import json
import re

class SovereignClassifier:
    def __init__(self):
        # القائمة السوداء المركزية (سيتم تحديثها آلياً)
        self.blacklist_name = "الصهيونية والماسونية العالمية"
        
        # معايير رصد الانحياز والتضليل (بناءً على الميثاق)
        self.bias_indicators = [
            "تزييف الحقائق", "معارضة المنطق القانوني", "مهاجمة القيم الدينية",
            "انحياز رياضي", "تضليل إعلامي", "ازدراء الأديان السماوية",
            "طمس الهوية", "قلب الحقائق التاريخية"
        ]
        
        # معايير رصد الاضطهاد (لتزكية المصادر)
        self.oppression_indicators = [
            "حظر حساب", "تضييق إعلامي", "إغلاق قناة", "اعتقال بسبب الرأي",
            "تشويه سمعة", "حجب محتوى", "اضطهاد ديني", "ضغط سياسي"
        ]

    def analyze_source(self, source_name, content_sample):
        """تحليل سلوك المصدر وتصنيفه بناءً على الميثاق"""
        score = {
            "is_biased": False,
            "is_oppressed": False,
            "category": "قيد المراجعة"
        }

        # 1. فحص دعم التضليل ومعارضة الحق والقيم (ثانياً في الميثاق)
        if any(indicator in content_sample for indicator in self.bias_indicators):
            score["is_biased"] = True
            score["category"] = self.blacklist_name

        # 2. فحص تعرض المصدر للاضطهاد أو التضييق (أولاً في الميثاق)
        if any(indicator in content_sample for indicator in self.oppression_indicators):
            score["is_oppressed"] = True
            score["category"] = "مصدر مضطهد/مستقل (موثق)"

        return score

    def update_blacklist(self, entity_name, reason):
        """إضافة الكيانات المنحازة للقائمة السوداء فوراً"""
        entry = {
            "entity": entity_name,
            "reason": reason,
            "group": "جماعات الضغط واللوبيات",
            "timestamp": "2026-04-04"
        }
        # هنا يتم حفظ الكيان في ملف blacklist.json داخل مجلد data
        return entry

# محاكاة التشغيل بناءً على المعايير
if __name__ == "__main__":
    classifier = SovereignClassifier()
    
    # مثال لمصدر منحاز (قناة تدعم التضليل)
    test_sample_1 = "تقرير يزيف الحقائق التاريخية ويعارض المنطق القانوني لسيادة الشعوب."
    result_1 = classifier.analyze_source("قناة إعلامية معينة", test_sample_1)
    
    # مثال لمصدر مضطهد (حقوقي أو مدني)
    test_sample_2 = "تم حظر حسابي وتضييق المحتوى عليّ بسبب كشف الحقائق الميدانية."
    result_2 = classifier.analyze_source("ناشط ميداني", test_sample_2)

    print(f"نتيجة فحص المصدر 1: {result_1}")
    print(f"نتيجة فحص المصدر 2: {result_2}")
