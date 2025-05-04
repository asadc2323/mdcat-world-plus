import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# --- Streamlit Config ---
st.set_page_config(page_title="Mentr Landing Page", layout="wide")

# --- Enhanced Landing Page HTML + CSS ---
landing_page_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mentr: MDCAT World Plus</title>
  <style>
    /* Fonts & Variables */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    :root {
      --clr-bg: #03162A;
      --clr-gradient: linear-gradient(135deg, #03162A 0%, #002B3A 50%, #2DD0BE 100%);
      --clr-accent: #2DD0BE;
      --clr-light: #FFFFFF;
      --clr-card: rgba(255,255,255,0.05);
      --radius: 1rem;
      --transition: 0.4s;
    }
    *, *::before, *::after { box-sizing: border-box; margin:0; padding:0; }
    body {
      font-family:'Inter',sans-serif;
      background: var(--clr-bg);
      color: var(--clr-light);
      scroll-behavior: smooth;
    }
    a { text-decoration:none; color:inherit; }
    /* Navbar */
    nav {
      position:fixed; top:0; width:100%; padding:1rem 2rem;
      display:flex; justify-content:space-between; align-items:center;
      background: rgba(3,22,42,0.75);
      backdrop-filter: blur(10px);
      z-index:1000;
    }
    nav .logo { font-size:1.75rem; font-weight:700; color:var(--clr-accent); }
    nav .menu a { margin-left:2rem; font-weight:600; transition:color var(--transition); }
    nav .menu a:hover { color:var(--clr-accent); }
    /* Hero */
    .hero {
      min-height:100vh; display:flex; align-items:center; justify-content:center;
      background: var(--clr-gradient) no-repeat center/cover;
      position:relative; padding:0 2rem;
    }
    .hero .overlay { position:absolute; inset:0; background:rgba(0,0,0,0.5); }
    .hero .content {
      position:relative; text-align:center; max-width:800px; z-index:1;
    }
    .hero h1 { font-size:3rem; margin-bottom:1rem; line-height:1.2; }
    .hero h1 span { color:var(--clr-accent); }
    .hero p { font-size:1.25rem; margin-bottom:2rem; }
    .hero .actions a {
      display:inline-block; margin:0 0.5rem;
      padding:0.75rem 1.75rem; border-radius:var(--radius);
      font-weight:600; transition: all var(--transition);
    }
    .btn-primary {
      background:var(--clr-accent); color:var(--clr-bg);
    }
    .btn-primary:hover {
      background: #24a89e;
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(45,208,190,0.4);
    }
    .btn-secondary {
      border:2px solid var(--clr-accent); color:var(--clr-accent);
    }
    .btn-secondary:hover {
      background:var(--clr-accent); color:var(--clr-bg);
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(45,208,190,0.4);
    }
    /* Section Separator */
    .wave {
      width:100%; height:120px; overflow:hidden;
      transform:rotate(180deg);
    }
    .wave svg { width:100%; height:100%; }
    /* Features */
    #features { padding:6rem 2rem; }
    #features .grid {
      display:grid; grid-template-columns: repeat(auto-fit,minmax(280px,1fr)); gap:2rem;
    }
    .card {
      background: var(--clr-card);
      padding:2.5rem 2rem;
      border-radius:var(--radius);
      backdrop-filter: blur(10px);
      transition: transform var(--transition), box-shadow var(--transition);
    }
    .card:hover {
      transform: translateY(-10px);
      box-shadow: 0 15px 30px rgba(0,0,0,0.5);
    }
    .card img { width:50px; margin-bottom:1rem; }
    .card h5 { color:var(--clr-accent); margin-bottom:1rem; }
    .card ul li { margin-bottom:0.75rem; line-height:1.4; }
    /* Testimonials */
    #testimonials { padding:6rem 2rem; }
    .testimonials {
      display:flex; overflow:hidden; position:relative;
    }
    .testimonial {
      min-width:100%; padding:2rem;
      transition: transform var(--transition);
      text-align:center;
    }
    .testimonial p { font-size:1.5rem; margin-bottom:1rem; }
    .testimonial small { font-size:1rem; color:#ccc; }
    .dots {
      position:absolute; bottom:1rem; left:50%; transform:translateX(-50%);
      display:flex;
    }
    .dot {
      width:12px; height:12px; margin:0 6px;
      background:#ccc; border-radius:50%; cursor:pointer;
      transition: background var(--transition);
    }
    .dot.active { background:var(--clr-accent); }
    /* Countdown */
    #countdown { text-align:center; padding:4rem 2rem; font-size:2rem; color:var(--clr-accent); }
    /* Register Form */
    #register { padding:4rem 2rem; }
    .form-container {
      max-width:480px; margin:0 auto;
      background: var(--clr-card); padding:2rem;
      border-radius:var(--radius); backdrop-filter: blur(10px);
    }
    .form-container label { display:block; margin-top:1rem; font-weight:600; }
    .form-container input {
      width:100%; padding:0.75rem; margin-top:0.5rem;
      border:none; border-radius:0.5rem;
    }
    .form-container button {
      margin-top:2rem; width:100%; padding:0.75rem;
      border:none; border-radius:0.5rem;
      background:var(--clr-accent); color:var(--clr-bg);
      font-size:1rem; font-weight:600;
      cursor:pointer; transition: background var(--transition);
    }
    .form-container button:hover { background:#24a89e; }
    /* Footer */
    footer { text-align:center; padding:2rem; font-size:0.9rem; color:#666; }
    /* Responsive */
    @media (max-width:768px) {
      .hero h1 { font-size:2.5rem; }
      .hero p { font-size:1rem; }
    }
  </style>
</head>
<body>
  <nav data-aos="fade-down" data-aos-duration="800">
    <div class="logo">Mentr</div>
    <div class="menu">
      <a href="#features">Features</a>
      <a href="#testimonials">Testimonials</a>
      <a href="#register">Register</a>
    </div>
  </nav>
  <header class="hero" data-aos="fade-up" data-aos-duration="1000">
    <div class="overlay"></div>
    <div class="content">
      <h1>Welcome to <span>MDCAT World (Plus)</span></h1>
      <p>Your all-in-one pathway from Freshers Session to MDCAT success.</p>
      <div class="actions">
        <a href="#register" class="btn btn-primary">Get Started</a>
        <a href="#testimonials" class="btn btn-secondary">See Reviews</a>
      </div>
    </div>
  </header>
  <div class="wave">
    <svg viewBox="0 0 1440 120" preserveAspectRatio="none"><path fill="#03162A" d="M0,120 C480,0 960,240 1440,120 L1440,0 L0,0 Z"></path></svg>
  </div>
  <section id="features" data-aos="fade-up" data-aos-duration="800">
    <div class="grid">
      <div class="card" data-aos="zoom-in" data-aos-delay="100">
        <img src="https://img.icons8.com/ios-filled/80/2DD0BE/book.png" alt="Academic Support"/>
        <h5>Academic Support</h5>
        <ul>
          <li>Complete syllabus A–Z</li>
          <li>Intensive revision & crash-tests</li>
          <li>Concise written & video lessons</li>
          <li>7-day zero-stress roadmap</li>
        </ul>
      </div>
      <div class="card" data-aos="zoom-in" data-aos-delay="200">
        <img src="https://img.icons8.com/ios-glyphs/80/2DD0BE/user-group-man-woman.png" alt="Mentorship"/>
        <h5>Mentorship</h5>
        <ul>
          <li>24/7 doubt support</li>
          <li>One-on-one progress calls</li>
          <li>Daily accountability nudges</li>
        </ul>
      </div>
      <div class="card" data-aos="zoom-in" data-aos-delay="300">
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
  <section id="testimonials" data-aos="fade-up" data-aos-duration="800">   
    <div class="testimonials">  
      <div class="testimonial" id="t1"><p>“Jumped from 60% → 85% in 8 weeks!”</p><small>— Ayesha Z.</small></div>
      <div class="testimonial" id="t2"><p>“Accountability nudges changed my study routine.”</p><small>— Hamza R.</small></div>
      <div class="testimonial" id="t3"><p>“Secured my dream MBBS seat!”</p><small>— Ali S.</small></div>
    </div>
    <div class="dots">
      <div class="dot active" onclick="showTestimonial(1)"></div>
      <div class="dot" onclick="showTestimonial(2)"></div>
      <div class="dot" onclick="showTestimonial(3)"></div>
    </div>
  </section>
  <section id="countdown" data-aos="zoom-in" data-aos-duration="800">
    <div class="countdown" id="count">Loading countdown...</div>
  </section>
  <section id="register" data-aos="fade-up" data-aos-duration="800">
    <div class="form-container">
      <form id="regForm">
        <label for="name">Full Name</label>
        <input type="text" id="name" placeholder="Your Name" required>
        <label for="email">Email Address</label>
        <input type="email" id="email" placeholder="you@example.com" required>
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" placeholder="0300-1234567" required>
        <button type="submit">Register Now</button>
      </form>
    </div>
  </section>
  <footer>
    &copy; 2025 Mentr. All rights reserved.
  </footer>
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    // Initialize AOS
    AOS.init({ duration:800, once:true });
    // Countdown Timer
    const end = new Date('2025-06-01T20:00:00').getTime();
    const countEl = document.getElementById('count');
    const timer = setInterval(() => {
      let now = Date.now(); let diff = end - now;
      if(diff <= 0){ clearInterval(timer); return countEl.innerText = 'Live Q&A Now!'; }
      const d = Math.floor(diff/(1000*60*60*24));
      const h = Math.floor((diff/(1000*60*60))%24);
      const m = Math.floor((diff/(1000*60))%60);
      countEl.innerText = `Next Live Q&A in: ${d}d : ${h}h : ${m}m`;
    },1000);
    // Testimonial switcher
    function showTestimonial(n) {
      document.querySelectorAll('.testimonial').forEach((el,i) => {
        el.style.transform = `translateX(${(i-(n-1))*100}%)`;
      });
      document.querySelectorAll('.dot').forEach((dot,i) => {
        dot.classList.toggle('active', i === n-1);
      });
    }
  </script>
</body>
</html>
'''

# Render the landing page
components.html(landing_page_html, height=1600, scrolling=True)
