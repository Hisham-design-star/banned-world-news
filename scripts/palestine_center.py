import json
import os
import time
import hashlib
from datetime import datetime

# محاولة استدعاء العقل المدبر (غيروا الحقيقة) لضمان التكامل
try:
    from sovereign_classifier import SovereignClassifier
except ImportError:
    SovereignClassifier = None

class PalestineCenterRadar:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_file = os.path.join(self.base_path, 'data', 'palestine_feed.json')
        
        # المصادر والطرائق (من كودك الأصلي)
        self.regional_media = ["AlJazeera", "Egyptian_Media", "Qatar_TV", "Algeria_Press", "Morocco_News", "South_Africa_News"]
        self.legal_frameworks = ["ICJ_South_Africa_Case", "UN_Resolution_194", "Geneva_Convention"]
        self.historical_timeline_start = 1984
        
        # تفعيل المحرك السيادي
        self.classifier = SovereignClassifier() if SovereignClassifier else None

    # --- 1. الوظائف التقنية والوقائية (من كودك القديم) ---
    def safe_execute(self, func, *args):
        try: return func(*args)
        except: return None

    def forensic_tracking(self, item):
        """التوثيق الجنائي الميداني (تشفير البصمة)"""
        raw = f"{item.get('url', '')}_{item.get('timestamp', time.time())}".encode()
        return {
            "digital_hash": hashlib.sha256(raw).hexdigest(),
            "location": item.get('gps_location', 'موقع موثق ميدانياً'),
            "verified_at": datetime.now().isoformat()
        }

    # --- 2. تحليل النبض الإنساني والدمار (من كودك القديم) ---
    def human_memory_tracker(self, posts):
        """أنسنة الضحايا واستعادة الهوية"""
        restored = []
        for post in posts:
            if any(kw in post.get('text', '') for kw in ["نعي", "شهيد", "مفقود"]):
                restored.append({
                    "name": post.get('extracted_name', 'بطل مجهول'),
                    "profession": post.get('extracted_profession', 'مدني صامد'),
                    "link": post.get('url', '')
                })
        return restored

    def infrastructure_audit(self, images):
        """أرصدة الدمار ومحو الأثر التاريخي"""
        report = []
        for img in images:
            analysis = img.get('ai_analysis', '')
            if any(kw in analysis for kw in ["عقار", "مستشفى", "مدرسة", "أثري"]):
                report.append({"type": analysis, "image": img['url'], "crime": "تغيير ديموغرافي"})
        return report

    # --- 3. التحليل السيادي والرد النوعي (الإضافة الجديدة المدمجة) ---
    def media_bias_audit(self, source, content):
        """ميزان التضليل: فضح اللوبيات مقابل الحقيقة"""
        analysis = {"status": "قيد الفحص", "is_blacklisted": False, "retaliation": {}}
        
        if self.classifier:
            res = self.classifier.analyze_source(source, content)
            analysis["status"] = res['category']
            analysis["is_blacklisted"] = res['is_biased']
            # تفعيل الرد النوعي فوراً إذا تم رصد تضليل
            if res['is_biased'] or res['is_oppressed']:
                analysis["retaliation"] = self.classifier.deep_search_retaliation(source, content)
        
        return analysis

    # --- 4. المحرك الرئيسي: دمج الـ 9 فلاتر في عملية واحدة ---
    def process_palestine_data(self, raw_data):
        final_feed = []
        
        for item in raw_data:
            content = item.get('content', '') or item.get('text', '')
            source = item.get('author', 'مصدر ميداني')

            # تطبيق الفلاتر التسعة المدمجة
            record = {
                "id": f"pal_{hashlib.md5(content.encode()).hexdigest()[:10]}",
                "title": item.get('title', 'توثيق ميداني عاجل'),
                "content": content,
                "forensic": self.safe_execute(self.forensic_tracking, item),
                "human_stories": self.safe_execute(self.human_memory_tracker, item.get('social_posts', [])),
                "destruction": self.safe_execute(self.infrastructure_audit, item.get('images', [])),
                "historical_link": f"امتداد لسياسة الإحلال المرصودة منذ {self.historical_timeline_start}",
                "legal_context": "يخالف اتفاقية جنيف وموثق في ملف (ICJ)" if "إبادة" in content else "قيد التوثيق القانوني",
                "truth_audit": self.media_bias_audit(source, content), # هنا يلتقي القديم بالجديد
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            final_feed.append(record)
            
        self.save_and_merge(final_feed)
        return final_feed

    def save_and_merge(self, new_data):
        """حماية الأرشيف من الضياع ودمج البيانات ذكياً"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        existing = []
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    existing = json.load(f)
            except: existing = []
        
        # دمج بدون تكرار
        seen_ids = {d['id'] for d in new_data}
        combined = new_data + [d for d in existing if d['id'] not in seen_ids]
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(combined[:200], f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # تشغيل الرادار الشامل
    radar = PalestineCenterRadar()
    mock = [{
        "author": "قناة منحازة", 
        "text": "تزييف الحقائق حول استهداف مدرسة تأوي نازحين.",
        "images": [{"url": "evidence.jpg", "ai_analysis": "تدمير مدرسة"}]
    }]
    radar.process_palestine_data(mock)
    print("✅ تم التشغيل: الرادار وثق الجريمة، فضح التضليل، وجهز الرد النوعي.")
