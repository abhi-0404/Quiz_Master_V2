<template>
  <div>
    <!-- Hamburger for mobile -->
    <button class="sidebar-toggle" @click="$emit('toggle')" v-if="showToggle">
      <svg width="24" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <transition name="sidebar-slide">
      <aside class="sidebar" :class="{ 'sidebar-mobile': isMobile, 'sidebar-open': isOpen }" v-show="!isMobile || isOpen">
        <div class="sidebar-header">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="logo-icon"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><line x1="10" y1="9" x2="8" y2="9"></line></svg>
          <span class="logo-text">Quizzy</span>
        </div>
        <nav class="nav-menu">
          <router-link :to="{ name: 'StudentDashboard' }" class="nav-item" active-class="active" :exact="false">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            <span>Dashboard</span>
          </router-link>
          <router-link :to="{ name: 'QuizesLibrary' }" class="nav-item" active-class="active" :exact="false">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v15H6.5A2.5 2.5 0 0 1 4 14.5V4A2 2 0 0 1 6.5 2z"></path></svg>
            <span>Quizzes</span>
          </router-link>
          <router-link :to="{ name: 'AboutQuiz' }" class="nav-item" active-class="active" :exact="false">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span>Events</span>
          </router-link>
          <router-link :to="{ name: 'QuizResult' }" class="nav-item" active-class="active" :exact="false">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            <span>Result</span>
          </router-link>
          <router-link to="/student/profile" class="nav-item" active-class="active" :exact="false">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="nav-icon"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            <span>Profile</span>
          </router-link>
        </nav>
      </aside>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, defineProps, defineEmits } from 'vue';
const props = defineProps({
  isOpen: Boolean,
});
const emit = defineEmits(['toggle']);
const isMobile = ref(false);
const showToggle = ref(false);

function handleResize() {
  isMobile.value = window.innerWidth < 992;
  showToggle.value = isMobile.value;
}
onMounted(() => {
  handleResize();
  window.addEventListener('resize', handleResize);
});
onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped>
/* Sidebar */
 .sidebar {
  min-width: 180px;
  max-width: 320px;
  flex-basis: 18vw;
  background-color: #1E1E24;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  min-height: 0;
  max-height: 100dvh;
  height: auto;
  position: relative;
  z-index: 1000;
  transition: left 0.3s, box-shadow 0.3s;
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
}
@media (max-width: 991px) {
  .sidebar {
    min-width: 120px;
    max-width: 100vw;
    flex-basis: 60vw;
    width: 100%;
    min-height: 0;
    max-height: 100dvh;
    height: auto;
  }
}
.sidebar::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
}
/* Search input style fix for white background */
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
.search-input {
  background-color: #24242C;
  border: 1px solid #3A3A43;
  border-radius: 0.5rem;
  color: #FFFFFF;
  padding: 0.6rem 1rem 0.6rem 2.5rem;
  width: 250px;
  transition: all 0.3s ease;
}
.search-input::placeholder {
  color: #94A3B8;
}
.search-input:focus {
  outline: none;
  border-color: #6E56F1;
  box-shadow: 0 0 0 2px rgba(110, 86, 241, 0.2);
}
.sidebar-mobile {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  box-shadow: 2px 0 16px rgba(0,0,0,0.2);
  background: #1E1E24;
  transform: translateX(-100%);
}
.sidebar-open.sidebar-mobile {
  transform: translateX(0);
}
.sidebar-toggle {
  display: none;
  position: fixed;
  top: 1.2rem;
  left: 1.2rem;
  z-index: 1100;
  background: none;
  border: none;
  cursor: pointer;
}
@media (max-width: 991px) {
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    z-index: 1000;
    transform: translateX(-100%);
    box-shadow: 2px 0 16px rgba(0,0,0,0.2);
  }
  .sidebar-open.sidebar-mobile {
    transform: translateX(0);
  }
  .sidebar-toggle {
    display: block;
  }
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
.sidebar-slide-enter-active, .sidebar-slide-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.sidebar-slide-enter-from, .sidebar-slide-leave-to {
  opacity: 0;
  transform: translateX(-100%);
}
</style>
