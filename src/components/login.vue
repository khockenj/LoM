<template>
  <div class="login" style="max-width:600px;">
    <div class="overlay"></div>
        <b-card class='card-holder' header-bg-variant="secondary" border-variant="secondary" header-text-variant="light">
       <template v-slot:header>
    Sign In
    </template>
     <img src="/static/logo.png" style="max-width:45%;padding-bottom:5%;" />
      <b-row class="pt-4 pb-2">
        <b-col>
          <b-button
            style="background-color:#7289da;color:white;"
            target="_blank"
            href="/login"
            block
          >
          Sign in with
            Discord  <i style="color:white!important;" class="fab fa-discord"></i>
          </b-button>
        </b-col>
      </b-row>
      <b-row>
        <b-col lg="6" style='text-align:left;'>
          <b-form-checkbox
          style='display:none'
            id="checkbox-1"
            name="checkbox-1"
            value="remember"
            unchecked-value="dont_remember"
          >Remember me</b-form-checkbox>
        </b-col>
        <b-col style='text-align:right;'>
          <router-link
            class="nav-link custom-control"
            to="/signup"
            style='padding-right:0;'
          >New user?</router-link>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>
<script>
export default {
  name: "LoginPage",
  components: {},
  methods: {}
};
</script>

<style scoped>
.overlay {
  /* background-color: rgba(0, 0, 0, 0.5) !important; */
  background-image: url("/static/kevin.png");
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  /* background-position: center; */
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1000;
  filter: blur(2px);
  -webkit-filter: blur(2px);
}
.card-holder {
  max-width:600px;
  margin:auto;
  background-color:rgba(255,255,255,.85);
}
.card {
  border:5px solid inherit;
}
.login {
  margin: auto;
  padding-top: 5%;
}
.no-hover-header, .no-hover-header:hover {
  cursor:default;
  color:inherit;
}

.card-header {
  font-size:2rem;
}
</style>