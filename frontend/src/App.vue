<script setup>
import { ref } from 'vue'
import LandingPage from './components/LandingPage.vue'
import LoginPage from './components/LoginPage.vue'
import RegisterPage from './components/RegisterPage.vue'

const currentPage = ref('landing')

function goTo(page) {
  currentPage.value = page
}
</script>

<template>
  <div>
    <LandingPage v-if="currentPage === 'landing'" @navigate="goTo" />
    <LoginPage v-else-if="currentPage === 'login'" @navigate="goTo" />
    <RegisterPage v-else-if="currentPage === 'register'" @navigate="goTo" />
  </div>
</template>
