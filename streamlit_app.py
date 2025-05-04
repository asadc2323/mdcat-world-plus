import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import random, time

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mentr • Top G MDCAT World",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS (Black & Gold) ─────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&display=swap');
html, body, [class*="css"] {
  font-family: 'Oswald', sans-serif !important;
  background: #000; color: #fff; margin:0; padding:0;
}
h1, h2, h3 { margin: .5rem 0; }
h1 { color: #FFD700; font-size: 3rem; text-align: center; }
h2 { color: #CCC; font-size: 1.5rem; text-align: center; }
.topg-btn button {
  background: #FFD700; color: #000; font-weight:700;
  padding: .75rem 1.5rem; border:none; border-radius:.3rem;
  transition: transform .2s ease;
}
.topg-btn button:hover { transform: scale(1.05); }
.card {
  background: rgba(255,255,255,0.05); border: 2px solid #FFD700;
  border-radius: .5rem; padding: 1.5rem; margin:1rem 0;
}
.challenge .stRadio > div > label { color: #FFD700; }
.countdown { text-align:center; color:#FFD700; margin:2rem 0; font-size:1.2rem;}
.toast {
  position: fixed; bottom:1rem; left:50%; transform:translateX(-50%);
  background: rgba(255,215,0,0.9); color:#000; padding:.75rem 1rem;
  border-radius:1rem; opacity:0; transition: opacity .5s;
  font-weight:700; z-index:9999;
}
.toast.show { opacity:1; }
.stSidebar { background:#111; padding:1rem; }
.sidebar-content a { color:#FFD700; text-decoration:none; font-weight:700; }
</style>
""", unsafe_allow_html=True)

# ── Typewriter Hero ───────────────────────────────────────────────────────────────
components.html("""
<div style="text-align:center; margin:2rem 0;">
  <h1 id="typewriter"></h1>
</div>
<script>
  const txt = "ARE YOU A TOP G?";
  let i=0;
  function type() {
    if(i<txt.length){
      document.getElementById("typewriter").innerHTML += txt.charAt(i++);
      setTimeout(type, 100);
    }
  }
  type();
</script>
""", height=120)

st.markdown("<h2>Stop Whining. Start Winning. This Is High-Stakes MDCAT Prep for the Elite.</h2>", unsafe_allow_html=True)

# ── Live Toasts (Social Proof) ──────────────────────────────────────────────────
components.html("""
<div id="toast" class="toast"></div>
<script>
  const msgs = ["🔥 Ali from Lahore just joined!", "🚀 Sara from Karachi locked her seat!", "💎 Hamza from Islamabad is in the Top G circle!"];
  function showToast(){
    const el=document.getElementById("toast");
    el.textContent=msgs[Math.floor(Math.random()*msgs.length)];
    el.classList.add("show");
    setTimeout(()=>el.classList.remove("show"),3000);
  }
  setInterval(showToast, 5000);
</script>
""", height=0)

# ── “Top G Challenge” Quiz ───────────────────────────────────────────────────────
st.markdown("---\n<h2 style='text-align:center;color:#FFD700;'>🛡️ Top G Discipline Test</h2>", unsafe_allow_html=True)
with st.form("challenge", clear_on_submit=True):
    st.markdown("**Only serious grinders play.** Answer these to prove your mindset:")
    q1 = st.radio("1) My typical study session is:", [
        "A) 30 min then break", 
        "B) 2 hrs no distractions", 
        "C) I don’t study regularly",
    ])
    q2 = st.radio("2) When I fail a mock, I:", [
        "A) Get angry & redo", 
        "B) Blame external factors", 
        "C) Move on quickly",
    ])
    q3 = st.radio("3) My late-night study strategy:", [
        "A) Full focus till dawn", 
        "B) Quick glance at notes", 
        "C) I sleep early",
    ])
    sub = st.form_submit_button("🔒 Prove It")
    if sub:
        score = ({"A) 30 min then break":0,"B) 2 hrs no distractions":1,"C) I don’t study regularly":0}[q1] +
                 {"A) Get angry & redo":1,"B) Blame external factors":0,"C) Move on quickly":0}[q2] +
                 {"A) Full focus till dawn":1,"B) Quick glance at notes":0,"C) I sleep early":0}[q3])
        if score >= 2:
            st.success("💪 You passed the Top G mindset test. Welcome to the circle.")
            st.session_state.topg = True
        else:
            st.error("❌ Not quite there. Build discipline & retry.")

# ── Core Features (Alpha Cards) ─────────────────────────────────────────────────
features = [
    {"title":"Adaptive Paths","desc":"AI-powered plans that evolve as you level up."},
    {"title":"24/7 Mentor Backing","desc":"Elite mentors at your beck & call."},
    {"title":"Gamified Mastery","desc":"Badges, Leaderboards & Battle-tested community."},
]
st.markdown("---\n<h2 class='section-title' style='color:#FFD700;'>🏆 Core Arsenal</h2>", unsafe_allow_html=True)
cols = st.columns(3, gap="large")
for col, f in zip(cols, features):
    with col:
        st.markdown(f"<div class='card'><h3>{f['title']}</h3><p>{f['desc']}</p></div>", unsafe_allow_html=True)

# ── Scarcity & Countdown ─────────────────────────────────────────────────────────
seats = st.session_state.get("seats_left", random.randint(3,12))
st.session_state.seats_left = seats
st.markdown(f"<p style='text-align:center;color:#FF4500;'>🚨 {seats} Top G seats left!</p>", unsafe_allow_html=True)

deadline = datetime(2025,5,15,18,0,0)
diff = deadline - datetime.now()
st.markdown(
    f"<div class='countdown'>⏰ Next Elite Q&A in <strong>{diff.days}d {diff.seconds//3600}h {(diff.seconds%3600)//60}m</strong></div>",
    unsafe_allow_html=True
)

# ── Final Alpha CTA ──────────────────────────────────────────────────────────────
st.markdown("---\n<h2 style='text-align:center;color:#FFD700;'>Ready to Dominate?</h2>", unsafe_allow_html=True)
with st.container():
    if st.session_state.get("topg", False):
        st.markdown("<p style='text-align:center;'>Your Top G reward: <strong>Free 1-on-1 Mentor Session</strong></p>", unsafe_allow_html=True)
    colA, colB, colC = st.columns([1,2,1])
    with colB:
        if st.button("🚀 Join the Top G MDCAT Circle", key="join", help="Lock in your elite spot"):
            st.success("🎉 You’re In! Check your email for VIP access.")
            st.balloons()

# ── Sidebar Help & Metrics ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 Live Impact")
    st.metric("Avg. Score ↑","28%","+12%")
    st.metric("Happy Mentees","4.8K","+25%")
    st.markdown("---")
    st.markdown("## ❓ Instant Support")
    st.markdown("[💬 WhatsApp Chat](https://wa.me/92300XXXXXXX)", unsafe_allow_html=True)
