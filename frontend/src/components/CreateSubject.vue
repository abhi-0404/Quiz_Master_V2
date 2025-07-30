<template>
  <div class="modal fade show d-block" tabindex="-1" :style="show ? 'display:block;' : 'display:none;'" aria-modal="true" role="dialog">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content bg-dark text-white">
        <div class="modal-header d-flex justify-content-between align-items-center border-secondary-subtle">
          <div>
            <h4 class="fw-bold mb-0 text-white">{{ mode === 'edit' ? 'Edit Subject' : 'Create Subject' }}</h4>
            <small class="text-white-50">Add Chapter, set answers and configure quiz settings</small>
          </div>
          <button type="button" class="btn btn-outline-light nav-btn-icon ms-2" @click="emitClose" title="Close">
            <span class="bi bi-x-lg"></span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label text-white">Subject Name</label>
              <input type="text" class="form-control bg-dark text-white border-secondary" placeholder="Enter subject name" v-model="form.name" />
            </div>
            <div class="mb-3">
              <label class="form-label text-white">Description</label>
              <textarea rows="4" class="form-control bg-dark text-white border-secondary" placeholder="Enter subject description..." v-model="form.description"></textarea>
            </div>
          </form>
        </div>
        <div class="d-flex justify-content-end gap-2 p-4 border-top border-secondary-subtle">
          <button type="button" class="btn btn-outline-light px-4" @click="emitClose">Cancel</button>
          <button type="button" class="btn btn-purple px-4" :disabled="!form.name.trim()" @click="onSave">
            {{ mode === 'edit' ? 'Update' : 'Save' }} <span class="bi bi-arrow-right ms-2"></span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
const emit = defineEmits(['save', 'close']);
const props = defineProps({
  show: Boolean,
  mode: { type: String, default: 'create' },
  subjectData: { type: Object, default: () => ({ name: '', description: '', id: null }) }
});

const form = ref({ name: '', description: '', id: null });

watch(() => props.subjectData, (val) => {
  form.value = { ...val };
}, { immediate: true });

function onSave() {
  if (!form.value.name.trim()) return;
  emit('save', { ...form.value });
}
function emitClose() {
  emit('close');
}
</script>

<style scoped>
.modal.show.d-block {
  background: rgba(0,0,0,0.7);
  z-index: 2000;
}
.modal-content.bg-dark {
  background-color: #181818 !important;
  color: #fff !important;
}
.form-control.bg-dark {
  background-color: #222 !important;
  color: #fff !important;
  border-color: #444 !important;
}
.form-control.bg-dark:focus {
  background-color: #222 !important;
  color: #fff !important;
  border-color: #9f42f9 !important;
  box-shadow: 0 0 0 0.1rem #9f42f9;
}
.btn-purple {
  background-color: #9f42f9;
  color: white;
  border: none;
}
.btn-purple:disabled {
  background-color: #bda4e6;
  color: #eee;
  cursor: not-allowed;
}
.btn-purple:hover:not(:disabled) {
  background-color: #892be2;
}
.btn-outline-light.nav-btn-icon {
  border-width: 2px;
  font-weight: 500;
}
.btn-outline-light.nav-btn-icon:hover {
  background: #222;
  color: #fff;
}
</style>
