<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const fullName = ref('');
const username = ref('');
const email = ref('');
const password = ref('');
const error = ref(null);
const successMessage = ref(null);
const isLoading = ref(false);

async function register() {
  error.value = null;
  successMessage.value = null;
  isLoading.value = true;
  try {
    // *** CRITICAL FIX: The URL now points to the correct blueprint route ***
    const response = await axios.post('http://127.0.0.1:5000/api/auth/register', {
      full_name: fullName.value,
      username: username.value,
      email: email.value,
      password: password.value,
    });
    successMessage.value = `${response.data.message} Redirecting to login...`;
    setTimeout(() => {
      router.push('/login');
    }, 2000);
  } catch (err) {
    error.value = err.response?.data?.message || 'Registration failed. Please try again.';
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <div class="d-flex vh-100 auth-container">
    <div class="w-50 logo-panel d-none d-md-flex justify-content-center align-items-center">
      <h1 class="logo-text">Quizzy</h1>
    </div>
    <div class="w-100 w-md-50 form-panel d-flex flex-column justify-content-center">
      <h3 class="fw-bold">Create Account</h3>
      <p class="text-muted">Start your journey with us.</p>
      <form class="mt-4" @submit.prevent="register">
        <div class="row">
          <div class="mb-3 col">
            <label class="form-label">Full Name</label>
            <input type="text" class="form-control" placeholder="John Doe" v-model="fullName" required />
          </div>
          <div class="mb-3 col">
            <label class="form-label">Username</label>
            <input type="text" class="form-control" placeholder="johndoe" v-model="username" required />
          </div>
        </div>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input type="email" class="form-control" placeholder="name@example.com" v-model="email" required />
        </div>
        <div class="mb-4">
          <label class="form-label">Password</label>
          <input type="password" class="form-control" placeholder="********" v-model="password" required />
        </div>
        <div v-if="error" class="alert alert-danger">{{ error }}</div>
        <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
        <button class="btn btn-purple w-100 mb-3" type="submit" :disabled="isLoading">
          {{ isLoading ? 'Signing Up...' : 'Sign Up' }}
        </button>
      </form>
      <p class="text-center text-muted bottom-link">
        Already have an account?
        <router-link to="/login">Login</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.w-md-50 { width: 50% !important; }
@media (max-width: 768px) {
  .form-panel { padding: 0 2rem; }
  .w-100 { width: 100% !important; }
}
</style>
