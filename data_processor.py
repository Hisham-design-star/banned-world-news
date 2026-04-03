# المعالج الذكي الشامل للبيانات الإنسانية والعسكرية
def process_all_platforms_data(posts_collection):
    report_summary = {
        "human_losses": [],       # سجل الشهداء والمفقودين
        "infrastructure": [],    # سجل دمار المباني والطرق
        "military_assets": [],   # سجل العتاد المحطم
        "public_sentiment": ""    # ملخص الرأي العام
    }

    for post in posts_collection:
        # 1. فيسبوك وانستجرام: استخراج البيانات الإنسانية (صور الضحايا والنعيات)
        if post.platform in ['facebook', 'instagram']:
            if post.contains_human_loss():
                report_summary["human_losses"].append({
                    "name": post.extract_name(),
                    "image": post.media_url,
                    "source_link": post.permalink,
                    "context": "نشر بواسطة ذويه/أهالي المنطقة"
                })
            
            # استخراج بيانات دمار المباني والبنى التحتية (صور الدمار)
            if post.contains_structure_damage():
                report_summary["infrastructure"].append({
                    "location": post.extract_location(),
                    "damage_image": post.media_url,
                    "description": post.text_description() # وصف الدمار (منزل، مستشفى، جسر)
                })

        # 2. تليجرام واكس: استخراج بيانات العتاد العسكري والإخفاقات
        elif post.platform in ['telegram', 'x']:
            if "تدمير" in post.text or "سقوط" in post.text:
                report_summary["military_assets"].append({
                    "type": post.detect_weapon_type(), # (دبابة، مسيرة، مدرعة)
                    "evidence_video": post.media_url
                })
            
            # تحليل الرأي العام الرافض أو الغاضب
            report_summary["public_sentiment"] += post.extract_opinion()

    return report_summary
