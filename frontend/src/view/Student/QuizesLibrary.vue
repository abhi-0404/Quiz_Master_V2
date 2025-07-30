<template>
  <div class="d-flex student-dashboard-responsive quizes-library-root">
    <!-- Sidebar Navigation -->
    <aside class="sidebar sidebar-fixed">
      <StudentSidebar />
    </aside>

    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <div class="quiz-library-container bg-dark text-white min-vh-100 p-4">
        <div class="quiz-header d-flex justify-content-between align-items-center mb-3 flex-wrap">
          <div class="mb-2 mb-md-0">
            <h2 class="fw-bold mb-1">Quizzes</h2>
            <div class="text-muted">Create, manage and analyze your quizzes</div>
          </div>
          <div class="search-wrapper">
            <input v-model="search" type="text" class="form-control search-input" placeholder="Search..." />
          </div>
        </div>
        <div class="quiz-library-card bg-black rounded shadow-sm p-4 mt-4">
          <div class="mb-3">
            <h5 class="fw-bold mb-1">Quiz Library</h5>
            <div class="text-muted">Browse and manage all your quizzes</div>
          </div>
          <div v-if="filteredQuizzes.length === 0" class="text-center text-muted py-5">
            No quizzes found.
          </div>
          <div v-for="quiz in filteredQuizzes" :key="quiz.id" class="quiz-item d-flex align-items-center justify-content-between bg-dark rounded p-3 mb-3 flex-wrap flex-column flex-md-row">
            <div class="d-flex align-items-center flex-grow-1 mb-2 mb-md-0">
              <div class="quiz-icon d-flex align-items-center justify-content-center me-3">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#6E56F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 3v18"/><path d="M16 3v18"/></svg>
              </div>
              <div>
                <div class="fw-bold fs-5">{{ quiz.title }}</div>
                <div class="text-muted small">{{ quiz.description }}</div>
              </div>
            </div>
            <div class="d-flex align-items-center gap-2">
              <router-link :to="{ name: 'AboutQuiz', params: { quiz_id: quiz.id } }" class="btn btn-outline-light btn-sm">About</router-link>
              <router-link :to="{ name: 'StartQuiz', params: { quiz_id: quiz.id } }" class="btn btn-primary btn-sm">Start</router-link>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import StudentSidebar from '../../components/StudentSidebar.vue'

const quizzes = ref([])
const search = ref('')

onMounted(async () => {
  try {
    const res = await axios.get('/api/student/quizzes')
    if (res.data && res.data.quizzes) {
      quizzes.value = res.data.quizzes.map(q => ({
        ...q,
        description: q.description || 'Basic concepts of biology for beginners' // fallback
      }))
    }
  } catch (err) {
    // handle error
    quizzes.value = []
  }
})

const filteredQuizzes = computed(() => {
  if (!search.value) return quizzes.value
  return quizzes.value.filter(q =>
    q.title.toLowerCase().includes(search.value.toLowerCase()) ||
    (q.description && q.description.toLowerCase().includes(search.value.toLowerCase()))
  )
})
</script>

<style scoped>
.quizes-library-root {
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
.quiz-library-container {
  background: linear-gradient(120deg, #181824 0%, #1E1E24 100%);
  min-height: 100vh;
}
.quiz-header {
  flex-wrap: wrap;
  gap: 1rem;
}
.quiz-library-card {
  background: #181824;
  border-radius: 1rem;
  box-shadow: 0 2px 16px rgba(0,0,0,0.12);
}
.quiz-item {
  border: 1px solid #232336;
  transition: box-shadow 0.2s, border-color 0.2s;
  flex-wrap: wrap;
}
.quiz-item:hover {
  border-color: #6E56F1;
  box-shadow: 0 2px 12px rgba(110,86,241,0.08);
}
.quiz-icon {
  width: 48px;
  height: 48px;
  background: #232336;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.search-wrapper {
  position: relative;
  min-width: 180px;
  max-width: 260px;
  width: 100%;
}
.search-input {
  background-color: #232336;
  border: 1px solid #3A3A43;
  border-radius: 0.5rem;
  color: #FFFFFF;
  padding: 0.6rem 1rem;
  width: 100%;
  min-width: 120px;
  max-width: 260px;
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
.btn-primary {
  background: #6E56F1;
  border: none;
  color: #fff;
  font-weight: 500;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #7C5CFA;
}
.btn-outline-light {
  border: 1px solid #fff;
  color: #fff;
  background: transparent;
}
.btn-outline-light:hover {
  background: #fff;
  color: #181824;
}
@media (max-width: 991px) {
  .quizes-library-root {
    flex-direction: column;
  }
  .sidebar-fixed {
    position: static;
    width: 100%;
    height: auto;
    max-height: none;
    overflow-y: visible;
    z-index: auto;
  }
  .main-content {
    padding: 1rem 0.5rem;
  }
  .quiz-library-container {
    padding: 1rem 0.5rem;
  }
  .quiz-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  .quiz-item {
    flex-direction: column;
    align-items: flex-start !important;
    gap: 0.5rem;
  }
  .search-wrapper {
    width: 100%;
    max-width: 100%;
    margin-top: 0.5rem;
  }
}
</style>
