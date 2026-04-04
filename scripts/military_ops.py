import json
import time
import hashlib
import os
from datetime import datetime

class MilitaryOpsRadar:
    def __init__(self):
        # تصنيفات الأسلحة المحرمة دولياً ومراجعها
        self.prohibited_weapons = {
            "فسفور أبيض": "اتفاقية جنيف - بروتوكول III",
            "قنابل عنقودية": "اتفاقية الذخائر العنقودية (CCM)",
            "يورانيوم منضب": "قوانين حماية البيئة والمدنيين"
        }
        
    def safe_execute(self, func, *args):
        """درع الحماية لمنع توقف البرنامج عند حدوث خطأ في سحب أي بيانات"""
        try:
            return func(*args)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            return None

    def handle_visual_evidence(self, real_media_urls, event_category):
        """آلية الدعم البصري: إرفاق الدليل الحقيقي أو البديل التعبيري بدقة"""
        if real_media_urls and len(real_media_urls) > 0:
            # توثيق جنائي للصور الحقيقية
            media_hash = hashlib.md5(real_media_urls[0].encode()).hexdigest()
            return {
                "media_type": "real_evidence",
                "urls": real_media_urls,
                "verification_hash": media_hash,
                "label": "🔴 توثيق ميداني حقيقي"
            }
        else:
            # إرفاق صورة تعبيرية بناءً على نوع الحدث
            fallback_images = {
                "arsenal_failure": "assets/illustrations/tank_ambush_tactic.jpg",
                "prohibited_weapon": "assets/illustrations/white_phosphorus_effect.jpg",
                "infrastructure_hit": "assets/illustrations/civilian_infrastructure_map.jpg",
                "default": "assets/illustrations/standard_conflict_zone.jpg"
            }
            selected_fallback = fallback_images.get(event_category, fallback_images["default"])
            return {
                "media_type": "representative_illustration",
                "urls": [selected_fallback],
                "verification_hash": "N/A",
                "label": "⚠️ محاكاة بصرية تعبيرية"
            }

    def arsenal_failure_audit(self, event_text):
        """تحليل فشل الترسانة أمام التكتيكات البسيطة"""
        advanced_tech = ["ميركافا", "قبة حديدية", "درون", "رادار متطور", "مدرعة ذكية"]
        simple_tactics = ["عبوة ناسفة", "مسافة صفر", "قذيفة يدوية", "كمين مركب", "قناص"]
        
        has_tech = any(tech in event_text for tech in advanced_tech)
        has_tactic = any(tactic in event_text for tactic in simple_tactics)
        
        if has_tech and has_tactic:
            return "سقوط أسطورة السلاح: تكنولوجيا متطورة تم تحييدها بتكتيكات بسيطة."
        return "اشتباك تكتيكي اعتيادي."

    def prohibited_weapons_radar(self, event_text):
        """رصد الأسلحة المحرمة وربطها بالقانون"""
        detected_crimes = []
        for weapon, law in self.prohibited_weapons.items():
            if weapon in event_text:
                detected_crimes.append({"weapon": weapon, "violated_law": law})
        return detected_crimes

    def synergy_alerts(self, event_text, has_civilian_casualties):
        """إشارات التكامل للأقسام الأخرى"""
        alerts = {
            "notify_palestine_center": False,
            "notify_banned_news": False
        }
        if any(place in event_text for place in ["مستشفى", "مدرسة", "مخيم"]):
            alerts["notify_palestine_center"] = True
        if has_civilian_casualties:
            alerts["notify_banned_news"] = True
        return alerts

    def process_military_data(self, raw_combat_data):
        """المحرك الرئيسي لمعالجة البيانات"""
        final_military_feed = []
        for item in raw_combat_data:
            event_category = "default"
            if "فشل" in item['text'] or "تدمير آلية" in item['text']: event_category = "arsenal_failure"
            elif any(w in item['text'] for w in self.prohibited_weapons.keys()): event_category = "prohibited_weapon"
            
            visual_evidence = self.safe_execute(self.handle_visual_evidence, item.get('media_urls', []), event_category)
            failure_audit = self.safe_execute(self.arsenal_failure_audit, item['text'])
            prohibited_scan = self.safe_execute(self.prohibited_weapons_radar, item['text'])
            cross_alerts = self.safe_execute(self.synergy_alerts, item['text'], item.get('civilian_casualties', False))
            
            military_record = {
                "id": f"mil_op_{int(time.time())}_{hashlib.md5(item['text'][:20].encode()).hexdigest()[:5]}",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "operation_title": item.get('title', 'تقرير ميداني عاجل'),
                "combat_details": item['text'],
                "visual_documentation": visual_evidence,
                "arsenal_analysis": failure_audit,
                "war_crimes_radar": prohibited_scan,
                "system_alerts": cross_alerts
            }
            final_military_feed.append(military_record)
        return final_military_feed

# ==========================================
# تشغيل الرادار وحفظ النتائج (تم تصحيح المسار والصياغة)
# ==========================================
if __name__ == "__main__":
    radar = MilitaryOpsRadar()
    
    mock_combat_data = [
        {
            "title": "كمين مركب يدمر مدرعة ميركافا",
            "text": "تم تدمير مدرعة ميركافا من مسافة صفر باستخدام عبوة ناسفة محلية الصنع في حي الشجاعية.",
            "media_urls": [],
            "civilian_casualties": False
        },
        {
            "title": "قصف عنيف بقنابل الفسفور",
            "text": "استهداف محيط مستشفى الشفاء بقنابل الفسفور الأبيض مما أدى لحرائق وانقطاع تام.",
            "media_urls": ["https://real-field-image.com/img1.jpg"],
            "civilian_casualties": True
        }
    ]
    
    results = radar.process_military_data(mock_combat_data)
    
    # التأكد من وجود مجلد data لتجنب خطأ FileNotFoundError
    if not os.path.exists('data'):
        os.makedirs('data')

    # المسار المباشر 'data/...' هو الصحيح للتشغيل عبر GitHub Actions
    with open('data/military_feed.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print(f"✅ تم بنجاح! تم تحليل وتوثيق {len(results)} عمليات عسكرية في مجلد data.")
