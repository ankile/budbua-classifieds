import Vue from 'vue'
import Router from 'vue-router'
import index from './views/Index.vue'
import Details from "./views/ad/Details";
import About from "./views/About";

Vue.use(Router);

export default new Router({
  mode: 'hash',
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
      path: '/about',
      name: 'about',
      component: About
    }
  ],
  scrollBehavior(to, from, savedPosition) { //preserves the scrolling position of history entries
    if (savedPosition) {
      console.log(savedPosition);
      return savedPosition
    } else {
      console.log("no saved position");
      return { x: 0, y: 0 }
    }
  }
})
