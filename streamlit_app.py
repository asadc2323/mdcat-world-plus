import streamlit as st  # TODO: Consider caching or loading external CSS to avoid re-injecting on every rerun


# Page configuration
st.set_page_config(
    page_title="The MDCAT World (Plus)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS for styling
# ⚠️ WARNING: Using Streamlit's auto-generated class selectors (e.g., .css-18e3th9) is brittle and may break on updates

st.markdown("""
<style>
/* Background and base font */
html, body, [data-testid='stAppViewContainer'] {
    background: #03162a;
    color: #e0e0e0;
}

/* Title Gradient Text */
h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 0.2em;
    background: linear-gradient(90deg, #2DD0BE, #12736A);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
h2 {
    font-size: 1.5rem;
    color: #2DD0BE;
    margin-bottom: 2rem;
}

/* Card Styles */
.card {
    background: rgba(255,255,255,0.05);
    padding: 1.5rem;
    border-left: 4px solid #2DD0BE;
    border-radius: 0.75rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
}
.card h3 {
    color: #2DD0BE;
    margin-bottom: 0.5em;
    font-size: 1.25rem;
}
.card ul {
    list-style: none;
    padding-left: 0;
}
.card ul li::before {
    content: "•";
    color: #2DD0BE;
    margin-right: 0.5em;
}

/* CTA Box */
.cta-box {
    background: linear-gradient(90deg, #2DD0BE, #12736A);
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    color: #fff;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    transition: background 0.3s ease;
}
.cta-box:hover {
    background: linear-gradient(90deg, #12736A, #2DD0BE);
}
.cta-box h3 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}
.cta-box p {
    font-size: 1.2rem;
}

/* Remove default padding */
.css-18e3th9 {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Main Title and Subtitle
st.markdown("<h1>The MDCAT World (Plus)</h1>", unsafe_allow_html=True)
st.markdown("<h2>Freshers Session - Till MDCAT</h2>", unsafe_allow_html=True)

# Three support cards in columns
# NOTE: Markup is duplicated; consider generating cards via a loop or helper function to DRY code

cols = st.columns(3, gap="large")

with cols[0]:
    st.markdown("<div class='card'>" +
                "<h3>Academic Support</h3>" +
                "<ul>" +
                "<li>Complete syllabus completion</li>" +
                "<li>Revision and Crash Test Session</li>" +
                "<li>Written explanation & Video Discussions</li>" +
                "<li>Last Week Plan before MDCAT</li>" +
                "</ul>" +
                "</div>", unsafe_allow_html=True)

with cols[1]:
    st.markdown("<div class='card'>" +
                "<h3>Mentorship</h3>" +
                "<ul>" +
                "<li>Complete Doubt Solving Support till MDCAT</li>" +
                "<li>One-on-one Mentorship till MDCAT</li>" +
                "<li>Daily Accountability till MDCAT</li>" +
                "</ul>" +
                "</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<div class='card'>" +
                "<h3>Post-MDCAT Support</h3>" +
                "<ul>" +
                "<li>Post-MDCAT admission support for MBBS Colleges</li>" +
                "<li>Prize Distribution Ceremony after MBBS Admissions</li>" +
                "<li>Mentr Ecosystem with MBBS professionals</li>" +
                "</ul>" +
                "</div>", unsafe_allow_html=True)

# Spacer
st.write("\n")

# CTA Box: WAIT!
st.markdown(
    "<div class='cta-box'>" +
    "<h3>WAIT!</h3>" +
    "<p>Read reviews before joining</p>" +
    "</div>",
    unsafe_allow_html=True
)
