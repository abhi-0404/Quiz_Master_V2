<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="logo-icon"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><line x1="10" y1="9" x2="8" y2="9"></line></svg>
      <span class="logo-text">Quizzy</span>
    </div>
    <nav class="nav-menu">
      <router-link to="/admin/dashboard" class="nav-item" active-class="active" :exact="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
        <span>Dashboard</span>
      </router-link>
      <router-link to="/admin/create-quiz" class="nav-item" active-class="active" :exact="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v15H6.5A2.5 2.5 0 0 1 4 14.5V4A2 2 0 0 1 6.5 2z"></path></svg>
        <span>Quizzes</span>
      </router-link>
      <router-link to="/admin/events" class="nav-item" active-class="active" :exact="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        <span>Events</span>
      </router-link>
      <router-link to="/admin/students" class="nav-item" active-class="active" :exact="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        <span>Students</span>
      </router-link>
      <router-link to="/admin/profile" class="nav-item" active-class="active" :exact="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        <span>Profile</span>
      </router-link>
    </nav>
  </aside>
</template>

<script setup>
// No script needed for static sidebar
</script>

<style scoped>
/* Sidebar */
.sidebar {
  width: 260px;
  background-color: #1E1E24;
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
  color: #6E56F1;
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
  color: #94A3B8;
  text-decoration: none;
  transition: all 0.3s ease;
}

.nav-menu .nav-item:hover {
  background-color: #24242C;
  color: #FFFFFF;
}

.nav-menu .nav-item.active {
  background-color: #6E56F1;
  color: #FFFFFF;
  font-weight: 500;
}

.nav-icon {
  width: 20px;
  height: 20px;
  margin-right: 1rem;
}
</style>
