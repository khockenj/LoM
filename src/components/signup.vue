<template>
<div class="login" style="max-width:1500px;">
<div class="overlay"></div>
<b-card-group>
<b-card class='card-holder' header-bg-variant="info" border-variant="secondary" header-text-variant="light">
   <template v-slot:header>
    League of Mentoring
    </template>
  <p>League of Mentoring started in 2016 by <a href='https://euw.op.gg/summoner/userName=katniss+evermeme'>Katniss Evermeme</a> as a discord server to help his friends improve
  at League of Legends. Since then, it has grown to be a community of players all seeking to improve at their craft.  </p>

  <p>League of Mentoring is the place to come if you want to improve and unlock your potential</p>

  <b-list-group>
 <b-list-group-item variant='secondary' style='text-align:center;' >
   <h5 style='margin:0;'>Perks and Benefits</h5>
  </b-list-group-item>

  <b-list-group-item class="d-flex justify-content-between align-items-center">
    Recieve coaching
    <i class="fas fa-check-circle green no-hover"></i>
  </b-list-group-item>

  <b-list-group-item  class="d-flex justify-content-between align-items-center">
    Track your stats
    <i class="fas fa-check-circle green no-hover"></i>
  </b-list-group-item>

  <b-list-group-item class="d-flex justify-content-between align-items-center">
    Get notified about exclusive events
    <i class="fas fa-check-circle green no-hover"></i>
  </b-list-group-item>

  <b-list-group-item class="d-flex justify-content-between align-items-center">
    Gain access to exclusive League of Mentoring content
    <i class="fas fa-check-circle green no-hover"></i>
  </b-list-group-item>

  <b-list-group-item  class="d-flex justify-content-between align-items-center">
    Crush your competition!
     <i class="fas fa-check-circle green no-hover"></i>
  </b-list-group-item>
</b-list-group>
    </b-card>

 <b-card class='card-holder' style="max-width:600px;" header-bg-variant="info" border-variant="secondary" header-text-variant="light">
       <template v-slot:header>
    Sign Up
    </template>
     <img src="/static/logo.png" style="max-width:52%;padding-bottom:6.5%;" />
      <b-row class="pt-4 pb-2">
        <b-col>
        <b-button style="background-color:#7289da;color:white;" href="/login?r=1&m=0" block>Sign up with Discord<i style="color:white!important;" class="fab fa-discord"></i></b-button>
        </b-col>
      </b-row>
      <b-row class='pb-1'>
      <b-col>
        <b-button variant="success" v-b-modal.mentorCode block>Sign up as Mentor with Discord<i style="color:white!important;" class="fab fa-discord"></i></b-button>
      </b-col>
    </b-row>
      <b-row>
        <b-col class='pt-2 pb-0' lg="8" style='text-align:left;'>
             <router-link to="/login">Want to join the mentoring team?</router-link>
         </b-col>
         <b-col class='pt-2 pb-0' lg="4" style='text-align:right;'>
             <router-link to="/login">Already a user?</router-link>
         </b-col>
      </b-row>
    </b-card>
</b-card-group>
  <b-modal @ok="checkCode" id="mentorCode">   
   <template v-slot:modal-title>
      Mentor Code
    </template>
    <form ref='form'  @submit.stop.prevent="checkCode">
    <b-form-input v-model="mcode" id="mentor-code" placeholder="Mentor Code" required></b-form-input>
        </form>
     <b-alert v-model="wrongCode" variant="danger">
      Wrong code
    </b-alert>
    </b-modal>
</div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'SignupPage',
  data() {
      return {
        mcode: '',
        wrongCode: false
      }
    },
  components: {},
  methods: {
    checkCode: function(bvModalEvt) {
    const path = 'http://localhost:5000/api/checkCode/' + this.mcode;
    //const path = '/api/checkCode/' + this.mcode;
    bvModalEvt.preventDefault();
    axios.get(path)
    .then(response => {
      if(response.data != null && response.data.used == false && response.data.type == "mentor") {
          this.wrongCode = false;
          window.location.href = "/login?r=1&mcode=" + this.mcode;
      } else {
          this.wrongCode = true;
      }
    })
    .catch(error => {
      console.log(error)
    })
    

    }
  }
  }
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

.card {
  margin:0;
}
.card-holder {
  background-color:rgba(255,255,255,.85);
}

.login {
  margin: auto;
  padding-top: 7%;
}
.no-hover-header, .no-hover-header:hover {
  cursor:default;
  color:inherit;
}
.no-hover {
  pointer-events: none;
}
.card-header {
  font-size:2rem;
}
</style>