<template>
  <div class="d-flex admin-dashboard-responsive">
    <!-- Sidebar Navigation -->
    <aside class="sidebar sidebar-fixed">
      <AdminSidebar :isOpen="sidebarOpen" @toggle="toggleSidebar" />
    </aside>

    <!-- Overlay for mobile -->
    <div v-if="sidebarOpen && isMobile" class="sidebar-overlay" @click="toggleSidebar"></div>

    <!-- Main Content -->
    <main class="main-content flex-grow-1">
      <header class="main-header d-flex justify-content-between align-items-center">
        <div>
          <h1 class="welcome-title">Quizzes</h1>
          <p class="welcome-subtitle">Create, manage and analyze your quizzes</p>
        </div>
        <button class="btn btn-primary create-btn align-self-md-end" @click="openCreateQuizModal">+ Create New Quiz</button>
      </header>

      <section class="quiz-library d-flex flex-column">
        <div class="quiz-library-header mb-3">
          <h4 class="section-title mb-1">Quiz Library</h4>
          <p class="section-subtitle mb-0">Browse and manage all your quizzes</p>
        </div>
        <div class="quiz-list d-flex flex-column gap-3">
          <div v-for="quiz in quizzes" :key="quiz.id" class="quiz-step-wrapper">
            <!-- Quiz Row -->
            <div class="quiz-item d-flex flex-row align-items-center justify-content-between">
              <div class="d-flex align-items-center gap-3">
                <div class="icon-box d-flex align-items-center justify-content-center">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="4" width="18" height="16" rx="2"/>
                    <path d="M16 2v4"/>
                    <path d="M8 2v4"/>
                    <line x1="3" y1="10" x2="21" y2="10"/>
                    <rect x="7" y="14" width="2" height="2" rx="0.5"/>
                    <rect x="11" y="14" width="2" height="2" rx="0.5"/>
                    <rect x="15" y="14" width="2" height="2" rx="0.5"/>
                  </svg>
                </div>
                <div>
                  <h6 class="quiz-title mb-1">{{ quiz.title || 'Quiz Name' }}</h6>
                  <small class="quiz-details">{{ quiz.description || 'Basic concepts of biology for beginners' }}</small>
                </div>
              </div>
              <div class="d-flex align-items-center gap-2">
                <button class="btn btn-outline-danger" @click="askDeleteQuiz(quiz.id)" title="Delete Quiz">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ff6b6b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"/>
                    <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
                    <rect x="5" y="6" width="14" height="14" rx="2"/>
                    <line x1="10" y1="11" x2="10" y2="17"/>
                    <line x1="14" y1="11" x2="14" y2="17"/>
                  </svg>
                </button>
                <button class="btn btn-outline-light" @click="editQuiz(quiz)">Edit</button>
                <button class="btn btn-purple" @click="addSubject(quiz)">+ Subject</button>
                <button class="btn btn-dark dropdown-toggle" @click="toggleQuizDropdown(quiz.id)">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline :points="openQuizDropdown === quiz.id ? '6 15 12 9 18 15' : '6 9 12 15 18 9'" />
                  </svg>
                </button>
              </div>
            </div>
            <!-- Subjects Dropdown -->
            <transition name="fade">
              <div v-if="openQuizDropdown === quiz.id" class="subject-step-list">
                <div v-if="subjectsLoading" class="text-muted">Loading subjects...</div>
                <div v-else>
                  <div v-for="subject in subjects[quiz.id] || []" :key="subject.id" class="subject-step d-flex flex-row align-items-center justify-content-between">
                    <div class="d-flex align-items-center gap-3">
                      <div class="icon-box subject-icon d-flex align-items-center justify-content-center">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#a855f7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <rect x="4" y="4" width="16" height="16" rx="3"/>
                          <path d="M8 8h8v8H8z"/>
                        </svg>
                      </div>
                      <div>
                        <h6 class="subject-title mb-1">{{ subject.title || 'Subject Name' }}</h6>
                        <small class="subject-details">{{ subject.description || 'Basic concepts of biology for beginners' }}</small>
                      </div>
                    </div>
                    <div class="d-flex align-items-center gap-2">
                      <button class="btn btn-outline-danger" @click="askDeleteSubject(subject.id, quiz.id)" title="Delete Subject">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ff6b6b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polyline points="3 6 5 6 21 6"/>
                          <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
                          <rect x="5" y="6" width="14" height="14" rx="2"/>
                          <line x1="10" y1="11" x2="10" y2="17"/>
                          <line x1="14" y1="11" x2="14" y2="17"/>
                        </svg>
                      </button>
                      <button class="btn btn-outline-light" @click="editSubject(subject, quiz.id)">Edit</button>
                      <button class="btn btn-purple" @click="addChapter(subject, quiz.id)">+ Chapter</button>
                      <button class="btn btn-dark dropdown-toggle" @click="toggleSubjectDropdown(subject.id, quiz.id)">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polyline :points="openSubjectDropdown === subject.id ? '6 15 12 9 18 15' : '6 9 12 15 18 9'" />
                        </svg>
                      </button>
                    </div>
                  </div>
                  <!-- Chapters Dropdown -->
                  <transition name="fade">
                    <div v-if="openSubjectDropdown && chaptersLoading" class="chapter-step-list text-muted">Loading chapters...</div>
                    <div v-else-if="openSubjectDropdown && chapters[openSubjectDropdown]" class="chapter-step-list">
                      <div v-for="chapter in chapters[openSubjectDropdown] || []" :key="chapter.id" class="chapter-step d-flex flex-row align-items-center justify-content-between">
                        <div class="d-flex align-items-center gap-3">
                          <div class="icon-box chapter-icon d-flex align-items-center justify-content-center">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                              <circle cx="12" cy="12" r="9"/>
                              <path d="M9 12h6"/>
                              <path d="M12 9v6"/>
                            </svg>
                          </div>
                          <div>
                            <h6 class="chapter-title mb-1">{{ chapter.title || 'Chapter Name' }}</h6>
                            <small class="chapter-details">{{ chapter.questions ? chapter.questions + ' Questions' : '0 Questions' }}</small>
                          </div>
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <button class="btn btn-outline-danger" @click="askDeleteChapter(chapter.id, openSubjectDropdown)" title="Delete Chapter">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ff6b6b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                              <polyline points="3 6 5 6 21 6"/>
                              <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
                              <rect x="5" y="6" width="14" height="14" rx="2"/>
                              <line x1="10" y1="11" x2="10" y2="17"/>
                              <line x1="14" y1="11" x2="14" y2="17"/>
                            </svg>
                          </button>
                          <button class="btn btn-outline-light" @click="editChapter(chapter, openSubjectDropdown)">Edit</button>
                          <button class="btn btn-purple" @click="addQuestion(chapter, openSubjectDropdown)">+ Question</button>
                        </div>
                      </div>
                    </div>
                  </transition>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </section>
    </main>
  </div>

  <CreateSubject
    v-if="showSubjectModal"
    :show="showSubjectModal"
    :mode="subjectModalMode"
    :subjectData="subjectModalData"
    @save="handleSubjectModalSave"
    @close="handleSubjectModalClose"
  />
  <!-- Edit Quiz Modal -->
  <div v-if="showEditQuizModal" class="modal fade show d-block" tabindex="-1" style="display:block;" aria-modal="true" role="dialog">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content bg-dark text-white">
        <div class="modal-header d-flex justify-content-between align-items-center border-secondary-subtle">
          <div>
            <h4 class="fw-bold mb-0 text-white">Edit Quiz</h4>
            <small class="text-white-50">Edit quiz title and settings</small>
          </div>
          <button type="button" class="btn btn-outline-light nav-btn-icon ms-2" @click="closeEditQuizModal" title="Close">
            <span class="bi bi-x-lg"></span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="saveEditQuiz">
            <div class="mb-3">
              <label class="form-label text-white">Quiz Title</label>
              <input type="text" class="form-control bg-dark text-white border-secondary" v-model="editQuizForm.title" required />
            </div>
            <div class="mb-3">
              <label class="form-label text-white">Time Duration (minutes)</label>
              <input type="number" class="form-control bg-dark text-white border-secondary" v-model="editQuizForm.time_duration" min="1" />
            </div>
          </form>
        </div>
        <div class="d-flex justify-content-end gap-2 p-4 border-top border-secondary-subtle">
          <button type="button" class="btn btn-outline-light px-4" @click="closeEditQuizModal">Cancel</button>
          <button type="button" class="btn btn-purple px-4" :disabled="!editQuizForm.title.trim()" @click="saveEditQuiz">
            Update <span class="bi bi-arrow-right ms-2"></span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <CreateChapter
    v-if="showChapterModal"
    :show="showChapterModal"
    :mode="chapterModalMode"
    :chapterData="chapterModalData"
    @save="handleChapterModalSave"
    @close="handleChapterModalClose"
  />
  <CreateQuestion
    v-if="showQuestionModal"
    :show="showQuestionModal"
    :mode="questionModalMode"
    :questionData="questionModalData"
    :subjectName="questionModalSubjectName"
    :chapterName="questionModalChapterName"
    @save="handleQuestionModalSave"
    @close="handleQuestionModalClose"
  />
  <DeleteConfirmModal
    v-if="showDeleteModal"
    :show="showDeleteModal"
    :type="deleteType"
    @delete="handleDeleteConfirm"
    @close="handleDeleteCancel"
  />

  <CreateQuiz
    v-if="showCreateQuizModal"
    :show="showCreateQuizModal"
    mode="create"
    @save="handleCreateQuizSave"
    @close="closeCreateQuizModal"
  />
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import CreateQuiz from '../../components/CreateQuiz.vue';
// Edit Quiz Modal State
// Create Quiz Modal State
const showCreateQuizModal = ref(false);

function openCreateQuizModal() {
  showCreateQuizModal.value = true;
}
function closeCreateQuizModal() {
  showCreateQuizModal.value = false;
}

async function handleCreateQuizSave(quizData) {
  // quizData: { title, description, category, difficulty, date_time }
  try {
    const token = localStorage.getItem('authToken');
    await axios.post('http://127.0.0.1:5000/api/admin/events', {
      title: quizData.title,
      description: quizData.description,
      category: quizData.category,
      difficulty: quizData.difficulty,
      date_time: quizData.date_time
    }, {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    await fetchQuizzes();
    showCreateQuizModal.value = false;
  } catch (e) {
    alert('Failed to create quiz.');
  }
}
const showEditQuizModal = ref(false);
const editQuizForm = ref({ id: null, title: '', time_duration: 0 });
let editQuizCallback = null;
function openEditQuizModal(quiz) {
  editQuizForm.value = { id: quiz.id, title: quiz.title || '', time_duration: quiz.time_duration || 0 };
  showEditQuizModal.value = true;
}

function closeEditQuizModal() {
  showEditQuizModal.value = false;
}

async function saveEditQuiz() {
  const { id, title, time_duration } = editQuizForm.value;
  try {
    const token = localStorage.getItem('authToken');
    await axios.put(`http://127.0.0.1:5000/api/admin/events/${id}`, {
      title,
      time_duration
    }, {
      withCredentials: true
    });
    // Update local quizzes list
    const idx = quizzes.value.findIndex(q => q.id === id);
    if (idx !== -1) {
      quizzes.value[idx].title = title;
      quizzes.value[idx].time_duration = time_duration;
    }
    showEditQuizModal.value = false;
  } catch (e) {
    alert('Failed to update quiz.');
  }
}

function editQuiz(quiz) {
  openEditQuizModal(quiz);
}
import axios from 'axios';
import AdminSidebar from '../../components/AdminSidebar.vue';
import CreateSubject from '../../components/CreateSubject.vue';
import CreateChapter from '../../components/CreateChapter.vue';
import CreateQuestion from '../../components/CreateQuestion.vue';
import DeleteConfirmModal from '../../components/DeleteConfirmModal.vue';

const quizzes = ref([]);
const loading = ref(false);
const error = ref(null);

const sidebarOpen = ref(false);
const isMobile = ref(false);

// Dropdown state
const openQuizDropdown = ref(null); // quiz.id
const openSubjectDropdown = ref(null); // subject.id
const subjects = ref({}); // { [quizId]: [subject, ...] }
const chapters = ref({}); // { [subjectId]: [chapter, ...] }
const subjectsLoading = ref(false);
const chaptersLoading = ref(false);

// Modal state for subject create/edit
const showSubjectModal = ref(false);
const subjectModalMode = ref('create'); // 'create' or 'edit'
const subjectModalQuizId = ref(null);
const subjectModalData = ref({ name: '', description: '', id: null });

// Modal state for chapter create/edit
const showChapterModal = ref(false);
const chapterModalMode = ref('create'); // 'create' or 'edit'
const chapterModalSubjectId = ref(null);
const chapterModalData = ref({ name: '', description: '', id: null });

// Modal state for question create/edit
const showQuestionModal = ref(false);
const questionModalMode = ref('create'); // 'create' or 'edit'
const questionModalChapterId = ref(null);
const questionModalData = ref({ text: '', points: 0, answer: 0, options: ['', '', '', ''], id: null });
const questionModalSubjectName = ref('');
const questionModalChapterName = ref('');

// Modal state for delete confirmation
const showDeleteModal = ref(false);
const deleteType = ref('item'); // 'quiz' | 'subject' | 'chapter'
const deleteId = ref(null);
const deleteParentId = ref(null); // for subject: quizId, for chapter: subjectId

function toggleQuizDropdown(quizId) {
  if (openQuizDropdown.value === quizId) {
    openQuizDropdown.value = null;
    openSubjectDropdown.value = null;
    return;
  }
  openQuizDropdown.value = quizId;
  openSubjectDropdown.value = null;
  fetchSubjects(quizId);
}
function toggleSubjectDropdown(subjectId, quizId) {
  if (openSubjectDropdown.value === subjectId) {
    openSubjectDropdown.value = null;
    return;
  }
  openSubjectDropdown.value = subjectId;
  fetchChapters(subjectId);
}

async function fetchSubjects(quizId) {
  subjectsLoading.value = true;
  try {
    const token = localStorage.getItem('authToken');
    const res = await axios.get(`http://127.0.0.1:5000/api/admin/quiz/${quizId}/subjects`, {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    subjects.value[quizId] = res.data.subjects || [];
  } catch (e) {
    subjects.value[quizId] = [];
  } finally {
    subjectsLoading.value = false;
  }
}

async function fetchChapters(subjectId) {
  chaptersLoading.value = true;
  try {
    const token = localStorage.getItem('authToken');
    const res = await axios.get(`http://127.0.0.1:5000/api/admin/subject/${subjectId}/chapters`, {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    chapters.value[subjectId] = res.data.chapters || [];
  } catch (e) {
    chapters.value[subjectId] = [];
  } finally {
    chaptersLoading.value = false;
  }
}

function handleResize() {
  isMobile.value = window.innerWidth < 992;
  if (!isMobile.value) sidebarOpen.value = false;
}
function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value;
}

onMounted(() => {
  handleResize();
  window.addEventListener('resize', handleResize);
  fetchQuizzes();
});
onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});

async function fetchQuizzes() {
  loading.value = true;
  error.value = null;
  try {
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Authentication token not found.');
    const response = await axios.get('http://127.0.0.1:5000/api/admin/events', {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    quizzes.value = response.data.events || [];
  } catch (err) {
    error.value = 'Failed to fetch quizzes.';
    console.error(err);
  } finally {
    loading.value = false;
  }
}

async function deleteQuiz(quizId) {
  try {
    const token = localStorage.getItem('authToken');
    await axios.delete(`http://127.0.0.1:5000/api/admin/events/${quizId}`, {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    quizzes.value = quizzes.value.filter(q => q.id !== quizId);
    delete subjects.value[quizId];
  } catch (e) {
    alert('Failed to delete quiz.');
  }
}

async function deleteSubject(subjectId, quizId) {
  try {
    const token = localStorage.getItem('authToken');
    await axios.delete(`http://127.0.0.1:5000/api/admin/subject/${subjectId}`, {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    subjects.value[quizId] = (subjects.value[quizId] || []).filter(s => s.id !== subjectId);
    delete chapters.value[subjectId];
  } catch (e) {
    alert('Failed to delete subject.');
  }
}

async function deleteChapter(chapterId, subjectId) {
  try {
    const token = localStorage.getItem('authToken');
    await axios.delete(`http://127.0.0.1:5000/api/admin/chapter/${chapterId}`, {
      headers: { 'Authorization': `Bearer ${token}` },
      withCredentials: true
    });
    chapters.value[subjectId] = (chapters.value[subjectId] || []).filter(c => c.id !== chapterId);
  } catch (e) {
    alert('Failed to delete chapter.');
  }
}

// Add/Edit handlers (show prompt for demo, replace with modal in real app)
// ...existing code...
// Register CreateQuiz
function addSubject(quiz) {
  subjectModalMode.value = 'create';
  subjectModalQuizId.value = quiz.id;
  subjectModalData.value = { name: '', description: '', id: null };
  showSubjectModal.value = true;
}
function editSubject(subject, quizId) {
  subjectModalMode.value = 'edit';
  subjectModalQuizId.value = quizId;
  subjectModalData.value = { name: subject.title, description: subject.description, id: subject.id };
  showSubjectModal.value = true;
}

function addChapter(subject, quizId) {
  chapterModalMode.value = 'create';
  chapterModalSubjectId.value = subject.id;
  chapterModalData.value = { name: '', description: '', id: null };
  showChapterModal.value = true;
}
function editChapter(chapter, subjectId) {
  chapterModalMode.value = 'edit';
  chapterModalSubjectId.value = subjectId;
  chapterModalData.value = { name: chapter.title, description: chapter.description, id: chapter.id };
  showChapterModal.value = true;
}

function addQuestion(chapter, subjectId) {
  questionModalMode.value = 'create';
  questionModalChapterId.value = chapter.id;
  questionModalData.value = { text: '', points: 0, answer: 0, options: ['', '', '', ''], id: null };
  questionModalSubjectName.value = (subjects.value[subjectId]?.[0]?.title) || '';
  questionModalChapterName.value = chapter.title || '';
  showQuestionModal.value = true;
}
function editQuestion(question, chapter, subjectId) {
  questionModalMode.value = 'edit';
  questionModalChapterId.value = chapter.id;
  questionModalData.value = { ...question };
  questionModalSubjectName.value = (subjects.value[subjectId]?.[0]?.title) || '';
  questionModalChapterName.value = chapter.title || '';
  showQuestionModal.value = true;
}

function askDeleteQuiz(quizId) {
  deleteType.value = 'quiz';
  deleteId.value = quizId;
  showDeleteModal.value = true;
}
function askDeleteSubject(subjectId, quizId) {
  deleteType.value = 'subject';
  deleteId.value = subjectId;
  deleteParentId.value = quizId;
  showDeleteModal.value = true;
}
function askDeleteChapter(chapterId, subjectId) {
  deleteType.value = 'chapter';
  deleteId.value = chapterId;
  deleteParentId.value = subjectId;
  showDeleteModal.value = true;
}

async function handleDeleteConfirm() {
  if (deleteType.value === 'quiz') {
    await deleteQuiz(deleteId.value);
  } else if (deleteType.value === 'subject') {
    await deleteSubject(deleteId.value, deleteParentId.value);
  } else if (deleteType.value === 'chapter') {
    await deleteChapter(deleteId.value, deleteParentId.value);
  }
  showDeleteModal.value = false;
}
function handleDeleteCancel() {
  showDeleteModal.value = false;
}

async function handleSubjectModalSave({ name, description, id }) {
  const quizId = subjectModalQuizId.value;
  try {
    const token = localStorage.getItem('authToken');
    if (subjectModalMode.value === 'create') {
      await axios.post(`http://127.0.0.1:5000/api/admin/subject`, {
        name,
        description,
      }, {
        headers: { 'Authorization': `Bearer ${token}` },
        withCredentials: true
      });
    } else if (subjectModalMode.value === 'edit' && id) {
      await axios.put(`http://127.0.0.1:5000/api/admin/subject/${id}`, {
        name,
        description,
      }, {
        headers: { 'Authorization': `Bearer ${token}` },
        withCredentials: true
      });
    }
    await fetchSubjects(quizId);
    showSubjectModal.value = false;
  } catch (e) {
    alert('Failed to save subject.');
  }
}
function handleSubjectModalClose() {
  showSubjectModal.value = false;
}

async function handleChapterModalSave({ name, description, id }) {
  const subjectId = chapterModalSubjectId.value;
  try {
    const token = localStorage.getItem('authToken');
    if (chapterModalMode.value === 'create') {
      await axios.post(`http://127.0.0.1:5000/api/admin/chapter`, {
        name,
        description,
        subject_id: subjectId,
      }, {
        headers: { 'Authorization': `Bearer ${token}` },
        withCredentials: true
      });
    } else if (chapterModalMode.value === 'edit' && id) {
      await axios.put(`http://127.0.0.1:5000/api/admin/chapter/${id}`, {
        name,
        description,
      }, {
        headers: { 'Authorization': `Bearer ${token}` },
        withCredentials: true
      });
    }
    await fetchChapters(subjectId);
    showChapterModal.value = false;
  } catch (e) {
    alert('Failed to save chapter.');
  }
}
function handleChapterModalClose() {
  showChapterModal.value = false;
}

async function handleQuestionModalSave({ text, points, answer, options, id }) {
  const chapterId = questionModalChapterId.value;
  try {
    const token = localStorage.getItem('authToken');
    if (questionModalMode.value === 'create') {
      await axios.post(`http://127.0.0.1:5000/api/admin/question`, {
        statement: text,
        option1: options[0],
        option2: options[1],
        option3: options[2],
        option4: options[3],
        correct_option: answer,
        quiz_id: chapterId,
        points
      }, {
        headers: { 'Authorization': `Bearer ${token}` },
        withCredentials: true
      });
    } else if (questionModalMode.value === 'edit' && id) {
      await axios.put(`http://127.0.0.1:5000/api/admin/question/${id}`, {
        statement: text,
        option1: options[0],
        option2: options[1],
        option3: options[2],
        option4: options[3],
        correct_option: answer,
        points
      }, {
        headers: { 'Authorization': `Bearer ${token}` },
        withCredentials: true
      });
    }
    // Optionally refresh questions list here
    showQuestionModal.value = false;
  } catch (e) {
    alert('Failed to save question.');
  }
}
function handleQuestionModalClose() {
  showQuestionModal.value = false;
}
// ...existing code...
</script>

<style scoped>
/* Sidebar and responsive layout */
.admin-dashboard-responsive {
  font-family: 'Inter', sans-serif;
  background-color: #16161A;
  color: #FFFFFF;
  min-height: 100vh;
  position: relative;
}
.sidebar-fixed {
  position: sticky;
  top: 0;
  height: 100vh;
  align-self: flex-start;
  z-index: 100;
  overflow-y: auto;
  max-height: 100vh;
}
@media (max-width: 991.98px) {
  .sidebar-fixed {
    position: static;
    width: 100%;
    height: auto;
    max-height: none;
    overflow-y: visible;
    z-index: auto;
  }
}
.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.3);
  z-index: 999;
}

/* Main Content Styling (match AdminDashboard) */
.main-content {
  padding: 2rem 3rem;
  overflow-y: auto;
}
@media (max-width: 991px) {
  .main-content {
    padding: 1rem 0.5rem;
  }
}
.main-header {
  margin-bottom: 2rem;
}
.welcome-title {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 0;
  color: #fff;
}
.welcome-subtitle {
  color: #94A3B8;
  font-size: 1rem;
  margin-top: 0.25rem;
}
.create-btn {
  background-color: #6E56F1;
  border: none;
  border-radius: 0.5rem;
  padding: 0.75rem 1.25rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.create-btn:hover {
  background-color: #5a43d1;
}
.quiz-library {
  background-color: #24242C;
  border-radius: 0.75rem;
  border: 1px solid #3A3A43;
  padding: 2rem 1.5rem;
  width: 100%;
}
.quiz-library-header {
  width: 100%;
}
.section-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
}
.section-subtitle {
  color: #94A3B8;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
}
.quiz-list {
  width: 100%;
}
.quiz-step-wrapper {
  margin-bottom: 0.5rem;
}
.quiz-item {
  background-color: #18181f;
  border: 1px solid #292933;
  padding: 1rem 1.5rem;
  border-radius: 0.75rem 0.75rem 0.5rem 0.5rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 2;
}
.icon-box {
  width: 40px;
  height: 40px;
  background-color: #23232a;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
}
.subject-icon {
  background-color: #2d193c;
}
.chapter-icon {
  background-color: #23244a;
}
.quiz-title {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
}
.quiz-details {
  color: #94A3B8;
  font-size: 0.85rem;
  margin-top: 0.25rem;
}
.btn-purple {
  background-color: #a855f7;
  color: white;
  border: none;
}
.btn-purple:hover {
  background-color: #9333ea;
}
.dropdown-toggle {
  background: #23232a;
  border: none;
  color: #fff;
  border-radius: 0.5rem;
  padding: 0.4rem 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.subject-step-list {
  background: #20202a;
  border-radius: 0 0 0.5rem 0.5rem;
  border-left: 2.5px solid #a855f7;
  margin-left: 2.2rem;
  margin-top: -0.5rem;
  margin-bottom: 0.5rem;
  padding: 0.5rem 0.5rem 0.5rem 1.5rem;
  position: relative;
  z-index: 1;
}
.subject-step {
  background: #23232a;
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
  padding: 0.75rem 1.2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #2d193c;
}
.subject-title {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
}
.subject-details {
  color: #bda4e6;
  font-size: 0.85rem;
  margin-top: 0.25rem;
}
.chapter-step-list {
  background: #19192a;
  border-radius: 0 0 0.5rem 0.5rem;
  border-left: 2.5px solid #6366f1;
  margin-left: 2.2rem;
  margin-top: -0.5rem;
  margin-bottom: 0.5rem;
  padding: 0.5rem 0.5rem 0.5rem 1.5rem;
  position: relative;
  z-index: 0;
}
.chapter-step {
  background: #23244a;
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
  padding: 0.75rem 1.2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #23244a;
}
.chapter-title {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
}
.chapter-details {
  color: #b3baff;
  font-size: 0.85rem;
  margin-top: 0.25rem;
}
.fade-enter-active, .fade-leave-active {
  transition: all 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
@media (max-width: 991px) {
  .quiz-library {
    padding: 1rem 0.5rem;
  }
}
</style>
