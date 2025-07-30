
<template>
  <div class="modal fade show d-block" tabindex="-1" :style="show ? 'display:block;' : 'display:none;'" aria-modal="true" role="dialog">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content bg-dark text-white">
        <div class="modal-header d-flex justify-content-between align-items-center border-secondary-subtle">
          <div class="d-flex align-items-center gap-3">
            <div>
              <h4 class="fw-bold mb-0 text-white">{{ mode === 'edit' ? 'Edit Question' : 'Quiz Name' }}</h4>
              <small class="text-white-50">Add questions, set answers and points for this quiz.</small>
            </div>
          </div>
          <div class="d-flex align-items-center gap-2">
            <button type="button" class="btn btn-outline-light nav-btn-icon" @click="onPrev" title="Previous">
              <span class="bi bi-chevron-left"></span>
            </button>
            <button type="button" class="btn btn-outline-light nav-btn-icon" @click="onNext" title="Next">
              <span class="bi bi-chevron-right"></span>
            </button>
            <button type="button" class="btn btn-outline-light nav-btn-icon ms-2" @click="emitClose" title="Close">
              <span class="bi bi-x-lg"></span>
            </button>
          </div>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3 d-flex align-items-center gap-3">
              <label class="form-label text-white mb-0">Points:</label>
              <input type="number" class="form-control form-control-sm w-auto bg-dark text-white border-secondary" v-model.number="form.points" min="0" />
              <button type="button" class="btn btn-link text-danger p-0 fs-5" @click.prevent="emitDelete" v-if="mode === 'edit'">
                <span class="bi bi-trash"></span>
              </button>
            </div>
            <div class="mb-3">
              <label class="form-label text-white">Question:</label>
              <textarea rows="3" class="form-control bg-dark text-white border-secondary" placeholder="Enter your question..." v-model="form.text"></textarea>
            </div>
            <div>
              <label class="form-label text-white">Answer Options</label>
              <div v-for="(option, index) in visibleOptionsArray" :key="index" class="mb-2 d-flex align-items-center">
                <input
                  class="form-check-input bg-dark border-secondary me-2"
                  type="radio"
                  :name="'answer0'"
                  :value="index"
                  v-model="form.answer"
                  :disabled="form.options[index].trim() === '' || index >= visibleOptions"
                />
                <input
                  class="form-control bg-dark text-white border-secondary me-2"
                  v-model="form.options[index]"
                  :placeholder="'Option ' + (index+1)"
                  :readonly="index < visibleOptions - 1"
                />
                <button v-if="index === visibleOptions - 1 && visibleOptions < 4" type="button" class="btn btn-outline-secondary add-option-btn-responsive d-flex align-items-center justify-content-center" style="width:2.2rem;height:2.2rem;padding:0;" @click.prevent="addOption">
                  <span class="bi bi-plus-lg"></span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { computed } from 'vue';

const visibleOptionsArray = computed(() => {
  return form.value.options.slice(0, visibleOptions.value);
});

const emit = defineEmits(['save', 'close', 'delete']);
const props = defineProps({
  show: Boolean,
  mode: { type: String, default: 'create' },
  questionData: { type: Object, default: () => ({ text: '', points: 0, answer: 0, options: ['', '', '', ''], id: null }) },
  subjectName: { type: String, default: '' },
  chapterName: { type: String, default: '' }
});


const form = ref({ text: '', points: 0, answer: 0, options: ['', ''], id: null });
const visibleOptions = ref(1);


watch(() => props.questionData, (val) => {
  // Ensure at least 2 options, max 4
  let opts = val.options ? val.options.slice(0, 4) : ['',''];
  while (opts.length < 2) opts.push('');
  form.value = { ...val, options: opts };
  visibleOptions.value = Math.max(1, opts.findIndex(opt => !opt.trim()) + 1);
  if (visibleOptions.value < 1) visibleOptions.value = opts.length;
}, { immediate: true });

function onSave() {
  if (!form.value.text.trim() || form.value.options.some(opt => !opt.trim())) return;
  emit('save', { ...form.value });
}
function emitClose() {
  emit('close');
}
function emitDelete() {
  emit('delete', form.value.id);
}
function addOption() {
  if (visibleOptions.value < 4) {
    if (form.value.options.length < visibleOptions.value + 1) {
      form.value.options.push('');
    }
    visibleOptions.value++;
  }
}
function onPrev() {
  onSave();
  emit('close', { direction: 'prev' });
}
function onNext() {
  onSave();
  emit('close', { direction: 'next' });
}
</script>


<style scoped>
/* Bootstrap modal override for always show */
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
.form-check-input.bg-dark {
  background-color: #181818 !important;
  border-color: #444 !important;
}
.form-check-input.bg-dark:checked {
  background-color: #9f42f9 !important;
  border-color: #9f42f9 !important;
}
.btn-outline-light.nav-btn-icon, .btn-outline-secondary.add-option-btn-responsive {
  border-width: 2px;
  font-weight: 500;
}
.btn-outline-light.nav-btn-icon:hover, .btn-outline-secondary.add-option-btn-responsive:hover {
  background: #222;
  color: #fff;
}
</style>
