<template>
  <div class="container mx-auto px-4">
    <AddUser @finish="finish"></AddUser>
    <Table :data="userData" @finish="finish"></Table>
    <Pagination :total="total" :page-size="pageSize" @current-page="getNowPageData"></Pagination>
  </div>
</template>

<script setup>
import Table from './Table.vue'
import Pagination from './Pagination.vue'
import AddUser from './AddUser.vue'
import Axios from 'axios'
import { ref } from 'vue'

const userData = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = 5
const initData = () => {
  Axios.get('http://localhost:5000/get_user_list').then((data) => {
    let start = (currentPage.value - 1) * pageSize
    let end = currentPage.value * pageSize
    userData.value = data.data.data.slice(start, end)
    total.value = data.data.data.length
  })
}

initData()

const finish = () => {
  initData()
}

const getNowPageData = (page) => {
  currentPage.value = page
  initData()
}
</script>
