import Vue from 'vue'
import Router from 'vue-router'
import SearchPage from '../components/search'
import HomePage from '../components/home'
import LoginPage from '../components/login'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
	 {
      path: '/',
      name: 'Home',
      component: HomePage
    },
    {
      path: '/search',
      name: 'Search',
      component: SearchPage
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    }
  ]
})
