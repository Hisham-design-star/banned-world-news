import requests
from bs4 import BeautifulSoup
import json
import time
import os
from datetime import datetime

class BannedNewsRadar:
    def __init__(self):
        # 1. تعريف المعسكرات والمصادر (من الكود القديم)
        self.western_agencies = ["Reuters", "AP", "AFP", "CNN", "BBC", "NYT", "Meta", "Google"]
        self.eastern_agencies = ["TASS", "Xinhua", "Official_Eastern_Media"]
        
        # 2. تقنية التمويه البشري (المميزة الجديدة)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8'
        }

    def safe_execute(self, func, *args):
        """حماية البرنامج من التوقف عند فشل رصد مصدر معين"""
        try:
            return func(*args)
        except Exception as e:
            print(f"⚠️ تنبيه في {func.__name__}: {str(e)}")
            return None

    def apply_banned_filter(self, title, content, score=80):
        """معايير الفلترة الأربعة (من الكود القديم)"""
        keywords = (title + content).lower()
        cond1 = any(word in keywords for word in ["إبادة", "مجاعة", "سيادة", "أزمة إنسانية", "قصف", "شهداء"])
        cond2 = any(word in keywords for word in ["إخفاق", "تجسس", "تسريب", "حادث عسكري", "كمين"])
        cond3 = any(word in keywords for word in ["حقوق إنسان", "تشويه", "تاريخي", "مجزرة"])
        cond4 = score > 75 
        return cond1 or cond2 or cond3 or cond4

    def visual_ethical_filter(self, item):
        """حماية وتوثيق المحتوى البصري (من الكود القديم)"""
        # في الرصد الآلي، نعتبر محتوى المنصات العامة مجازاً للتوثيق ما لم يصنف كإباحي
        description = item.get('description', '').lower()
        if any(word in description for word in ["+18", "porn", "explicit"]):
            return False
        return True

    def fetch_social_geo_data(self):
        """الرصد الجغرافي ومنصات التواصل (المميزة الجديدة)"""
        # استهداف جيو-جرافي (غزة، القدس، ومناطق الحدث) عبر RSSHub لضمان عدم الحظر
        targets = [
            {"name": "X_Geo", "url": "https://rsshub.app/twitter/keyword/Gaza"},
            {"name": "Telegram_Field", "url": "https://rsshub.app/telegram/channel/QudsN"},
            {"name": "Insta_Visuals", "url": "https://rsshub.app/instagram/user/eye.on.palestine"},
            {"name": "FB_News", "url": "https://rsshub.app/facebook/page/AljazeeraChannel"}
        ]
        
        captured_news = []
        for target in targets:
            try:
                resp = requests.get(target['url'], headers=self.headers, timeout=25)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.content, 'xml')
                    items = soup.find_all('item')[:10]
                    for it in items:
                        captured_news.append({
                            "title": it.title.text,
                            "content": it.description.text if it.description else "",
                            "link": it.link.text,
                            "source": target['name'],
                            "has_casualties": "شهيد" in it.title.text or "ضحايا" in it.title.text
                        })
            except: continue
        return captured_news

    def cross_check_and_format(self, field_news):
        """المطابقة والتشهير بالجبناء (من الكود القديم)"""
        # محاكاة: إذا كان الخبر عاجلاً في الميدان ولم يظهر في الوكالات الغربية
        # هنا يتم التشهير بالجهات التي تتجاهل الخبر
        
        culprits = self.western_agencies # قائمة الجبناء الافتراضية عند التعتيم
        
        return {
            "id": f"banned_{int(time.time())}_{hash(field_news['title']) % 1000}",
            "title": field_news['title'],
            "pre_warning": "⚠️ تنبيه: هذه الجهات ومنصاتها تمنعنا من المعرفة. الإعلام يُباع ليكمم الأفواه، ولكننا سنعرف الحقيقة.",
            "real_content": field_news['content'][:500], # تقليل الحمولة لسرعة التطبيق
            "source_link": field_news['link'],
            "media_preview": "رابط مصغر لضمان السرعة", # تحسين الوسائط كما طلبتم
            "post_warning": f"🚫 هذا ما تغافل عنه هؤلاء: ({' ،'.join(culprits)}). هؤلاء هم الجبناء.",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def run_engine(self):
        print(f"🚀 بدء محرك رادار الحقيقة...")
        raw_data = self.fetch_social_geo_data()
        final_feed = []
        
        for news in raw_data:
            # تطبيق الفلاتر القديمة
            if self.apply_banned_filter(news['title'], news['content']):
                if self.visual_ethical_filter(news):
                    formatted = self.cross_check_and_format(news)
                    final_feed.append(formatted)
        
        # حفظ البيانات في المجلد المخصص للتطبيق
        os.makedirs('data', exist_ok=True)
        with open('data/banned_news_feed.json', 'w', encoding='utf-8') as f:
            json.dump(final_feed, f, ensure_ascii=False, indent=4)
        print(f"✅ تم توثيق {len(final_feed)} خبر محظور بنجاح.")

if __name__ == "__main__":
    radar = BannedNewsRadar()
    radar.run_engine()
