<template>
  <div class="container-fluid bg-dark text-white min-vh-100 p-4">
    <!-- Header -->
    <div class="d-flex justify-content-between align-items-start mb-4">
      <div>
        <h4 class="fw-bold mb-0">{{ quizData.quiz_name }}</h4>
        <small class="text-muted">About Quiz</small>
      </div>
      <div>
        <input type="datetime-local" class="form-control bg-dark text-white border-secondary" />
      </div>
    </div>

    <!-- Stats Grid -->
    <div class="bg-black rounded shadow-sm p-4 mb-4">
      <div class="row text-center mb-3">
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Subject</label>
          <div class="form-control bg-dark text-white">{{ quizData.subject }}</div>
        </div>
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Chapter</label>
          <div class="form-control bg-dark text-white">{{ quizData.chapter }}</div>
        </div>
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Total Questions</label>
          <div class="form-control bg-dark text-white">{{ quizData.total_questions }}</div>
        </div>
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Difficulty Level</label>
          <div class="form-control bg-dark text-white">{{ quizData.difficulty }}</div>
        </div>
      </div>

      <!-- Chapter Dropdown Blocks -->
      <div v-for="(chapter, index) in quizData.chapters" :key="chapter.id" class="mb-3">
        <button
          class="btn btn-dark w-100 text-start d-flex justify-content-between align-items-center mb-2"
          @click="toggle(index)"
        >
          <span>{{ chapter.name }}</span>
          <i :class="expanded[index] ? 'bi bi-chevron-up' : 'bi bi-chevron-down'"></i>
        </button>
        <div v-if="expanded[index]" class="ms-3">
          <div class="form-control bg-dark text-white d-flex justify-content-between mb-2">
            <span>Questions</span>
            <span class="text-muted">{{ chapter.questions }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="d-flex justify-content-end gap-2">
      <button class="btn btn-outline-light">Close</button>
      <button class="btn btn-purple px-4">Start</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const quizId = ref(route.params.quiz_id || route.query.quiz_id || null)
const loading = ref(false)
const error = ref(null)

const quizData = ref({
  quiz_name: '',
  subject: '',
  chapter: '',
  total_questions: 0,
  difficulty: '',
  chapters: []
})
const expanded = ref([])

async function fetchQuizData() {
  if (!quizId.value) return
  loading.value = true
  error.value = null
  try {
    const token = localStorage.getItem('authToken')
    const res = await axios.get(`http://127.0.0.1:5000/api/student/about-quiz/${quizId.value}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    quizData.value = res.data
    expanded.value = quizData.value.chapters.map(() => false)
  } catch (e) {
    error.value = 'Failed to load quiz info.'
  } finally {
    loading.value = false
  }
}

function toggle(index) {
  expanded.value[index] = !expanded.value[index]
}

onMounted(() => {
  fetchQuizData()
})
</script>

<style scoped>
.btn-purple {
  background-color: #9f42f9;
  color: white;
  border: none;
}
.btn-purple:hover {
  background-color: #892be2;
}
</style>

