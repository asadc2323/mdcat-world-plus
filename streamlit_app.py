import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# --- Streamlit Page Config ---
st.set_page_config(page_title="Mentr Landing Page", layout="wide")

# --- Embed Fully Responsive Landing Page with Embedded CSS & AOS ---
landing_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mentr: MDCAT World Plus</title>
  <style>
    /* Embed AOS CSS */
    @import url('https://unpkg.com/aos@2.3.1/dist/aos.css');
    /* Font */
    @import url('https://fonts.googleapis.com/css?family=Inter:400,600,700&display=swap');
    :root {
      --bg-dark: #03162A;
      --gradient: linear-gradient(135deg, #03162A, #002B3A, #2DD0BE);
      --accent: #2DD0BE;
      --text-light: #FFFFFF;
      --card-bg: rgba(0,31,51,0.8);
      --transition: 0.3s;
    }
    *, *::before, *::after { box-sizing: border-box; margin:0; padding:0; }
    body { font-family:'Inter',sans-serif; background: var(--bg-dark); color: var(--text-light); }
    /* Navigation */
    nav { position: fixed; top:0; width:100%; background:rgba(3,22,42,0.9); padding:1rem 2rem; display:flex; justify-content:space-between; align-items:center; z-index:1000; }
    nav .logo { font-size:1.5rem; font-weight:700; color: var(--accent); text-decoration:none; }
    nav .links a { color: var(--text-light); margin-left:1.5rem; text-decoration:none; transition: color var(--transition); }
    nav .links a:hover { color: var(--accent); }
    /* Hero Section */
    .hero { min-height:100vh; display:flex; align-items:center; justify-content:center; text-align:center; background: var(--gradient); padding:0 2rem; position:relative; }
    .hero::before { content:''; position:absolute; inset:0; background:rgba(0,0,0,0.4); }
    .hero .content { position:relative; z-index:1; max-width:800px; }
    .hero h1 { font-size:3rem; margin-bottom:1rem; line-height:1.2; }
    .hero p { font-size:1.25rem; margin-bottom:2rem; }
    .btn { display:inline-block; padding:0.75rem 1.5rem; border-radius:0.5rem; font-weight:600; text-decoration:none; transition: background var(--transition), color var(--transition); }
    .btn-primary { background: var(--accent); color: var(--bg-dark); margin-right:1rem; }
    .btn-primary:hover { background: #24a89e; }
    .btn-secondary { background: transparent; border:2px solid var(--accent); color: var(--accent); }
    .btn-secondary:hover { background: var(--accent); color: var(--bg-dark); }
    /* Sections */
    section { padding:4rem 2rem; }
    /* Features */
    .features .grid { display:grid; grid-template-columns: repeat(auto-fit,minmax(260px,1fr)); gap:2rem; }
    .card { background: var(--card-bg); padding:2rem; border-radius:1rem; transition: transform var(--transition); }
    .card:hover { transform: translateY(-10px); }
    .card img { width:48px; margin-bottom:1rem; }
    .card h5 { color: var(--accent); margin-bottom:1rem; }
    .card ul { list-style:none; }
    .card ul li { margin-bottom:0.75rem; }
    /* Testimonials */
    .testimonials { position:relative; overflow:hidden; }
    .slides { display:flex; width:300%; animation: slide 12s infinite ease-in-out; }
    .slide { min-width:100%; padding:4rem 2rem; text-align:center; }
    .slide p { font-size:1.5rem; margin-bottom:0.5rem; }
    .slide small { font-size:1rem; color:#ccc; }
    @keyframes slide { 0%,20%{transform:translateX(0);}33%,53%{transform:translateX(-100%);}66%,86%{transform:translateX(-200%);}100%{transform:translateX(0);} }
    /* Countdown */
    .countdown { text-align:center; font-size:2rem; color: var(--accent); margin-bottom:2rem; }
    /* Footer */
    footer { text-align:center; padding:2rem; font-size:0.9rem; color:#888; }
    /* Responsive */
    @media (max-width:768px) {
      nav { padding:0.75rem 1rem; }
      .hero h1 { font-size:2.25rem; }
      .hero p { font-size:1rem; }
      .slides { animation: none; }
    }
  </style>
</head>
<body>
  <nav>
    <a href="#" class="logo">Mentr</a>
    <div class="links">
      <a href="#features">Features</a>
      <a href="#testimonials">Testimonials</a>
      <a href="#register">Register</a>
    </div>
  </nav>
  <header class="hero" data-aos="fade-up">
    <div class="content">
      <h1>Welcome to <span style="color:var(--accent);">MDCAT World (Plus)</span></h1>
      <p>Your all-in-one pathway from Freshers Session to MDCAT success.</p>
      <a href="#register" class="btn btn-primary" data-aos="zoom-in" data-aos-delay="200">Join Now</a>
      <a href="#reviews" class="btn btn-secondary" data-aos="zoom-in" data-aos-delay="400">Read Reviews</a>
    </div>
  </header>
  <section id="features" class="features" data-aos="fade-up">
    <div class="grid">
      <div class="card" data-aos="fade-up" data-aos-delay="100">
        <img src="https://img.icons8.com/ios-filled/80/2DD0BE/book.png" alt="Academic Support"/>
        <h5>Academic Support</h5>
        <ul>
          <li>Complete syllabus A–Z</li>
          <li>Intensive revision & crash-tests</li>
          <li>Concise written & video lessons</li>
          <li>7-day zero-stress roadmap</li>
        </ul>
      </div>
      <div class="card" data-aos="fade-up" data-aos-delay="200">
        <img src="https://img.icons8.com/ios-glyphs/80/2DD0BE/user-group-man-woman.png" alt="Mentorship"/>
        <h5>Mentorship</h5>
        <ul>
          <li>24/7 doubt support</li>
          <li>One-on-one progress calls</li>
          <li>Daily accountability nudges</li>
        </ul>
      </div>
      <div class="card" data-aos="fade-up" data-aos-delay="300">
        <img src="https://img.icons8.com/ios-filled/80/2DD0BE/medal.png" alt="Post-MDCAT Support"/>
        <h5>Post-MDCAT Support</h5>
        <ul>
          <li>MBBS admission roadmap</li>
          <li>Celebrate success ceremonies</li>
          <li>Exclusive MBBS pro network</li>
        </ul>
      </div>
    </div>
  </section>
  <section id="testimonials" class="testimonials" data-aos="fade-up">
    <div class="slides">
      <div class="slide"><p>“Jumped from 60% → 85% in 8 weeks!”</p><small>— Ayesha Z.</small></div>
      <div class="slide"><p>“Accountability nudges changed my study routine.”</p><small>— Hamza R.</small></div>
      <div class="slide"><p>“Secured my dream MBBS seat!”</p><small>— Ali S.</small></div>
    </div>
  </section>
  <section id="countdown" data-aos="zoom-in">
    <div class="countdown" id="count">Loading countdown...</div>
  </section>
  <section id="register" class="text-center" data-aos="fade-up">
    <a href="#" class="btn btn-primary btn-lg">Register Now</a>
  </section>
  <footer>
    &copy; 2025 Mentr. All rights reserved.
  </footer>
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    AOS.init({ duration: 800, once: true });
    const end = new Date('2025-06-01T20:00:00').getTime();
    const update = () => {
      const now = Date.now(); const diff = end - now;
      if(diff < 0){ document.getElementById('count').innerText = 'Live now!'; clearInterval(interval); return; }
      const d = Math.floor(diff/(1000*60*60*24));
      const h = Math.floor((diff/(1000*60*60))%24);
      const m = Math.floor((diff/(1000*60))%60);
      document.getElementById('count').innerText = `Next Live Q&A in: ${d}d : ${h}h : ${m}m`;
    };
    const interval = setInterval(update,1000);
    update();
  </script>
</body>
</html>
"""

# Render the landing page
components.html(landing_page_html, height=900, scrolling=True)
