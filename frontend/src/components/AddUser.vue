<template>
  <div>
    <button
      type="button"
      @click="openDialog = true"
      class="rounded-md bg-indigo-600 px-4 py-2 mx-8 my-2 text-sm font-medium text-white hover:bg-indigo-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75"
    >
      Add User
    </button>
    <UserDialog
      :show="openDialog"
      :message="message"
      @close="onClose"
      @confirm="onConfirm"
    ></UserDialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import UserDialog from './UserDialog.vue'
import Axios from 'axios'

const emits = defineEmits(['finish'])
const openDialog = ref(false)
const message = ref('')

const onClose = () => {
  openDialog.value = false
}
const onConfirm = (data) => {
  message.value = ''
  Axios.post('http://localhost:5000/add_user', data).then((data) => {
    message.value = data.data.message
    openDialog.value = false
    emits('finish')
  })
}
</script>
