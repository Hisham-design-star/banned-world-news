import json
import time
from datetime import datetime

class BannedNewsRadar:
    def __init__(self):
        # 1. تعريف المعسكرات والمصادر
        self.western_agencies = ["Reuters", "AP", "AFP", "CNN", "BBC", "NYT", "Meta", "Google"]
        self.eastern_agencies = ["TASS", "Xinhua", "Official_Eastern_Media"]
        self.free_sources = ["Telegram", "X", "TikTok", "Instagram"]
        
    def safe_execute(self, func, *args):
        """دالة حماية: تمنع تعطل البرنامج بالكامل إذا فشل رصد خبر معين"""
        try:
            return func(*args)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            return None

    def apply_banned_filter(self, news_item):
        """3. معايير الفلترة الأربعة (قبول الخبر)"""
        keywords = news_item.get('content', '') + news_item.get('title', '')
        
        condition_1 = any(word in keywords for word in ["إبادة", "مجاعة", "سيادة", "أزمة إنسانية"])
        condition_2 = any(word in keywords for word in ["إخفاق", "تجسس", "تسريب", "حادث عسكري"])
        condition_3 = any(word in keywords for word in ["حقوق إنسان", "تشويه", "تاريخي"])
        condition_4 = news_item.get('global_interest_score', 0) > 75 # يهم الرأي العام العالمي

        return condition_1 or condition_2 or condition_3 or condition_4

    def visual_ethical_filter(self, media_content):
        """6. حماية وتوثيق المحتوى البصري"""
        # إذا كان المحتوى فاضحاً أو إباحياً -> حظر تام
        if media_content.get('is_explicit_porn'):
            return False
        # إذا كان دماء، جروح، ضحايا (والمعتدي مستمر) -> مسموح للتوثيق
        if media_content.get('is_human_casualty'):
            return True
        return True

    def validate_eyewitnesses(self, location, timeframe):
        """4. تحليل شهود العيان لتأكيد الخبر أو نفيه"""
        # هنا يتم سحب منشورات إنستجرام وفيسبوك من نفس الموقع الجغرافي
        eyewitness_data = self.scrape_local_social_media(location, timeframe)
        validation_score = 0
        
        for post in eyewitness_data:
            if "دمار" in post['background_image_analysis'] or "انفجار" in post['comments']:
                validation_score += 1
                
        return validation_score > 5 # تأكيد الخبر إذا وجدنا تفاعلاً ميدانياً كافياً

    def cross_check_agencies(self, field_news):
        """4. المطابقة: مقارنة الميدان بالوكالات العالمية"""
        broadcasted_news = self.search_agencies(field_news['keywords'])
        
        # إذا لم يتم ذكر الخبر أصلاً
        if not broadcasted_news:
            return "ignored", self.western_agencies + self.eastern_agencies
            
        # إذا تم ذكره ولكن بصور مزيفة أو نص يخفي الحقيقة
        visual_gap = field_news['has_casualties'] and not broadcasted_news['shows_casualties']
        text_gap = "مجزرة" in field_news['content'] and "حادث بسيط" in broadcasted_news['content']
        
        if visual_gap or text_gap:
            return "manipulated", broadcasted_news['source']
            
        return "verified_by_all", []

    def format_output(self, field_news, censorship_type, cowards_list):
        """5. مواصفات الإخراج والتشهير"""
        cowards_str = "، ".join(cowards_list)
        
        return {
            "id": f"banned_{int(time.time())}",
            "title": field_news['title'],
            "pre_warning": f"⚠️ تنبيه: هذه الجهات وحكوماتها ومنصاتها تمنعنا من المعرفة وحظرت النشر. الإعلام يُباع ليغطي العيون ويكمم الأفواه، ولكننا نرى ونسمع وسنعرف الحقيقة وسنرفض الظلم.",
            "real_content": field_news['content'],
            "media_url": field_news['media_url'],
            "broadcasted_fake_version": field_news.get('broadcasted_version', 'تم التعتيم بالكامل'),
            "post_warning": f"🚫 هذا ما تغافل عنه هؤلاء: ({cowards_str}). هؤلاء من ادعوا العمى.. هؤلاء هم الجبناء.",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def process_banned_radar(self, raw_field_data):
        """المحرك الرئيسي للقسم (يعمل بسلاسة دون التداخل مع الأقسام الأخرى)"""
        final_banned_feed = []
        
        for item in raw_field_data:
            # 1. هل يستوفي شروط الأهمية العالمية؟
            if not self.safe_execute(self.apply_banned_filter, item):
                continue
                
            # 2. هل المحتوى البصري مقبول أخلاقياً؟
            if not self.safe_execute(self.visual_ethical_filter, item.get('media', {})):
                continue
                
            # 3. هل أكده شهود العيان على فيسبوك وانستجرام؟
            if not self.safe_execute(self.validate_eyewitnesses, item['location'], item['time']):
                continue
                
            # 4. هل تجاهلته أو زيفته الوكالات؟
            status, culprits = self.safe_execute(self.cross_check_agencies, item)
            if status in ["ignored", "manipulated"]:
                formatted_news = self.format_output(item, status, culprits)
                final_banned_feed.append(formatted_news)
                
        return final_banned_feed

    # --- دوال مساعدة (لجلب البيانات) ---
    def scrape_local_social_media(self, location, timeframe):
        # كود وهمي يمثل ربط الـ API بفيسبوك وانستجرام
        return [{'background_image_analysis': 'دمار', 'comments': 'انفجار قوي'}]
        
    def search_agencies(self, keywords):
        # كود وهمي يمثل البحث في رويترز و CNN
        return None

# ==========================================
# تشغيل الرادار وحفظ النتائج في ملف JSON
# ==========================================
if __name__ == "__main__":
    radar = BannedNewsRadar()
    
    # محاكاة لبيانات قادمة من تليجرام واكس (للتجربة)
    mock_field_data = [{
        "title": "مجزرة وتدمير بنية تحتية في قرية معزولة",
        "content": "شهود عيان يؤكدون وقوع ضحايا وتدمير الجسر الرئيسي، وتفاعل كبير من الأهالي على انستجرام.",
        "location": "الشرق الأوسط",
        "time": "2023-10-25",
        "has_casualties": True,
        "global_interest_score": 80,
        "media_url": "link_to_real_video.mp4",
        "media": {"is_explicit_porn": False, "is_human_casualty": True}
    }]
    
    # المعالجة
    results = radar.process_banned_radar(mock_field_data)
    
    # حفظ النتائج في ملف JSON ليقرأه موقعك (index.html)
    with open('../data/banned_news_feed.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print(f"تم بنجاح! تم رصد وتوثيق {len(results)} أخبار محظورة.")
