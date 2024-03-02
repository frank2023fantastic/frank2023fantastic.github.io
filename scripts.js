// JavaScript code for your blog website (if any)
// You can add your dynamic behavior here

import { createApp, ref } from 'vue'

createApp({
  setup() {
    return {
      count: ref(0)
    }
  }
}).mount('#app')