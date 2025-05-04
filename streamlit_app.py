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
html, body, [class*="css"]  {
  font-family: 'Inter', sans-serif;
  color: #fff;
  background-color: #03162A;
  margin: 0; padding: 0;
}
.hero { text-align:center; padding:3rem 1rem; }
.hero h1 { font-size:3rem; margin-bottom:.5rem; color:#2DD0BE; }
.hero p  { font-size:1.2rem; color:#B0C4DE; }
.stSelectbox > div>div { background: rgba(45,208,190,0.1); border-radius: 0.5rem; }
.stProgress > div > div { background: #2DD0BE !important; }
.countdown { text-align:center; margin:2rem 0; font-size:1.5rem; color:#2DD0BE; }
.cta-button button { background:#2DD0BE; color:#03162A; font-weight:600; padding:.75rem 1.5rem; border-radius:.5rem; border:none; }
.cta-button button:hover { opacity:.9; }
.stSidebar { background-color: #021022; padding:1rem; }
.sidebar-content a { color: #2DD0BE; text-decoration:none; font-weight:600; }
</style>
""", unsafe_allow_html=True)

# ── Hero & Personalization ────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>MDCAT World by Mentr</h1>
  <p>Immersive, mentor-backed learning that guarantees improvement—or your money back.</p>
</div>
""", unsafe_allow_html=True)

# ── Self-Assessment Quiz Hook ─────────────────────────────────────────────────
with st.expander("📝 Quick 2-Question Self-Assessment"):
    q1 = st.radio("How confident are you in Organic Chemistry?", ["Not at all", "Somewhat", "Very"])
    q2 = st.radio("How many full mock tests have you taken?", ["0", "1–5", "6+"])
    if st.button("▶️ Get My Readiness Score"):
        score_map = {"Not at all": 20, "Somewhat": 50, "Very": 80}
        test_map  = {"0": 0, "1–5": 20, "6+": 40}
        readiness = (score_map[q1] + test_map[q2]) // 2
        st.metric("Your Readiness Score", f"{readiness}/100")
        st.success("80% of students with a similar score improve by 28%+ using Mentr.")

# ── Improvement Calculator ─────────────────────────────────────────────────────
with st.expander("⚙️ Improvement Potential Calculator"):
    current = st.slider("Current mock test score (%)", 0, 100, 50)
    potential = min(100, round(current * 1.28))
    st.write(f"**With Mentr**, you could reach **{potential}%**!")
    st.progress(potential)

# ── Core Feature Explorer ─────────────────────────────────────────────────────
features = [
    {
        "title": "Adaptive Learning Paths",
        "desc": "AI-driven study plans that adapt to your pace & weak spots.",
        "stat": ("Avg. Score Gain", "28%", "+12%"),
        "lottie": "https://assets3.lottiefiles.com/packages/lf20_x9m3j9kv.json",
        "video": "https://youtu.be/adaptive-demo"
    },
    {
        "title": "24/7 Mentor Chat",
        "desc": "Instant, expert doubt-solving any time of day.",
        "stat": ("Avg. Response Time", "2m 15s", "—"),
        "lottie": "https://assets2.lottiefiles.com/packages/lf20_mentor.json",
        "video": "https://youtu.be/mentor-demo"
    },
    {
        "title": "Gamified Progress",
        "desc": "Earn badges, points & leaderboards to stay motivated.",
        "stat": ("Active Users", "3.2K", "+18%"),
        "lottie": "https://assets1.lottiefiles.com/packages/lf20_game.json",
        "video": "https://youtu.be/game-demo"
    },
]

st.markdown("## 🔍 Explore Our Core Features")
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
    with st.expander("▶️ Watch a 30s Demo"):
        st.video(feat["video"])

# ── Social Proof & Scarcity ────────────────────────────────────────────────────
seats_left = random.randint(1, 8)
st.markdown(f"<p style='text-align:center; color:#F45C48;'>🚨 Only **{seats_left}** seats left at this rate!</p>", unsafe_allow_html=True)

# ── Impact Metrics ─────────────────────────────────────────────────────────────
st.markdown("---\n## 🚀 Real Impact So Far")
m1, m2, m3 = st.columns(3)
m1.metric("Avg. Score ↑", "28%", "+12%")
m2.metric("Happy Mentees", "4.8K", "+25%")
m3.metric("Mentor Satisfaction", "4.9/5", "+0.2")

# ── Live Countdown ────────────────────────────────────────────────────────────
deadline = datetime(2025, 5, 15, 18, 0, 0)
diff = deadline - datetime.now()
days, hrs, mins = diff.days, diff.seconds//3600, (diff.seconds%3600)//60
st.markdown(f"<div class='countdown'>⏳ Next Live Q&A in <strong>{days}d {hrs}h {mins}m</strong></div>", unsafe_allow_html=True)

# ── Registration & Bonuses ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>Ready to Transform Your MDCAT Journey?</h2>", unsafe_allow_html=True)
with st.form("register", clear_on_submit=True):
    name  = st.text_input("Your Full Name")
    email = st.text_input("Email Address")
    guide = st.checkbox("Yes, send me the **FREE MDCAT Shortcut Guide**", value=True)
    submit = st.form_submit_button("🚀 Get Early Access & Guide", help="Immediate email with your guide")
    if submit:
        st.success(f"Thank you, {name}! Check your inbox in a sec.")
        st.balloons()
        if guide:
            # Dummy PDF content, replace with your actual file
            pdf = b"%PDF-1.4 your-guide-content..."
            st.download_button("📥 Download Your Guide", pdf, "MDCAT_Shortcut_Guide.pdf", mime="application/pdf")

# ── Persistent Help Sidebar ───────────────────────────────────────────────────
st.sidebar.markdown("## ❓ Need Instant Help?")
st.sidebar.markdown("[💬 Chat with us on WhatsApp](https://wa.me/92300XXXXXXX)", unsafe_allow_html=True)
