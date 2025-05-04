import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="Mentr • Features", layout="wide")

# Hero (unchanged)...
# ...

# 1. Define your features (same as before)
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

# 2. Tabs for each feature, with client-side Lottie loading
tabs = st.tabs([f["title"] for f in features])
for tab, feat in zip(tabs, features):
    with tab:
        c1, c2 = st.columns([1, 2])
        # Left: embed the Lottie player
        with c1:
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
                height=320,  # give enough height for the player
            )
        # Right: content
        with c2:
            st.header(feat["title"])
            st.write(feat["desc"])
            label, val, delta = feat["stat"]
            st.metric(label, val, delta)
            with st.expander("▶️ Watch a 30s demo"):
                st.video(feat["demo_url"])
        st.divider()

# 3. The rest of your app (metrics, countdown, form, etc.)…
# live countdown
deadline = datetime(2025, 5, 15, 18, 0, 0)
now = datetime.now()
diff = deadline - now
days, hrs, mins = diff.days, diff.seconds//3600, (diff.seconds%3600)//60
st.markdown(
    f"<h2 style='text-align:center;'>Next Live Q&A in {days}d {hrs}h {mins}m</h2>",
    unsafe_allow_html=True
)

# registration form
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

# sidebar chat link
st.sidebar.markdown(
    """
    **❓ Need help?**  
    [Chat on WhatsApp](https://wa.me/92300XXXXXXX)  
    We're here 24/7!
    """
)
