<template>
<div class="editProfile">
     {{this.$route.query.new}}
<div class="overlay"></div>
<b-container style="max-width:1200px">
    <b-row>
        <b-col lg="12">
    <b-form-input v-on:change='updateList' list="champions" v-model="champs"></b-form-input>
    <datalist autocomplete='off' id="champions">
    <option v-for="c in champions" :value='c'>{{c}}</option>
  </datalist>
        </b-col>
     </b-row>
     <b-form-group>

       <b-row>
         <b-col style='padding:12px;'>Champion</b-col>
         <b-col style='padding:12px;'>Main?</b-form-radio></b-col>
         <b-col style='padding:12px;'>Remove</i></b-col>
         </b-row>

     <b-row v-for="x in removedChamps" :key=x>
         <b-col><img style="max-width:48px":src="'/static/squareicons/' + x.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'" />{{x}}</b-col>
         <b-col style='padding:12px;'><b-form-radio v-model="main" :value='x'></b-form-radio></b-col>
         <b-col style='padding:12px;'><i style="font-size:24px;" :value='x' class="fas fa-trash-alt red" :v-model='x' v-on:click='deleteRow(x)'></i></b-col>
         </b-row>
            </b-form-group>
  </b-container>
</div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'EditPage',
  data() {
      return {
          champions: this.championsList(),
          removedChamps: [],
          main: '',
          champs: '',
      }
    },
  components: {},
  methods: {
	championsList: function() {	
	var vm = this;
	console.log(this);
	var championList = [];
	for (const [key, value] of Object.entries(this.$parent.$parent.champions)) {
		championList.push(value.name);
	}
	console.log(championList);
	return championList;
  },
    updateList: function() {
        if(this.removedChamps.length <= 5 && this.champions.includes(this.champs) && !this.removedChamps.includes(this.champs)) {
        this.removedChamps.push(this.champs);
        }
        this.champs = '';
    },
    deleteRow: function(c) {
        console.log(c);
        var index = this.removedChamps.indexOf(c);
        this.removedChamps.splice(index, 1);
    }
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