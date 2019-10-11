<template>
  <b-navbar toggleable="lg" type="dark" style="background-color:black;">
    <b-navbar-brand href="#">LoM
    <!--<img src="/static/logo.png" style="max-width:128px;position:absolute;z-index:1000;left:-1.5rem;top:-.5rem;" class="d-inline-block align-top" alt="LoM">-->
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
		  <b-nav-item><router-link class="nav-link" to="/">Home</router-link></b-nav-item>
      <b-nav-item><router-link class="nav-link" to="/search">Search</router-link></b-nav-item>
      <b-nav-item v-if='!loggedIn'><router-link class="nav-link" to="/login">Sign In</router-link></b-nav-item>
      <b-nav-item v-if='loggedIn'><a class="nav-link" href="/logout">Sign out</a></b-nav-item>
      <b-nav-item v-if='loggedIn'><router-link class="nav-link" to="/editProfile">Edit Profile</router-link></b-nav-item>
      <b-nav-item v-if='loggedIn'><router-link class="nav-link" :to="'/profile/' + profileData.name">Your Profile</router-link></b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
<style>
.nav-link {
display:inline;
}
</style>
<script>
import axios from 'axios'
export default {
  
  name: 'Navbar',
  props: ['loggedIn', 'profileData'],
  methods: {
    checkUser: function() {
      //console.log(document.cookie);
    //const path = 'http://localhost:5000/api/checkUser
    const path = '/api/checkUser'
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
},
mounted: function() {
  this.checkUser();
}
}
</script>