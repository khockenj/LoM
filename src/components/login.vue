<template>
<div class="login">
<div class="overlay"></div>
   <!-- <img src="/static/logo.png" style="max-width:60%;padding-bottom:1%;" />-->
  <b-container bg-variant="dark" style="color:white;padding-bottom:15%;text-align:left" fluid>
    <b-row class="my-1 py-2">
        <b-col style="font-size:2rem;text-align:center;padding-bottom:3%">Sign In</b-col>
        </b-row>
    <b-row class="my-1 py-2">
      <b-col lg="3">
        <label for="email">Email</label>
      </b-col>
      <b-col>
        <b-form-input id='email' type='email'></b-form-input>
      </b-col>
    </b-row>
     <b-row class="my-1  py-2">
      <b-col lg="3">
        <label for="email">Password</label>
      </b-col>
      <b-col>
        <b-form-input id='password' type='password'></b-form-input>
      </b-col>
    </b-row>
    <b-row class="my-1 py-2" style="padding-bottom:3%;">
        <b-col>
           <b-button block variant="info">Sign in</b-button>
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
        <router-link class="nav-link" style="margin-left:2.5rem;" to="/search">Forgot info?</router-link>
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
  background-color: rgba(238, 238, 238, 0.5) !important;
  background-image:url('/static/backgrounds/yasuo.jpg');
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position:fixed;
  width:100%;
  height:100%;
  top:5%;
  left:0px;
  z-index:-1000;
}

.login {
border:2px solid white;
margin:auto;
width:20%;
margin-top:5%;
border-radius:5rem;
background-color:#32383E;
}
</style>