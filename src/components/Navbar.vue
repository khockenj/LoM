<template>
  <b-navbar v-if="p" toggleable="lg" type="dark" style="background-color:transparent;">
    <b-navbar-brand to="/">
      LoM
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
           
        <b-button variant='outline-danger' to="/nowLive"><i class="fas fa-video textIcon" style="color:rgb(156,0,6);"></i>Live Mentors</b-button>
      </b-navbar-nav>

     
  
 

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
      <b-input-group class="semi-transparent">
         <template v-slot:append>
      <b-input-group-text v-on:click="sendSearch" class='semi-transparent'><i class="fas fa-search textIcon" style="color:steelblue"></i></b-input-group-text>
    </template>
      <b-input class='semi-transparent' v-model='searchText' placeholder="Search Mentors"></b-input>
      </b-input-group>
    </b-nav-form>
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
        <b-button variant="primary" to="/signup"><i class="fas fa-user-plus textIcon"></i>Sign Up</b-button>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<style>
.navbar {
  font-size:1.25rem;
}
.nav-link {
  display: inline;
  margin:auto;
}
.nav-item {
  border: 1px solid #fff;
  border-radius: .25rem;
}
.semi-transparent {
  background-color:rgba(255,255,255,.85);
  font-size:1.25rem;
}
.btn {
  font-size:1.25rem;
}
.invisButton {
  background-color:rgba(0,0,0,0);
  border:0;
}
</style>
<script>
export default {
  name: "Navbar",
  methods: {
    sendSearch: function() {
      console.log(this.searchText);
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