<template>
<div class="profile">
<div class="overlay" :style="setBG"></div>
<div>
<b-jumbotron style="padding:1rem 1rem!important;" bg-variant="dark" text-variant="white" header-level="4" fluid>
     <div style="display:flex;">
    <div style="flex-grow:12;"><i class="fas fa-star star" v-for="s in Math.floor(profileData.score)"></i><i class="fas fa-star-half-alt star" v-for="s in customRound(profileData.score-Math.floor(profileData.score))[0]"></i><i class="far fa-star star" v-for="s in 5-Math.ceil(profileData.score)+customRound(profileData.score-Math.floor(profileData.score))[1]"></i></div>
    <div class="iconHolder" style="flex-grow:0;">
      <a v-if="profileData.socials.twitch" :href="'https://www.twitch.tv/' + profileData.socials.twitch"><i class="fab fa-twitch"></i></a>
      <a v-if="profileData.socials.youtube" :href="'https://www.youtube.com/user/' + profileData.socials.youtube"><i class="fab fa-youtube"></i></a>
      <a v-if="profileData.socials.discord" :href="'https://discord.gg/' + profileData.socials.discord"><i class="fab fa-discord"></i></a>
      <a v-if="profileData.socials.twitter" :href="'https://www.twitter.com/' + profileData.socials.twitter"><i class="fab fa-twitter"></i></a>
      <a v-if="profileData.socials.patreon" :href="'https://www.patreon.com/' + profileData.socials.patreon"><i class="fab fa-patreon"></i></a>
      </div>
      </div>
    <span v-if='$parent.$parent.profileData'><i v-if='$parent.$parent.profileData.did == profileData.did' class="fas fa-cog" style="position: absolute;right:.6rem;top:4rem;" v-b-modal.settings></i></span>
    <i class="fas fa-info-circle" style="position:absolute; left:.6rem; top:4rem;" v-b-modal.info></i>
    <template v-slot:header>{{profileData.name}}<img class="rankIcon" :src="'/static/ranks/' + profileData.rank + '.png'" /></template>
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
            <requirements :requirements="profileData.requirements" v-if="profileData.type == 'mentor'" style="height:100%;" />
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
            <profile-champion :champ="m" :main="profileData.main"/>
        </b-col>
    </b-row>
</b-container>

<b-modal @ok="saveBG" id="settings" ok-title="Save">   
   <template v-slot:modal-title>
      Settings
    </template>
    <b-container>
      <b-row class='py-2'>
  <b-col lg="3">
    <label for='champ'>Champion:</label>
    </b-col><b-col lg="9">
    <b-form-select id='champ' v-on:change='filterList' v-model="selectedChamp">
          <option :key='k' v-for='(v,k) in skinList' :value='k'>{{k}}</option>
        </b-form-select>
  </b-col></b-row>
  <b-row>
    <b-col lg="3">
      <label for='yourbg'>Splash:</label>
      </b-col>
      <b-col lg="9">
      <b-form-select id='yourbg' v-model="selectedBG">
          <option :key='s.id' v-for='s in filteredList' :value='s.id'>{{s.name}}</option>
        </b-form-select>
        </b-col></b-row>
    </b-container>
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
import skinlist from '../../static/skinList.json'
//http://ddragon.leagueoflegends.com/cdn/9.20.1/data/en_US/champion/[champ].json 
//-> get list of skins for each champ, add into a file as dict champ:{text: skinName, value: num}, save list so we can figure out which num belongs to which name
//champ.data.skins[.name .num]
//eg. {"Ekko": [{"name": "Trick or Treat Ekko", "value": 12}]}
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
  props: ['p'],
  data: function() {
  return {
    selectedChamp: null,
    selectedBG: null,
    filteredList: null,
    skinList: skinlist,
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
        makeToast(title, content, variant = null) {
        this.$bvToast.toast(content, {
          title: `${title}`,
          variant: variant,
          solid: true,
          toaster: 'b-toaster-top-center'
        })
      },
    saveBG: function() {
      console.log(this.selectedBG);
      this.profileData.bg = this.selectedChamp + "_" + this.selectedBG;
      const path = 'http://localhost:5000/api/profileInfo/' + 'K3Vx'
      //const path = '/api/profileInfo/' + this.p.name;
      axios.post(path, {'did': this.$parent.$parent.profileData.did, 'bg': this.profileData.bg})
    .then(response => {
      console.log(response);
      this.makeToast('Updated', 'Updated background', 'success')
    })
    .catch(error => {
      this.makeToast('Error', "Err - there's been an error in the back. Try again or report it - thank you!", 'danger');
      console.log(error)
    })

    },
    filterList: function() {
      this.filteredList = this.skinList[this.selectedChamp]
      console.log(this.filteredList)
    },
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
    const path = 'http://localhost:5000/api/profileInfo/' + this.$route.params.user
    //const path = '/api/profileInfo/' + this.$route.params.user
    axios.get(path)
    .then(response => {
      this.profileData = response.data;
      console.log(this.profileData);
    })
    .catch(error => {
      console.log(error)
    })

  },
    
  },
  mounted: async function(){
    await this.$parent;
    console.log(this.$parent);
    this.getData();
  },
  updated: function() {
  },
  watch: {
  '$route'(to,from) {
    this.getData();
  }
  },
  computed: {
    setBG: function() {
      return {
        '--bg': "url('/static/backgrounds/splash/" + this.profileData.bg + ".jpg')"
      }
    }
  }
}

 

</script>

<style scoped>
.overlay {
  background-color: rgba(0,0,0, 0.4) !important;
  background-image:var(--bg);
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

.iconHolder {
  text-align:right;
  font-size:calc(12px + .6vw);
}

</style>
