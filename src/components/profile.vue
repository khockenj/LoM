<template>
<div class="profile">
<div class="overlay"></div>
<div>
  <b-jumbotron style="padding:1rem 1rem!important;" bg-variant="dark" text-variant="white" header-level="4" fluid>
    <i class="fas fa-cog" style="position: absolute;right:.5%;top:7%;"></i>
    <template v-slot:header>{{ $route.params.user }}<img class="rankIcon" :src="'/static/ranks/' + 'diamond_4' + '.png'" /></template>
  </b-jumbotron>
</div>
<b-container fluid>
    <b-row class="equal">
        <b-col lg="6">
            <Plotly :data="data" :layout="layout" :displayModeBar="true"/>
        </b-col>
        <b-col>
            <goals/>
        </b-col>
        <b-col>
            <stats/>
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
        <b-col v-for="m in mains" v-bind:key="m" :champ="m">
            <profile-champion :champ="m"/>
        </b-col>
    </b-row>
</b-container>

</div>
</template>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
import { Plotly } from 'vue-plotly'
import Goals from './Goals'
import ProfileStats from './ProfileStats'
import ProfileChampionCard from './ProfileChampionCard'
export default {
  name: 'ProfilePage',
    components: {
    Plotly,
    'goals': Goals,
    'stats': ProfileStats,
    'profile-champion': ProfileChampionCard
  },
  data: function() {
  return {
    data:[{
      x: [1,2,3,4],
      y: [10,15,13,17],
      type:"scatter"
    }],
    layout:{
      title: "Rank Graph"
    },
    mains: ["Ryze", "Cassiopeia", "Neeko", "Velkoz", "Taliyah", "Diana"]
  }
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
  top:5%;
  left:0px;
  z-index:-1000;
}

.rankIcon {
	max-width:96px;
	max-height:96px;
	vertical-align: middle;
}
</style>
