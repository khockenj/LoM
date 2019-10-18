<template>
  <b-navbar v-if='p' toggleable="lg" type="dark" style="background-color:black;">
    <b-navbar-brand to="/">LoM
    <!--<img src="/static/logo.png" style="max-width:128px;position:absolute;z-index:1000;left:-1.5rem;top:-.5rem;" class="d-inline-block align-top" alt="LoM">-->
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
      <b-nav-item><router-link class="nav-link" to="/search">Search Mentors</router-link></b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto" v-if='p.loggedIn'>
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <img style='max-width:32px;' :src="'/static/squareicons/' + p.profileData.main.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"/>
            <em>{{p.profileData.name}}</em>
          </template>
          <b-dropdown-item :to="'/profile/' + p.profileData.name"><i class="fas fa-user textIcon"></i>Your Profile</b-dropdown-item>
          <b-dropdown-item to="/editProfile"><i class="fas fa-cog textIcon"></i>Settings</b-dropdown-item>
          <b-dropdown-item href="/logout"><i class="fas fa-sign-out-alt textIcon"></i>Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    <b-navbar-nav class="ml-auto" v-if='!p.loggedIn' right>
      <b-button class='mx-2' variant="primary" to="/login">Sign In</b-button>
      <b-button variant="success" to="/signup">Sign Up</b-button>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
</template>
<style>
.nav-link {
display:inline;
}
</style>
<script>
export default {
  name: 'Navbar',
  props: ['p'],
  methods: {
},
data: {
},
mounted: async function() {
this.p = await this.$parent;
}
}
</script>