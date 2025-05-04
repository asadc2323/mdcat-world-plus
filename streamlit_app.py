import streamlit as st
from datetime import datetime

# --- Streamlit Config ---
st.set_page_config(
    page_title="Mentr: MDCAT World Plus",
    page_icon="🚀",
    layout="wide"
)

# --- Custom Theme via CSS Override ---
st.markdown(
    """
    <style>
    .reportview-container, .css-1d391kg {background-color: #03162A;}
    .stButton>button {background-color: #2DD0BE; color: #03162A; border-radius: 0.5rem;}
    .stButton>button:hover {background-color: #24a89e;}
    .stMetricValue, .stMetricDelta {color: #FFFFFF;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Hero Section ---
with st.container():
    col1, col2 = st.columns([6,4])
    with col1:
        st.title("Welcome to MDCAT World (Plus)")
        st.write("Your all-in-one pathway from Freshers Session to MDCAT success.")
        st.metric(label="Students Joined Today", value="125+", delta="+20%")
        if st.button("Get Started"):
            st.balloons()
    with col2:
        st.image("https://via.placeholder.com/400x300.png?text=Hero+Image", use_container_width=True)

st.markdown("---")

# --- Features Section ---
st.header("Features")
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

# --- Testimonials Section ---
st.header("What Our Students Say")
testimonials = [
    ("Jumped from 60% → 85% in 8 weeks!", "— Ayesha Z."),
    ("Accountability nudges changed my study routine.", "— Hamza R."),
    ("Secured my dream MBBS seat!", "— Ali S.")
]
choice = st.selectbox(
    "Choose a testimonial:",
    options=list(range(len(testimonials))),
    format_func=lambda i: testimonials[i][1]
)
st.info(f"{testimonials[choice][0]}\n\n{testimonials[choice][1]}")

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

# --- Registration Form Section ---
st.header("Register Now")
with st.form(key="register_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    submitted = st.form_submit_button("Register Now")
    if submitted:
        st.success(f"Thanks {name}! We have received your registration.")
        st.balloons()

st.markdown("---")

# --- Footer ---
st.write("© 2025 Mentr. All rights reserved.")
