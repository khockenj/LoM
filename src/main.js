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


var Search = new Vue({
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


http.createServer((req, res) => {
  fs.readFile('index.htm', 'utf-8', (err, content) => {
    if (err) {
      console.log('We cannot open "index.htm" file.')
    }

    res.writeHead(200, {
      'Content-Type': 'text/html; charset=utf-8'
    })

    res.end(content)
  })
}).listen(httpPort, () => {
  console.log('Server listening on: http://localhost:%s', httpPort)
})