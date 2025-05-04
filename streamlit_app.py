import streamlit as st

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="The MDCAT World (Plus)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Centralized CSS (loaded once) ---
css = """
:root {
  --primary-start: #2DD0BE;
  --primary-end: #12736A;
  --accent: #8CFFE0;
  --dark-start: #03162A;
  --dark-end: #072A35;
}

/* Global Styles */
html, body, [data-testid='stAppViewContainer'] {
  background: linear-gradient(to bottom, var(--dark-start), var(--dark-end));
  color: #e0e0e0;
  font-family: 'Inter', sans-serif;
}

/* Hero Section */
.hero {
  position: relative;
  height: 100vh;
  display: grid;
  place-items: center;
  overflow: hidden;
}
.hero video.video-bg {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%; min-height: 100%;
  object-fit: cover;
  z-index: -2;
}
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  backdrop-filter: brightness(0.6) blur(4px);
  z-index: -1;
}
.hero-content {
  text-align: center;
  color: white;
  max-width: 800px;
}
.hero-content h1 {
  font-family: 'Poppins', sans-serif;
  font-size: clamp(2rem, 6vw, 4rem);
  background: linear-gradient(90deg, var(--primary-start), var(--primary-end), var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
}
.hero-content .cta {
  padding: 1rem 2rem;
  font-size: 1.25rem;
  font-weight: 600;
  color: #000;
  background: linear-gradient(90deg, var(--primary-start), var(--primary-end));
  border: none;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  transition: transform 0.3s ease;
}
.hero-content .cta:hover {
  transform: scale(1.05);
}

/* Support Cards */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin: 4rem 0;
}
.card {
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  flex: 1;
  min-width: 280px;
  max-width: 350px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.card:hover {
  transform: translateY(-8px) rotateX(3deg);
  box-shadow: 0 12px 48px rgba(0,0,0,0.6);
}
.card h3 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--primary-start);
  margin-bottom: 1rem;
}
.card ul {
  list-style: none;
  padding: 0;
}
.card li {
  margin-bottom: 0.75rem;
  padding-left: 1.5rem;
  position: relative;
}
.card li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-start);
}

/* CTA Banner */
.cta-banner {
  background: linear-gradient(90deg, var(--primary-start), var(--primary-end));
  padding: 3rem;
  border-radius: 1rem;
  text-align: center;
  color: #fff;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  transition: background 0.3s ease;
}
.cta-banner:hover {
  background: linear-gradient(90deg, var(--primary-end), var(--primary-start));
}
.cta-banner h3 { font-size: 2rem; margin-bottom: 0.5rem; }
.cta-banner p { font-size: 1.125rem; margin: 0; }

@media(max-width:768px) {
  .cards { flex-direction: column; align-items: center; }
}
"""

# Apply CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown(
    """
    <header class='hero'>
      <video class='video-bg' autoplay loop muted playsinline>
        <source src='assets/video-hero.mp4' type='video/mp4'/>
      </video>
      <div class='hero-content'>
        <h1>Rebuilding Education,<br/>One Student at a Time</h1>
        <button class='cta'>Apply Now &rarr;</button>
      </div>
    </header>
    """,
    unsafe_allow_html=True
)

# --- Support Cards Section ---
card_data = [
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

cols = st.columns(1 if st.session_state.get('mobile', False) else 3, gap='large')

for col, (title, items) in zip(cols, card_data):
    with col:
        list_items = ''.join(f"<li>{i}</li>" for i in items)
        st.markdown(
            f"<div class='card'><h3>{title}</h3><ul>{list_items}</ul></div>",
            unsafe_allow_html=True
        )

# --- Final CTA Banner ---
st.markdown(
    """
    <div class='cta-banner'>
      <h3>WAIT!</h3>
      <p>Read reviews before joining</p>
    </div>
    """,
    unsafe_allow_html=True
)
