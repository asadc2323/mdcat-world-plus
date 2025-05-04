import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import random, time

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mentr • MDCAT World",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Brand CSS Overrides ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif !important;
  background: #03162A;
  color: #FFF;
  margin: 0; padding: 0;
}
/* Hero */
.hero { text-align: center; padding: 4rem 1rem; }
.hero h1 { color: #2DD0BE; font-size: 3.5rem; margin-bottom: .5rem; }
.hero p  { color: #B0C4DE; font-size: 1.25rem; }
/* Glass cards */
.card {
  background: rgba(45,208,190,0.1);
  backdrop-filter: blur(8px);
  border-radius: 1rem;
  padding: 1.5rem;
  margin: 1rem 0;
  border: 1px solid rgba(45,208,190,0.2);
}
/* Toast */
.toast {
  position: fixed; bottom: 1.5rem; left: 50%; transform: translateX(-50%);
  background: rgba(45,208,190,0.9); color: #03162A; padding: .75rem 1.5rem;
  border-radius: 2rem; font-weight: 600; opacity: 0;
  transition: opacity .5s ease-in-out; z-index: 9999;
}
.toast.show { opacity: 1; }
/* Buttons */
.stButton>button {
  background-color: #2DD0BE !important;
  color: #03162A !important;
  font-weight: 600;
  padding: .75rem 1.5rem !important;
  border-radius: .75rem !important;
  border: none !important;
}
.stButton>button:hover {
  opacity: .9 !important;
}
/* Selectbox styling */
.stSelectbox > div>div { background: rgba(45,208,190,0.1); border-radius: .5rem; }
/* Progress bars */
.stProgress > div>div { background: #2DD0BE !important; }
/* Countdown */
.countdown { text-align: center; color: #2DD0BE; margin: 2rem 0; font-size: 1.25rem; }
/* Sidebar */
.stSidebar { background: #021022; padding: 1rem; }
.stSidebar h2 { color: #2DD0BE; }
.stSidebar a { color: #2DD0BE !important; font-weight: 600; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── 1. Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Welcome to Mentr’s MDCAT World</h1>
  <p>Re-building Education: Personalized, Holistic, Infinite. Increase Your Every Quotient!</p>
</div>
""", unsafe_allow_html=True)

# ── 2. Live Social-Proof Toasts ─────────────────────────────────────────────────
components.html("""
<div id="toast" class="toast"></div>
<script>
  const msgs = [
    "✨ Ayesha just joined from Karachi!",
    "🚀 Hamza locked in his seat!",
    "🌟 Sara from Lahore reserved her spot!"
  ];
  function showToast(){
    const el = document.getElementById("toast");
    el.innerText = msgs[Math.floor(Math.random()*msgs.length)];
    el.classList.add("show");
    setTimeout(()=> el.classList.remove("show"), 3000);
  }
  setInterval(showToast, 6000);
</script>
""", height=0)

# ── 3. Quick Mentr Mindset Check ─────────────────────────────────────────────────
with st.expander("🧠 Quick Mentr Mindset Check"):
    q1 = st.radio("Your study vibe is:", ["Focused marathon", "Short bursts", "Mostly distracted"])
    q2 = st.radio("When stuck on a problem, you:", ["Ask a mentor", "Re-read notes", "Skip ahead"])
    if st.button("🔍 Check My Mindset"):
        score = (q1=="Focused marathon")*50 + (q2=="Ask a mentor")*50
        verdict = "🔥 Top Mentr Mind" if score>=50 else "💡 Grow with Mentr"
        st.metric("Mentr Mindset", verdict)

# ── 4. Feature Explorer ─────────────────────────────────────────────────────────
features = [
    {
      "title":"Adaptive Learning Paths",
      "desc":"AI-driven plans that evolve with you.",
      "stat":("Avg. Score Gain","28%","+12%"),
      "lottie":"https://assets3.lottiefiles.com/packages/lf20_x9m3j9kv.json"
    },
    {
      "title":"Personalized Mentorship",
      "desc":"One-on-one guidance with proven mentors.",
      "stat":("Response Time","<5m","—"),
      "lottie":"https://assets2.lottiefiles.com/packages/lf20_mentor.json"
    },
    {
      "title":"Holistic Development",
      "desc":"EQ, stress-management & focus modules.",
      "stat":("EQ ↑","35%","+15%"),
      "lottie":"https://assets9.lottiefiles.com/packages/lf20_holistic.json"
    },
    {
      "title":"Community & Gamification",
      "desc":"Peer circles, badges & leaderboards.",
      "stat":("Active Users","4.8K","+20%"),
      "lottie":"https://assets1.lottiefiles.com/packages/lf20_game.json"
    },
]
st.markdown("---\n## 🚀 Explore Mentr’s Core Features")
choice = st.selectbox("", [f["title"] for f in features])
feat = next(f for f in features if f["title"]==choice)
c1,c2 = st.columns([1,2], gap="large")
with c1:
    components.html(f"""
      <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
      <lottie-player src="{feat['lottie']}" background="transparent" speed="1"
        style="width:100%;height:300px;" loop autoplay>
      </lottie-player>
    """, height=320)
with c2:
    st.subheader(feat["title"])
    st.write(feat["desc"])
    lbl, val, delta = feat["stat"]
    st.metric(lbl, val, delta)
    if val.endswith("%"): st.progress(int(val.strip("%")))

# ── 5. Impact Metrics & Scarcity ────────────────────────────────────────────────
st.markdown("---")
seats = random.randint(3,12)
st.markdown(f"<p style='text-align:center;color:#F45C48;'>🚨 Only <strong>{seats}</strong> seats left!</p>", unsafe_allow_html=True)
m1,m2,m3 = st.columns(3)
m1.metric("Avg. Score ↑","28%","+12%")
m2.metric("Happy Mentees","4.8K","+25%")
m3.metric("Mentr Quotient Avg.","72/100","+8")

# ── 6. Countdown to Next Live Q&A ──────────────────────────────────────────────
dl = datetime(2025,5,15,18,0,0)
diff = dl - datetime.now()
st.markdown(
    f"<div class='countdown'>⏳ Next Live Q&A in <strong>{diff.days}d {diff.seconds//3600}h {(diff.seconds%3600)//60}m</strong></div>",
    unsafe_allow_html=True
)

# ── 7. Final CTA & Free Guide ───────────────────────────────────────────────────
st.markdown("---\n<h2 style='text-align:center;color:#2DD0BE;'>Ready to Elevate Your MDCAT Journey?</h2>", unsafe_allow_html=True)
with st.form("register", clear_on_submit=True):
    name  = st.text_input("Full Name")
    email = st.text_input("Email Address")
    guide = st.checkbox("Send me the **FREE Mentr Vision Guide**", value=True)
    submit = st.form_submit_button("🚀 Join Mentr & Get Guide")
    if submit:
        st.success(f"Thank you, {name}! 📩 Check your email shortly.")
        st.balloons()
        if guide:
            pdf = b"%PDF-1.4...(your-guide-content here)"
            st.download_button("📥 Download Vision Guide", pdf, "Mentr_Vision_Guide.pdf", mime="application/pdf")

# ── 8. Persistent Sidebar Support ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ❓ Need Instant Help?")
    st.markdown("[💬 Chat on WhatsApp](https://wa.me/92300XXXXXXX)", unsafe_allow_html=True)
    st.markdown("---")
    st.metric("Active Users","4.8K","+20%")
    st.metric("Avg. Score ↑","28%","+12%")
