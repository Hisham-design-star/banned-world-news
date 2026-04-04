import json
import os
from datetime import datetime

class SovereignClassifier:
    def __init__(self):
        # مسمى القائمة السوداء حسب الميثاق
        self.blacklist_name = "غيروا الحقيقة"
        
        # تحديد المسارات بشكل ديناميكي لضمان العمل على GitHub Actions
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.blacklist_path = os.path.join(self.base_path, 'data', 'blacklist.json')
        
        # التأكد من وجود مجلد data وملف القائمة السوداء
        os.makedirs(os.path.dirname(self.blacklist_path), exist_ok=True)
        if not os.path.exists(self.blacklist_path):
            with open(self.blacklist_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

        # معايير رصد الانحياز والتضليل (بناءً على الميثاق)
        self.bias_indicators = [
            "تزييف الحقائق", "معارضة المنطق القانوني", "مهاجمة القيم الدينية",
            "انحياز رياضي", "تضليل إعلامي", "ازدراء الأديان السماوية",
            "طمس الهوية", "قلب الحقائق التاريخية", "الحق"
        ]
        
        # معايير رصد الاضطهاد (لتزكية المصادر)
        self.oppression_indicators = [
            "حظر حساب", "تضييق إعلامي", "إغلاق قناة", "اعتقال بسبب الرأي",
            "تشويه سمعة", "حجب محتوى", "اضطهاد ديني", "ضغط سياسي"
        ]

    def _load_blacklist(self):
        """تحميل القائمة السوداء الحالية من الملف"""
        try:
            with open(self.blacklist_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    def analyze_source(self, source_name, content_sample):
        """تحليل سلوك المصدر وتصنيفه بربط كامل مع قاعدة البيانات"""
        blacklist = self._load_blacklist()
        
        # التحقق أولاً إذا كان المصدر مدرجاً مسبقاً في القائمة السوداء
        is_already_blacklisted = any(item['entity'] == source_name for item in blacklist)
        
        score = {
            "is_biased": is_already_blacklisted,
            "is_oppressed": False,
            "category": self.blacklist_name if is_already_blacklisted else "تحت الفحص الميداني"
        }

        # 1. رصد التضليل الجديد (ثانياً في الميثاق)
        if not is_already_blacklisted:
            if any(indicator in content_sample for indicator in self.bias_indicators):
                score["is_biased"] = True
                score["category"] = self.blacklist_name
                self.update_blacklist(source_name, "رصد آلي: انتهاك معايير الحق والمنطق والقيم")

        # 2. رصد الاضطهاد (أولاً في الميثاق)
        if any(indicator in content_sample for indicator in self.oppression_indicators):
            score["is_oppressed"] = True
            score["category"] = "✅ صوت يتعرض للإضطهاد والضغط والتضييق والهجوم"

        return score

    def update_blacklist(self, entity_name, reason):
        """تحديث القائمة السوداء فعلياً في الملف مع منع التكرار"""
        blacklist = self._load_blacklist()
        if not any(item['entity'] == entity_name for item in blacklist):
            entry = {
                "entity": entity_name,
                "reason": reason,
                "group": "جماعات الضغط واللوبيات",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            blacklist.append(entry)
            with open(self.blacklist_path, 'w', encoding='utf-8') as f:
                json.dump(blacklist, f, ensure_ascii=False, indent=4)
            return True
        return False

    def deep_search_retaliation(self, victim_name, context_of_attack):
        """محرك الرد النوعي وكشف الدوافع (الأتمتة التحليلية)"""
        return {
            "retaliation": {
                "search_target": f"الحالة الحقيقية لـ {victim_name}",
                "priority_sources": ["المصادر الميدانية القريبة", "شهود العيان", "الحسابات المستقلة"],
                "action": "استدعاء الرواية المقابلة من النطاق الجغرافي للضحية"
            },
            "motives": {
                "motive_check": f"تحليل دوافع هجوم اللوبي على {victim_name}",
                "linked_lobbies": ["اللوبي المالي", "الكيانات السياسية المنحازة"],
                "hidden_agenda": "ربط التضليل بالمصالح المستترة"
            }
        }
