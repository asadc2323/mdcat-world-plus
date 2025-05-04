import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# --- Streamlit Config ---
st.set_page_config(page_title="Mentr Landing Page", layout="wide")

# --- Full Landing Page HTML/CSS ---
landing_page_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mentr: MDCAT World Plus</title>
  <style>
    /* Reset & Base */
    *, *::before, *::after { box-sizing: border-box; margin:0; padding:0; }
    html, body { height:100%; font-family:'Inter', sans-serif; background:#03162A; color:#FFF; }
    a { text-decoration:none; }
    img { max-width:100%; display:block; }
    /* Container */
    .container { width:90%; max-width:1200px; margin:0 auto; padding:2rem 0; }
    /* Navbar */
    nav { position:fixed; top:0; width:100%; background: rgba(0,0,0,0.6); backdrop-filter:blur(8px); z-index:100; }
    .nav-inner { display:flex; justify-content:space-between; align-items:center; padding:1rem 2rem; }
    .logo { font-weight:700; font-size:1.5rem; color:#2DD0BE; }
    .nav-links { display:flex; gap:2rem; }
    .nav-links a { color:#EEE; font-weight:500; transition:color .3s; }
    .nav-links a:hover { color:#2DD0BE; }
    /* Hero */
    .hero { height:100vh; display:flex; align-items:center; background: linear-gradient(135deg,#03162A 20%,#002B3A 60%,#2DD0BE 100%); clip-path: polygon(0 0,100% 0,100% 85vh,0 100%); position:relative; }
    .hero::after { content:''; position:absolute; bottom:0; left:0; width:100%; height:15vh; background:#03162A; }
    .hero-content { width:50%; padding-left:4rem; }
    .hero-content h1 { font-size:3.5rem; line-height:1.1; margin-bottom:1rem; }
    .hero-content h1 span { color:#FFF; }
    .hero-content p { font-size:1.25rem; margin-bottom:2rem; color:#DDD; }
    .hero-actions { display:flex; gap:1.5rem; }
    .btn { padding:0.75rem 1.75rem; border-radius:0.5rem; font-weight:600; transition:all .3s; }
    .btn-primary { background:#2DD0BE; color:#03162A; }
    .btn-primary:hover { background:#24a89e; transform:translateY(-3px); }
    .btn-secondary { border:2px solid #2DD0BE; color:#2DD0BE; background:transparent; }
    .btn-secondary:hover { background:#2DD0BE; color:#03162A; transform:translateY(-3px); }
    /* Features */
    #features { padding:6rem 0; }
    .features-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:2rem; }
    .feature-card { background:rgba(255,255,255,0.05); padding:2rem; border-radius:1rem; transition:transform .3s; }
    .feature-card:hover { transform:translateY(-10px); }
    .feature-card img { width:48px; margin-bottom:1rem; }
    .feature-card h3 { color:#2DD0BE; margin-bottom:1rem; font-size:1.25rem; }
    .feature-card ul { list-style:none; color:#DDD; }
    .feature-card ul li { margin-bottom:0.75rem; }
    /* Testimonials */
    #testimonials { background:#002B3A; padding:6rem 0; }
    .testimonials-inner { display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:2rem; }
    .testimonial { flex:0 0 80%; max-width:80%; background:rgba(255,255,255,0.05); padding:2rem; border-radius:1rem; scroll-snap-align:center; }
    .testimonial p { font-size:1.5rem; margin-bottom:1rem; }
    .testimonial small { font-size:1rem; color:#AAA; }
    /* Countdown */
    #countdown { text-align:center; padding:4rem 0; font-size:2rem; color:#2DD0BE; }
    /* Register */
    #register { padding:6rem 0; }
    .form-wrapper { max-width:500px; margin:0 auto; background:rgba(255,255,255,0.05); padding:2.5rem; border-radius:1rem; }
    .form-wrapper label { display:block; margin-top:1rem; font-weight:500; color:#EEE; }
    .form-wrapper input { width:100%; padding:0.75rem; margin-top:0.5rem; border:none; border-radius:0.5rem; }
    .form-wrapper button { margin-top:2rem; width:100%; padding:0.75rem; border:none; border-radius:0.5rem; background:#2DD0BE; color:#03162A; font-weight:600; transition:background .3s; }
    .form-wrapper button:hover { background:#24a89e; }
    /* Footer */
    footer { text-align:center; padding:2rem 0; font-size:0.9rem; color:#666; }
    /* Responsive */
    @media(max-width:768px) {
      .hero-content { width:100%; padding:2rem; }
      .hero-content h1 { font-size:2.5rem; }
      .hero { clip-path:none; }
      .testimonials-inner { flex-wrap:nowrap; }
    }
  </style>
</head>
<body>
  <nav>
    <div class="nav-inner container">
      <div class="logo">Mentr</div>
      <div class="nav-links">
        <a href="#features">Features</a>
        <a href="#testimonials">Testimonials</a>
        <a href="#register">Register</a>
      </div>
    </div>
  </nav>
  <header class="hero">
    <div class="hero-content container">
      <h1><span>Welcome to</span><br/>MDCAT World (Plus)</h1>
      <p>Your all-in-one pathway from Freshers Session to MDCAT success.</p>
      <div class="hero-actions">
        <a href="#register" class="btn btn-primary">Get Started</a>
        <a href="#testimonials" class="btn btn-secondary">See Reviews</a>
      </div>
    </div>
  </header>
  <section id="features" class="container">
    <div class="features-grid">
      <div class="feature-card">
        <img src="https://img.icons8.com/ios-filled/80/2DD0BE/book.png" alt="Academic Support">
        <h3>Academic Support</h3>
        <ul>
          <li>Complete syllabus A–Z</li>
          <li>Intensive revision & crash-tests</li>
          <li>Concise written & video lessons</li>
          <li>7-day zero-stress roadmap</li>
        </ul>
      </div>
      <div class="feature-card">
        <img src="https://img.icons8.com/ios-glyphs/80/2DD0BE/user-group-man-woman.png" alt="Mentorship">
        <h3>Mentorship</h3>
        <ul>
          <li>24/7 doubt support</li>
          <li>One-on-one progress calls</li>
          <li>Daily accountability nudges</li>
        </ul>
      </div>
      <div class="feature-card">
        <img src="https://img.icons8.com/ios-filled/80/2DD0BE/medal.png" alt="Post-MDCAT Support">
        <h3>Post-MDCAT Support</h3>
        <ul>
          <li>MBBS admission roadmap</li>
          <li>Celebrate success ceremonies</li>
          <li>Exclusive MBBS pro network</li>
        </ul>
      </div>
    </div>
  </section>
  <section id="testimonials">
    <div class="testimonials-inner container">
      <div class="testimonial">
        <p>“Jumped from 60% → 85% in 8 weeks!”</p>
        <small>— Ayesha Z.</small>
      </div>
      <div class="testimonial">
        <p>“Accountability nudges changed my study routine.”</p>
        <small>— Hamza R.</small>
      </div>
      <div class="testimonial">
        <p>“Secured my dream MBBS seat!”</p>
        <small>— Ali S.</small>
      </div>
    </div>
  </section>
  <section id="countdown">
    <div class="container" id="countdown-timer">Loading countdown...</div>
  </section>
  <section id="register">
    <div class="form-wrapper container">
      <form>
        <label for="name">Full Name</label>
        <input id="name" type="text" placeholder="Your Name" required>
        <label for="email">Email Address</label>
        <input id="email" type="email" placeholder="you@example.com" required>
        <label for="phone">Phone Number</label>
        <input id="phone" type="tel" placeholder="0300-1234567" required>
        <button type="submit">Register Now</button>
      </form>
    </div>
  </section>
  <footer>
    &copy; 2025 Mentr. All rights reserved.
  </footer>
  <script>
    // Countdown
    const endDate = new Date('2025-06-01T20:00:00').getTime();
    const countEl = document.getElementById('countdown-timer');
    const updateTimer = () => {
      const now = Date.now(); const diff = endDate - now;
      if(diff <= 0) return countEl.innerText = 'Live Q&A Now!';
      const d = Math.floor(diff/(1000*60*60*24));
      const h = Math.floor((diff/(1000*60*60))%24);
      const m = Math.floor((diff/(1000*60))%60);
      countEl.innerText = `Next Live Q&A in: ${d}d : ${h}h : ${m}m`;
    };
    setInterval(updateTimer,1000);
    updateTimer();
  </script>
</body>
</html>
'''

# Render HTML
components.html(landing_page_html, height=1600, scrolling=True)
