<template>
<div class="editProfile" style="max-width:1200px">
     <!--{{this.$route.query.new}}-->
<div class="overlay"></div>
<b-container style="max-width:1000px">
  <your-info/>
  <mentor-section v-if="true"/>
  <b-row v-if="false">
    <b-col lg="2" style="text-align:left;"><label for="yourgoals">Your Goals:</label></b-col>
    <b-col style='text-align:left'>[placeholder]</b-col>
  </b-row>
  <b-row class="py-2"><b-col>
    <b-button v-if="this.$route.query.new == '1'" variant="info" block>Create your Profile</b-button>
    <b-button v-if="this.$route.query.new != '1'" variant="info" block>Update Information</b-button>
    </b-col></b-row>
  </b-container>
</div>
</template>
<script>
import axios from 'axios'
import EditProfileMentor from './EditProfileMentor'
import EditProfileYourInfo from './EditProfileYourInfo'
export default {
  name: 'EditPage',
  data() {
      return {
          
      }
    },
  components: {
    'mentor-section': EditProfileMentor,
    'your-info': EditProfileYourInfo
  },
  
  }
</script>

<style scoped>
.overlay {
  background-color: rgba(0,0,0, 0.4) !important;
  background-image:url('/static/backgrounds/viktor.jpg');
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

.editProfile {
border:2px solid white;
color:white;
margin:auto;
margin-top:3%;
border-radius:5rem;
background-color:#32383E;
}

</style>