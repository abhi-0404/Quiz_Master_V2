<template>
  <div class="d-flex admin-dashboard-responsive">
    <!-- Sidebar Navigation -->
    <aside class="sidebar sidebar-fixed">
      <AdminSidebar :isOpen="sidebarOpen" @toggle="toggleSidebar" />
    </aside>

    <!-- Overlay for mobile -->
    <div v-if="sidebarOpen && isMobile" class="sidebar-overlay" @click="toggleSidebar"></div>

    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <div class="container-fluid py-4 px-5">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <div>
            <h2 class="fw-bold">Quiz Events</h2>
            <p class="text-muted">Schedule and manage quiz sessions for your students</p>
          </div>
          <div>
            <input type="search" v-model="searchQuery" class="form-control" placeholder="Search..." style="width: 250px" />
          </div>
        </div>

        <div>
          <h5 class="fw-semibold mb-3">Event Calendar</h5>
          <div class="mb-4">
            <div
              v-for="event in filteredEvents"
              :key="event.id"
              class="event-card card mb-3 px-3 py-3 d-flex flex-row justify-content-between align-items-center"
            >
              <div class="d-flex align-items-center">
                <div :class="['event-icon rounded-circle d-flex justify-content-center align-items-center me-3', iconBgClass(event.status)]">
                  <span v-if="event.status === 'Active'">
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="none" stroke="#34C38F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="9"/><path d="M11 7v4l3 2"/></svg>
                  </span>
                  <span v-else-if="event.status === 'Completed'">
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="none" stroke="#6C757D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="9"/><polyline points="8 11 11 14 16 9"/></svg>
                  </span>
                  <span v-else>
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="none" stroke="#6E56F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="9"/><path d="M11 6v5l4 2"/></svg>
                  </span>
                </div>
                <div>
                  <h6 class="mb-1">{{ event.title }}</h6>
                  <small class="event-date" :class="dateTextClass(event.status)">{{ event.created_at }}</small>
                </div>
              </div>
              <div>
                <span :class="['badge me-3', badgeClass(event.status)]">{{ event.status }}</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" stroke="#94A3B8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 4 12 9 7 14"/></svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import axios from 'axios';
import AdminSidebar from '../../components/AdminSidebar.vue';

const searchQuery = ref('');
const events = ref([]);
const loading = ref(false);
const error = ref(null);

const sidebarOpen = ref(false);
const isMobile = ref(false);

function handleResize() {
  isMobile.value = window.innerWidth < 992;
  if (!isMobile.value) sidebarOpen.value = false;
}
function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value;
}

onMounted(() => {
  handleResize();
  window.addEventListener('resize', handleResize);
  fetchEvents();
});
onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});

async function fetchEvents() {
  loading.value = true;
  error.value = null;
  try {
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Authentication token not found.');
    const response = await axios.get('http://127.0.0.1:5000/api/admin/events', {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    // Add status for demo: alternate status for variety
    const statusArr = ['Active', 'Completed', 'Upcoming'];
    events.value = (response.data.events || []).map((e, i) => ({
      ...e,
      status: statusArr[i % statusArr.length]
    }));
  } catch (err) {
    error.value = 'Failed to fetch events.';
    console.error(err);
  } finally {
    loading.value = false;
  }
}

const filteredEvents = computed(() => {
  return events.value.filter(event =>
    event.title && event.title.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const badgeClass = (status) => {
  switch (status) {
    case 'Active': return 'bg-success text-white';
    case 'Completed': return 'bg-secondary text-white';
    case 'Upcoming': return 'bg-primary text-white';
    default: return 'bg-light text-dark';
  }
};
const iconBgClass = (status) => {
  switch (status) {
    case 'Active': return 'bg-success bg-opacity-10';
    case 'Completed': return 'bg-secondary bg-opacity-10';
    case 'Upcoming': return 'bg-primary bg-opacity-10';
    default: return 'bg-light';
  }
};
const dateTextClass = (status) => {
  switch (status) {
    case 'Active': return 'text-success';
    case 'Completed': return 'text-secondary';
    case 'Upcoming': return 'text-primary';
    default: return 'text-muted';
  }
};
</script>
<style scoped>
.admin-dashboard-responsive {
  font-family: 'Inter', sans-serif;
  background-color: #16161A;
  color: #FFFFFF;
  min-height: 100vh;
  position: relative;
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
.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.3);
  z-index: 999;
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
.event-card {
  background-color: #23232a !important;
  border: 1px solid #3A3A43 !important;
  border-radius: 0.75rem !important;
  color: #fff !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.event-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.event-date {
  font-size: 0.9rem;
  font-weight: 500;
}
</style>
