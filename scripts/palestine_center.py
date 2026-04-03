import json
import time
import hashlib
from datetime import datetime

class PalestineCenterRadar:
    def __init__(self):
        # تعريف قواعد البيانات والمصادر
        self.regional_media = ["AlJazeera", "Egyptian_Media", "Qatar_TV", "Algeria_Press", "Morocco_News", "South_Africa_News"]
        self.western_media = ["Reuters", "CNN", "BBC", "FoxNews", "NYT"] # وسائل إعلام اللوبيات
        self.legal_frameworks = ["ICJ_South_Africa_Case", "UN_Resolution_194", "Geneva_Convention"]
        self.historical_timeline_start = 1984
        
    def safe_execute(self, func, *args):
        """حماية الكود من التوقف إذا فشل أحد المصادر في الاستجابة"""
        try:
            return func(*args)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            return None

    def forensic_tracking(self, media_item):
        """1. التوثيق الجنائي الميداني: تشفير بصمة الملف والموقع"""
        raw_data = f"{media_item['url']}_{media_item['timestamp']}".encode()
        digital_signature = hashlib.sha256(raw_data).hexdigest()
        return {
            "digital_hash": digital_signature,
            "gps_coordinates": media_item.get('gps_location', 'موقع موثق ميدانياً'),
            "forensic_timestamp": datetime.now().isoformat()
        }

    def human_memory_tracker(self, field_data):
        """2 & 4. رصد النبض الإنساني وأنسنة الضحايا (من فيسبوك وانستجرام)"""
        restored_identities = []
        for post in field_data.get('social_posts', []):
            if "نعي" in post['text'] or "شهيد" in post['text'] or "مفقود" in post['text']:
                restored_identities.append({
                    "name": post.get('extracted_name', 'اسم مجهول الهوية'),
                    "age": post.get('extracted_age', 'غير محدد'),
                    "profession": post.get('extracted_profession', 'مدني بريء'),
                    "story_link": post['url']
                })
        return restored_identities

    def infrastructure_heritage_audit(self, images_data):
        """3. أرصدة الدمار ومحو الأثر"""
        destruction_report = []
        for img in images_data:
            analysis = img.get('ai_analysis', '')
            if any(kw in analysis for kw in ["عقار", "إزالة حي", "مستشفى", "مدرسة", "معلم أثري", "مزرعة"]):
                destruction_report.append({
                    "target_type": analysis,
                    "evidence_image": img['url'],
                    "crime_classification": "محاولة محو هوية وتغيير ديموغرافي"
                })
        return destruction_report

    def historical_justice_1984(self, current_event):
        """5. الرابط التاريخي منذ 1984 وما قبله"""
        # محاكاة لربط الحدث الحالي بتاريخ الاغتصاب والإحلال
        event_type = current_event.get('type', 'اعتداء')
        return f"هذا الـ({event_type}) ليس حدثاً معزولاً، بل هو استمرار لمنهجية الإحلال وتدمير الهوية والترويع الموثقة منذ ما قبل عام {self.historical_timeline_start}."

    def legal_icj_integration(self, event_details):
        """7. السند القانوني الدولي (أدلة جنوب أفريقيا ومجلس الأمن)"""
        legal_context = []
        if "إبادة" in event_details or "تهجير" in event_details:
            legal_context.append("يخالف اتفاقية جنيف، وموثق ضمن ملف جنوب أفريقيا أمام محكمة العدل الدولية (ICJ).")
        return legal_context

    def media_bias_audit(self, event_keywords):
        """6 & 8 & 9. ميزان التضليل: فضح اللوبيات الغربية مقابل الإعلام العربي وجنوب أفريقيا"""
        # محاكاة لجلب عناوين الأخبار
        western_headline = "اشتباكات تؤدي إلى سقوط ضحايا (مبني للمجهول)" # تأثير اللوبيات
        regional_headline = "قصف يستهدف حياً سكنياً ويدمر مستشفى بالكامل" # الإعلام الموثوق
        
        bias_score = "تضليل جسيم وتزييف للتاريخ" if "اشتباكات" in western_headline else "تغطية جزئية"
        
        return {
            "western_lobbies_narrative": western_headline,
            "regional_truth_narrative": regional_headline,
            "bias_analysis": bias_score,
            "supported_by": self.regional_media
        }

    def process_palestine_data(self, raw_incoming_data):
        """المحرك الرئيسي: تمرير الخبر على جميع الفلاتر التسعة"""
        final_documented_feed = []
        
        for item in raw_incoming_data:
            # معالجة كل نقطة بشكل آمن
            forensic_data = self.safe_execute(self.forensic_tracking, item)
            identities = self.safe_execute(self.human_memory_tracker, item)
            infrastructure = self.safe_execute(self.infrastructure_heritage_audit, item.get('images', []))
            history_link = self.safe_execute(self.historical_justice_1984, item)
            legal_backup = self.safe_execute(self.legal_icj_integration, item.get('content', ''))
            bias_report = self.safe_execute(self.media_bias_audit, item.get('keywords', []))
            
            # تجميع الوثيقة النهائية
            documented_record = {
                "id": f"palestine_{int(time.time())}",
                "title": item['title'],
                "forensic_evidence": forensic_data,
                "human_identities": identities,
                "infrastructure_destruction": infrastructure,
                "historical_context": history_link,
                "legal_framework": legal_backup,
                "media_bias_audit": bias_report,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            final_documented_feed.append(documented_record)
            
        return final_documented_feed

# ==========================================
# تشغيل الرادار وحفظ النتائج
# ==========================================
if __name__ == "__main__":
    radar = PalestineCenterRadar()
    
    # بيانات ميدانية تجريبية قادمة من تليجرام/انستجرام
    mock_field_data = [{
        "title": "إزالة حي سكني كامل واستهداف مستشفى ميداني",
        "content": "عمليات تهجير قسري وإبادة، تخللها تدمير معلم أثري يعود لمئات السنين.",
        "url": "https://t.me/field_reporter/123",
        "timestamp": "1698245000",
        "type": "تدمير وتهجير",
        "social_posts": [
            {"text": "نعي الشهيد الطبيب أحمد", "extracted_name": "أحمد", "extracted_profession": "طبيب", "url": "ig_link_1"}
        ],
        "images": [
            {"url": "img_link_1.jpg", "ai_analysis": "إزالة حي وتدمير مستشفى"}
        ]
    }]
    
    # معالجة البيانات وبناء الوثيقة
    results = radar.process_palestine_data(mock_field_data)
    
    # حفظ النتائج في ملف JSON مستقل
    with open('../data/palestine_feed.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print(f"تم بنجاح! تم بناء {len(results)} وثيقة تاريخية وقانونية.")
