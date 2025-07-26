<template>
  <div class="admin-dashboard-container d-flex">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="logo-icon"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><line x1="10" y1="9" x2="8" y2="9"></line></svg>
        <span class="logo-text">Quizzy</span>
      </div>
      <nav class="nav-menu">
        <a href="#" class="nav-item active">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
          <span>Dashboard</span>
        </a>
        <a href="#" class="nav-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v15H6.5A2.5 2.5 0 0 1 4 14.5V4A2 2 0 0 1 6.5 2z"></path></svg>
          <span>Quizzes</span>
        </a>
        <a href="#" class="nav-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          <span>Events</span>
        </a>
        <a href="#" class="nav-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          <span>Students</span>
        </a>
        <a href="#" class="nav-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          <span>Profile</span>
        </a>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <header class="main-header d-flex justify-content-between align-items-center">
        <div>
          <h1 class="welcome-title">Welcome Admin</h1>
          <p class="welcome-subtitle">Welcome back, Sarah! Here's what's happening with your quizzes.</p>
        </div>
        <div class="d-flex align-items-center">
          <div class="search-wrapper me-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" class="search-input" placeholder="Search...">
          </div>
          <button class="btn btn-primary create-quiz-btn">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            Create New Quiz
          </button>
        </div>
      </header>

      <!-- Summary Cards -->
      <section class="summary-cards row">
        <div v-for="card in summaryCards" :key="card.title" class="col-md-3">
          <div class="summary-card">
            <div class="card-body d-flex justify-content-between align-items-center">
              <div>
                <p class="card-title-text">{{ card.title }}</p>
                <h3 class="card-value">{{ card.value }}</h3>
              </div>
              <div class="card-icon-wrapper" :style="{ backgroundColor: card.iconBg }">
                <div v-html="card.icon"></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Recent Events -->
      <section class="recent-events mt-4">
        <h2 class="section-title">Recent Events</h2>
        <p class="section-subtitle">Manage your upcoming and active quiz events</p>
        <div class="events-list">
          <div v-for="event in recentEvents" :key="event.title" class="event-item d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
              <div class="event-icon-wrapper">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              </div>
              <div>
                <p class="event-title">{{ event.title }}</p>
                <p class="event-details">{{ event.time }} <span class="dot-separator">•</span> {{ event.participants }} participants</p>
              </div>
            </div>
            <button :class="['btn', event.isLive ? 'btn-view-live' : 'btn-manage']">{{ event.isLive ? 'View Live' : 'Manage' }}</button>
          </div>
        </div>
      </section>

      <!-- Recent Quizzes -->
      <section class="recent-quizzes mt-4">
        <h2 class="section-title">Recent Quizzes</h2>
        <p class="section-subtitle">Your recently created quizzes</p>
        <div class="row">
          <div v-for="quiz in recentQuizzes" :key="quiz.title" class="col-md-4">
            <div class="quiz-card">
              <div class="quiz-card-header d-flex justify-content-between align-items-center">
                <h5 class="quiz-title">{{ quiz.title }}</h5>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </div>
              <div class="quiz-card-body">
                <p class="quiz-details">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                  {{ quiz.questions }} questions
                  <span class="dot-separator">•</span>
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  {{ quiz.completions }} completions
                </p>
                <div class="progress-bar-wrapper">
                  <div class="progress-bar-label d-flex justify-content-between">
                    <span>Completion Rate</span>
                    <span>{{ quiz.completionRate }}%</span>
                  </div>
                  <div class="progress-bar-bg">
                    <div class="progress-bar-fg" :style="{ width: quiz.completionRate + '%' }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// --- Placeholder Data ---
// You will replace this with data from your API

const summaryCards = ref([
  { title: 'Total Quizzes', value: '2,543', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v15H6.5A2.5 2.5 0 0 1 4 14.5V4A2 2 0 0 1 6.5 2z"></path></svg>', iconBg: 'rgba(110, 86, 241, 0.1)' },
  { title: 'Active Events', value: '2,543', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>', iconBg: 'rgba(52, 195, 143, 0.1)' },
  { title: 'Students', value: '2,543', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>', iconBg: 'rgba(80, 165, 241, 0.1)' },
  { title: 'Total Questions', value: '2,543', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>', iconBg: 'rgba(241, 180, 76, 0.1)' }
]);

const recentEvents = ref([
  { title: 'Science Mid-term Quiz', time: 'Today, 2:30 PM', participants: 32, isLive: true },
  { title: 'Mathematics Weekly Test', time: 'Tomorrow, 10:00 AM', participants: 28, isLive: false },
  { title: 'History Final Exam', time: 'May 20, 9:00 AM', participants: 45, isLive: false },
]);

const recentQuizzes = ref([
  { title: 'Introduction to Biology', questions: 15, completions: 28, completionRate: 75 },
  { title: 'Introduction to Biology', questions: 15, completions: 28, completionRate: 40 },
  { title: 'Introduction to Biology', questions: 15, completions: 28, completionRate: 90 },
]);

</script>

<style scoped>
/* Main Layout & Theme */
:root {
  --primary-color: #6E56F1;
  --background-color: #16161A;
  --sidebar-bg: #1E1E24;
  --card-bg: #24242C;
  --text-primary: #FFFFFF;
  --text-secondary: #94A3B8;
  --border-color: #3A3A43;
  --green-color: #34C38F;
  --orange-color: #F1B44C;
  --blue-color: #50A5F1;
}

.admin-dashboard-container {
  font-family: 'Inter', sans-serif;
  background-color: var(--background-color);
  color: var(--text-primary);
  min-height: 100vh;
}

/* Sidebar */
.sidebar {
  width: 260px;
  background-color: var(--sidebar-bg);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}

.sidebar-header {
  display: flex;
  align-items: center;
  margin-bottom: 2.5rem;
}

.logo-icon {
  color: var(--primary-color);
  width: 32px;
  height: 32px;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  margin-left: 0.75rem;
}

.nav-menu .nav-item {
  display: flex;
  align-items: center;
  padding: 0.9rem 1rem;
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.3s ease;
}

.nav-menu .nav-item:hover {
  background-color: var(--card-bg);
  color: var(--text-primary);
}

.nav-menu .nav-item.active {
  background-color: var(--primary-color);
  color: var(--text-primary);
  font-weight: 500;
}

.nav-icon {
  width: 20px;
  height: 20px;
  margin-right: 1rem;
}

/* Main Content */
.main-content {
  padding: 2rem 3rem;
}

.main-header {
  margin-bottom: 2rem;
}

.welcome-title {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 0;
}

.welcome-subtitle {
  color: var(--text-secondary);
  font-size: 1rem;
  margin-top: 0.25rem;
}

.search-wrapper {
  position: relative;
}

.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-secondary);
}

.search-input {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  color: var(--text-primary);
  padding: 0.6rem 1rem 0.6rem 2.5rem; /* left padding for icon */
  width: 250px;
  transition: all 0.3s ease;
}
.search-input::placeholder {
  color: var(--text-secondary);
}
.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(110, 86, 241, 0.2);
}

.create-quiz-btn {
  background-color: var(--primary-color);
  border: none;
  border-radius: 0.5rem;
  padding: 0.75rem 1.25rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.create-quiz-btn:hover {
  background-color: #5a43d1;
}

/* Section Titles */
.section-title {
  font-size: 1.25rem;
  font-weight: 600;
}
.section-subtitle {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
}

/* Summary Cards */
.summary-card {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: 1.5rem;
}
.card-title-text {
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}
.card-value {
  font-size: 2rem;
  font-weight: 600;
}
.card-icon-wrapper {
  width: 50px;
  height: 50px;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.card-icon-wrapper svg {
  width: 24px;
  height: 24px;
  color: var(--primary-color);
}
.summary-cards .col-md-3:nth-child(2) .card-icon-wrapper svg { color: var(--green-color); }
.summary-cards .col-md-3:nth-child(3) .card-icon-wrapper svg { color: var(--blue-color); }
.summary-cards .col-md-3:nth-child(4) .card-icon-wrapper svg { color: var(--orange-color); }

/* Recent Events */
.events-list {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: 1rem;
}
.event-item {
  padding: 1rem;
  border-radius: 0.5rem;
}
.event-item:not(:last-child) {
  border-bottom: 1px solid var(--border-color);
}
.event-icon-wrapper {
  background-color: rgba(52, 195, 143, 0.1);
  color: var(--green-color);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
}
.event-icon-wrapper svg {
  width: 20px;
  height: 20px;
}
.event-title {
  font-weight: 500;
  margin-bottom: 0.25rem;
}
.event-details {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin: 0;
}
.dot-separator {
  margin: 0 0.5rem;
}
.btn-manage, .btn-view-live {
  border-radius: 0.5rem;
  font-size: 0.85rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
}
.btn-manage {
  background-color: #3A3A43;
  border: 1px solid #555;
  color: var(--text-primary);
}
.btn-view-live {
  background-color: var(--primary-color);
  border: none;
  color: var(--text-primary);
}

/* Recent Quizzes */
.quiz-card {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
}
.quiz-card:hover {
  transform: translateY(-5px);
  border-color: var(--primary-color);
}
.quiz-title {
  font-size: 1rem;
  font-weight: 600;
}
.quiz-card-header svg {
  color: var(--text-secondary);
}
.quiz-details {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin-top: 1rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.progress-bar-wrapper .progress-bar-label {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}
.progress-bar-bg {
  background-color: #3A3A43;
  height: 6px;
  border-radius: 3px;
  overflow: hidden;
}
.progress-bar-fg {
  background-color: var(--primary-color);
  height: 100%;
  border-radius: 3px;
}
</style>
