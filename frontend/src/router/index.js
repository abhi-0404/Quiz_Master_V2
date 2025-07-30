// src/router/index.js or wherever you define your routes

import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../view/LandingPage.vue';
import LoginPage from '../view/LoginPage.vue';
import RegisterPage from '../view/RegisterPage.vue';
import AdminDashboard from '../view/Admin/AdminDashboard.vue';
import EventsPage from '../view/Admin/EventsPage.vue';
import QuizPage from '../view/Admin/QuizPage.vue';
import ProfilePage from '../view/Admin/ProfilePage.vue';
import StudentsPage from '../view/Admin/StudentsPage.vue';
import StudentDashboard from '../view/Student/StudentDashboard.vue';
import AboutQuiz from '../view/Student/AboutQuiz.vue';
import QuizesLibrary from '../view/Student/QuizesLibrary.vue';
import StartQuiz from '../view/Student/QuizPage.vue';
import QuizResult from '../view/Student/QuizResult.vue';

const routes = [
  { path: '/', name: 'Landing', component: LandingPage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },

  // Admin routes
  { path: '/admin/dashboard', name: 'AdminDashboard', component: AdminDashboard, meta: { requiresAuth: true, role: 'admin' } },
  { path: '/admin/events', name: 'EventsPage', component: EventsPage, meta: { requiresAuth: true, role: 'admin' } },
  { path: '/admin/quizes', name: 'QuizPage', component: QuizPage, meta: { requiresAuth: true, role: 'admin' } },
  { path: '/admin/profile', name: 'ProfilePage', component: ProfilePage, meta: { requiresAuth: true, role: 'admin' } },
  { path: '/admin/students', name: 'StudentsPage', component: StudentsPage, meta: { requiresAuth: true, role: 'admin' } },

  // Student routes
  { path: '/student/dashboard', name: 'StudentDashboard', component: StudentDashboard, meta: { requiresAuth: true, role: 'student' } },
  { path: '/student/about-quiz', name: 'AboutQuiz', component: AboutQuiz, meta: { requiresAuth: true, role: 'student' } },
  { path: '/student/quizzes', name: 'QuizesLibrary', component: QuizesLibrary, meta: { requiresAuth: true, role: 'student' } },
  { path: '/student/result', name: 'QuizResult', component: QuizResult, meta: { requiresAuth: true, role: 'student' } },
  { path: '/student/start-quiz', name: 'StartQuiz', component: StartQuiz, meta: { requiresAuth: true, role: 'student' } },
  // Add more student routes as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// ✅ Global navigation guard
router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('authToken');
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !loggedIn) {
    next({ name: 'Login' }); // ✅ Use name instead of path
  } else if (requiresAuth && loggedIn) {
    try {
      const tokenPayload = JSON.parse(atob(loggedIn.split('.')[1]));
      const userRole = tokenPayload.sub?.role;

      if (to.meta.role && to.meta.role !== userRole) {
        // ✅ Role mismatch fallback
        if (userRole === 'admin') {
          next({ name: 'AdminDashboard' });
        } else {
          next({ name: 'StudentDashboard' });
        }
      } else {
        next(); // ✅ Role matches
      }
    } catch (e) {
      localStorage.removeItem('authToken');
      next({ name: 'Login' });
    }
  } else {
    next(); // ✅ No auth required
  }
});

export default router;
