import Vue from 'vue'
import Router from 'vue-router'
import index from './views/Index.vue'
import Details from "./views/ad/Details";
import LoginWrapper from "./views/login/LoginWrapper";
import RegisterWrapper from "./views/register/RegisterWrapper";
import About from "./views/About";
import CreateAdWrapper from "./views/createAd/CreateAdWrapper";
import userProfile from "./views/userProfile/UserProfileWrapper";
import MessagesWrapper from "./views/message/MessagesWrapper";
import AnalyticsWrapper from "./views/analytics/AnalyticsWrapper";

Vue.use(Router);

export default new Router({
  mode: 'history',
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
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/create',
      name: 'create',
      component: CreateAdWrapper
    },
    {
      path: '/profile',
      name: 'profile',
      component: userProfile
    },
    {
      path: '/messages',
      name: 'messages',
      component: MessagesWrapper
    },
    {
      path: '/analytics',
      name: 'analytics',
      component: AnalyticsWrapper,
    },

  ],
  scrollBehavior(to, from, savedPosition) { //preserves the scrolling position of history entries
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})
