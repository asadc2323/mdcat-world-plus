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

# ── Brand & Layout CSS ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif !important;
  background: #03162A;
  color: #FFF;
  margin:0; padding:0;
}
/* Hero */
.hero { text-align:center; padding:3rem 1rem; }
.hero h1 { color:#2DD0BE; font-size:3rem; margin-bottom:.3rem; }
.hero p  { color:#B0C4DE; font-size:1.2rem; }
/* Toast */
.toast {
  position: fixed; bottom:1rem; left:50%; transform:translateX(-50%);
  background: rgba(0,0,0,0.75); color:#FFF; padding:.75rem 1.5rem;
  border-radius:1rem; opacity:0; transition:opacity .5s ease-in-out;
  z-index:9999;
}
.toast.show { opacity:1; }
/* Spin section */
.spin-btn > button { background:#2DD0BE; color:#03162A; font-weight:600; padding:.75rem 1.5rem; border-radius:.5rem; border:none; }
.spin-btn > button:hover { opacity:.9; }
/* Feature selector */
.stSelectbox > div>div { background: rgba(45,208,190,0.1); border-radius:0.5rem; }
/* Progress bars */
.stProgress > div > div { background: #2DD0BE !important; }
/* Countdown */
.countdown { text-align:center; color:#2DD0BE; margin:2rem 0; font-size:1.5rem; }
/* CTA buttons */
.cta-btn button { background:#2DD0BE; color:#03162A; font-weight:600; padding:.75rem 1.5rem; border-radius:.5rem; border:none; }
.cta-btn button:hover { opacity:.9; }
/* Sidebar */
.stSidebar { background:#021022; padding:1rem; }
</style>
""", unsafe_allow_html=True)

# ── 1. Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Welcome to Mentr’s MDCAT World</h1>
  <p>Re-building Education: Personalized, Holistic, Boundless. Increase Your Every Quotient!</p>
</div>
""", unsafe_allow_html=True)

# ── 2. Live Social Proof Toasts ─────────────────────────────────────────────────
components.html("""
<div id="toast" class="toast"></div>
<script>
  const messages = [
    "Ali from Lahore just joined!",
    "Sara from Karachi reserved her seat!",
    "Hamza from Islamabad is on board!",
    "Usman from Peshawar locked in MDCAT World!"
  ];
  function showToast() {
    const msg = messages[Math.floor(Math.random()*messages.length)];
    const el = document.getElementById("toast");
    el.innerText = msg; el.classList.add("show");
    setTimeout(()=>el.classList.remove("show"), 3000);
  }
  setInterval(showToast, 6000);
</script>
""", height=0)

# ── 3. Gamified Spin-the-Wheel Reward ─────────────────────────────────────────────
st.markdown("## 🎡 Spin the Wheel & Claim Your Early-Bird Reward")
if "reward" not in st.session_state:
    if st.button("Spin & Reveal", key="spin", help="Win a discount or bonus!"):
        with st.spinner("Spinning the wheel..."):
            time.sleep(2)
        st.session_state.reward = random.choice([
            "10% off tuition",
            "Free 1-on-1 mentor session",
            "Exclusive MDCAT Shortcut Guide",
            "Priority access to live Q&A"
        ])
if "reward" in st.session_state:
    st.success(f"🎉 Congratulations! You won: **{st.session_state.reward}**")

# ── 4. Core Feature Explorer ────────────────────────────────────────────────────
features = [
    {"title":"Adaptive Learning Paths","desc":"AI crafts your minute-by-minute study plan.","stat":("Avg. Score Gain","28%","+12%"),"lottie":"https://assets3.lottiefiles.com/packages/lf20_x9m3j9kv.json"},
    {"title":"24/7 Mentor Chat","desc":"Top MDCAT mentors, any time you need.","stat":("Avg. Response Time","2m 15s","—"),"lottie":"https://assets2.lottiefiles.com/packages/lf20_mentor.json"},
    {"title":"Gamified Progress","desc":"Earn badges, climb leaderboards.","stat":("Active Users","3.2K","+18%"),"lottie":"https://assets1.lottiefiles.com/packages/lf20_game.json"}
]
st.markdown("---\n## 🔍 Explore Our Core Features")
choice = st.selectbox("", [f["title"] for f in features], index=0)
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
    lbl,val,delta = feat["stat"]
    st.metric(lbl, val, delta)
    if val.endswith("%"): st.progress(int(val.strip("%")))

# ── 5. Impact Metrics & Countdown ───────────────────────────────────────────────
seats_left = random.randint(2,10)
st.markdown(f"<p style='text-align:center;color:#F45C48;'>🚨 Only **{seats_left}** seats left at this rate!</p>", unsafe_allow_html=True)
m1,m2,m3 = st.columns(3)
m1.metric("Avg. Score ↑","28%","+12%")
m2.metric("Happy Mentees","4.8K","+25%")
m3.metric("Mentor Satisfaction","4.9/5","+0.2")
deadline = datetime(2025,5,15,18,0,0)
d = deadline - datetime.now()
st.markdown(f"<div class='countdown'>⏳ Next Live Q&A in <strong>{d.days}d {(d.seconds//3600)}h {((d.seconds%3600)//60)}m</strong></div>", unsafe_allow_html=True)

# ── 6. Registration Form (with Spin Reward) ────────────────────────────────────
st.markdown("---\n<h2 style='text-align:center;color:#2DD0BE;'>Ready to Level Up?</h2>", unsafe_allow_html=True)
with st.form("register", clear_on_submit=True):
    name  = st.text_input("Full Name")
    email = st.text_input("Email Address")
    if "reward" in st.session_state:
        st.write(f"**Your Reward:** {st.session_state.reward}")
    submit = st.form_submit_button("🚀 Claim My Spot")
    if submit:
        st.success(f"Thank you, {name}! 🎉 Check your email for details.")
        st.balloons()

# ── 7. 24/7 Chat Widget ─────────────────────────────────────────────────────────
components.html("""
<script type="text/javascript">
window.$crisp=[];window.CRISP_WEBSITE_ID="YOUR_CRISP_ID_HERE";
(function(){ d=document; s=d.createElement("script");
  s.src="https://client.crisp.chat/l.js"; s.async=1;
  d.getElementsByTagName("head")[0].appendChild(s);
})();
</script>
""", height=0)
st.sidebar.markdown("## ❓ Need Help?  \n[💬 Chat on WhatsApp](https://wa.me/92300XXXXXXX)", unsafe_allow_html=True)
