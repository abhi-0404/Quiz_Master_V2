import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Import the router
import './style.css'
import './assets/auth.css'

const app = createApp(App)
app.use(router) // Tell the app to use the router
app.mount('#app')
