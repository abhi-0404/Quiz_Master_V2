<!-- components/LandingPage.vue -->
<template>
  <div class="landing-page text-white">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-transparent px-4 py-3">
      <div class="container-fluid">
        <!-- The brand logo now links to the home page -->
        <router-link class="navbar-brand fw-bold text-gradient" to="/">Quizzy</router-link>
        <div class="collapse navbar-collapse">
      
          <div class="d-flex gap-2">
            <!-- UPDATED: Use router-link for navigation -->
            <router-link to="/login" class="btn btn-outline-light btn-sm">Sign In</router-link>
            <router-link to="/register" class="btn btn-primary btn-sm">Register</router-link>
          </div>
        </div>
      </div>
    </nav>

    <!-- Hero -->
    <section class="hero-section text-center px-3 py-5">
      <div class="mb-3 small badge-text">✨ The ultimate quiz experience</div>
      <h1 class="display-4 fw-bold">
        Learn, Quiz, <span class="text-purple">Earn</span> <span class="text-orange">Rewards</span>
      </h1>
      <p class="lead text-light mt-3 mb-4">
        Join thousands of students and teachers on the ultimate quiz platform.<br/>Test your knowledge, compete with peers, and win exciting rewards.
      </p>
      <div class="d-flex justify-content-center gap-3 mb-5">
        <!-- UPDATED: Use router-link for navigation -->
        <router-link to="/login" class="btn btn-purple px-4">Get Started</router-link>
        <button class="btn btn-light px-4">Explore Quizzes</button>
      </div>

      <!-- Students joined -->
      <div class="d-flex justify-content-center align-items-center gap-3">
        <div class="avatars d-flex">
          <img src="https://i.pravatar.cc/40?img=1" class="rounded-circle border border-white avatar" alt="avatar"/>
          <img src="https://i.pravatar.cc/40?img=2" class="rounded-circle border border-white avatar" alt="avatar"/>
          <img src="https://i.pravatar.cc/40?img=3" class="rounded-circle border border-white avatar" alt="avatar"/>
          <img src="https://i.pravatar.cc/40?img=4" class="rounded-circle border border-white avatar" alt="avatar"/>
        </div>
        <span class="text-light">
          <span class="text-info">5,000+</span> students joined this week
        </span>
      </div>
    </section>
  </div>
</template>

<script setup>
// No script logic is needed for navigation anymore,
// as <router-link> handles it automatically.
</script>

<style scoped>
/* Your existing styles for LandingPage.vue go here */
.landing-page {
  /* It's good practice to ensure the background covers the full view */
  background: linear-gradient(135deg, #1b082f, #1e0c2c, #39120d);
  min-height: 100vh;
}
.navbar {
  background-color: rgba(0, 0, 0, 0.4) !important;
  backdrop-filter: blur(10px);
}
.text-gradient {
  background: linear-gradient(90deg, #f72585, #7209b7);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
}
.hero-section {
  padding-top: 80px;
  padding-bottom: 80px;
}
.text-purple {
  color: #a259ff;
}
.text-orange {
  color: #ff6a3d;
}
.btn-purple {
  background-color: #9b5de5;
  color: white;
}
.btn-purple:hover {
  background-color: #8338ec;
}
.badge-text {
  display: inline-block;
  background-color: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 999px;
  padding: 5px 15px;
  font-size: 0.75rem;
  color: #ddd;
}
.avatar {
  width: 36px;
  height: 36px;
  margin-left: -10px;
  border: 2px solid white;
}
</style>
