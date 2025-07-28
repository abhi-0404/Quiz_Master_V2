// src/router/index.js or wherever you define your routes

import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../view/LandingPage.vue';
import LoginPage from '../view/LoginPage.vue';
import RegisterPage from '../view/RegisterPage.vue';
import AdminDashboard from '../view/AdminDashboard.vue';
import StudentDashboard from '../view/StudentDashboard.vue';

const routes = [
  { path: '/', name: 'Landing', component: LandingPage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  {
    path: '/admin/dashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true, role: 'admin' }   // ✅ Added
  },
  {
    path: '/student/dashboard',
    name: 'StudentDashboard',
    component: StudentDashboard,
    meta: { requiresAuth: true, role: 'student' } // ✅ Added
  }
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
      const userRole = tokenPayload.role;

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
