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
      champions: Champions['data'],
      loggedIn: false
  },
  methods: {
   checkUser: function() {
   //console.log(document.cookie);
    const path = 'http://localhost:5000/api/checkUser'
    //const path = '/api/checkUser'
    axios.get(path)
    .then(response => {
      if(response.data == false) {
          this.loggedIn = false;
          console.log(this.loggedIn)
      } else {
        this.profileData = response.data;
        console.log(this.profileData);
        this.loggedIn = true;
      }
    })
    .catch(error => {
      console.log(error)
      this.loggedIn = false;
    })
  }
  }
});

var Nav = new Vue({
   router,
   template: '<Navbar/>',
   el: "#navbar",
   components: {
	   Navbar
   }
});
