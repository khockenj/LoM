<template>
  <b-navbar v-if="p" toggleable="lg" type="dark" style="background-color:black;">
    <b-navbar-brand to="/">
      LoM
      <!--<img src="/static/logo.png" style="max-width:128px;position:absolute;z-index:1000;left:-1.5rem;top:-.5rem;" class="d-inline-block align-top" alt="LoM">-->
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item>
          <router-link class="nav-link" to="/nowLive">
            <i class="fas fa-video textIcon" style="color:rgb(156,0,6);"></i>Live Mentors
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link class="nav-link" to="/search">
            <i class="fas fa-search textIcon" style="color:steelblue"></i>Search Mentors
          </router-link>
        </b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto" v-if="p.loggedIn">
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

      <b-navbar-nav class="ml-auto" v-if="!p.loggedIn" right>
        <b-button class="mx-2" variant="primary" to="/login"><i class="fas fa-sign-in-alt textIcon"></i>Sign In</b-button>
        <b-button variant="success" to="/signup"><i class="fas fa-user-plus textIcon"></i>Sign Up</b-button>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<style>
.nav-link {
  display: inline;
}
</style>
<script>
export default {
  name: "Navbar",
  props: ["p"],
  methods: {},
  data: {},
  mounted: async function() {
    this.p = await this.$parent;
  }
};
</script>