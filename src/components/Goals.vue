<template>
  <b-card
    border-variant="success"
    header="Weekly Goals"
    header-bg-variant="success"
    header-text-variant="white"
    align="center"
    title="Successful"
  >
    <b-card-text>{{this.feelBetterMessage()}}</b-card-text>
    <b-list-group flush>
      <b-list-group-item v-for='(g,k) in goalProgress' :key='g'>
        <span v-if="k == 'gamesPlayed'">Weekly Games:</span>
        <span v-if="k == 'gamesPlayed'" :class="colorSwitcher(g, 100)">{{g}}/100</span>

        <span v-if="k == 'champsPlayed'">Total Champs Played:</span>
        <span v-if="k == 'champsPlayed'" :class="colorSwitcher(g, 11, true)">{{g}}/11</span>

      <span class='text-muted' v-if="k=='lastUpdate'">{{new Date((g*1000)-604800000).toLocaleDateString()}} - {{new Date(g*1000).toLocaleDateString()}}</span>
    </b-list-group-item>
    </b-list-group>
    <template v-slot:footer>
      <b-card-body class="mx-auto" style="padding:0!important;">
        <b-button variant="warning" v-b-modal.changeGoals>Edit Goals</b-button>
        <b-button variant="success" v-b-modal.shareGoals>Share</b-button>
      </b-card-body>
    </template>
  </b-card>
</template>

  <script>
export default {
  name: "Goals",
  props: ["goals", "goalProgress"],
  data: function() {
    return {
      failCount: 0
    }
  },
  methods: {
    colorSwitcher: function(actual, goal, reverse = false) {
    let r = "green";
    if(!reverse) {
      if(actual >= goal) r = "green";
      else if(goal*.5 <= actual) r =  "yellow";
      else r = "red";
    } else {
      if(actual <= goal) r = "green";
      else if(goal*1.5 >= actual) r = "yellow";
      else r = "red"; 
    }
    return r;
  },
  feelBetterMessage: function() {
    if(this.failCount == 0) return "You're crushing your goals this week"
    else if(this.failCount <= 1) return "You're doing pretty great"
    else if(this.failCount <= 2) return "You can step it up"
    else if(this.failCount > 2) return "Faker would be disappointed..."
  },
  failCounter: function(actual, goal, reverse = false) {
    let r = 0;
    if(!reverse) {
      if(actual >= goal) r = 0;
      else if(goal*.5 <= actual) r =  .5;
      else r = 1;
    } else {
      if(actual <= goal) r = 0;
      else if(goal*1.5 >= actual) r = .5;
      else r = 1; 
    }
    return r;
  }
  },
  mounted: function() {
    for (const [key, value] of Object.entries(this.goalProgress)) {
      console.log(key);
      if(key == "gamesPlayed") this.failCount+=this.failCounter(value,100,false);
      else if(key == "champsPlayed") this.failCount+=this.failCounter(value,11,true);
      console.log(this.failCount)
    }
  }
};
</script>