<template>
<div class="login" style="max-width:400px;">
<div class="overlay"></div>
   <!-- <img src="/static/logo.png" style="max-width:60%;padding-bottom:1%;" />-->
  <b-container bg-variant="dark" style="color:white;padding-bottom:15%;text-align:left">
    <b-row class="my-1 py-2">
        <b-col style="font-size:2rem;text-align:center;padding-bottom:3%">Sign In</b-col>
        </b-row>
    <b-row class="my-1 py-2">
      <b-col>
        <b-button style="background-color:#7289da;color:white;" target="_blank" href="/login" block>Sign in with <i style="color:white!important;" class="fab fa-discord"></i>Discord</b-button>
      </b-col>
    </b-row>
    <b-row class="my-1">
        <b-col lg="6">
           <b-form-checkbox
      id="checkbox-1"
      name="checkbox-1"
      value="remember"
      unchecked-value="dont_remember"
    >
      Remember me
    </b-form-checkbox>
         </b-col>
         <b-col>
        <router-link class="nav-link" style="position:absolute;bottom:0;right:0;" to="/signup">New user?</router-link>
         </b-col>
        </b-row>
  </b-container>
</div>
</template>
<script>
export default {
  name: 'LoginPage',
  components: {},
  methods: {}
  }
</script>

<style scoped>
.overlay {
  background-color: rgba(0,0,0, 0.4) !important;
  background-image:url('/static/backgrounds/splash/Yasuo_0.jpg');
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position:fixed;
  width:100%;
  height:100%;
  top:0%;
  left:0px;
  z-index:-1000;
}

.login {
border:2px solid white;
margin:auto;
margin-top:5%;
border-radius:5rem;
background-color:#32383E;
}
</style>