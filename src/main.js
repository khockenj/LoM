import Vue from 'vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import './default.css'
import MentorSearch from './components/MentorSearch'
import Navbar from './components/Navbar'
import SearchCard from './components/SearchCard'
import App from './components/App'
import Champions from '../static/champions.json'
import SearchPage from './components/search'
const http = require('http')
const fs = require('fs')
const httpPort = 80

Vue.config.productionTip = false
Vue.use(BootstrapVue)


var base = new Vue({
   router,
   template: '<App/>',
   el: "#app",
   components: {
	App
   },
   build: {
    assetsPublicPath: '/',
    assetsSubDirectory: 'static'
  },
	data: {
		champions: Champions['data']
  },
  methods: {}
});

var Nav = new Vue({
   router,
   template: '<Navbar/>',
   el: "#navbar",
   components: {
	   Navbar
   }
});
