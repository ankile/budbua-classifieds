import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { MdButton, MdContent, MdTabs } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'

Vue.use(MdButton);
Vue.use(MdContent);
Vue.use(MdTabs);
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
