<!-- components/RegisterPage.vue -->
<template>
  <div class="d-flex vh-100">
    <div class="w-50 bg-dark grid-bg d-flex justify-content-center align-items-center">
      <h1 class="text-gradient fw-bold display-5">Quizzy</h1>
    </div>
    <div class="w-50 d-flex flex-column justify-content-center px-5">
      <h3 class="fw-bold">Create Account</h3>
      <p class="text-muted">Choose your account type and start your journey with us</p>

      <form class="mt-4">
        <div class="row">
          <div class="mb-3 col">
            <label class="form-label">Full Name</label>
            <input type="text" class="form-control" placeholder="John Doe" />
          </div>
          <div class="mb-3 col">
            <label class="form-label">Username</label>
            <input type="text" class="form-control" placeholder="John Doe" />
          </div>
        </div>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input type="email" class="form-control" placeholder="name@example.com" />
        </div>
        <div class="mb-4">
          <label class="form-label">Password</label>
          <input type="password" class="form-control" placeholder="********" />
        </div>
        <button class="btn btn-purple w-100 mb-3" type="submit">Sign Up</button>
      </form>

      <p class="text-center text-muted">
        Already have an account?
        <a href="#" @click.prevent="$emit('navigate', 'login')">Sign In</a>
      </p>
    </div>
  </div>
</template>
