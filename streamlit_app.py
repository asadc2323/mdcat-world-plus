import streamlit as st  # TODO: Consider caching or external CSS for performance

# Page configuration
st.set_page_config(
    page_title="The MDCAT World (Plus)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS for styling
# ⚙️ Move this to a static CSS file to avoid reinjecting on each run
st.markdown(
    """
    <style>
    /* Background and base font */
    html, body, [data-testid='stAppViewContainer'] {
        background: #03162a;
        color: #e0e0e0;
    }
    h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.2em;
        background: linear-gradient(90deg, #2DD0BE, #12736A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    h2 {
        font-size: 1.5rem;
        color: #2DD0BE;
        margin-bottom: 2rem;
    }
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
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title and Subtitle
st.markdown("<h1>The MDCAT World (Plus)</h1>", unsafe_allow_html=True)
st.markdown("<h2>Freshers Session - Till MDCAT</h2>", unsafe_allow_html=True)

# Three support cards in columns
cols = st.columns(3, gap="large")

card_contents = [
    ("Academic Support", [
        "Complete syllabus completion",
        "Revision and Crash Test Session",
        "Written explanation & Video Discussions",
        "Last Week Plan before MDCAT"
    ]),
    ("Mentorship", [
        "Complete Doubt Solving Support till MDCAT",
        "One-on-one Mentorship till MDCAT",
        "Daily Accountability till MDCAT"
    ]),
    ("Post-MDCAT Support", [
        "Post-MDCAT admission support for MBBS Colleges",
        "Prize Distribution Ceremony after MBBS Admissions",
        "Mentr Ecosystem with MBBS professionals"
    ])
]

for col, (title, items) in zip(cols, card_contents):
    with col:
        list_items = ''.join([f"<li>{i}</li>" for i in items])
        st.markdown(
            f"<div class='card'>"
            f"<h3>{title}</h3>"
            f"<ul>{list_items}</ul>"
            f"</div>",
            unsafe_allow_html=True
        )

# Spacer
# Fixed: Use a single markdown call for a line break
st.markdown("<br>", unsafe_allow_html=True)

# CTA Box: WAIT!
st.markdown(
    "<div class='cta-box'>"
    "<h3>WAIT!</h3>"
    "<p>Read reviews before joining</p>"
    "</div>",
    unsafe_allow_html=True
)
