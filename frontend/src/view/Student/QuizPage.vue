<template>
  <div class="container-fluid bg-dark text-white min-vh-100 py-4 px-5">
    <div class="text-center mb-3">
      <h5>Quiz Name</h5>
    </div>

    <!-- Progress & Meta -->
    <div class="d-flex justify-content-between align-items-center mb-2">
      <span>Question 1 of 10</span>
      <span>10% Complete</span>
    </div>
    <div class="progress mb-4" style="height: 4px;">
      <div class="progress-bar bg-purple" role="progressbar" style="width: 10%;"></div>
    </div>

    <!-- Question Card -->
    <div class="card bg-black text-white border-0 p-4 mb-4">
      <div class="d-flex justify-content-between align-items-center mb-2">
        <span class="badge bg-purple">100 points</span>
        <span class="text-danger fw-bold">
          <i class="bi bi-alarm"></i> 00:00
        </span>
        <span class="badge bg-secondary">Medium</span>
      </div>

      <h5 class="fw-bold">
        Which of the following energy sources cannot be replenished naturally on a human timescale,
        making it an example of a non-renewable resource?
      </h5>
    </div>

    <!-- Answer Options -->
    <div class="row g-3 mb-4">
      <div class="col-md-6">
        <button class="btn w-100 text-start bg-black text-white border border-secondary p-3 rounded-4">
          <span class="fw-bold me-2">A</span> Solar Power
        </button>
      </div>
      <div class="col-md-6">
        <button class="btn w-100 text-start bg-black text-white border border-secondary p-3 rounded-4">
          <span class="fw-bold me-2">B</span> Wind Power
        </button>
      </div>
      <div class="col-md-6">
        <button class="btn w-100 text-start bg-black text-white border border-secondary p-3 rounded-4">
          <span class="fw-bold me-2">C</span> Natural Gas
        </button>
      </div>
      <div class="col-md-6">
        <button class="btn w-100 text-start bg-black text-white border border-secondary p-3 rounded-4">
          <span class="fw-bold me-2">D</span> Hydroelectric Power
        </button>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="d-flex justify-content-between align-items-center">
      <button class="btn btn-outline-light rounded-3">
        <i class="bi bi-arrow-left"></i> Prev
      </button>
      <button class="btn btn-purple px-4 py-2">Submit</button>
      <button class="btn btn-outline-light rounded-3">
        Next <i class="bi bi-arrow-right"></i>
      </button>
    </div>
  </div>
</template>

<style scoped>
.bg-purple {
  background-color: #a855f7 !important;
}
.btn-purple {
  background-color: #a855f7;
  color: white;
  font-weight: 600;
}
</style>
