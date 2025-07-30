<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const email = ref('');
const password = ref('');
const error = ref(null);
const isLoading = ref(false);

function decodeToken(token) {
  try {
    const payload = token.split('.')[1];
    return JSON.parse(atob(payload));
  } catch (e) {
    return null;
  }
}

async function login() {
  error.value = null;
  isLoading.value = true;
  try {
    const response = await axios.post('http://127.0.0.1:5000/api/auth/login', {
      email: email.value,
      password: password.value,
    });
    console.log(response.data)
    const token = response.data.access_token;
    if (!token) throw new Error("Token not received from server");

    localStorage.setItem('authToken', token);
    const payload = decodeToken(token);
    if (!payload || !payload.sub || !payload.sub.role) throw new Error("Invalid token payload");

    const role = payload.sub.role.toLowerCase();
    if (role === 'admin') {
      router.push('/admin/dashboard');
    } else if (role === 'student') {
      router.push('/student/dashboard');
    }
  } catch (err) {
    console.error('Login failed:', err);
    if (err.response) {
      error.value = err.response.data.message || 'Invalid credentials.';
    } else if (err.request) {
      error.value = 'Cannot connect to backend server.';
    } else {
      error.value = err.message || 'Login failed.';
    }
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
      <h3 class="fw-bold">Welcome Back!</h3>
      <p class="text-muted">Enter your credentials to access your account.</p>
      <form class="mt-4" @submit.prevent="login">
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" id="email" class="form-control" placeholder="name@example.com" v-model="email" required />
        </div>
        <div class="mb-4">
          <label for="password" class="form-label">Password</label>
          <input type="password" id="password" class="form-control" placeholder="********" v-model="password" required />
        </div>
        <div v-if="error" class="alert alert-danger">{{ error }}</div>
        <button class="btn btn-purple w-100 mb-3" type="submit" :disabled="isLoading">
          {{ isLoading ? 'Signing In...' : 'Sign In' }}
        </button>
      </form>
      <p class="text-center text-muted bottom-link">
        Don’t have an account?
        <router-link to="/register">Sign Up</router-link>
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
