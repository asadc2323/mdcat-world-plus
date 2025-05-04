import streamlit as st
from datetime import datetime

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
      body, .css-18e3th9 { background-color: #03162A; color: #FFFFFF; font-family: 'Inter', sans-serif; }
      /* Header */
      .header { text-align: center; padding: 4rem 1rem; background: linear-gradient(135deg,#03162A,#002B3A,#2DD0BE); border-radius: 1rem; margin-bottom: 2rem; }
      .header h1 { font-size: 3rem; margin: 0; }
      .header .highlight { color: #2DD0BE; }
      .header p { font-size: 1.25rem; margin-top: 0.5rem; }
      /* Pillar Cards */
      .pillar h3 { color: #2DD0BE; margin-bottom: 0.5rem; }
      /* Testimonial Ticker */
      .ticker { display: flex; overflow: hidden; white-space: nowrap; margin-bottom: 2rem; }
      .ticker-item { padding-right: 4rem; font-size: 1rem; }
      @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
      .ticker { animation: scroll 20s linear infinite; }
      /* Countdown */
      .countdown { text-align: center; font-size: 1.75rem; color: #2DD0BE; margin: 1rem 0; }
      /* Buttons */
      .btn-primary { background: #2DD0BE; color: #03162A; padding: 0.75rem 1.5rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; }
      .btn-secondary { border: 2px solid #2DD0BE; color: #2DD0BE; padding: 0.75rem 1.5rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; }
      /* Sticky Join */
      @media (min-width: 768px) {
        .join-btn { position: fixed; bottom: 2rem; right: 2rem; z-index: 100; }
      }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Hero Header ---
st.markdown(
    """
    <div class="header">
      <h1>The <span class="highlight">MDCAT World (Plus)</span></h1>
      <p>Freshers Session — Till MDCAT</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Three Core Pillars ---
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("<div class='pillar'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios-filled/50/2DD0BE/book.png", width=40)
    st.markdown("### Academic Support")
    st.markdown(
        """
- Complete syllabus from A–Z  
- Intensive revision & crash-test sessions  
- Concise written & video discussions  
- 7-day “zero-stress” final plan
        """
    )
    with st.expander("More details"):
        st.write("Our subject-matter experts guide you step-by-step, ensuring mastery and confidence before the big day.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='pillar'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios-glyphs/50/2DD0BE/user-group-man-woman.png", width=40)
    st.markdown("### Mentorship")
    st.markdown(
        """
- 24/7 doubt-solving until exam day  
- One-on-one progress check-ins  
- Daily accountability reminders
        """
    )
    with st.expander("More details"):
        st.write("Personalized mentorship plans and data-driven feedback keep you on track every day.")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='pillar'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios-filled/50/2DD0BE/medal.png", width=40)
    st.markdown("### Post-MDCAT Support")
    st.markdown(
        """
- MBBS admission roadmap & guidance  
- Celebrate success at our prize ceremony  
- Exclusive access to MBBS professional network
        """
    )
    with st.expander("More details"):
        st.write("Stay connected with mentors and peers as you transition into medical school and beyond.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Testimonial Ticker ---
st.markdown(
    """
    <div class="ticker">
      <div class="ticker-item">⭐⭐⭐⭐⭐ “Jumped from 60% to 85% in 8 weeks!” — Ayesha Z.</div>
      <div class="ticker-item">⭐⭐⭐⭐⭐ “Accountability check-ins saved my study routine.” — Hamza R.</div>
      <div class="ticker-item">⭐⭐⭐⭐⭐ “Landed my dream MBBS seat!” — Ali S.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Live Countdown to Q&A ---
target = datetime(2025, 6, 1, 20, 0)
now = datetime.now()
delta = target - now

days = delta.days
hours, rem = divmod(delta.seconds, 3600)
minutes, _ = divmod(rem, 60)

st.markdown(
    f"""
    <div class="countdown">
      Next Live Q&A in: {days:02d}d : {hours:02d}h : {minutes:02d}m
    </div>
    """,
    unsafe_allow_html=True
)

# --- Primary CTAs ---
cta_col, rev_col = st.columns([2,1])

with cta_col:
    st.markdown(
        "<a href='#join' class='btn-primary'>Join Mentr World →</a>",
        unsafe_allow_html=True
    )
with rev_col:
    st.markdown(
        "<a href='#reviews' class='btn-secondary'>Read Reviews →</a>",
        unsafe_allow_html=True
    )

# --- Sticky Join Button ---
st.markdown(
    """
    <style>
      .join-btn { background: #2DD0BE; color: #03162A; padding: 0.75rem 1.25rem; border-radius: 0.5rem; font-weight: 600; text-decoration: none; }
    </style>
    <a href='#join' class='join-btn'>Join Mentr World</a>
    """,
    unsafe_allow_html=True
)
