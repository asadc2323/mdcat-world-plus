import streamlit as st
from datetime import datetime

# --- Streamlit Config ---
st.set_page_config(
    page_title="Mentr: MDCAT World Plus",
    page_icon="🚀",
    layout="wide"
)

# --- Theme CSS Overrides ---
st.markdown(
    """
    <style>
    .reportview-container, .css-1d391kg {background-color: #03162A;}
    .stButton>button {background-color: #2DD0BE; color: #03162A; border-radius: 0.5rem;}
    .stButton>button:hover {background-color: #24a89e;}
    .stMetricValue, .stMetricDelta {color: #FFFFFF;}
    .stDownloadButton>button {background-color: #2DD0BE; color: #03162A; border-radius: 0.5rem; margin-top: 1rem;}
    .stDownloadButton>button:hover {background-color: #24a89e;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Hero Section ---
with st.container():
    col1, col2 = st.columns((6,4))
    with col1:
        st.title("Welcome to MDCAT World (Plus)")
        st.write("Your all-in-one pathway from Freshers Session to MDCAT success.")
        st.metric(label="Students Joined Today", value="125+", delta="+20%")
        if st.button("Get Started"):
            st.balloons()
    with col2:
        st.image(
            "https://via.placeholder.com/400x300.png?text=Mentr+MDCAT+World+Hero",
            use_container_width=True
        )

st.markdown("---")

# --- Introduction Video ---
st.header("Why Choose Mentr?")
st.write("Watch this quick overview to see how we transform your MDCAT preparation:")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with your actual promo video

# --- Free Guide Download ---
st.subheader("Get Your Free MDCAT Study Guide")
guide_text = """
MDCAT Mastery Guide\n\n
• Proven strategies for high scores\n
• Time management tips\n
• Common pitfalls & how to avoid them\n"""
st.download_button(
    label="Download Free Guide",
    data=guide_text,
    file_name="MDCAT_Study_Guide.txt",
    mime="text/plain"
)

st.markdown("---")

# --- Features Section ---
st.header("Our Core Features")
features = [
    ("📚 Academic Support", [
        "Complete syllabus A–Z",
        "Intensive revision & crash-tests",
        "Concise written & video lessons",
        "7-day zero-stress roadmap"
    ]),
    ("👥 Mentorship", [
        "24/7 doubt support",
        "One-on-one progress calls",
        "Daily accountability nudges"
    ]),
    ("🏆 Post-MDCAT Support", [
        "MBBS admission roadmap",
        "Celebrate success ceremonies",
        "Exclusive MBBS pro network"
    ])
]
cols = st.columns(3)
for idx, (title, items) in enumerate(features):
    with cols[idx]:
        st.subheader(title)
        for item in items:
            st.write(f"- {item}")
        st.progress((idx+1)/len(features))

st.markdown("---")

# --- Interactive Testimonials ---
st.header("What Our Students Say")
testimonials = [
    ("Jumped from 60% → 85% in 8 weeks!", "— Ayesha Z."),
    ("Accountability nudges changed my routine.", "— Hamza R."),
    ("Secured my dream MBBS seat!", "— Ali S.")
]
with st.expander("See all testimonials", expanded=False):
    for quote, author in testimonials:
        st.info(f"“{quote}”  \n{author}")

st.markdown("---")

# --- Live Countdown Section ---
st.header("Next Live Q&A")
countdown_placeholder = st.empty()
def update_countdown():
    end = datetime(2025, 6, 1, 20, 0)
    now = datetime.now()
    diff = end - now
    if diff.total_seconds() <= 0:
        countdown_placeholder.success("🔴 Live Q&A is now! 🔴")
    else:
        days = diff.days
        hours, rem = divmod(diff.seconds, 3600)
        minutes, _ = divmod(rem, 60)
        countdown_placeholder.write(f"Next Live Q&A in: **{days}d {hours}h {minutes}m**")
update_countdown()

st.markdown("---")

# --- FAQs Expanders ---
st.header("Frequently Asked Questions")
faqs = [
    ("How do I join the Freshers Session?", "Simply click 'Get Started', fill out the form, and we’ll reach out to you via email and phone."),
    ("What’s included in the mentorship?", "Daily check-ins, one-on-one calls, and 24/7 doubt support until the exam day. "),
    ("Is there a money-back guarantee?", "Yes! If you don't see improvement in 30 days, we'll refund your fee—no questions asked.")
]
for q, a in faqs:
    with st.expander(q):
        st.write(a)

st.markdown("---")

# --- Team Showcase ---
st.header("Meet Our Mentors")
names = ["Dr. Sara Zaka", "Mr. Hamza Ali", "Ms. Ayesha Khan"]
roles = ["Batch Head, English", "Senior Mentor, Biology", "Lead Mentor, Chemistry"]
cols = st.columns(3)
for idx, (n, r) in enumerate(zip(names, roles)):
    with cols[idx]:
        st.image("https://via.placeholder.com/150", caption=f"{n}\n{r}")
        st.write(r)

st.markdown("---")

# --- Contact & Chat CTA ---
st.write("**Need help?**  ")
st.markdown("[Chat with us on WhatsApp](https://wa.me/1234567890?text=Hi%20Mentr%2C%20I%20need%20assistance)")

st.markdown("---")

# --- Registration Form Section ---
st.header("Register Now")
with st.form(key="register_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    referral = st.text_input("Referral Code (if any)")
    submitted = st.form_submit_button("Register Now")
    if submitted:
        st.success(f"Thanks {name}! We have received your registration.")
        st.balloons()

st.markdown("---")

# --- Footer ---
st.write("© 2025 Mentr. All rights reserved.")
