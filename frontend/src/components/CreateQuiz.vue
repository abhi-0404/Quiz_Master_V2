<template>
  <div class="modal fade show d-block" tabindex="-1" style="display:block; background:rgba(0,0,0,0.5);" v-if="show" aria-modal="true" role="dialog">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content bg-dark text-white">
        <div class="modal-header border-secondary-subtle d-flex justify-content-between align-items-center">
          <div>
            <h4 class="fw-bold mb-0">{{ mode === 'edit' ? 'Edit Quiz' : 'Create New Quiz' }}</h4>
            <small class="text-white-50">Add questions, set answers and configure quiz settings</small>
          </div>
          <button type="button" class="btn btn-outline-light nav-btn-icon ms-2" @click="handleClose" title="Close">
            <span class="bi bi-x-lg"></span>
          </button>
        </div>
        <form @submit.prevent="handleSave">
          <div class="modal-body">
            <div class="bg-black rounded p-3 shadow-sm">
              <h5 class="fw-semibold mb-1">Quiz Details</h5>
              <small class="text-muted mb-3 d-block">Basic information about your quiz</small>

              <!-- Date & Time Picker -->
              <div class="d-flex justify-content-end mb-3">
                <input type="datetime-local" class="form-control bg-dark text-white w-auto" v-model="form.date_time" required />
              </div>

              <!-- Quiz Title -->
              <div class="mb-3">
                <label class="form-label text-white">Quiz Title</label>
                <input type="text" class="form-control bg-dark text-white border-secondary" placeholder="Enter quiz title" v-model="form.title" required />
              </div>

              <!-- Description -->
              <div class="mb-3">
                <label class="form-label text-white">Description</label>
                <textarea rows="3" class="form-control bg-dark text-white border-secondary" placeholder="Enter quiz description..." v-model="form.description" required></textarea>
              </div>

              <!-- Category & Difficulty -->
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="form-label text-white">Category</label>
                  <select class="form-select bg-dark text-white border-secondary" v-model="form.category" required>
                    <option value="">Select category</option>
                    <option>Science</option>
                    <option>Mathematics</option>
                    <option>History</option>
                    <option>Technology</option>
                  </select>
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label text-white">Difficulty Level</label>
                  <select class="form-select bg-dark text-white border-secondary" v-model="form.difficulty" required>
                    <option value="">Select difficulty</option>
                    <option>Easy</option>
                    <option>Medium</option>
                    <option>Hard</option>
                  </select>
                </div>
              </div>
              <div v-if="error" class="alert alert-danger py-2 my-2">{{ error }}</div>
            </div>
          </div>
          <div class="modal-footer d-flex justify-content-end gap-2 border-top border-secondary-subtle">
            <button type="button" class="btn btn-outline-light px-4" @click="handleClose">Cancel</button>
            <button type="submit" class="btn btn-purple px-4" :disabled="loading || !isFormValid">
              <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
              {{ mode === 'edit' ? 'Update' : 'Save' }} <span class="bi bi-arrow-right ms-2"></span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, toRefs } from 'vue';
import { useAttrs, defineProps, defineEmits } from 'vue';

const props = defineProps({
  show: Boolean,
  mode: { type: String, default: 'create' }, // 'create' or 'edit'
  quizData: { type: Object, default: () => ({}) }
});
const emit = defineEmits(['save', 'close']);

const loading = ref(false);
const error = ref('');

const defaultForm = () => ({
  title: '',
  description: '',
  category: '',
  difficulty: '',
  date_time: ''
});

const form = ref(defaultForm());

// Watch for quizData changes (for edit mode)
watch(() => props.quizData, (val) => {
  if (props.mode === 'edit' && val) {
    form.value = {
      title: val.title || '',
      description: val.description || '',
      category: val.category || '',
      difficulty: val.difficulty || '',
      date_time: val.date_time || ''
    };
  } else if (props.mode === 'create') {
    form.value = defaultForm();
  }
}, { immediate: true });

const isFormValid = computed(() => {
  return (
    form.value.title.trim() &&
    form.value.description.trim() &&
    form.value.category &&
    form.value.difficulty &&
    form.value.date_time
  );
});

function handleClose() {
  error.value = '';
  emit('close');
}

async function handleSave() {
  if (!isFormValid.value) {
    error.value = 'Please fill all fields.';
    return;
  }
  loading.value = true;
  error.value = '';
  try {
    // Pass form data to parent
    await emit('save', { ...form.value });
    // Reset form if creating
    if (props.mode === 'create') form.value = defaultForm();
  } catch (e) {
    error.value = 'Failed to save quiz.';
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.modal {
  z-index: 2000;
}
.modal-content {
  background: #18181f;
  color: #fff;
  border-radius: 1rem;
  border: 1px solid #292933;
}
.modal-header {
  border-bottom: 1px solid #292933;
  background: #18181f;
}
.modal-footer {
  border-top: 1px solid #292933;
  background: #18181f;
}
.btn-purple {
  background-color: #9f42f9;
  color: white;
  border: none;
}
.btn-purple:hover {
  background-color: #892be2;
}
.nav-btn-icon {
  border-radius: 50%;
  padding: 0.4rem 0.6rem;
  font-size: 1.1rem;
}
.form-control, .form-select {
  background: #23232a;
  color: #fff;
  border: 1px solid #292933;
}
.form-control:focus, .form-select:focus {
  background: #23232a;
  color: #fff;
  border-color: #9f42f9;
  box-shadow: none;
}
.alert-danger {
  background: #2d193c;
  color: #ffb4b4;
  border: none;
}
</style>
