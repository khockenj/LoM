import Vue from 'vue'
import Router from 'vue-router'
import SearchPage from '../components/search'
import HomePage from '../components/home'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/search',
      name: 'Search',
      component: SearchPage
    },
	 {
      path: '/',
      name: 'Home',
      component: HomePage
    }
  ]
})
