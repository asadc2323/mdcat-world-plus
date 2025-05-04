import streamlit as st
import datetime

# Page configuration
st.set_page_config(
    page_title="The MDCAT World Plus", layout="wide", initial_sidebar_state="collapsed"
)

# Inject custom CSS
st.markdown(
    """
    <style>
    /* Global background and font */
    .css-18e3th9 {background-color: #03162A; color: #FFFFFF;} /* Streamlit app main container */

    /* Header styles */
    .header {
        padding: 4rem 1rem;
        background: linear-gradient(135deg, #03162A, #002B3A, #2DD0BE);
        text-align: center;
        border-radius: 1rem;
        margin-bottom: 2rem;
    }
    .header h2 {
        font-size: 3rem;
        margin: 0;
    }
    .highlight {
        color: #2DD0BE;
    }
    .subhead {
        font-size: 1.25rem;
        margin-top: 0.5rem;
    }

    /* Pillar card grid */
    .pillars-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    .pillar-card {
        background: rgba(0, 31, 51, 0.6);
        border-radius: 1rem;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
        min-height: 240px;
    }
    .pillar-card::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: #2DD0BE;
        border-radius: 0 5px 5px 0;
    }
    .pillar-icon {
        width: 40px;
        margin-bottom: 1rem;
    }
    .pillar-card h3 {
        color: #2DD0BE;
        margin-bottom: 1rem;
    }
    .pillar-card ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .pillar-card ul li {
        margin-bottom: 0.75rem;
    }

    /* Testimonial ticker */
    .testimonial-ticker {
        background: rgba(45, 208, 190, 0.1);
        padding: 1rem;
        border-radius: 0.75rem;
        overflow: hidden;
        white-space: nowrap;
        margin-bottom: 2rem;
    }
    .testimonial-ticker marquee {
        font-size: 1rem;
        color: #FFFFFF;
    }

    /* Wait CTA */
    .wait-cta {
        text-align: center;
        background: rgba(0, 31, 51, 0.5);
        padding: 2rem 1rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
    }
    .wait-cta h3 {
        margin: 0;
        font-size: 2rem;
        color: #FFFFFF;
    }
    .countdown {
        font-size: 1.75rem;
        color: #2DD0BE;
        margin: 0.5rem 0 1rem;
    }
    .btn-secondary {
        display: inline-block;
        color: #2DD0BE;
        text-decoration: none;
        border: 2px solid #2DD0BE;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown(
    """
    <div class="header">
        <h2>The <span class="highlight">MDCAT World<br>(Plus)</span></h2>
        <p class="subhead">Freshers Session — Till MDCAT</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Pillars Grid
st.markdown('<div class="pillars-grid">', unsafe_allow_html=True)

# Academic Support Card
st.markdown(
    """
    <div class="pillar-card">
        <img src="https://via.placeholder.com/40" class="pillar-icon" alt="Academic Support">
        <h3>Academic Support</h3>
        <ul>
            <li>Complete syllabus completion</li>
            <li>Revision & crash-test sessions</li>
            <li>Written explanations & video discussions</li>
            <li>Last-week, “zero-stress” plan</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Mentorship Card
st.markdown(
    """
    <div class="pillar-card">
        <img src="https://via.placeholder.com/40" class="pillar-icon" alt="Mentorship">
        <h3>Mentorship</h3>
        <ul>
            <li>24/7 doubt-solving till MDCAT</li>
            <li>One-on-one progress calls</li>
            <li>Daily accountability check-ins</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Post-MDCAT Support Card
st.markdown(
    """
    <div class="pillar-card">
        <img src="https://via.placeholder.com/40" class="pillar-icon" alt="Post-MDCAT Support">
        <h3>Post-MDCAT Support</h3>
        <ul>
            <li>MBBS admission roadmap</li>
            <li>Prize distribution ceremony</li>
            <li>“Mentor Club” with MBBS pros</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)

# Testimonial Ticker
st.markdown(
    """
    <div class="testimonial-ticker">
        <marquee behavior="scroll" direction="left">
            ⭐⭐⭐⭐⭐ “I went from 60% to 85% in just 8 weeks!” — Ayesha Z.
            &nbsp;&nbsp;
            ⭐⭐⭐⭐⭐ “Mentr’s accountability check-ins kept me on track.” — Hamza R.
            &nbsp;&nbsp;
            ⭐⭐⭐⭐⭐ “I got into my dream MBBS college!” — Ali S.
        </marquee>
    </div>
    """,
    unsafe_allow_html=True,
)

# Countdown CTA
# Set your target Q&A datetime here
target = datetime.datetime(2025, 6, 1, 20, 0)
now = datetime.datetime.now()
delta = target - now

days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.markdown(
    f"""
    <div class="wait-cta">
        <h3>Wait! Don’t miss our next live Q&A</h3>
        <div class="countdown">{days:02d}d : {hours:02d}h : {minutes:02d}m</div>
        <a href="#reviews" class="btn-secondary">Read reviews before joining</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sticky Join Button (Desktop)
sticky = """
<style>
@media (min-width: 768px) {
  .join-btn {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background: #2DD0BE;
    color: #03162A;
    padding: 1rem 1.5rem;
    border-radius: 0.75rem;
    font-weight: bold;
    text-decoration: none;
  }
}
</style>
<a href="#join" class="join-btn">Join Mentr World →</a>
"""
st.markdown(sticky, unsafe_allow_html=True)
