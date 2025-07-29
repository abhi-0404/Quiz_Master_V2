<template>
  <div class="d-flex">
    <AdminSidebar />
    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <header class="main-header d-flex justify-content-between align-items-center">
        <div>
          <h1 class="page-title">Students</h1>
          <p class="page-subtitle">Manage your students and track their progress</p>
        </div>
        <button class="btn btn-primary invite-btn">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="17" y1="11" x2="23" y2="11"></line></svg>
          Invite Students
        </button>
      </header>

      <!-- Student Directory Section -->
      <section class="student-directory">
        <div class="card-header d-flex justify-content-between align-items-center">
          <div>
              <h2 class="section-title">Student Directory</h2>
              <p class="section-subtitle">View and manage all your students</p>
          </div>
        </div>
        <div class="card-filters d-flex justify-content-between align-items-center">
            <div class="tabs">
                <button class="tab-btn active">All Students</button>
                <button class="tab-btn">10A</button>
                <button class="tab-btn">10B</button>
            </div>
            <div class="d-flex gap-3">
                <div class="search-wrapper">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                  <input type="text" class="search-input" placeholder="Search students...">
                </div>
                <select class="form-select filter-select">
                    <option selected>Name</option>
                    <option value="1">Score (High to Low)</option>
                    <option value="2">Score (Low to High)</option>
                </select>
            </div>
        </div>
        <div class="students-table-wrapper">
          <table class="table">
              <thead>
                  <tr>
                      <th>Name</th>
                      <th>Quizzes Taken</th>
                      <th>Average Score</th>
                      <th>Average Time</th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="student in students" :key="student.name">
                      <td>
                          <div class="d-flex align-items-center">
                              <img :src="student.avatar" class="avatar me-3" alt="avatar">
                              <span>{{ student.name }}</span>
                          </div>
                      </td>
                      <td>{{ student.quizzesTaken }}</td>
                      <td>{{ student.avgScore }}%</td>
                      <td>{{ student.avgTime }}%</td>
                  </tr>
              </tbody>
          </table>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import AdminSidebar from '../../components/AdminSidebar.vue';

const students = ref([]);
const loading = ref(false);
const error = ref(null);

async function fetchStudents() {
  loading.value = true;
  error.value = null;
  try {
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Authentication token not found.');
    const response = await axios.get('http://127.0.0.1:5000/api/admin/students', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    console.log(response.data);
    students.value = response.data.students || [];
  } catch (err) {
    error.value = 'Failed to fetch students.';
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchStudents();
});
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

.invite-btn {
  background-color: #6E56F1;
  border: none;
  border-radius: 0.5rem;
  padding: 0.75rem 1.25rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.invite-btn:hover {
  background-color: #5a43d1;
}

.student-directory {
    background-color: #24242C;
    border: 1px solid #3A3A43;
    border-radius: 0.75rem;
}

.card-header {
    padding: 1.5rem;
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

.card-filters {
    padding: 0 1.5rem 1.5rem;
    border-bottom: 1px solid #3A3A43;
}

.tabs .tab-btn {
    background: none;
    border: none;
    color: #94A3B8;
    padding: 0.5rem 1rem;
    font-weight: 500;
    border-radius: 0.5rem;
}
.tabs .tab-btn.active {
    background-color: #3A3A43;
    color: #FFFFFF;
}

.search-wrapper {
  position: relative;
}
.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #94A3B8;
}
.search-input, .filter-select {
  background-color: #1E1E24;
  border: 1px solid #3A3A43;
  border-radius: 0.5rem;
  color: #FFFFFF;
  padding: 0.6rem 1rem;
  transition: all 0.3s ease;
}
.search-input {
  padding-left: 2.5rem;
  width: 220px;
}
.filter-select {
    width: 180px;
}
.search-input::placeholder { color: #94A3B8; }
.search-input:focus, .filter-select:focus {
  outline: none;
  border-color: #6E56F1;
  box-shadow: 0 0 0 2px rgba(110, 86, 241, 0.2);
  background-color: #1E1E24;
  color: #FFFFFF;
}

.students-table-wrapper {
    padding: 0 1rem;
}
.table {
    color: #FFFFFF;
    margin-bottom: 0; /* Remove default bottom margin */
}
.table thead th {
    border-bottom: 1px solid #3A3A43;
    border-top: none;
    color: #94A3B8;
    font-weight: 500;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.table tbody td {
    vertical-align: middle;
    border-color: #3A3A43;
    padding-top: 1rem;
    padding-bottom: 1rem;
}
.table tbody tr:last-child td {
    border-bottom: none;
}
.avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
}
</style>
