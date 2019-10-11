<template>
  <b-navbar toggleable="lg" type="dark" style="background-color:black;">
    <b-navbar-brand to="/">LoM
    <!--<img src="/static/logo.png" style="max-width:128px;position:absolute;z-index:1000;left:-1.5rem;top:-.5rem;" class="d-inline-block align-top" alt="LoM">-->
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
      <b-nav-item><router-link class="nav-link" to="/search">Search Mentors</router-link></b-nav-item>
      <b-nav-item v-if='!loggedIn'><router-link class="nav-link" >Sign In</router-link></b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto" v-if='loggedIn'>
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <img style='max-width:32px;' :src="'/static/squareicons/' + profileData.main.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"/>
            <em>{{profileData.name}}</em>
          </template>
          <b-dropdown-item :to="'/profile/' + profileData.name"><i class="fas fa-user textIcon"></i>Your Profile</b-dropdown-item>
          <b-dropdown-item to="/editProfile"><i class="fas fa-cog textIcon"></i>Settings</b-dropdown-item>
          <b-dropdown-item href="/logout"><i class="fas fa-sign-out-alt textIcon"></i>Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    <b-navbar-nav class="ml-auto" v-if='!loggedIn' right>
      <b-button class='mx-2' variant="primary" to="/login">Sign In</b-button>
      <b-button variant="success" to="/signup">Sign Up</b-button>
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