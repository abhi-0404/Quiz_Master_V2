<script setup>
import { ref } from 'vue'
import axios from 'axios'

const title = ref('')
const description = ref('')
const message = ref(null)
const error = ref(null)
const isLoading = ref(false)

const createQuiz = async () => {
  error.value = null
  message.value = null
  isLoading.value = true

  try {
    const token = localStorage.getItem('authToken')
    const response = await axios.post(
      'http://127.0.0.1:5000/api/quiz/create',
      {
        title: title.value,
        description: description.value,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    message.value = 'Quiz created successfully!'
    title.value = ''
    description.value = ''
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to create quiz'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="create-quiz-container">
    <h2>Create a New Quiz</h2>
    <form @submit.prevent="createQuiz">
      <div class="form-group">
        <label for="title">Quiz Title</label>
        <input
          type="text"
          id="title"
          v-model="title"
          placeholder="Enter quiz title"
          required
        />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea
          id="description"
          v-model="description"
          placeholder="Describe the quiz"
          required
        ></textarea>
      </div>
      <button type="submit" :disabled="isLoading">
        {{ isLoading ? 'Creating...' : 'Create Quiz' }}
      </button>
    </form>

    <p v-if="message" class="success">{{ message }}</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<style scoped>
.create-quiz-container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  background: #1e1e2f;
  border-radius: 12px;
  color: white;
  box-shadow: 0 0 10px rgba(0,0,0,0.4);
}
h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}
.form-group {
  margin-bottom: 1.2rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input, textarea {
  width: 100%;
  padding: 0.75rem;
  border: none;
  border-radius: 8px;
  background: #2d2d44;
  color: white;
}
textarea {
  resize: vertical;
  min-height: 100px;
}
button {
  width: 100%;
  padding: 0.8rem;
  background: linear-gradient(90deg, #9b51e0, #ff6b6b);
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  cursor: pointer;
}
.success {
  color: #6aff7d;
  margin-top: 1rem;
  text-align: center;
}
.error {
  color: #ff6b6b;
  margin-top: 1rem;
  text-align: center;
}
</style>
