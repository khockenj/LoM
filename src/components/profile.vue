<template>
<div class="profile">
<div class="overlay"></div>
<div>
  <b-jumbotron style="padding:1rem 1rem!important;" bg-variant="dark" text-variant="white" header-level="4" fluid>
    <i class="fas fa-cog" style="position: absolute;right:.5%;top:7%;" v-b-modal.settings></i>
    <i class="fas fa-info-circle" style="position:absolute; left:.5%; top:7%;" v-b-modal.info></i>
    <template v-slot:header>{{profileData.name}}<img class="rankIcon" :src="'/static/ranks/' + 'diamond_4' + '.png'" /></template>
    <div><i class="fas fa-star star" v-for="s in Math.floor(profileData.score)"></i><i class="fas fa-star-half-alt star" v-for="s in customRound(profileData.score-Math.floor(profileData.score))[0]"></i><i class="far fa-star star" v-for="s in 5-Math.ceil(profileData.score)+customRound(profileData.score-Math.floor(profileData.score))[1]"></i></div>
    <div style="font-size:24px;position:absolute;right:.5%;top:19%;"><i class="fab fa-twitch"></i><i class="fab fa-youtube"></i><i class="fab fa-discord"></i><i class="fab fa-twitter"></i><i class="fab fa-patreon"></i></div>
  </b-jumbotron>
</div>
<b-container style="max-width:1200px">
    <b-row>
        <b-col lg="6">
            <Plotly v-if="profileData.type == 'student'" style="height:100%;" :data="graphdata" :layout="layout" :displayModeBar="true"/>
            <about-me :bio="profileData.bio" v-if="profileData.type == 'mentor'" style="height:100%;" />
        </b-col>
        <b-col lg="3">
            <goals v-if="profileData.type == 'student'" style="height:100%;"/>
            <achievements :achievements="profileData.achievements" v-if="profileData.type == 'mentor'" style="height:100%;" />
        </b-col>
        <b-col lg="3">
            <stats v-if="profileData.type == 'student'" style="height:100%;"/>
            <requirements v-if="profileData.type == 'mentor'" style="height:100%;" />
        </b-col>
    </b-row>
    <b-row>
        <b-col style="padding:0">
    <b-jumbotron style="padding:1rem 1rem!important;margin-top:1rem;" bg-variant="dark" text-variant="white" header-level="4" fluid>
    <template v-slot:header>Champions</template>
  </b-jumbotron>
        </b-col>
 </b-row>
    <b-row style="padding-top:0;">
        <b-col v-for="m in profileData.champs" v-bind:key="m" :champ="m">
            <profile-champion :champ="m"/>
        </b-col>
    </b-row>
</b-container>

<b-modal id="settings">   
   <template v-slot:modal-title>
      Settings
    </template>
    settings
    </b-modal>

<b-modal id="info">   
   <template v-slot:modal-title>
      Information
    </template>
    info
    </b-modal>

  <b-modal id="shareGoals">   
   <template v-slot:modal-title>
      Share Goals
    </template>
    share
    </b-modal>

<b-modal id="changeGoals">   
   <template v-slot:modal-title>
      Change Goals
    </template>
    change
    </b-modal>

    <b-modal id="bookSession">   
   <template v-slot:modal-title>
      Book Session
    </template>
    calendar
    </b-modal>

</div>
</template>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
import { Plotly } from 'vue-plotly'
import Goals from './Goals'
import ProfileStats from './ProfileStats'
import ProfileChampionCard from './ProfileChampionCard'
import AboutMe from './AboutMe'
import Achievements from './Achievements'
import Requirements from './Requirements'
import axios from 'axios'
export default {
  name: 'ProfilePage',
    components: {
    Plotly,
    'goals': Goals,
    'stats': ProfileStats,
    'profile-champion': ProfileChampionCard,
    'about-me': AboutMe,
    'requirements': Requirements,
    'achievements': Achievements
  },
  data: function() {
  return {
    graphdata:[{
      x: [1,2,3,4],
      y: [10,15,13,17],
      type:"scatter"
    }],
    layout:{
      title: "Rank Graph"
    },
    profileData: {},
  }
},
  methods: {
    customRound: function(n){
      if(n>=.4) {
        return [1,0];
      } else if(n != 0) {
        return [0,1];
      } else {
        return [0,0];
      }
    },
    getData: function() {
    const path = './api/profileInfo/' + this.$route.params.user
    axios.get(path)
    .then(response => {
      this.profileData = response.data;
      console.log(this.profileData);
    })
    .catch(error => {
      console.log(error)
    })

  }
  },
  mounted: function(){
    this.getData();
  },
  updated: function() {
    //this.getData();
  }
}

 

</script>

<style scoped>
.overlay {
  background-color: rgba(0,0,0, 0.4) !important;
  background-image:url('/static/backgrounds/brand.jpg');
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position:fixed;
  width:100%;
  height:100%;
  top:0;
  left:0px;
  z-index:-1000;
}

.rankIcon {
	max-width:96px;
	max-height:96px;
	vertical-align: middle;
}

</style>
