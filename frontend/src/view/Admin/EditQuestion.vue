<template>
  <div class="container-fluid bg-dark text-white min-vh-100 p-4">
    <!-- Header -->
    <div class="d-flex justify-content-between align-items-start mb-4">
      <div class="d-flex gap-3 align-items-center">
        <button class="btn btn-outline-light rounded-circle p-2">
          <i class="bi bi-arrow-left"></i>
        </button>
        <div>
          <h4 class="fw-bold mb-0">Create New Quiz</h4>
          <small class="text-muted">Add questions, set answers and configure quiz settings</small>
        </div>
      </div>
      <button class="btn btn-purple px-4">Save</button>
    </div>

    <!-- Quiz Questions Section -->
    <div class="mb-4">
      <h5 class="fw-semibold mb-1">Quiz Questions</h5>
      <small class="text-muted">Create and manage your quiz questions</small>
    </div>

    <!-- Question Box -->
    <div class="bg-black rounded shadow-sm p-4 mb-4">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h6 class="mb-0 fw-bold">Question 1</h6>
        <div class="d-flex align-items-center gap-2">
          <span class="text-white">Points:</span>
          <input type="number" class="form-control form-control-sm bg-dark text-white border-secondary"
                 style="width: 80px;" v-model="question.points" />
          <select class="form-select form-select-sm bg-dark text-white border-secondary" style="width: 160px;"
                  v-model="question.type">
            <option>Multiple Choice</option>
            <option>Single Answer</option>
          </select>
          <button class="btn btn-link text-danger p-0 fs-5"><i class="bi bi-trash"></i></button>
        </div>
      </div>

      <!-- Question Text -->
      <div class="mb-3">
        <label class="form-label text-white">Question Text</label>
        <textarea rows="3" class="form-control bg-dark text-white border-secondary"
                  placeholder="Enter your question..." v-model="question.text" />
      </div>

      <!-- Answer Options -->
      <div>
        <label class="form-label text-white">Answer Options</label>
        <div class="form-check" v-for="(option, index) in question.options" :key="index">
          <input
            class="form-check-input bg-dark border-secondary"
            type="radio"
            :name="'answer'"
            :value="option"
            v-model="question.answer"
          />
          <label class="form-check-label text-white">
            {{ option }}
          </label>
        </div>
      </div>
    </div>

    <!-- Prev/Next Buttons -->
    <div class="d-flex justify-content-between">
      <button class="btn btn-outline-light">
        <i class="bi bi-arrow-left me-1"></i> Prev
      </button>
      <button class="btn btn-outline-light">
        Next <i class="bi bi-arrow-right ms-1"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const question = reactive({
  text: 'Which of the following is NOT a renewable energy source?',
  points: 10,
  type: 'Multiple Choice',
  answer: 'Natural Gas',
  options: ['Solar Power', 'Wind Power', 'Natural Gas', 'Hydroelectric Power']
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
