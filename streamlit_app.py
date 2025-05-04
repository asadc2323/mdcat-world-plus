import streamlit as st
import requests
from datetime import datetime

# 1. Helper to load Lotties
def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

# 2. Feature definitions
features = [
    {
        "title": "Adaptive Learning Paths",
        "desc": "AI-driven study plans that adapt to your pace and weak spots in real time.",
        "stat": ("Avg. Score Gain", "28%", "+12% from last month"),
        "lottie_url": "https://assetsX.lottiefiles.com/packages/…/adaptive.json",
        "demo_url": "https://youtu.be/adaptive-demo"
    },
    {
        "title": "24/7 Mentor Chat",
        "desc": "Instant doubt-solving with expert mentors, any time of day.",
        "stat": ("Avg. Response Time", "2m 15s", "—"),
        "lottie_url": "https://assetsX.lottiefiles.com/packages/…/mentor.json",
        "demo_url": "https://youtu.be/mentor-demo"
    },
    {
        "title": "Gamified Progress",
        "desc": "Earn badges, points & leaderboards to stay motivated and social.",
        "stat": ("Active Users", "3.2K", "+18% this week"),
        "lottie_url": "https://assetsX.lottiefiles.com/packages/…/game.json",
        "demo_url": "https://youtu.be/game-demo"
    },
]

st.set_page_config(page_title="Mentr • Features", layout="wide")

# Hero
st.markdown(
    """
    <div style="text-align:center; padding:2rem 0;">
      <h1 style="font-size:3rem; margin-bottom:.2rem;">Why Students 💚 Mentr</h1>
      <p style="font-size:1.2rem; color:#aaa;">An immersive, personalized, mentor-backed learning ecosystem</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 3. Tabs for each feature
tabs = st.tabs([f["title"] for f in features])
for tab, feat in zip(tabs, features):
    with tab:
        c1, c2 = st.columns([1, 2])
        # Left: Lottie animation
        lottie_json = load_lottie(feat["lottie_url"])
        if lottie_json:
            st_lottie = st.empty()
            st_lottie.json(lottie_json)  # if you're using streamlit_lottie
        # Right: headline, description, stat, demo
        with c2:
            st.header(feat["title"])
            st.write(feat["desc"])
            label, val, delta = feat["stat"]
            st.metric(label, val, delta)
            # Demo video expander
            with st.expander("▶️ Watch a 30s demo"):
                st.video(feat["demo_url"])
        st.divider()

# 4. A quick “tour” of metrics
st.markdown("## Real Impact So Far")
m1, m2, m3 = st.columns(3)
m1.metric("Avg. Score Improvement", "28%", "+12%")
m2.metric("Happy Mentees", "4.8K", "+25%")
m3.metric("Mentor Satisfaction", "4.9/5", "+0.2")

# 5. Live countdown to next Q&A
deadline = datetime(2025, 5, 15, 18, 0, 0)
now = datetime.now()
diff = deadline - now
days, hrs, mins = diff.days, diff.seconds//3600, (diff.seconds%3600)//60
st.markdown(
    f"<h2 style='text-align:center;'>Next Live Q&A in {days}d {hrs}h {mins}m</h2>",
    unsafe_allow_html=True
)

# 6. Registration form with social proof
st.markdown("---")
with st.form("register"):
    st.subheader("Join Mentr Today")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    code = st.text_input("Referral Code (optional)")
    submitted = st.form_submit_button("🚀 Get Early Access")
    if submitted:
        st.success("Thanks! 🚀 We've sent you a link.")
        st.balloons()

# 7. Persistent “Chat with us” badge
st.sidebar.markdown(
    """
    **❓ Need help?**  
    [Chat on WhatsApp](https://wa.me/92300XXXXXXX)  
    We're here 24/7!
    """
)
