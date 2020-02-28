<template>
<div class="login" style="max-width:400px;">
<div class="overlay"></div>
   <!-- <img src="/static/logo.png" style="max-width:60%;padding-bottom:1%;" />-->
 <b-card bg-variant='dark' text-variant="light" style="max-width:400px;margin:auto;" header-bg-variant="info" border-variant="info">
       <template v-slot:header>
     <i class="fas fa-user-plus no-hover-header"></i> Sign Up
    </template>

    <b-row class="my-1 py-2">
      <b-col>
        <b-button style="background-color:#7289da;color:white;" href="/login?r=1&m=0" block>Sign up with <i style="color:white!important;" class="fab fa-discord"></i>Discord</b-button>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-button variant="success" v-b-modal.mentorCode block>Sign up as Mentor with <i style="color:white!important;" class="fab fa-discord"></i>Discord</b-button>
      </b-col>
    </b-row>
    <b-row class="my-1">
        <b-col lg="12" style='text-align:right;'>
             <router-link class="nav-link custom-control" to="/login">Already a user?</router-link>
         </b-col>
         <b-col>
         </b-col>
        </b-row>
    </b-card>
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