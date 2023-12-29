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
        <tr v-for="(item, index) in data" :key="index">
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
            {{ item.gender }}
          </td>
          <td
            class="border border-slate-300 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400"
          >
            <div
              class="w-1/6 pointer-events-auto rounded-md bg-indigo-600 px-3 py-2 text-[0.8125rem] font-semibold leading-5 text-white hover:bg-indigo-500 text-center"
            >
              edit
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const data = [
  {
    id: 1,
    name: 'apple',
    gender: 'female'
  },
  {
    id: 2,
    name: 'pill',
    gender: 'male'
  }
]
</script>
