<!-- components/LandingPage.vue -->
<template>
  <div class="landing-page text-white">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-transparent px-4 py-3">
      <div class="container-fluid">
        <a class="navbar-brand fw-bold text-gradient" href="#">Quizzy</a>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item"><a class="nav-link" href="#">Quiz</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Weekly Quiz</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Rewards</a></li>
            <li class="nav-item"><a class="nav-link" href="#">About</a></li>
          </ul>
          <div class="d-flex gap-2">
            <span><a href="#" class="btn btn-outline-light btn-sm" @click.prevent="$emit('navigate', 'login')">Sign In</a></span>
            <span><a href="#" class="btn btn-primary btn-sm" @click.prevent="$emit('navigate', 'register')">Register</a></span>
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
        Join thousands of students and teachers on the ultimate quiz platform.\nTest your knowledge, compete with peers, and win exciting rewards.
      </p>
      <div class="d-flex justify-content-center gap-3 mb-5">
        <span><a href="#" class="btn btn-purple px-4" @click.prevent="$emit('navigate', 'login')">Get Started</a></span>
        <button class="btn btn-light px-4">Explore Quizzes</button>
      </div>

      <!-- Students joined -->
      <div class="d-flex justify-content-center align-items-center gap-3">
        <div class="avatars d-flex">
          <img src="https://i.pravatar.cc/40?img=1" class="rounded-circle border border-white avatar" />
          <img src="https://i.pravatar.cc/40?img=2" class="rounded-circle border border-white avatar" />
          <img src="https://i.pravatar.cc/40?img=3" class="rounded-circle border border-white avatar" />
          <img src="https://i.pravatar.cc/40?img=4" class="rounded-circle border border-white avatar" />
        </div>
        <span class="text-light">
          <span class="text-info">5,000+</span> students joined this week
        </span>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>
