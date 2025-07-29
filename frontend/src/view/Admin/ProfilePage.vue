<template>
  <div class="d-flex">
    <AdminSidebar />
    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <header class="main-header">
        <div>
          <h1 class="page-title">Profile</h1>
          <p class="page-subtitle">Manage your account Profile</p>
        </div>
      </header>

      <!-- Profile Information Section -->
      <section class="profile-section">
        <div class="card-header">
          <div>
              <h2 class="section-title">Profile Information</h2>
              <p class="section-subtitle">Update your account's profile information and public details</p>
          </div>
        </div>
        <div class="card-body">
          <div class="row">
              <!-- Avatar Section -->
              <div class="col-md-2 text-center">
                  <img :src="profile.avatar" class="avatar-img mb-3" alt="avatar">
                  <button class="btn btn-sm btn-change-photo">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
                      Change Photo
                  </button>
              </div>
              <!-- Form Fields Section -->
              <div class="col-md-10">
                  <form @submit.prevent="saveProfile">
                      <div class="row">
                          <div class="col-md-6 mb-3">
                              <label for="firstName" class="form-label">First Name</label>
                              <input type="text" id="firstName" class="form-control" v-model="profile.firstName">
                          </div>
                          <div class="col-md-6 mb-3">
                              <label for="lastName" class="form-label">Last Name</label>
                              <input type="text" id="lastName" class="form-control" v-model="profile.lastName">
                          </div>
                      </div>
                      <div class="row">
                          <div class="col-md-6 mb-3">
                              <label for="email" class="form-label">Email</label>
                              <input type="email" id="email" class="form-control" v-model="profile.email">
                          </div>
                          <div class="col-md-6 mb-3">
                              <label for="role" class="form-label">Role</label>
                              <input type="text" id="role" class="form-control" v-model="profile.role" disabled>
                          </div>
                      </div>
                      <div class="mb-4">
                          <label for="bio" class="form-label">Bio</label>
                          <textarea id="bio" class="form-control" rows="4" v-model="profile.bio"></textarea>
                      </div>
                      <div class="d-flex justify-content-end">
                          <button type="submit" class="btn btn-primary save-changes-btn">Save Changes</button>
                      </div>
                  </form>
              </div>
          </div>
        </div>
      </section>
      
      <footer class="text-center mt-4">
          <p class="footer-text">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
              Need help with your account settings? <a href="#">Contact Support</a>
          </p>
      </footer>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import AdminSidebar from '../../components/AdminSidebar.vue';


const profile = ref({});
const loading = ref(false);
const error = ref(null);

async function fetchProfile() {
  loading.value = true;
  error.value = null;
  try {
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Authentication token not found.');
    const response = await axios.get('http://127.0.0.1:5000/api/admin/profile', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    console.log(response.data);
    profile.value = response.data.profile || {};
  } catch (err) {
    error.value = 'Failed to fetch profile.';
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchProfile();
});

const saveProfile = () => {
    // Logic to save profile changes will be added here later
    console.log('Saving profile...', profile.value);
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

.profile-section {
    background-color: #24242C;
    border: 1px solid #3A3A43;
    border-radius: 0.75rem;
}

.card-header {
    padding: 1.5rem;
    border-bottom: 1px solid #3A3A43;
}

.card-body {
    padding: 2rem;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}
.section-subtitle {
  color: #94A3B8;
  font-size: 0.9rem;
  margin-top: 0.25rem;
  margin-bottom: 0;
}

.avatar-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 3px solid #3A3A43;
}

.btn-change-photo {
    background-color: #3A3A43;
    border: 1px solid #555;
    color: #FFFFFF;
    font-size: 0.85rem;
    font-weight: 500;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.form-label {
    color: #94A3B8;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.form-control {
  background-color: #1E1E24;
  border: 1px solid #3A3A43;
  border-radius: 0.5rem;
  color: #FFFFFF;
  padding: 0.75rem 1rem;
  transition: all 0.3s ease;
}

.form-control:disabled {
    background-color: #2a2a33;
    color: #777;
}

.form-control:focus {
  outline: none;
  border-color: #6E56F1;
  box-shadow: 0 0 0 2px rgba(110, 86, 241, 0.2);
  background-color: #1E1E24;
  color: #FFFFFF;
}

.save-changes-btn {
  background-color: #6E56F1;
  border: none;
  border-radius: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-weight: 500;
}

.save-changes-btn:hover {
  background-color: #5a43d1;
}

.footer-text {
    color: #94A3B8;
    font-size: 0.9rem;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}
.footer-text a {
    color: #6E56F1;
    text-decoration: none;
    font-weight: 500;
}
.footer-text a:hover {
    text-decoration: underline;
}
</style>
