import Vue from 'vue'
import Router from 'vue-router'
import SearchPage from '../components/search'
import HomePage from '../components/home'
import LoginPage from '../components/login'
import ProfilePage from '../components/profile'
import SignupPage from '../components/signup'
import EditPage from '../components/editprofile'
import NowLive from '../components/nowlive'
import Dashboard from '../components/dashboard'
import Admin from '../components/Admin'
import NotFound from '../components/NotFound'
import News from '../components/News'
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
      component: SearchPage,
      props:true
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
    {
      path: '/nowLive',
      name: 'Now Live',
      component: NowLive
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/news',
      name: 'News',
      component: News
    },
    { 
     path: '*',
     component: NotFound 
    }
  ]
})
