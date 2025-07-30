<template>
  <div class="d-flex student-dashboard-responsive">
    <!-- Sidebar Navigation -->
    <aside class="sidebar sidebar-fixed">
      <StudentSidebar />
    </aside>

    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <header class="main-header d-flex justify-content-between align-items-center">
        <div>
          <h1 class="welcome-title">Welcome {{ firstname }}</h1>
          <p class="welcome-subtitle">Welcome back, {{ firstname }}! Here's what's happening with your quizzes.</p>
        </div>
        <div class="d-flex align-items-center">
          <div class="search-wrapper me-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" class="search-input" placeholder="Search...">
          </div>
        </div>
      </header>

      <!-- Summary Cards -->
      <section class="summary-cards d-flex flex-row gap-3" style="flex-wrap:nowrap; overflow-x:auto;">
        <div v-for="card in summaryCards" :key="card.title" class="summary-card d-flex align-items-stretch flex-shrink-0">
          <div class="card-body d-flex flex-column flex-md-row justify-content-between align-items-center">
            <div class="mb-2 mb-md-0">
              <p class="card-title-text">{{ card.title }}</p>
              <h3 class="card-value">{{ card.value }}</h3>
            </div>
            <div class="card-icon-wrapper d-flex align-items-center justify-content-center">
              <span v-html="card.icon"></span>
            </div>
          </div>
        </div>
      </section>

      <!-- Recent Events -->
      <section class="recent-events mt-4">
        <h2 class="section-title">Recent Events</h2>
        <p class="section-subtitle">Manage your upcoming and active quiz events</p>
        <div class="events-list d-flex flex-column gap-2">
          <div v-for="event in recentEvents" :key="event.title" class="event-item d-flex flex-column flex-md-row align-items-start align-items-md-center justify-content-between gap-2 gap-md-0">
            <div class="d-flex align-items-center gap-2">
              <div class="event-icon-wrapper d-flex align-items-center justify-content-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              </div>
              <div>
                <p class="event-title mb-1">{{ event.title }}</p>
                <p class="event-details mb-0">
                  {{ event.questions }} questions
                  <span class="dot-separator">•</span>
                  {{ event.completions }} completions
                </p>
              </div>
            </div>
            <div class="progress-bar-wrapper">
              <div class="progress-bar-label d-flex justify-content-between">
                <span>Completion Rate</span>
                <span>{{ event.completionRate || 0 }}%</span>
              </div>
              <div class="progress-bar-bg">
                <div class="progress-bar-fg" :style="{ width: (event.completionRate || 0) + '%' }"></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Graphs Section (Placeholder) -->
      <!-- Graphs Section -->
      <div class="mt-4">
        <div class="d-flex flex-column flex-md-row align-items-start justify-content-between gap-2 mb-2">
          <div>
            <h2 class="section-title mb-0">Graphs</h2>
            <p class="section-subtitle mb-0">Your recently created quizzes</p>
          </div>
        </div>
        <section class="dashboard-graphs d-flex flex-column">
          <div class="graphs-row d-flex flex-row flex-wrap gap-3">
            <div class="graph-card d-flex align-items-center justify-content-center"></div>
            <div class="graph-card d-flex align-items-center justify-content-center"></div>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue';
import axios from 'axios';
import StudentSidebar from '../../components/StudentSidebar.vue';

const firstname = ref('');
const summaryCards = ref([
  { title: 'Quizzes available', value: '-', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v15H6.5A2.5 2.5 0 0 1 4 14.5V4A2 2 0 0 1 6.5 2z"></path></svg>', iconBg: 'rgba(110, 86, 241, 0.1)' },
  { title: 'Quizzes attempted', value: '-', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>', iconBg: 'rgba(52, 195, 143, 0.1)' },
  { title: 'Time spent', value: '-', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>', iconBg: 'rgba(80, 165, 241, 0.1)' },
  { title: 'Average marks', value: '-', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>', iconBg: 'rgba(241, 180, 76, 0.1)' }
]);
const recentEvents = ref([]);
const loading = ref(false);
const error = ref(null);

async function fetchDashboardData() {
  loading.value = true;
  error.value = null;
  try {
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Authentication token not found.');
    const response = await axios.get('http://127.0.0.1:5000/api/student/dashboard', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = response.data;
    // Update summary cards, preserving icons and backgrounds by title
    if (data.summaryCards) {
      const iconMap = {};
      summaryCards.value.forEach(card => {
        iconMap[card.title] = { icon: card.icon, iconBg: card.iconBg };
      });
      summaryCards.value = data.summaryCards.map(card => ({
        ...card,
        icon: iconMap[card.title]?.icon || '',
        iconBg: iconMap[card.title]?.iconBg || ''
      }));
    }
    // Update recent events
    if (data.recentEvents) {
      recentEvents.value = data.recentEvents;
    }
    // Optionally fetch student profile for firstname
    const profileRes = await axios.get('http://127.0.0.1:5000/api/student/profile', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    firstname.value = profileRes.data.profile?.full_name?.split(' ')[0] || 'Student';
  } catch (err) {
    error.value = 'Failed to fetch dashboard data. Please try again later.';
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchDashboardData();
});

</script>

<style scoped>
/* Responsive Dashboard Layout */
.student-dashboard-responsive {
  font-family: 'Inter', sans-serif;
  background-color: #16161A;
  color: #FFFFFF;
  min-height: 100vh;
  position: relative;
}

/* Sidebar sticky/fixed for desktop, scrollable for short screens */
.sidebar {
  width: 260px;
  background-color: #1E1E24;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}
.sidebar-fixed {
  position: sticky;
  top: 0;
  height: 100vh;
  align-self: flex-start;
  z-index: 100;
  overflow-y: auto;
  max-height: 100vh;
}
@media (max-width: 991.98px) {
  .sidebar-fixed {
    position: static;
    width: 100%;
    height: auto;
    max-height: none;
    overflow-y: visible;
    z-index: auto;
  }
}
.main-content {
  padding: 2rem 3rem;
  overflow-y: auto;
}
@media (max-width: 991px) {
  .main-content {
    padding: 1rem 0.5rem;
  }
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
  color: #94A3B8;
  font-size: 1rem;
  margin-top: 0.25rem;
}
.summary-cards {
  gap: 2rem;
  flex-wrap: nowrap;
  overflow-x: auto;
}
@media (max-width: 991px) {
  .summary-cards {
    gap: 1rem !important;
    padding-bottom: 1rem;
    overflow-x: auto;
    flex-wrap: nowrap !important;
  }
  .summary-card {
    min-width: 170px;
    max-width: 200px;
    flex: 0 0 auto;
  }
}
.summary-card {
  background-color: #24242C;
  border: 1px solid #3A3A43;
  border-radius: 0.75rem;
  padding: 1.5rem;
  min-width: 220px;
  max-width: 240px;
  flex: 1 1 0;
  box-sizing: border-box;
}
.card-title-text {
  color: #94A3B8;
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
  color: #6E56F1;
}
.summary-cards .summary-card:nth-child(2) .card-icon-wrapper svg { color: #34C38F; }
.summary-cards .summary-card:nth-child(3) .card-icon-wrapper svg { color: #50A5F1; }
.summary-cards .summary-card:nth-child(4) .card-icon-wrapper svg { color: #F1B44C; }
.events-list {
  background-color: #24242C;
  border: 1px solid #3A3A43;
  border-radius: 0.75rem;
  padding: 1rem;
}
.event-item {
  padding: 1rem;
  border-radius: 0.5rem;
}
.event-item:not(:last-child) {
  border-bottom: 1px solid #3A3A43;
}
.event-icon-wrapper {
  background-color: rgba(52, 195, 143, 0.1);
  color: #34C38F;
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
  color: #94A3B8;
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
  color: #FFFFFF;
}
.btn-view-live {
  background-color: #6E56F1;
  border: none;
  color: #FFFFFF;
}
.dashboard-graphs {
  background-color: #23232a;
  border-radius: 1rem;
  padding: 2rem 2rem 2.5rem 2rem;
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
}
.graphs-row {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  justify-content: flex-start;
  flex-wrap: wrap;
}
.graph-card {
  flex: 1 1 0;
  min-width: 300px;
  min-height: 260px;
  background: #18181f;
  border-radius: 0.75rem;
  border: 1px solid #292933;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  display: flex;
  align-items: center;
  justify-content: center;
}
@media (max-width: 991px) {
  .graphs-row {
    flex-direction: column;
    gap: 1.5rem;
  }
  .graph-card {
    min-width: 0;
    width: 100%;
  }
}
</style>
