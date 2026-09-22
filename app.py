import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. إعدادات الصفحة وتصميم جبال أجا الفاخر
# ---------------------------------------------------------
st.set_page_config(
    page_title="مُرافق حائل | Mroafiq AI",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif !important;
    }

    .stApp {
        background: 
            radial-gradient(circle at 50% 10%, rgba(216, 180, 254, 0.18) 0%, transparent 45%),
            radial-gradient(circle at 20% 90%, rgba(168, 85, 247, 0.12) 0%, transparent 40%),
            linear-gradient(180deg, #130B1E 0%, #1A102F 50%, #0F0818 100%) !important;
        background-attachment: fixed !important;
        color: #F3E8FF !important;
    }

    [data-testid="stSidebar"] {
        background: rgba(19, 11, 30, 0.96) !important;
        border-left: 1px solid rgba(216, 180, 254, 0.2) !important;
        backdrop-filter: blur(20px) !important;
    }
    [data-testid="stSidebar"] * {
        color: #F3E8FF !important;
    }

    .hero-container {
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.25) 0%, rgba(45, 20, 75, 0.7) 100%);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(216, 180, 254, 0.4);
        border-radius: 24px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 0 50px rgba(168, 85, 247, 0.25);
        margin-bottom: 25px;
    }
    .hero-title {
        font-size: 3rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #FFFFFF, #E9D5FF, #D8B4FE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 !important;
        text-shadow: 0 0 25px rgba(216, 180, 254, 0.5);
    }
    .hero-subtitle {
        color: #E9D5FF !important;
        font-size: 1.25rem !important;
        margin-top: 10px !important;
    }

    .glass-card {
        background: rgba(30, 18, 48, 0.75) !important;
        backdrop-filter: blur(25px) !important;
        border: 1px solid rgba(216, 180, 254, 0.3) !important;
        border-radius: 20px !important;
        padding: 22px !important;
        margin-bottom: 18px !important;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4), inset 0 0 15px rgba(216, 180, 254, 0.08) !important;
        transition: all 0.3s ease !important;
    }
    .glass-card:hover {
        transform: translateY(-4px) !important;
        border-color: rgba(216, 180, 254, 0.7) !important;
        box-shadow: 0 12px 35px rgba(168, 85, 247, 0.35) !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #A855F7 0%, #9333EA 50%, #7C3AED 100%) !important;
        color: #FFFFFF !important;
        border-radius: 14px !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        padding: 12px 24px !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.4) !important;
        width: 100%;
        transition: all 0.3s ease !important;
    }
    .metric-badge {
        background: rgba(168, 85, 247, 0.15);
        border: 1px solid rgba(216, 180, 254, 0.35);
        border-radius: 18px;
        padding: 16px;
        text-align: center;
        backdrop-filter: blur(15px);
    }
    .metric-value {
        font-size: 1.9rem;
        font-weight: 900;
        color: #FFFFFF;
        text-shadow: 0 0 10px rgba(216, 180, 254, 0.5);
    }
    .metric-label {
        font-size: 0.9rem;
        color: #E9D5FF;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. القائمة الجانبية وإعدادات الترجمة (عربي / إنجليزي)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <h1 style="color: #D8B4FE; margin:0; font-size: 1.9rem; text-shadow: 0 0 12px rgba(216,180,254,0.6);">💜 مُرافق حائل</h1>
        <p style="color: #E9D5FF; font-size: 0.82rem; margin-top:4px;">Aja Hackathon Edition</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    # زر اختيار اللغة
    lang = st.selectbox("🌐 Choose Language / اختر اللغة", ["العربية", "English"])
    
    st.divider()
    
    if lang == "العربية":
        st.info("🤖 المرشد الذكي ومخطط الرحلات جاهز لتصميم خطتك السياحية والرد على استفساراتك فوراً!")
        active_tab = st.radio(
            "🚀 التنقل بين الأقسام:",
            [
                "📊 لوحة المؤشرات والملخص",
                "☕ الكوفيات والمقاهي",
                "🍽️ المطاعم والمذاق الفريد",
                "🌿 المزارع والمحميات والمنتجعات",
                "⛰️ المعالم التاريخية والطبيعية",
                "🛍️ المجمعات والتسوق",
                "🏨 الفنادق والإقامة",
                "🏎️ الترفيه والمغامرات والطيران",
                "💬 المرشد الذكي ومخطط الرحلات"
            ]
        )
    else:
        st.info("🤖 AI Guide & Trip Planner are ready to design your itinerary and answer instantly!")
        active_tab = st.radio(
            "🚀 Navigation:",
            [
                "📊 Dashboard & Summary",
                "☕ Cafes & Coffee Shops",
                "🍽️ Restaurants & Unique Tastes",
                "🌿 Farms, Reserves & Resorts",
                "⛰️ Historical & Natural Landmarks",
                "🛍️ Malls & Shopping",
                "🏨 Hotels & Accommodation",
                "🏎️ Entertainment, Adventures & Aviation",
                "💬 Instant AI Guide & Trip Planner"
            ]
        )
    st.divider()

# ---------------------------------------------------------
# 3. الهيدر الديناميكي حسب اللغة
# ---------------------------------------------------------
if lang == "العربية":
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">✨ مُرافق حائل | Mroafiq AI</h1>
        <p class="hero-subtitle">الدليل الذكي الفاخر لاستكشاف جبال أجا، المزارع، الكوفيات، والفنادق ⛰️💜</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">✨ Mroafiq Hail | AI Guide</h1>
        <p class="hero-subtitle">The Ultimate Smart Guide to Explore Aja Mountains, Farms, Cafes & Hotels ⛰️💜</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. قاعدة البيانات الشاملة (مع دعم اللغتين)
# ---------------------------------------------------------
CATEGORIZED_PLACES = {
    "الكوفيات والمقاهي": [
        {"name": "ارث (عقدة)", "name_en": "Arth (Ugda)", "desc": "تجربة ثقافية فريدة في منزل طيني تاريخي مُجدد بقهاوة وإفطار محلي أصيل.", "desc_en": "Unique cultural experience in a restored historic mud house with authentic local coffee and breakfast.", "loc": "عقدة، حائل", "loc_en": "Ugda, Hail", "lat": 27.5250, "lon": 41.6850, "rating": "4.9 ⭐"},
        {"name": "حدق الشاي (عقدة)", "name_en": "Hadaq Al-Shay (Ugda)", "desc": "متكأ ومرسى لجلسات الشاي والكرك والمشروبات الساخنة والمعجنات الطازجة وسط الطبيعة.", "desc_en": "A relaxing spot for tea, Karak, hot drinks, and fresh pastries amidst nature.", "loc": "عقدة، حائل", "loc_en": "Ugda, Hail", "lat": 27.5260, "lon": 41.6830, "rating": "4.7 ⭐"},
        {"name": "كوفي بانق", "name_en": "Bang Cafe", "desc": "وجهة عصرية مميزة للقهوة المختصة والحلويات اللذيذة.", "desc_en": "A modern destination for specialty coffee and delicious desserts.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5100, "lon": 41.7000, "rating": "4.8 ⭐"},
        {"name": "كوفي Up down", "name_en": "Up Down Cafe", "desc": "إطلالة وتصميم استثنائي يقدم أجمل المشروبات المختصة.", "desc_en": "Exceptional design and view serving the finest specialty drinks.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5220, "lon": 41.6980, "rating": "4.9 ⭐"},
        {"name": "كوفي VO", "name_en": "VO Cafe", "desc": "محطة مميزة لعشاق القهوة المختصة بخدمة سريعة وجلسات مريحة.", "desc_en": "A special station for specialty coffee lovers with fast service and comfortable seating.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5180, "lon": 41.6920, "rating": "4.8 ⭐"}
    ],
    "المطاعم والمذاق الفريد": [
        {"name": "مطعم أفاميا", "name_en": "Apamia Restaurant", "desc": "أشهى الأطباق الشرقية والغربية المتميزة بجودة عالية وخدمة ممتازة.", "desc_en": "Delicious oriental and western dishes with high quality and excellent service.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5110, "lon": 41.7020, "rating": "4.8 ⭐"},
        {"name": "مطعم سولاي", "name_en": "Solay Restaurant", "desc": "وجهة مميزة لعشاق الأكل الفاخر والوجبات الشهية.", "desc_en": "A distinctive destination for fine dining and gourmet meals.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5230, "lon": 41.7010, "rating": "4.9 ⭐"}
    ],
    "المزارع والمحميات والمنتجعات": [
        {"name": "الأدهم (عقدة)", "name_en": "Al-Adham (Ugda)", "desc": "وجهة سياحية وثقافية فريدة بين جبال حائل، تحتضن فعاليات تراثية ومقاهي وجلسات مفتوحة.", "desc_en": "A unique tourism and cultural destination among Hail mountains hosting heritage events and cafes.", "loc": "عقدة، حائل", "loc_en": "Ugda, Hail", "lat": 27.5240, "lon": 41.6820, "rating": "4.8 ⭐"},
        {"name": "منتجع حياة", "name_en": "Hayat Resort", "desc": "منتجع متكامل يضم مطعم وكوفي ومساحات تضم حيوانات وأجواء ريفية ساحرة.", "desc_en": "An integrated resort featuring a restaurant, cafe, animals, and charming rural vibes.", "loc": "حائل", "loc_en": "Hail", "lat": 27.4800, "lon": 41.6500, "rating": "4.9 ⭐"},
        {"name": "مزرعة الديدحان (الخطه)", "name_en": "Al-Daidahan Farm (Al-Khotta)", "desc": "من أجمل المزارع الريفية التراثية، جلسات هادئة وسط النخيل وفعاليات عائلية.", "desc_en": "One of the most beautiful rural heritage farms, peaceful palm seating and family events.", "loc": "الخطه، حائل", "loc_en": "Al-Khotta, Hail", "lat": 27.4600, "lon": 41.6000, "rating": "4.9 ⭐"},
        {"name": "محمية القحويان (القاعد)", "name_en": "Al-Qahwiyan Reserve (Al-Qaid)", "desc": "تضم مساحات خضراء وزهور الأقحوان، شاليهات فندقية، ومرابط للخيول.", "desc_en": "Features green spaces, daisy flowers, hotel chalets, and horse stables.", "loc": "القاعد، حائل", "loc_en": "Al-Qaid, Hail", "lat": 28.1000, "lon": 41.5000, "rating": "5.0 ⭐"}
    ],
    "المعالم التاريخية والطبيعية": [
        {"name": "مطل حاتم الطائي (السمرا)", "name_en": "Hatim Al-Tai Lookout (Samra)", "desc": "مطل تاريخي شهير يطل على مدينة حائل من جبل السمرا بأجواء ساحرة.", "desc_en": "A famous historic viewpoint overlooking Hail city from Samra Mountain.", "loc": "جبل السمرا، حائل", "loc_en": "Samra Mountain, Hail", "lat": 27.5400, "lon": 41.7200, "rating": "4.9 ⭐"},
        {"name": "منازل حاتم الطائي (توارن)", "name_en": "Hatim Al-Tai Houses (Tuwarin)", "desc": "موقع أثري عريق يعكس تاريخ الكرم والاصالة في قرية تووارن التاريخية.", "desc_en": "An ancient historical site reflecting generosity and heritage in Tuwarin village.", "loc": "توارن، حائل", "loc_en": "Tuwarin, Hail", "lat": 27.8000, "lon": 41.3500, "rating": "4.9 ⭐"}
    ],
    "المجمعات والتسوق": [
        {"name": "حايل زون", "name_en": "Hail Zone", "desc": "مجمع حيوي يضم كوفيات ومطاعم متنوعة وجلسات عصرية مميزة.", "desc_en": "A vibrant complex featuring diverse cafes, restaurants, and modern seating.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5150, "lon": 41.7030, "rating": "4.8 ⭐"},
        {"name": "العثيم مول", "name_en": "Othaim Mall", "desc": "وجهة تسوق رئيسية تضم أشهر الماركات العالمية، المطاعم، والترفيه.", "desc_en": "A major shopping destination featuring top international brands, dining, and entertainment.", "loc": "حائل", "loc_en": "Hail", "lat": 27.4950, "lon": 41.7100, "rating": "4.8 ⭐"}
    ],
    "الفنادق والإقامة": [
        {"name": "فندق ميلينيوم حائل", "name_en": "Millennium Hail Hotel", "desc": "فندق خمس نجوم فاخر يضم مرافق راقية، غرف مريحة، وخدمة عالمية.", "desc_en": "A luxury 5-star hotel featuring premium facilities, comfortable rooms, and world-class service.", "loc": "حائل", "loc_en": "Hail", "lat": 27.4850, "lon": 41.6900, "rating": "4.9 ⭐"},
        {"name": "فندق سكناي رويال", "name_en": "Sokany Royal Hotel", "desc": "إقامة فندقية راقية ومريحة تناسب العوائل ورجال الأعمال.", "desc_en": "Elegant and comfortable hotel accommodation suitable for families and business travelers.", "loc": "حائل", "loc_en": "Hail", "lat": 27.5020, "lon": 41.7020, "rating": "4.8 ⭐"}
    ],
    "الترفيه والمغامرات والطيران": [
        {"name": "نادي العزيزية للطيران وسيارات الدفع الرباعي (الخطه)", "name_en": "Al-Aziziyah Aviation & 4x4 Club (Al-Khotta)", "desc": "وجهة مثالية لهواة الطيران الشراعي، المغامرات، وتحديات سيارات الدفع الرباعي الصحراوية.", "desc_en": "An ideal destination for paragliding, adventures, and desert 4x4 challenges.", "loc": "الخطه، حائل", "loc_en": "Al-Khotta, Hail", "lat": 27.4700, "lon": 41.5900, "rating": "4.9 ⭐"}
    ]
}

ALL_FLAT_PLACES = []
for cat, places in CATEGORIZED_PLACES.items():
    for p in places:
        p_copy = p.copy()
        p_copy['category'] = cat
        ALL_FLAT_PLACES.append(p_copy)

# ---------------------------------------------------------
# 5. عرض محتوى الأقسام حسب اللغة المختارة
# ---------------------------------------------------------

if active_tab in ["📊 لوحة المؤشرات والملخص", "📊 Dashboard & Summary"]:
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="metric-badge"><div class="metric-value">22°C</div><div class="metric-label">{"طقس حائل المعتدل 🌤️" if lang=="العربية" else "Hail Weather 🌤️"}</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-badge"><div class="metric-value">35+</div><div class="metric-label">{"وجهة ومعلم سياحي ⛰️" if lang=="العربية" else "Tourist Destinations ⛰️"}</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-badge"><div class="metric-value">7</div><div class="metric-label">{"أقسام رئيسية متكاملة 💜" if lang=="العربية" else "Main Categories 💜"}</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="metric-badge"><div class="metric-value">100%</div><div class="metric-label">{"جاهز للهاكاثون والفوز 🚀" if lang=="العربية" else "Hackathon Ready 🚀"}</div></div>', unsafe_allow_html=True)

    st.write("")
    if lang == "العربية":
        st.markdown("### ⛰️ أهلاً بكِ في منصة مُرافق حائل الذكية")
        st.markdown("""
        <div class="glass-card">
            <p style="font-size: 1.15rem; line-height: 1.8; margin: 0;">
                يا بعد حيي! هذه المنصة مصممة خصيصاً لتكون دليلك السياحي الشامل والمتكامل لمنطقة حائل وجبال أجا العريقة. 
                استمتعي باستعراض الكوفيات، المطاعم، المزارع، والمحميات، والفنادق موزعة في أقسام مرتبة بعناية، مع المرشد الذكي المدمج للرد الفوري بدقة وتصميم خطط السفر! 🏆💜
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### ⛰️ Welcome to Mroafiq Hail Smart Platform")
        st.markdown("""
        <div class="glass-card">
            <p style="font-size: 1.15rem; line-height: 1.8; margin: 0;">
                Welcome! This platform is designed to be your comprehensive tour guide for Hail and the ancient Aja Mountains. 
                Explore cafes, restaurants, farms, reserves, and hotels with our integrated AI Smart Guide & Trip Planner ready to design your itinerary! 🏆💜
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.subheader("📍 Interactive Map" if lang=="English" else "📍 خريطة المواقع التفاعلية الشاملة")
    df_map = pd.DataFrame(ALL_FLAT_PLACES)
    st.map(df_map[['lat', 'lon']], zoom=8)

else:
    cat_mapping_ar = {
        "☕ الكوفيات والمقاهي": "الكوفيات والمقاهي",
        "🍽️ المطاعم والمذاق الفريد": "المطاعم والمذاق الفريد",
        "🌿 المزارع والمحميات والمنتجعات": "المزارع والمحميات والمنتجعات",
        "⛰️ المعالم التاريخية والطبيعية": "المعالم التاريخية والطبيعية",
        "🛍️ المجمعات والتسوق": "المجمعات والتسوق",
        "🏨 الفنادق والإقامة": "الفنادق والإقامة",
        "🏎️ الترفيه والمغامرات والطيران": "الترفيه والمغامرات والطيران"
    }
    cat_mapping_en = {
        "☕ Cafes & Coffee Shops": "الكوفيات والمقاهي",
        "🍽️ Restaurants & Unique Tastes": "المطاعم والمذاق الفريد",
        "🌿 Farms, Reserves & Resorts": "المزارع والمحميات والمنتجعات",
        "⛰️ Historical & Natural Landmarks": "المعالم التاريخية والطبيعية",
        "🛍️ Malls & Shopping": "المجمعات والتسوق",
        "🏨 Hotels & Accommodation": "الفنادق والإقامة",
        "🏎️ Entertainment, Adventures & Aviation": "الترفيه والمغامرات والطيران"
    }

    selected_cat_key = cat_mapping_ar.get(active_tab) or cat_mapping_en.get(active_tab)

    if selected_cat_key:
        st.subheader(active_tab)
        for place in CATEGORIZED_PLACES[selected_cat_key]:
            p_name = place['name'] if lang == "العربية" else place['name_en']
            p_desc = place['desc'] if lang == "العربية" else place['desc_en']
            p_loc = place['loc'] if lang == "العربية" else place['loc_en']
            loc_label = "الموقع الدقيق" if lang == "العربية" else "Exact Location"
            rating_label = "التقييم" if lang == "العربية" else "Rating"
            
            st.markdown(f"""
            <div class="glass-card">
                <h3 style="margin-top:0; color:#D8B4FE;">{p_name}</h3>
                <p style="font-size: 1.05rem; margin: 5px 0;">{p_desc}</p>
                <p style="margin: 5px 0; font-size: 0.9rem; color:#E9D5FF;">📍 <b>{loc_label}:</b> {p_loc} | ⭐ <b>{rating_label}:</b> {place['rating']}</p>
            </div>
            """, unsafe_allow_html=True)

    elif active_tab in ["💬 المرشد الذكي ومخطط الرحلات", "💬 Instant AI Guide & Trip Planner"]:
        st.subheader("💬 " + ("اسأل المرشد الذكي ومخطط الرحلات لمنطقة حائل" if lang=="العربية" else "Ask AI Guide & Trip Planner for Hail"))
        
        placeholder_text = "مثال: اصنع لي خطة سفر ليومين في حائل أو دلني على كوفي في عقدة" if lang=="العربية" else "Example: Create a 2-day trip plan in Hail or show a cafe in Ugda"
        user_prompt = st.text_input("اكتب سؤالك أو طلبك السياحي / Type your prompt or travel request:", placeholder=placeholder_text)
        
        if user_prompt:
            prompt_lower = user_prompt.lower()
            bot_reply = ""
            
            # 1. نظام خطة السفر الذكية (Itinerary / Trip Plan)
            if any(w in prompt_lower for w in ["خطة", "برنامج", "جدول", "يومين", "سفر", "trip", "plan", "itinerary", "schedule"]):
                if lang == "العربية":
                    bot_reply = """
                    🌟 <b>مقترح خطة سفر ذكية لمدة يومين في حائل وجبال أجا:</b><br><br>
                    ☀️ <b>اليوم الأول (عبق التراث والطبيعة):</b><br>
                    • <b>الصباح:</b> زيارة قرية عقدة وتاريخها العريق، مع الإفطار والقهوة في كوفي <b>'ارث'</b> أو <b>'حدق الشاي'</b> (موقع دقيق: عقدة، حائل).<br>
                    • <b>الظهر:</b> تناول الغداء الفاخر في <b>'مطعم أفاميا'</b> أو <b>'مطعم سولاي'</b>.<br>
                    • <b>المساء:</b> الاستمتاع بالإطلالة البانورامية الساحرة من <b>'مطل حاتم الطائي (السمرا)'</b>.<br><br>
                    🌙 <b>اليوم الثاني (المزارع والمغامرات):</b><br>
                    • <b>الصباح:</b> زيارة <b>'مزرعة الديدحان'</b> بالخطه أو <b>'محمية القحويان'</b> بالقاعد لأجواء ريفية خيالية.<br>
                    • <b>الظهر:</b> خوض تجربة حماسية في <b>'نادي العزيزية للطيران والدفع الرباعي'</b>.<br>
                    • <b>المساء:</b> التسوق وجلسات العشاء العصرية في <b>'حايل زون'</b> أو <b>'العثيم مول'</b>.
                    """
                else:
                    bot_reply = """
                    🌟 <b>Smart 2-Day Itinerary Proposal for Hail & Aja Mountains:</b><br><br>
                    ☀️ <b>Day 1 (Heritage & Nature):</b><br>
                    • <b>Morning:</b> Explore Ugda village and enjoy breakfast & coffee at <b>'Arth'</b> or <b>'Hadaq Al-Shay'</b>.<br>
                    • <b>Midday:</b> Enjoy lunch at <b>'Apamia Restaurant'</b> or <b>'Solay Restaurant'</b>.<br>
                    • <b>Evening:</b> Enjoy the panoramic sunset view from <b>'Hatim Al-Tai Lookout (Samra)'</b>.<br><br>
                    🌙 <b>Day 2 (Farms & Adventures):</b><br>
                    • <b>Morning:</b> Visit <b>'Al-Daidahan Farm'</b> in Al-Khotta or <b>'Al-Qahwiyan Reserve'</b>.<br>
                    • <b>Midday:</b> Experience thrilling paragliding and 4x4 at <b>'Al-Aziziyah Club'</b>.<br>
                    • <b>Evening:</b> Shopping & modern dining at <b>'Hail Zone'</b> or <b>'Othaim Mall'</b>.
                    """

            # 2. البحث عن الكوفيات
            elif any(w in prompt_lower for w in ["كوفي", "قهوة", "مقهى", "cafe", "coffee"]):
                matched = [p for p in ALL_FLAT_PLACES if p['category'] == "الكوفيات والمقاهي" and any(word in (p['name'] + " " + p['loc'] + " " + p['desc']).lower() for word in prompt_lower.split())]
                if not matched or "حائل" in prompt_lower or "hail" in prompt_lower:
                    matched = CATEGORIZED_PLACES["الكوفيات والمقاهي"]
                    
                bot_reply = "يا بعد حيي، هذه أبرز الكوفيات المقترحة والمواقع الدقيقة:<br><br>" if lang=="العربية" else "Here are the suggested cafes and exact locations:<br><br>"
                for c in matched:
                    c_name = c['name'] if lang=="العربية" else c['name_en']
                    c_loc = c['loc'] if lang=="العربية" else c['loc_en']
                    c_desc = c['desc'] if lang=="العربية" else c['desc_en']
                    bot_reply += f"☕ <b>{c_name}</b><br>📍 <b>Location:</b> {c_loc}<br>📝 {c_desc} ({c['rating']})<br><br>"
                    
            # 3. البحث عن المطاعم
            elif any(w in prompt_lower for w in ["مطعم", "أكل", "غداء", "عشاء", "restaurant", "food"]):
                matched = CATEGORIZED_PLACES["المطاعم والمذاق الفريد"]
                bot_reply = "يا بعد حيي، إليك أفضل المطاعم ومواقعها:<br><br>" if lang=="العربية" else "Here are the best restaurants:<br><br>"
                for r in matched:
                    r_name = r['name'] if lang=="العربية" else r['name_en']
                    r_loc = r['loc'] if lang=="العربية" else r['loc_en']
                    r_desc = r['desc'] if lang=="العربية" else r['desc_en']
                    bot_reply += f"🍽️ <b>{r_name}</b><br>📍 <b>Location:</b> {r_loc}<br>📝 {r_desc} ({r['rating']})<br><br>"
                    
            # 4. البحث عن المزارع والمنتجعات
            elif any(w in prompt_lower for w in ["مزرعة", "منتجع", "محمية", "farm", "resort", "reserve"]):
                matched = CATEGORIZED_PLACES["المزارع والمحميات والمنتجعات"]
                bot_reply = "يا بعد حيي، إليك أجمل المزارع والمنتجعات:<br><br>" if lang=="العربية" else "Here are the top farms and resorts:<br><br>"
                for m in matched:
                    m_name = m['name'] if lang=="العربية" else m['name_en']
                    m_loc = m['loc'] if lang=="العربية" else m['loc_en']
                    m_desc = m['desc'] if lang=="العربية" else m['desc_en']
                    bot_reply += f"🌿 <b>{m_name}</b><br>📍 <b>Location:</b> {m_loc}<br>📝 {m_desc} ({m['rating']})<br><br>"
                    
            else:
                bot_reply = f"يا بعد حيي، بالنسبة لسؤالك ({user_prompt})، جرب أن تطلب (خطة سفر ليومين)، أو تسأل عن (كوفي)، (مطعم)، أو (مزرعة) وسأقوم بخدمتك فوراً!" if lang=="العربية" else f"Regarding your question ({user_prompt}), try asking for a '2-day trip plan' or asking about cafes, restaurants, or farms!"

            st.markdown(f"""
            <div class="glass-card" style="border-right: 6px solid #D8B4FE !important;">
                <b style="color:#D8B4FE; font-size:1.15rem;">🤖 {"مُرافق حائل الذكي ومخطط الرحلات يقول:" if lang=="العربية" else "AI Guide & Trip Planner says:"}</b>
                <p style="font-size:1.05rem; margin-top:8px; color:#FFFFFF !important; line-height:1.7;">{bot_reply}</p>
            </div>
            """, unsafe_allow_html=True)