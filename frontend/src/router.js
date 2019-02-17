import Vue from 'vue'
import Router from 'vue-router'
import index from './views/Index.vue'
import Details from "./views/ad/Details";
import LoginWrapper from "./views/login/LoginWrapper";
import RegisterWrapper from "./views/register/RegisterWrapper";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/details/:id',
      name: 'details',
      component: Details
    },
    {
      path: '/login',
      name:'login',
      component:LoginWrapper
    },
    {
      path: '/register',
      name:'register',
      component:RegisterWrapper
    }
  ]
})
