<template>
  <b-navbar v-if="p" sticky='true' toggleable="lg" type="light" variant='light'>
    <b-navbar-brand to="/">
      <img src='/static/kevinlogo.png' style='max-width:300px;padding-top:.25rem;padding-left:.25rem;padding-right:.25rem;' />
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>

        <b-nav-item style='display:none'>
          <router-link class="nav-link" to="/search">
            <i class="fas fa-search textIcon" style="color:steelblue"></i>Search Mentors
          </router-link>
        </b-nav-item>

              <b-nav-item style='display:none;'>
          <router-link class="nav-link" to="/nowLive">
            <i class="fas fa-video textIcon" style="color:rgb(156,0,6);"></i>Live Mentors
          </router-link>
        </b-nav-item>
           
        <b-button variant='outline-danger' to="/nowLive" class='header-btn'><i class="fas fa-video textIcon"></i>Live Mentors</b-button>
        <b-button variant='outline-info' to="/nowLive" class='header-btn'><i class="fas fa-newspaper textIcon"></i>News &amp; Updates</b-button>
        <b-button variant='outline-info' to="/nowLive" class='header-btn'><i class="fas fa-calendar-week textIcon"></i>Events</b-button>
        <b-button variant='outline-info' to="/nowLive" class='header-btn'><i class="fab fa-discord textIcon"></i>Discord</b-button>
         <b-button variant='outline-info' to="/nowLive" class='header-btn'><i class="fas fa-paper-plane textIcon"></i>Contact Us</b-button>
      </b-navbar-nav>

     
  
 

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

      <b-input-group class="semi-transparent">
         <template v-slot:append>
      <b-input-group-text v-on:click="sendSearch" class='semi-transparent click'><i class="fas fa-search textIcon click" style="color:steelblue"></i></b-input-group-text>
    </template>
      <b-input v-on:keyup.enter="sendSearch" :disabled="$route.name == 'Search'" class='semi-transparent' v-model='searchText' placeholder="Search Mentors"></b-input>
      </b-input-group>

      </b-navbar-nav>

      <b-navbar-nav class="" v-if="p.loggedIn">
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <img
              style="max-width:32px;min-width:32px;"
              :src="p.profileData.main? '/static/squareicons/' + p.profileData.main.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png': 'data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII='"
            />
            <em>{{p.profileData.name}}</em>
          </template>
           <b-dropdown-item to='/admin' v-if='p.profileData.admin'>
            <i class="fas fa-toolbox textIcon"></i>Admin
          </b-dropdown-item>
           <b-dropdown-item to="/dashboard">
           <i class="fas fa-tachometer-alt textIcon"></i>Dashboard
          </b-dropdown-item>
          <b-dropdown-item :to="'/profile/' + p.profileData.did">
            <i class="fas fa-user textIcon"></i>Your Profile
          </b-dropdown-item>
          <b-dropdown-item to="/editProfile">
            <i class="fas fa-cog textIcon"></i>Settings
          </b-dropdown-item>
          <b-dropdown-item href="/logout">
            <i class="fas fa-sign-out-alt textIcon"></i>Sign Out
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>



      <b-navbar-nav class="" v-if="p && p.loggedIn == false" right>
        <b-button class="mx-2" variant="secondary" to="/login"><i class="fas fa-sign-in-alt textIcon"></i>Sign In</b-button>
        <b-button variant="info" to="/signup"><i class="fas fa-user-plus textIcon"></i>Sign Up</b-button>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<style>
@media (min-width: 1700px) {
.navbar {
  font-size:1.1rem;
}
.semi-transparent {
  font-size:1.1rem;

}
.btn {
  font-size:1.1rem;
}
}

@media (max-width: 1700px) {
.navbar {
  font-size:.9rem;
}
.semi-transparent {
  font-size:.9rem;
}
.btn {
  font-size:.9rem;
}
}

.nav-link {
  display: inline;
  margin:auto;
}

.invisButton {
  background-color:rgba(0,0,0,0);
  border:0;
}
.click {
  cursor:pointer;
}
.form-control {
  border-top-left-radius:.25rem!important;
  border-bottom-left-radius:.25rem!important;
  background-color:rgba(255,255,255,.9);
}
.input-group > .input-group-append > .input-group-text {
  border-top-right-radius:.25rem!important;
  border-bottom-right-radius:.25rem!important;
}
.header-btn {
  margin-left:1rem;
  margin-right:1rem;
}
</style>
<script>
export default {
  name: "Navbar",
  methods: {
    sendSearch: function() {
      if(this.searchText && this.$route.name != 'Search') {
       this.$router.push({'name': 'Search', 'params': {searchText: this.searchText}});
      }
    }
  },
  data: function() {
    return {
      p: null,
      searchText: null
    }
  },
  beforeCreate: async function() {
    this.p = await this.$parent;
  }
};
</script>