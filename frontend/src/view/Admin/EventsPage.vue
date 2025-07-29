<template>
  <div class="d-flex">
    <AdminSidebar />
    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <header class="main-header d-flex justify-content-between align-items-center">
        <div>
          <h1 class="page-title">Quiz Events</h1>
          <p class="page-subtitle">Schedule and manage quiz sessions for your students</p>
        </div>
        <button class="btn btn-primary schedule-event-btn">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Schedule Event
        </button>
      </header>

      <!-- Event Calendar Section -->
      <section class="event-calendar">
        <div class="card-header d-flex justify-content-between align-items-center">
          <div>
              <h2 class="section-title">Event Calendar</h2>
              <p class="section-subtitle">View and manage your scheduled quiz events</p>
          </div>
        </div>
        <div class="card-filters d-flex justify-content-between align-items-center">
            <div class="tabs">
                <button class="tab-btn active">All Events</button>
                <button class="tab-btn">Active</button>
                <button class="tab-btn">Upcoming</button>
                <button class="tab-btn">Completed</button>
            </div>
            <div class="d-flex gap-3">
                <div class="search-wrapper">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                  <input type="text" class="search-input" placeholder="Search events...">
                </div>
                <select class="form-select filter-select">
                    <option selected>All Quizzes</option>
                    <option value="1">Biology</option>
                    <option value="2">Mathematics</option>
                </select>
            </div>
        </div>
        <div class="events-list">
          <!-- Event Item Loop -->
          <div v-for="event in events" :key="event.title" class="event-item d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
              <div class="event-icon-wrapper">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v15H6.5A2.5 2.5 0 0 1 4 14.5V4A2 2 0 0 1 6.5 2z"></path></svg>
              </div>
              <div class="event-info">
                <p class="event-title">
                  {{ event.title }}
                  <span :class="['badge', getStatusClass(event.status)]">{{ event.status }}</span>
                </p>
                <p class="event-description">{{ event.description }}</p>
                <div class="event-details">
                  <span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> {{ event.questions }} questions</span>
                  <span class="dot-separator">•</span>
                  <span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> {{ event.duration }} min</span>
                  <span class="dot-separator">•</span>
                  <span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg> {{ event.completions }} completions</span>
                  <span class="dot-separator">•</span>
                  <span class="text-muted">Created {{ event.created }}</span>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center gap-2">
                <button :class="['btn', event.status === 'Active' ? 'btn-view-live' : 'btn-manage']">
                  {{ event.status === 'Active' ? 'View Live' : 'Manage' }}
                </button>
                <button class="btn btn-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle></svg>
                </button>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const events = ref([]);
const loading = ref(false);
const error = ref(null);

async function fetchEvents() {
  loading.value = true;
  error.value = null;
  try {
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Authentication token not found.');
    const response = await axios.get('http://127.0.0.1:5000/api/admin/events', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    console.log(response.data);
    events.value = response.data.events || [];
  } catch (err) {
    error.value = 'Failed to fetch events.';
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchEvents();
});

// Helper function to apply the correct CSS class based on the event status
const getStatusClass = (status) => {
  if (status === 'Active') return 'badge-active';
  if (status === 'Upcoming') return 'badge-upcoming';
  if (status === 'Completed') return 'badge-completed';
  return '';
};
</script>

<style scoped>
/* Scoped styles for this specific page */
.main-content {
  padding: 2rem 3rem;
  overflow-y: auto;
  width: calc(100% - 260px);
}

.main-header {
  margin-bottom: 2rem;
}

.page-title {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 0;
}

.page-subtitle {
  color: #94A3B8;
  font-size: 1rem;
  margin-top: 0.25rem;
}

.schedule-event-btn {
  background-color: #6E56F1;
  border: none;
  border-radius: 0.5rem;
  padding: 0.75rem 1.25rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.schedule-event-btn:hover {
  background-color: #5a43d1;
}

.event-calendar {
    background-color: #24242C;
    border: 1px solid #3A3A43;
    border-radius: 0.75rem;
}

.card-header {
    padding: 1.5rem;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}
.section-subtitle {
  color: #94A3B8;
  font-size: 0.9rem;
  margin-top: 0.25rem;
  margin-bottom: 0;
}

.card-filters {
    padding: 0 1.5rem 1.5rem;
    border-bottom: 1px solid #3A3A43;
}

.tabs .tab-btn {
    background: none;
    border: none;
    color: #94A3B8;
    padding: 0.5rem 1rem;
    font-weight: 500;
    border-radius: 0.5rem;
}
.tabs .tab-btn.active {
    background-color: #3A3A43;
    color: #FFFFFF;
}

.search-wrapper {
  position: relative;
}
.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #94A3B8;
}
.search-input, .filter-select {
  background-color: #1E1E24;
  border: 1px solid #3A3A43;
  border-radius: 0.5rem;
  color: #FFFFFF;
  padding: 0.6rem 1rem;
  transition: all 0.3s ease;
}
.search-input {
  padding-left: 2.5rem;
  width: 220px;
}
.filter-select {
    width: 180px;
}
.search-input::placeholder { color: #94A3B8; }
.search-input:focus, .filter-select:focus {
  outline: none;
  border-color: #6E56F1;
  box-shadow: 0 0 0 2px rgba(110, 86, 241, 0.2);
  background-color: #1E1E24;
  color: #FFFFFF;
}

.events-list {
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
  background-color: rgba(110, 86, 241, 0.1);
  color: #8c72f3;
  width: 44px;
  height: 44px;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
}
.event-icon-wrapper svg {
  width: 24px;
  height: 24px;
}
.event-title {
  font-weight: 500;
  margin-bottom: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.event-description {
  color: #94A3B8;
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}
.event-details {
  color: #94A3B8;
  font-size: 0.85rem;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.dot-separator {
  margin: 0 0.5rem;
}

.badge {
    font-size: 0.75rem;
    padding: 0.25em 0.6em;
    border-radius: 0.3rem;
    font-weight: 500;
}
.badge-active {
    background-color: rgba(52, 195, 143, 0.1);
    color: #34c38f;
}
.badge-upcoming {
    background-color: rgba(80, 165, 241, 0.1);
    color: #50a5f1;
}
.badge-completed {
    background-color: rgba(148, 163, 184, 0.1);
    color: #94a3b8;
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
.btn-icon {
    background-color: #3A3A43;
    border: 1px solid #555;
    color: #94A3B8;
}
</style>
