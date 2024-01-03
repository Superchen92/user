<template>
  <div class="px-4 py-8 sm:px-8">
    <table
      class="border-collapse w-full border border-slate-400 dark:border-slate-500 bg-white dark:bg-slate-800 text-sm shadow-sm"
    >
      <thead class="bg-slate-50 dark:bg-slate-700">
        <tr>
          <th
            class="w-1 border border-slate-300 dark:border-slate-600 font-semibold p-4 text-slate-900 dark:text-slate-200 text-left"
          >
            Id
          </th>
          <th
            class="w-2 border border-slate-300 dark:border-slate-600 font-semibold p-4 text-slate-900 dark:text-slate-200 text-left"
          >
            Name
          </th>
          <th
            class="w-2 border border-slate-300 dark:border-slate-600 font-semibold p-4 text-slate-900 dark:text-slate-200 text-left"
          >
            Gender
          </th>
          <th
            class="w-0.5 border border-slate-300 dark:border-slate-600 font-semibold p-4 text-slate-900 dark:text-slate-200 text-left"
          >
            Edit
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in props.data" :key="index">
          <td
            class="border border-slate-300 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400"
          >
            {{ item.id }}
          </td>
          <td
            class="border border-slate-300 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400"
          >
            {{ item.name }}
          </td>
          <td
            class="border border-slate-300 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400"
          >
            {{ changeSexLabel(item.gender) }}
          </td>
          <td
            class="border border-slate-300 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400"
          >
            <div
              class="w-1/6 pointer-events-auto rounded-md bg-indigo-600 px-3 py-2 text-[0.8125rem] font-semibold leading-5 text-white hover:bg-indigo-500 text-center"
              @click="openModal(item)"
            >
              edit
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <UserDialog
      :show="openDialog"
      :message="message"
      :form="formData"
      @close="onClose"
      @confirm="onConfirm"
    ></UserDialog>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import UserDialog from './UserDialog.vue'
import Axios from 'axios'

const props = defineProps({
  data: Object
})
const emits = defineEmits(['finish'])
const openDialog = ref(false)
const formData = ref()
const message = ref('')
const changeSexLabel = computed(() => {
  return (sex) => {
    return sex == 1 ? 'male' : 'female'
  }
})

const openModal = (data) => {
  formData.value = data
  openDialog.value = true
}

const onConfirm = (data) => {
  data.id = formData.value.id
  Axios.put('http://localhost:5000/edit_user', data).then((data) => {
    message.value = data.data.message
    openDialog.value = false
    emits('finish')
  })
}

const onClose = () => {}
</script>
