<template>
  <div class="login" style="max-width:600px;">
    <div class="overlay"></div>
        <b-card bg-variant='dark' text-variant="light" style="max-width:600px;margin:auto;" header-bg-variant="info" border-variant="info">
       <template v-slot:header>
     <i class="fas fa-sign-in-alt no-hover-header"></i> Sign In
    </template>
     <img src="/static/logo.png" style="max-width:45%;padding-bottom:1%;" />
      <b-row class="my-1 py-2">
        <b-col>
          <b-button
            style="background-color:#7289da;color:white;"
            target="_blank"
            href="/login"
            block
          >
           <i class="fas fa-sign-in-alt textIcon"></i>Sign in with
            <i style="color:white!important;" class="fab fa-discord"></i>Discord
          </b-button>
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col lg="6" style='text-align:left;'>
          <b-form-checkbox
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
  background-color: rgba(0, 0, 0, 0.5) !important;
  background-image: url("/static/backgrounds/splash/Yasuo_0.jpg");
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1000;
  filter: blur(2px)  drop-shadow(16px 16px 20px red);
  -webkit-filter: blur(2px);

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