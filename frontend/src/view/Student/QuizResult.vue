<template>
  <div class="container-fluid bg-dark text-white min-vh-100 p-4">
    <!-- Header -->
    <div class="d-flex justify-content-between align-items-start mb-4">
      <div>
        <h4 class="fw-bold mb-0">{{ quizResult.quiz_name || 'Quiz Name' }}</h4>
        <small class="text-muted">About Quiz</small>
      </div>
      <div>
        <input type="datetime-local" class="form-control bg-dark text-white border-secondary" :value="quizResult.completed_at ? formatDateTimeLocal(quizResult.completed_at) : ''" disabled />
      </div>
    </div>

    <!-- Stats Row -->
    <div class="bg-black rounded shadow-sm p-4 mb-4">
      <div class="row text-center mb-3">
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Subject</label>
          <div class="form-control bg-dark text-white">{{ quizResult.subject || '-' }}</div>
        </div>
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Chapter</label>
          <div class="form-control bg-dark text-white">{{ quizResult.chapter || '-' }}</div>
        </div>
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Total Marks</label>
          <div class="form-control bg-dark text-white">{{ quizResult.total_marks ?? '-' }}</div>
        </div>
        <div class="col-md-3 mb-2">
          <label class="form-label text-muted">Obtained Marks</label>
          <div class="form-control bg-dark text-white">{{ quizResult.total_scored ?? '-' }}</div>
        </div>
      </div>

      <!-- Quiz Accordion -->
      <div class="accordion" id="quizAccordion">
        <div class="accordion-item bg-dark text-white border-secondary">
          <h2 class="accordion-header" id="headingQuiz">
            <button
              class="accordion-button bg-dark text-white collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseQuiz"
            >
              {{ quizResult.quiz_name || 'Quiz Name' }} <span class="ms-auto text-muted">Total Marks: {{ quizResult.total_marks ?? '00' }}</span>
            </button>
          </h2>
          <div
            id="collapseQuiz"
            class="accordion-collapse collapse"
            data-bs-parent="#quizAccordion"
          >
            <div class="accordion-body">
              <!-- Subjects -->
              <div class="accordion" id="subjectAccordion">
                <div
                  v-for="(subject, sIndex) in quizResult.subjects"
                  :key="sIndex"
                  class="accordion-item bg-dark text-white border-secondary mb-2"
                >
                  <h2 class="accordion-header" :id="`headingSubject${sIndex}`">
                    <button
                      class="accordion-button bg-dark text-white collapsed"
                      type="button"
                      data-bs-toggle="collapse"
                      :data-bs-target="`#collapseSubject${sIndex}`"
                    >
                      {{ subject.name || 'Subject' }}
                    </button>
                  </h2>
                  <div
                    :id="`collapseSubject${sIndex}`"
                    class="accordion-collapse collapse"
                    :data-bs-parent="`#subjectAccordion`"
                  >
                    <div class="accordion-body">
                      <div
                        v-for="(chapter, cIndex) in subject.chapters"
                        :key="cIndex"
                        class="form-control bg-dark text-white d-flex justify-content-between mb-2"
                      >
                        <span>{{ chapter.name }}</span>
                        <span class="text-muted">Marks: {{ chapter.marks }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- End Subjects -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="d-flex justify-content-end">
      <button class="btn btn-outline-light" @click="$router.back()">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const quizResult = ref({
  quiz_name: '',
  subject: '',
  chapter: '',
  total_marks: 0,
  total_scored: 0,
  completed_at: '',
  subjects: []
})

function formatDateTimeLocal(dateStr) {
  if (!dateStr) return ''
  const d = new Date(dateStr)
  const pad = n => n.toString().padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`
}

onMounted(async () => {
  const quizId = route.params.quiz_id || route.params.id
  if (!quizId) return
  try {
    // Fetch quiz result details for this quiz
    const res = await axios.get(`/api/student/quiz-result/${quizId}`)
    if (res.data && res.data.result) {
      quizResult.value = res.data.result
    }
  } catch (err) {
    // handle error
    console.error(err)
  }
})
</script>

<style scoped>
.accordion-button:not(.collapsed) {
  box-shadow: none;
}
</style>
