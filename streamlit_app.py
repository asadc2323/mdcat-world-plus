import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ── Page Configuration ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mentr Journey",
    layout="wide",
    initial_sidebar_state="auto",
)

# ── Session State for Step Navigation ─────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step = min(st.session_state.step + 1, len(slides) - 1)

def prev_step():
    st.session_state.step = max(st.session_state.step - 1, 0)

# ── Slide Definitions ──────────────────────────────────────────────────────────
slides = [
    {
        "title": "🌌 Welcome to Mentr’s MDCAT World",
        "subtitle": "Re-building Education: Boundless, Holistic, Personal.",
        "media": """
        <video autoplay muted loop style="width:100%; height:auto; border-radius:1rem;">
          <source src="https://cdn.videvo.net/videvo_files/video/free/2017-12/large_watermarked/171118_SciFi_Computing_005_preview.mp4" type="video/mp4">
        </video>
        """,
        "text": "Dive into an immersive learning ecosystem where AI, mentors, and community collide to propel you beyond any traditional classroom.",
        "cta": "Next →"
    },
    {
        "title": "1️⃣ Your Personalized Learning Odyssey",
        "subtitle": "Adaptive Paths & Real-Time Feedback",
        "media": """
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player
          src="https://assets3.lottiefiles.com/packages/lf20_x9m3j9kv.json"
          background="transparent" speed="1"
          style="width:100%; height:300px;" loop autoplay>
        </lottie-player>
        """,
        "text": "Our AI crafts your study plan minute-by-minute, adapting to your weak spots and celebrating your strengths as you progress.",
        "cta": "Next →"
    },
    {
        "title": "2️⃣ Mentor-Backed Mastery",
        "subtitle": "24/7 Doubt-Solving & Progress Calls",
        "media": """
        <lottie-player
          src="https://assets2.lottiefiles.com/packages/lf20_mentor.json"
          background="transparent" speed="1"
          style="width:100%; height:300px;" loop autoplay>
        </lottie-player>
        """,
        "text": "Connect instantly with top MDCAT mentors—whether it’s 3 AM or during your lunch break—we’re here to clarify and guide.",
        "cta": "Next →"
    },
    {
        "title": "3️⃣ Community & Gamification",
        "subtitle": "Peer Circles, Badges & Leaderboards",
        "media": """
        <lottie-player
          src="https://assets1.lottiefiles.com/packages/lf20_game.json"
          background="transparent" speed="1"
          style="width:100%; height:300px;" loop autoplay>
        </lottie-player>
        """,
        "text": "Join daily study pods, earn badges for every milestone, and climb the global leaderboard alongside fellow achievers.",
        "cta": "Next →"
    },
    {
        "title": "🎯 Your Mentr Quotient",
        "subtitle": "Holistic IQ · EQ · CQ · PQ Tracking",
        "media": None,
        "text": """
Calculate your growth across four dimensions:

- **IQ**: Concept mastery  
- **EQ**: Stress & focus management  
- **CQ**: Creative problem-solving  
- **PQ**: Practical, real-world application  
""",
        "cta": "Next →"
    },
    {
        "title": "🚨 Limited Seats Remaining",
        "subtitle": "FOMO Meets Opportunity",
        "media": None,
        "text": f"Only **{st.session_state.get('seats', __import__('random').randint(2,10))}** seats left at this price—secure yours before they vanish!",
        "cta": "Claim Your Spot"
    },
]

# Generate a random seats left once
if "seats" not in st.session_state:
    st.session_state.seats = __import__("random").randint(2,10)

# ── Rendering ───────────────────────────────────────────────────────────────────
slide = slides[st.session_state.step]

# Full-width slide container
st.markdown(f"<h1 style='text-align:center; color:#2DD0BE'>{slide['title']}</h1>", unsafe_allow_html=True)
if slide["subtitle"]:
    st.markdown(f"<p style='text-align:center; color:#B0C4DE; font-size:1.2rem'>{slide['subtitle']}</p>", unsafe_allow_html=True)

if slide["media"]:
    components.html(slide["media"], height=350)

st.markdown(f"<div style='padding:1rem 2rem; background:rgba(0,0,0,0.4); border-radius:1rem; margin:1rem-auto; max-width:800px;'>{slide['text']}</div>", unsafe_allow_html=True)

# Navigation buttons
col1, col2, col3 = st.columns([1,2,1])
with col1:
    if st.session_state.step > 0:
        st.button("← Back", on_click=prev_step)
with col3:
    label = slide["cta"]
    # Final slide’s CTA opens the form below
    if st.button(label, on_click=(next_step if st.session_state.step < len(slides)-1 else None)):
        pass

# Progress indicator
progress = (st.session_state.step + 1) / len(slides)
st.progress(progress)

# ── Final Registration Form ────────────────────────────────────────────────────
if st.session_state.step == len(slides) - 1:
    st.markdown("---")
    st.markdown("<h2 style='text-align:center; color:#2DD0BE;'>Ready to Begin Your Journey?</h2>", unsafe_allow_html=True)
    with st.form("register"):
        name  = st.text_input("Full Name")
        email = st.text_input("Email Address")
        join  = st.form_submit_button("🚀 Lock My Seat")
        if join:
            st.success("🎉 Welcome aboard — check your inbox for next steps!")
            st.balloons()

# ── Sidebar for Instant Help & Metrics ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 Live Impact")
    st.metric("Happy Mentees", "4.8K", "+25%")
    st.metric("Avg. Score ↑", "28%", "+12%")
    st.markdown("---")
    st.markdown("## ❓ Need Help?")
    st.markdown("[💬 WhatsApp Chat](https://wa.me/92300XXXXXXX)", unsafe_allow_html=True)
