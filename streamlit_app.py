import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mentr • Feature Explorer",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Brand fonts and colors */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    color: #fff;
    background-color: #03162A;
}
/* Hero styling */
.hero {
    text-align: center;
    padding: 3rem 1rem;
}
.hero h1 { font-size: 3rem; margin-bottom: 0.3rem; color: #2DD0BE; }
.hero p  { font-size: 1.2rem; color: #B0C4DE; }
/* Feature selector */
.stSelectbox > div>div { background: rgba(45,208,190,0.1); border-radius: 0.5rem; }
/* Metrics & progress */
.stMetric { margin-top: 0.5rem; }
.stProgress > div > div { background: #2DD0BE !important; }
/* Demo expander */
.stExpanderHeader { background-color: rgba(45,208,190,0.1); border-radius: 0.5rem; }
/* CTA */
.cta-button button {
    background-color: #2DD0BE;
    color: #03162A;
    font-weight: 600;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    border: none;
}
.cta-button button:hover {
    opacity: 0.9;
}
/* Countdown */
.countdown { text-align:center; margin:2rem 0; font-size:1.5rem; color:#2DD0BE; }
/* Sidebar */
.stSidebar { background-color: #021022; }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
with st.container():
    st.markdown(
        """
        <div class="hero">
          <h1>Why Students 💚 Mentr</h1>
          <p>An immersive, personalized, mentor-backed learning ecosystem</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Feature Definitions ────────────────────────────────────────────────────────
features = [
    {
        "title": "Adaptive Learning Paths",
        "desc": "AI-driven study plans that adapt to your pace and weak spots in real time.",
        "stat": ("Avg. Score Gain", "28%", "+12% from last month"),
        "lottie_url": "https://assets3.lottiefiles.com/packages/lf20_x9m3j9kv.json",
        "demo_url": "https://youtu.be/adaptive-demo"
    },
    {
        "title": "24/7 Mentor Chat",
        "desc": "Instant doubt-solving with expert mentors, any time of day.",
        "stat": ("Avg. Response Time", "2m 15s", "—"),
        "lottie_url": "https://assets2.lottiefiles.com/packages/lf20_mentor.json",
        "demo_url": "https://youtu.be/mentor-demo"
    },
    {
        "title": "Gamified Progress",
        "desc": "Earn badges, points & leaderboards to stay motivated and social.",
        "stat": ("Active Users", "3.2K", "+18% this week"),
        "lottie_url": "https://assets1.lottiefiles.com/packages/lf20_game.json",
        "demo_url": "https://youtu.be/game-demo"
    },
]

# ── Feature Explorer ───────────────────────────────────────────────────────────
st.markdown("## 🔍 Explore Our Core Features")
feature_titles = [f["title"] for f in features]
choice = st.selectbox("Pick a feature:", feature_titles, index=0)

# pull selected
feat = next(f for f in features if f["title"] == choice)

col1, col2 = st.columns([1, 2], gap="large")
with col1:
    components.html(
        f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player
            src="{feat['lottie_url']}"
            background="transparent"
            speed="1"
            style="width:100%; height:300px;"
            loop
            autoplay
        ></lottie-player>
        """,
        height=320,
    )
with col2:
    st.subheader(feat["title"])
    st.write(feat["desc"])
    label, val, delta = feat["stat"]
    st.metric(label, val, delta)
    # Animate a progress bar if it's a percentage
    if val.endswith("%"):
        percent = int(val.strip("%"))
        st.progress(percent)
    with st.expander("▶️ Watch a 30s demo"):
        st.video(feat["demo_url"])

# ── Impact Metrics ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("## 🚀 Real Impact So Far")
m1, m2, m3 = st.columns(3)
m1.metric("Avg. Score Improvement", "28%", "+12%")
m2.metric("Happy Mentees", "4.8K", "+25%")
m3.metric("Mentor Satisfaction", "4.9 / 5", "+0.2")

# ── Live Countdown ────────────────────────────────────────────────────────────
deadline = datetime(2025, 5, 15, 18, 0, 0)
now = datetime.now()
diff = deadline - now
days, hrs, mins = diff.days, diff.seconds // 3600, (diff.seconds % 3600) // 60
st.markdown(
    f"<div class='countdown'>Next Live Q&A in <strong>{days}d {hrs}h {mins}m</strong></div>",
    unsafe_allow_html=True,
)

# ── Registration CTA ──────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>Ready to transform your learning?</h2>", unsafe_allow_html=True)
colA, colB, colC = st.columns([1, 1, 1])
with colB:
    if st.button("🚀 Get Early Access", key="early_access", help="Join the waitlist now"):
        st.success("Awesome—you’re on the list! Check your email for next steps.")
        st.balloons()

# ── Sidebar: Instant Chat ─────────────────────────────────────────────────────
st.sidebar.markdown("## ❓ Need help?")
st.sidebar.markdown(
    "[💬 Chat on WhatsApp](https://wa.me/92300XXXXXXX)  \n"
    "Our mentors are online 24/7!"
)
