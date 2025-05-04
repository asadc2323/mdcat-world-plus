# To run this prototype:
# pip install streamlit

import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# --- Page Configuration ---
st.set_page_config(
    page_title="Mentr: MDCAT World Plus",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS & Fonts ---
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css?family=Inter:400,600,700&display=swap" rel="stylesheet">
    <style>
      body, .css-18e3th9 { background-color: #03162A; color: #FFFFFF; font-family: 'Inter', sans-serif; margin:0; padding:0; }
      /* Hero */
      .hero { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; padding: 4rem 2rem; background: linear-gradient(135deg,#03162A,#002B3A,#2DD0BE); border-radius: 1rem; margin-bottom: 2rem; }
      .hero-text { max-width: 600px; }
      .hero-text h1 { font-size: 3rem; margin: 0; line-height: 1.2; }
      .hero-text .highlight { color: #FFFFFF; text-shadow: 0 0 8px rgba(255,255,255,0.5); }
      .hero-text p { font-size: 1.25rem; margin: 1rem 0; }
      /* Pillars */
      .pillars-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); gap: 24px; margin-bottom: 2rem; }
      .pillar-card { background: rgba(0,31,51,0.8); border-radius: 1rem; padding: 1.5rem; position: relative; overflow: hidden; opacity: 0; transform: translateY(20px); animation: fadeInUp 0.6s ease-out forwards; }
      .pillar-card:nth-child(1) { animation-delay: 0.1s; }
      .pillar-card:nth-child(2) { animation-delay: 0.2s; }
      .pillar-card:nth-child(3) { animation-delay: 0.3s; }
      .pillar-card::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: #2DD0BE; }
      .pillar-icon { width: 48px; margin-bottom: 1rem; }
      .pillar-card h3 { color: #2DD0BE; margin-bottom: 0.75rem; }
      .pillar-card ul { list-style: none; padding: 0; margin: 0; }
      .pillar-card ul li { margin-bottom: 0.75rem; line-height: 1.4; }
      @keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }
      /* Testimonial Ticker */
      .ticker { background: rgba(45,208,190,0.1); padding: 1rem; border-radius: 0.75rem; margin-bottom: 2rem; overflow: hidden; position: relative; }
      .ticker-content { display: inline-block; white-space: nowrap; animation: scroll 20s linear infinite; }
      .ticker-item { display: inline-block; padding-right: 4rem; font-size: 1rem; }
      @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
      /* Countdown */
      .countdown { text-align: center; font-size: 1.75rem; color: #2DD0BE; margin: 1rem 0; }
      /* Buttons */
      .btn-primary, .btn-secondary { display: inline-block; text-decoration: none; font-weight: 600; border-radius: 0.5rem; padding: 0.75rem 1.5rem; }
      .btn-primary { background: #2DD0BE; color: #03162A; margin-right: 1rem; }
      .btn-secondary { border: 2px solid #2DD0BE; color: #2DD0BE; }
      /* Sticky Join */
      @media (min-width:768px) { .join-btn { position: fixed; bottom:2rem; right:2rem; z-index:100; } }
      /* Mobile adjustments */
      @media (max-width:600px) {
        .hero { flex-direction: column-reverse; padding:2rem; }
        .hero-text h1 { font-size:2.25rem; }
        .pillar-card { min-width:80%; flex:0 0 auto; }
        .pillars-container { display:flex; overflow-x:auto; }
      }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Hero Section with Lottie Embed ---
st.markdown("<script src='https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js'></script>", unsafe_allow_html=True)
st.markdown("<div class='hero'>", unsafe_allow_html=True)
col1, col2 = st.columns([6,4], gap="large")
with col1:
    st.markdown("<div class='hero-text'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h1>Welcome to the <span class='highlight'>MDCAT World (Plus)</span></h1>
        <p>Your all-in-one path—from Freshers Session right <br/>up to MDCAT success.</p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    # Embed Lottie animation
    components.html(
        """
        <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_tfb3estd.json"  background="transparent"  speed="1"  style="width:100%; height:250px;"  loop  autoplay></lottie-player>
        """,
        height=300,
    )
st.markdown("</div>", unsafe_allow_html=True)

# --- Core Pillars ---
st.markdown("<div class='pillars-container'>", unsafe_allow_html=True)
pillars = [
    {"icon":"https://img.icons8.com/ios-filled/80/2DD0BE/book.png","title":"Academic Support","items":["Complete syllabus A–Z","Intensive revision & crash-tests","Concise written & video lessons","7-day zero-stress roadmap"]},
    {"icon":"https://img.icons8.com/ios-glyphs/80/2DD0BE/user-group-man-woman.png","title":"Mentorship","items":["24/7 doubt support","One-on-one progress calls","Daily accountability nudges"]},
    {"icon":"https://img.icons8.com/ios-filled/80/2DD0BE/medal.png","title":"Post-MDCAT Support","items":["MBBS admission roadmap","Celebrate success ceremonies","Exclusive MBBS pro network"]}
]
for p in pillars:
    st.markdown(f"""
    <div class='pillar-card'>
      <img src='{p['icon']}' class='pillar-icon'>
      <h3>{p['title']}</h3>
      <ul>
        {''.join([f"<li>{i}</li>" for i in p['items']])}
      </ul>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Testimonials Ticker ---
st.markdown(
    """
    <div class='ticker'>
      <div class='ticker-content'>
        <div class='ticker-item'>⭐⭐⭐⭐⭐ “Jumped 60% → 85% in 8 weeks!” — Ayesha Z.</div>
        <div class='ticker-item'>⭐⭐⭐⭐⭐ “Accountability nudges changed my routine.” — Hamza R.</div>
        <div class='ticker-item'>⭐⭐⭐⭐⭐ “Secured my dream MBBS seat!” — Ali S.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Live Countdown ---
target = datetime(2025,6,1,20,0)
now = datetime.now()
delta = target - now

days = delta.days
hours, rem = divmod(delta.seconds,3600)
minutes, _ = divmod(rem,60)

st.markdown(
    f"""
    <div class='countdown'>
      Next Live Q&A in: {days:02d}d : {hours:02d}h : {minutes:02d}m
    </div>
    """,
    unsafe_allow_html=True
)

# --- CTAs ---
st.markdown("<div style='text-align:center; margin-bottom:4rem;'>", unsafe_allow_html=True)
st.markdown("<a href='#join' class='btn-primary'>Join Mentr World →</a><a href='#reviews' class='btn-secondary'>Read Reviews →</a>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Sticky Join Button ---
st.markdown(
    """
    <a href='#join' class='join-btn'>Join Mentr World</a>
    """,
    unsafe_allow_html=True
)
