import Vue from 'vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
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
      loggedIn: false,
      profileData: null,
      complete: false,
  },
  methods: {
    checkUser: async function() {
    //console.log(document.cookie);
     const path = 'http://localhost:5000/api/checkUser'
     //const path = '/api/checkUser'
     axios.get(path)
     .then(response => {
       this.complete = true;
       if(response.data == false) {
           this.loggedIn = false;
           console.log(loggedIn)
       } else {
         this.loggedIn = true;
         this.profileData = response.data;
       }
     })
     .catch(error => {
       console.log(error)
       this.complete = true;
       this.loggedIn = false;
     })
   }
   },
   mounted: async function() {
     await this.checkUser();
   }
});

var Nav = new Vue({
   router,
   template: '<Navbar/>',
   el: "#navbar",
   components: {
	   Navbar
   },
   methods: {
    checkUser: async function() {
    //console.log(document.cookie);
     const path = 'http://localhost:5000/api/checkUser'
     //const path = '/api/checkUser'
     axios.get(path)
     .then(response => {
       this.complete = true;
       if(response.data == false) {
           this.loggedIn = false;
           console.log(loggedIn)
       } else {
         this.loggedIn = true;
         this.profileData = response.data;
       }
     })
     .catch(error => {
       console.log(error)
       this.complete = true;
       this.loggedIn = false;
     })
   }
   },
   data: {
     loggedIn: false,
     profileData: null,
     complete: false
   },
   mounted: async function() {
     await this.checkUser();
   }
});
