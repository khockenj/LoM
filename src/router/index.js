import Vue from 'vue'
import Router from 'vue-router'
import SearchPage from '../components/search'
import HomePage from '../components/home'
import LoginPage from '../components/login'
import ProfilePage from '../components/profile'
import SignupPage from '../components/signup'
import EditPage from '../components/editprofile'
Vue.use(Router)

export default new Router({
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
    },
    {
      path: '/signup',
      name: 'Sign Up',
      component: SignupPage
    },
    {
      path: '/profile/:user',
      name: 'Profile',
      component: ProfilePage
    },
    {
      path: '/editProfile',
      name: 'Edit Profile',
      component: EditPage
    },
  ]
})
