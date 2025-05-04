import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import random

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mentr • MDCAT World",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Brand CSS Overrides ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  color: #fff;
  background-color: #03162A;
  margin: 0; padding: 0;
}
.hero { text-align: center; padding: 3rem 1rem; }
.hero h1 { font-size: 3rem; margin-bottom: .3rem; color: #2DD0BE; }
.hero p { font-size: 1.2rem; color: #B0C4DE; }
.stSelectbox > div>div { background: rgba(45,208,190,0.1); border-radius: 0.5rem; }
.stProgress > div > div { background: #2DD0BE !important; }
.countdown { text-align: center; margin: 2rem 0; font-size: 1.5rem; color: #2DD0BE; }
.cta-button button { background: #2DD0BE; color: #03162A; font-weight: 600; padding: .75rem 1.5rem; border-radius: .5rem; border: none; }
.cta-button button:hover { opacity: .9; }
.stSidebar { background-color: #021022; padding: 1rem; }
.sidebar-content a { color: #2DD0BE; text-decoration: none; font-weight: 600; }
.section-title { color: #2DD0BE; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Mentr’s MDCAT World</h1>
  <p>Re-building Education: Personalized, Holistic, Boundless. Increase Your Every Quotient for Success!</p>
</div>
""", unsafe_allow_html=True)

# ── Self-Assessment Quiz ───────────────────────────────────────────────────────
with st.expander("📝 Quick 2-Question Self-Assessment"):
    q1 = st.radio("Confidence in Organic Chemistry?", ["Not at all", "Somewhat", "Very"])
    q2 = st.radio("Mocks Taken so far?", ["0", "1–5", "6+"])
    if st.button("▶️ Show My Readiness Score"):
        score_map = {"Not at all": 20, "Somewhat": 50, "Very": 80}
        test_map  = {"0": 0, "1–5": 20, "6+": 40}
        readiness = (score_map[q1] + test_map[q2]) // 2
        st.metric("Your MDCAT Readiness", f"{readiness}/100")
        st.success("80% of students at this level improve by 28%+ with Mentr!")

# ── Improvement & Mentr-Quotient Calculator ──────────────────────────────────
with st.expander("🎯 Improvement & Your Mentr Quotient"):
    current = st.slider("Current mock % score", 0, 100, 50)
    potential = min(100, round(current * 1.28))
    st.write(f"**With Mentr**, you could reach **{potential}%**!")
    st.progress(potential)

    st.write("---")
    st.write("**Calculate Your Mentr Quotient** (IQ, EQ, CQ, PQ):")
    iq = st.slider("Intellectual Quotient (IQ)", 0, 100, 60)
    eq = st.slider("Emotional Quotient (EQ)", 0, 100, 70)
    cq = st.slider("Creative Quotient (CQ)", 0, 100, 65)
    pq = st.slider("Practical Quotient (PQ)", 0, 100, 55)
    mq = (iq + eq + cq + pq) / 4
    st.metric("Your Mentr Quotient", f"{mq:.0f}/100")
    st.info("This holistic metric tracks your growth across knowledge, emotions, creativity, and real-world skills.")

# ── Core & Vision-Driven Features ──────────────────────────────────────────────
features = [
    {
        "title": "Adaptive Learning Paths",
        "desc": "AI-driven study plans that evolve with your pace, weak spots & style.",
        "stat": ("Avg. Score Gain", "28%", "+12%"),
        "lottie": "https://assets3.lottiefiles.com/packages/lf20_x9m3j9kv.json"
    },
    {
        "title": "24/7 Mentor Chat",
        "desc": "Instant doubt-solving by top MDCAT mentors, day or night.",
        "stat": ("Avg. Response Time", "2m 15s", "—"),
        "lottie": "https://assets2.lottiefiles.com/packages/lf20_mentor.json"
    },
    {
        "title": "Gamified Progress",
        "desc": "Badges, leaderboards & points keep you motivated & social.",
        "stat": ("Active Users", "3.2K", "+18%"),
        "lottie": "https://assets1.lottiefiles.com/packages/lf20_game.json"
    },
    {
        "title": "Holistic Development",
        "desc": "Modules on focus, stress-management & emotional intelligence.",
        "stat": ("EQ Improvement", "35%", "+15%"),
        "lottie": "https://assets9.lottiefiles.com/packages/lf20_holistic.json"
    },
    {
        "title": "Peer-Learning Circles",
        "desc": "Join daily group sessions & student communities worldwide.",
        "stat": ("Live Sessions", "150+", "+20% weekly"),
        "lottie": "https://assets7.lottiefiles.com/packages/lf20_peer.json"
    },
    {
        "title": "Global Accessibility",
        "desc": "Multi-language, region-specific content & Mentr ID single-sign-on.",
        "stat": ("Regions Covered", "12+", "+4 in last month"),
        "lottie": "https://assets5.lottiefiles.com/packages/lf20_global.json"
    },
]

st.markdown('<h2 class="section-title">🚀 Explore What Makes Mentr Unique</h2>', unsafe_allow_html=True)
choice = st.selectbox("", [f["title"] for f in features], index=0)
feat = next(f for f in features if f["title"] == choice)

c1, c2 = st.columns([1, 2], gap="large")
with c1:
    components.html(f"""
      <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
      <lottie-player
        src="{feat['lottie']}"
        background="transparent"
        speed="1"
        style="width:100%; height:300px;"
        loop autoplay
      ></lottie-player>
    """, height=320)
with c2:
    st.subheader(feat["title"])
    st.write(feat["desc"])
    label, val, delta = feat["stat"]
    st.metric(label, val, delta)
    if val.endswith("%"):
        st.progress(int(val.strip("%")))

# ── Scarcity, Social Proof & Metrics ───────────────────────────────────────────
seats_left = random.randint(1, 8)
st.markdown(
    f"<p style='text-align:center; color:#F45C48;'>🚨 Only <strong>{seats_left}</strong> seats left at this rate!</p>",
    unsafe_allow_html=True
)
st.markdown("---\n<h2 class='section-title'>📊 Real Impact So Far</h2>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
m1.metric("Avg. Score ↑", "28%", "+12%")
m2.metric("Happy Mentees", "4.8K", "+25%")
m3.metric("Mentr Quotient Avg.", "72/100", "+8")

# ── Countdown to Next Live Event ──────────────────────────────────────────────
deadline = datetime(2025, 5, 15, 18, 0, 0)
diff = deadline - datetime.now()
days, hrs, mins = diff.days, diff.seconds//3600, (diff.seconds%3600)//60
st.markdown(
    f"<div class='countdown'>⏳ Next Live Q&A in <strong>{days}d {hrs}h {mins}m</strong></div>",
    unsafe_allow_html=True
)

# ── Registration & Bonuses ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<h2 class='section-title'>Ready to Become a Boundless Learner?</h2>", unsafe_allow_html=True)
with st.form("register", clear_on_submit=True):
    name  = st.text_input("Full Name")
    email = st.text_input("Email Address")
    guide = st.checkbox("Send me the **FREE Mentr Vision & Strategy Guide**", value=True)
    club  = st.checkbox("Yes, enroll me in the Mentr Leadership Club", value=False)
    submit = st.form_submit_button("🚀 Join MDCAT World & Get Guide")
    if submit:
        st.success(f"Thank you, {name}! Check your inbox now.")
        st.balloons()
        if guide:
            pdf = b"%PDF-1.4 (your-guide-content...)"
            st.download_button("📥 Download Vision & Strategy Guide", pdf, "Mentr_Vision_Guide.pdf", mime="application/pdf")

# ── Persistent Help Sidebar ───────────────────────────────────────────────────
st.sidebar.markdown("## ❓ Need Instant Help?")
st.sidebar.markdown("[💬 Chat on WhatsApp](https://wa.me/92300XXXXXXX)", unsafe_allow_html=True)
