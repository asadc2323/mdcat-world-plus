import streamlit as st
import streamlit.components.v1 as components

# --- Streamlit Page Config ---
st.set_page_config(page_title="Mentr Landing Page", layout="wide")

# --- Embed Fully Responsive Landing Page via Bootstrap + AOS ---
landing_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mentr: MDCAT World Plus</title>
  <!-- Bootstrap 5 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- AOS Animations -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <!-- Custom Styles -->
  <style>
    body { font-family: 'Inter', sans-serif; background: #03162A; color: #fff; }
    .hero { background: linear-gradient(135deg,#03162A,#002B3A,#2DD0BE); padding: 100px 0; }
    .hero h1 { font-size: 3rem; font-weight: 700; }
    .hero p { font-size: 1.25rem; margin-bottom: 30px; }
    .btn-primary { background: #2DD0BE; border: none; }
    .features .card { background: rgba(0,31,51,0.8); border: none; }
    .features .card h5 { color: #2DD0BE; }
    .testimonial-carousel .carousel-item { text-align: center; }
    .countdown { font-size: 2rem; color: #2DD0BE; margin: 30px 0; }
    footer { padding: 50px 0; text-align: center; }
  </style>
</head>
<body data-bs-theme="dark">
  <!-- Hero Section -->
  <section class="hero text-center text-white">
    <div class="container" data-aos="fade-down">
      <h1>Welcome to <span class="text-white" style="text-shadow:0 0 8px rgba(255,255,255,0.5);">MDCAT World (Plus)</span></h1>
      <p>Your all-in-one path—from Freshers Session right up to MDCAT success</p>
      <a href="#register" class="btn btn-lg btn-primary me-3" data-aos="zoom-in" data-aos-delay="200">Join Now</a>
      <a href="#reviews" class="btn btn-outline-light btn-lg" data-aos="zoom-in" data-aos-delay="400">Read Reviews</a>
    </div>
  </section>

  <!-- Features -->
  <section class="features py-5">
    <div class="container">
      <div class="row g-4">
        <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
          <div class="card p-4 h-100">
            <img src="https://img.icons8.com/ios-filled/64/2DD0BE/book.png" class="mb-3" alt="Academic Support">
            <h5>Academic Support</h5>
            <ul>
              <li>Complete syllabus A–Z</li>
              <li>Intensive revision & crash-tests</li>
              <li>Concise written & video lessons</li>
              <li>7-day zero-stress roadmap</li>
            </ul>
          </div>
        </div>
        <div class="col-md-4" data-aos="fade-up" data-aos-delay="300">
          <div class="card p-4 h-100">
            <img src="https://img.icons8.com/ios-glyphs/64/2DD0BE/user-group-man-woman.png" class="mb-3" alt="Mentorship">
            <h5>Mentorship</h5>
            <ul>
              <li>24/7 doubt support</li>
              <li>One-on-one progress calls</li>
              <li>Daily accountability nudges</li>
            </ul>
          </div>
        </div>
        <div class="col-md-4" data-aos="fade-up" data-aos-delay="500">
          <div class="card p-4 h-100">
            <img src="https://img.icons8.com/ios-filled/64/2DD0BE/medal.png" class="mb-3" alt="Post-MDCAT Support">
            <h5>Post-MDCAT Support</h5>
            <ul>
              <li>MBBS admission roadmap</li>
              <li>Celebrate success ceremonies</li>
              <li>Exclusive MBBS pro network</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Testimonial Carousel -->
  <section class="testimonial-carousel py-5 bg-dark">
    <div class="container">
      <div id="carouselTestimonials" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <p class="h5">“Jumped from 60% → 85% in 8 weeks!”</p>
            <small>— Ayesha Z.</small>
          </div>
          <div class="carousel-item">
            <p class="h5">“Accountability nudges changed my study routine.”</p>
            <small>— Hamza R.</small>
          </div>
          <div class="carousel-item">
            <p class="h5">“Secured my dream MBBS seat!”</p>
            <small>— Ali S.</small>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselTestimonials" data-bs-slide="prev">
          <span class="carousel-control-prev-icon"></span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselTestimonials" data-bs-slide="next">
          <span class="carousel-control-next-icon"></span>
        </button>
      </div>
    </div>
  </section>

  <!-- Countdown -->
  <section class="text-center" data-aos="zoom-in" data-aos-delay="200">
    <div class="countdown" id="countdown">Loading countdown...</div>
  </section>

  <!-- Register CTA -->
  <section id="register" class="text-center py-5">
    <a href="#" class="btn btn-primary btn-lg" data-aos="fade-up" data-aos-delay="300">Register Now</a>
  </section>

  <!-- Footer -->
  <footer>
    &copy; 2025 Mentr. All rights reserved.
  </footer>

  <!-- JS Libraries -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    AOS.init({ duration: 800, once: true });
    // Countdown Timer
    const end = new Date('2025-06-01T20:00:00').getTime();
    const timer = setInterval(() => {
      const now = Date.now();
      const diff = end - now;
      if (diff <= 0) { clearInterval(timer); document.getElementById('countdown').innerHTML = 'Live now!'; return; }
      const d = Math.floor(diff / (1000*60*60*24));
      const h = Math.floor((diff/(1000*60*60)) % 24);
      const m = Math.floor((diff/(1000*60)) % 60);
      document.getElementById('countdown').innerHTML = `Next Live Q&A in: ${d}d : ${h}h : ${m}m`;
    }, 1000);
  </script>
</body>
</html>
"""

# Render the landing page
components.html(landing_page_html, height=1600, scrolling=True)
