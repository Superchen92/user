<template>
  <div>
    <TransitionRoot appear :show="model.show" as="template">
      <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black/25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <DialogPanel
                class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
              >
                <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">
                  Add User
                </DialogTitle>
                <div class="mt-2">
                  <div class="flex flex-row">
                    <div class="basis-1/4"><span>Name</span></div>
                    <div class="basis-1/2">
                      <input type="text" v-model="model.name" />
                    </div>
                  </div>
                  <div class="flex flex-row">
                    <div class="basis-1/4"><span>Gender</span></div>
                    <div class="basis-1/2">
                      <select
                        v-model="model.gender"
                        class="block w-full mt-1 rounded-md border-black shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                      >
                        <option value="2">female</option>
                        <option value="1">male</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div class="text-right">
                  <button
                    type="button"
                    class="inline-flex justify-center rounded-md border border-transparent bg-grey-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-grey-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 mx-2"
                    @click="closeModal"
                  >
                    cancal
                  </button>
                  <button
                    type="button"
                    class="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                    @click="confirm"
                  >
                    confirm
                  </button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
    <TransitionRoot appear :show="model.showMsg" as="template">
      <Dialog as="div" class="relative z-10">
        <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black/25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <DialogPanel
                class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
              >
                <div class="mt-2">
                  <p class="text-sm text-gray-500">{{ props.message }}</p>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>

<script setup>
import { TransitionRoot, TransitionChild, Dialog, DialogPanel, DialogTitle } from '@headlessui/vue'
import { reactive, watch } from 'vue'

const emits = defineEmits(['close', 'confirm'])
const props = defineProps({
  show: Boolean,
  message: String,
  form: Object
})

const model = reactive({
  show: props.show,
  showMsg: false,
  name: props.form?.name || '',
  gender: props.form?.gender || ''
})

function closeModal() {
  emits('close')
  model.show = false
}

const confirm = () => {
  emits('confirm', { name: model.name, gender: model.gender })
}

watch(
  () => props.show,
  () => {
    model.show = props.show
  }
)

watch(
  () => props.message,
  () => {
    if (props.message != '') {
      model.showMsg = true
      setTimeout(() => {
        model.showMsg = false
      }, 2000)
    }
  }
)

watch(
  () => props.form,
  () => {
    model.name = props.form.name
    model.gender = props.form.gender
  }
)
</script>
