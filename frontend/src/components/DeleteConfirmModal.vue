<template>
  <div v-if="show" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.45);">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content bg-dark text-white border-0 rounded-4 shadow-lg animate-modal">
        <div class="modal-header border-0 pb-0">
          <h5 class="modal-title fw-bold">Confirm Delete</h5>
          <button type="button" class="btn-close btn-close-white" @click="emitClose" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p class="mb-0">Are you sure you want to delete this {{ type }}?</p>
        </div>
        <div class="modal-footer border-0 pt-0 d-flex justify-content-end gap-2">
          <button type="button" class="btn btn-outline-light px-4" @click="emitClose">Cancel</button>
          <button type="button" class="btn btn-danger px-4" @click="emitDelete">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(['delete', 'close']);
const props = defineProps({
  show: Boolean,
  type: { type: String, default: 'item' }
});
function emitDelete() { emit('delete'); }
function emitClose() { emit('close'); }
</script>

<style scoped>
.modal.fade.show {
  display: block;
  z-index: 2050;
}
.modal-content {
  border-radius: 1.25rem;
  box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}
.btn-danger {
  background-color: #ff6b6b;
  border: none;
}
.btn-danger:hover {
  background-color: #e53e3e;
}
</style>
