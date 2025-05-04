import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timedelta

# --- Page Configuration & Theming ---
st.set_page_config(page_title="Mentr Landing", layout="wide")
st.markdown(
    """<style>
    :root {
        --primary-color: #2DD0BE;
        --bg-color: #03162A;
        --card-bg: rgba(45, 208, 190, 0.1);
    }
    body, .stApp {
        background-color: var(--bg-color);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    .metric-container {
        background: var(--card-bg);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .section-header {
        font-size: 2.2rem;
        margin: 2rem 0 1rem;
        color: var(--primary-color);
        text-align: center;
    }
    /* Flip-card styles */
    .flip-container { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem; }
    .flip-card { background: transparent; width: 220px; height: 260px; perspective: 1000px; }
    .flip-card-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }
    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; border-radius: 12px; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 1rem; }
    .flip-card-front { background-color: var(--primary-color); color: var(--bg-color); }
    .flip-card-back { background-color: var(--bg-color); color: white; transform: rotateY(180deg); border: 2px solid var(--primary-color); }
    .flip-card-front h4, .flip-card-back p { margin: 0.5rem 0; }
    </style>""",
    unsafe_allow_html=True
)

# --- Hero Section ---
st.title("Welcome to Mentr")
st.subheader("Re-building Education: From Freshers to MDCAT Success")
st.write("Join 1,000+ students who have skyrocketed their scores with our immersive, mentorship-driven platform.")
st.markdown("---")

# --- Real-Time Metrics ---
st.markdown("### Key Performance Metrics", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg. Score Increase", "30%", delta="+30%")
with col2:
    st.metric("Doubts Resolved / Day", "1,200")
with col3:
    st.metric("Completion Rate", "85%", delta="+5%")
st.markdown("---")

# --- Feature Flip-Card Showcase ---
st.markdown("### Our Core Features", unsafe_allow_html=True)

flip_card_html = r'''
<div class="flip-container">
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <h4>Academic Support</h4>
        <p>Complete syllabus mastery</p>
      </div>
      <div class="flip-card-back">
        <p>Before: 50% avg. scores</p>
        <p>After: 80% avg. scores</p>
        <p>⭐⭐⭐⭐⭐</p>
      </div>
    </div>
  </div>
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <h4>Mentorship</h4>
        <p>24/7 doubt-solving</p>
      </div>
      <div class="flip-card-back">
        <p>Before: 2 doubts/day</p>
        <p>After: 20 solved/day</p>
        <p>⭐⭐⭐⭐⭐</p>
      </div>
    </div>
  </div>
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <h4>Post-MDCAT Support</h4>
        <p>Admissions roadmap</p>
      </div>
      <div class="flip-card-back">
        <p>Before: 10% admission rate</p>
        <p>After: 70% admission rate</p>
        <p>⭐⭐⭐⭐⭐</p>
      </div>
    </div>
  </div>
</div>
'''
components.html(flip_card_html, height=340)

# --- Registration CTA Form ---
st.markdown("---")
st.markdown("### Ready to transform your MDCAT journey?", unsafe_allow_html=True)
with st.form("register_form"):
    name  = st.text_input("Full Name")
    email = st.text_input("Email Address")
    submit = st.form_submit_button("Join Mentr World")
    if submit:
        st.success("You're registered! 🎉")
        st.balloons()

# --- Footer / Contact ---
st.markdown("---")
st.write("Have questions? [Chat with us on WhatsApp](https://wa.me/1234567890)")
