<template>
  <!-- Main Content -->
  <main class="main-content flex-grow-1">
    <header class="main-header d-flex justify-content-between align-items-center">
      <div>
        <h1 class="page-title">Create New Quiz</h1>
        <p class="page-subtitle">Fill out the details below to create a new quiz</p>
      </div>
      <!-- The router-link will take the user back to the main quizzes library -->
      <router-link to="/admin/quizzes" class="btn btn-secondary back-btn">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
        Back to Quiz Library
      </router-link>
    </header>

    <!-- Create Quiz Form Section -->
    <section class="create-quiz-form">
      <div class="card-body">
        <form @submit.prevent="createQuiz">
          <div class="mb-4">
            <label for="quizTitle" class="form-label">Quiz Title</label>
            <input type="text" id="quizTitle" class="form-control" v-model="quiz.title" placeholder="e.g., Introduction to Biology">
          </div>

          <div class="mb-4">
            <label for="quizDescription" class="form-label">Description</label>
            <textarea id="quizDescription" class="form-control" rows="3" v-model="quiz.description" placeholder="A short description of what this quiz covers"></textarea>
          </div>

          <div class="row">
            <div class="col-md-6 mb-4">
                <label for="quizCategory" class="form-label">Category / Subject</label>
                <select id="quizCategory" class="form-select" v-model="quiz.category">
                    <option disabled value="">Please select one</option>
                    <option>Biology</option>
                    <option>Mathematics</option>
                    <option>Chemistry</option>
                </select>
            </div>
            <div class="col-md-6 mb-4">
                <label for="quizDuration" class="form-label">Time Duration (minutes)</label>
                <input type="number" id="quizDuration" class="form-control" v-model="quiz.duration" placeholder="e.g., 20">
            </div>
          </div>

          <hr class="form-divider">

          <!-- This is where you will add questions later -->
          <h3 class="questions-title">Questions</h3>
          <div class="text-center p-5 border-dashed">
            <p class="text-muted">You can add questions after creating the quiz.</p>
          </div>

          <div class="d-flex justify-content-end gap-3 mt-5">
            <button type="button" class="btn btn-secondary">Save as Draft</button>
            <button type="submit" class="btn btn-primary publish-btn">Create & Publish Quiz</button>
          </div>
        </form>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue';

// Form data for the new quiz
const quiz = ref({
  title: '',
  description: '',
  category: '',
  duration: null,
});

const createQuiz = () => {
    // Logic to send the quiz data to the backend will be added here
    console.log('Creating quiz...', quiz.value);
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

.back-btn, .publish-btn {
  border-radius: 0.5rem;
  padding: 0.75rem 1.25rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.back-btn {
    background-color: #3A3A43;
    border-color: #555;
    color: #FFFFFF;
}

.publish-btn {
    background-color: #6E56F1;
    border: none;
}
.publish-btn:hover {
    background-color: #5a43d1;
}


.create-quiz-form {
    background-color: #24242C;
    border: 1px solid #3A3A43;
    border-radius: 0.75rem;
}

.card-body {
    padding: 2rem;
}

.form-label {
    color: #94A3B8;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    font-weight: 500;
}

.form-control, .form-select {
  background-color: #1E1E24;
  border: 1px solid #3A3A43;
  border-radius: 0.5rem;
  color: #FFFFFF;
  padding: 0.75rem 1rem;
  transition: all 0.3s ease;
}

.form-control::placeholder {
    color: #5a5a6a;
}

.form-control:focus, .form-select:focus {
  outline: none;
  border-color: #6E56F1;
  box-shadow: 0 0 0 2px rgba(110, 86, 241, 0.2);
  background-color: #1E1E24;
  color: #FFFFFF;
}

.form-divider {
    border-color: #3A3A43;
    margin: 2rem 0;
}

.questions-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
}

.border-dashed {
    border: 2px dashed #3A3A43;
    border-radius: 0.5rem;
}
</style>
