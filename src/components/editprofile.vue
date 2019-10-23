<template>
<div class="editProfile" style="max-width:1200px">
     <!--{{this.$route.query.new}}-->
<div class="overlay" v-if="p"></div>
<b-container v-if="p" style="max-width:1000px">
  <b-row>
    <b-col lg="12" class="py-1"><h1>Your Profile</h1></b-col>
    </b-row>
    <b-row>
    <b-col lg="12" style="text-align:left;"><h2>Your Stuff</h2></b-col>
    </b-row>
    <b-row>
      <b-col lg="2"  style="text-align:left;">    
    <label for="yourchamps">Your Champions:</label>
    </b-col>
    <b-col lg="10">
    <b-form-input id='yourchamps' v-on:change='updateList' list='champions' v-model="champs"></b-form-input>
    <datalist autocomplete='off' class='champions' id='champions'>
    <option :key='c' v-for="c in champions" :value='c'>{{c}}</option>
  </datalist>
        </b-col>
     </b-row>
     <b-form-group>

      
     <b-row class='mx-auto' style='padding-top:1rem;text-align:center;'>
         <b-col v-for="x in removedChamps" :key=x class="py-3" lg="2" style="max-width:100%;justify-content: space-between;position:relative;"> 
         <div class='img-holder'>
           <img v-on:click='setMain(x)' style="max-width:128px;position:relative;" :src="'/static/squareicons/' + x.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'" />
         <i style="font-size:24px;" :value='x' class="fas fa-trash-alt deleteChamp" :v-model='x' v-on:click="deleteRow(x, 'champ')"></i>
          <b-badge v-if="x == main" class='badgeChamp' variant='success'>MAIN</b-badge>
         </div>
        
         </b-col>
         </span>
         </b-row>
            </b-form-group>
<b-form-group>
  <b-row style='padding-bottom:1rem'>
    <b-col lg="2" class='py-1' style="text-align:left;"><label for="youracc">Add Accounts:</label></b-col>
    <b-col lg="4"  class='py-1' ><b-form-input id='youracc' v-model="account" placeholder="Account Name"></b-form-input></b-col>
    <b-col lg="2"  class='py-1' >
      <b-form-select id='youracc' v-model="region" :options="regionOptions">
        <template v-slot:first>
          <option disabled :value="null">Region</option>
        </template>
        </b-form-select>
        </b-col>
    <b-col lg="4"><b-button variant="success" block v-on:click='updateAccounts'>Add</b-button></b-col>
  </b-row>
  <b-row style='padding-bottom:1rem'>
    <b-col lg="2" style="text-align:left;"><label for="youracc">Add Socials<i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="Click one to add!"></i></label></b-col>
    <b-col style='text-align:left;'><i v-on:click='socialsAdd(social)' v-for="social in socialsOptions" :class="'fab fa-' + social" :id='social'></i></b-col>
      </b-row>
  </b-form-group>
  
  <div style="display:flex;">
  <b-container style='width:50%;'>
  <b-row style='align-items: center;'><b-col lg='12' class='border border-dark rounded'><h5>Your Accounts<i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="Click an account to assign a main"></i></h5></b-col></b-row>
  <b-row style='align-items: center;height:54.5px;' class='py-1 accounts border border-dark rounded' v-on:click='setMainAccount(a.id)' :key='a.id' v-for='a in accountList'>
         <b-col lg='12' style="text-align:left;">{{a.name}} <b-badge class='mx-1' variant='info'>{{a.region.toUpperCase()}}</b-badge><b-badge class='mx-1' v-if='a.id == mainAccount' variant='success'>Main</b-badge><i style="font-size:20px;" :value='a.id' class="fas fa-trash-alt red delete px-1" :v-model='a.id' v-on:click="deleteRow(a, 'account')"></i></b-col>
         </b-row>
  </b-container>
  <b-container style='width:50%;'>
  <b-row style='align-items: center;'><b-col lg='12' class='border border-dark rounded'>
      <h5>Your Socials</h5>
    </b-col></b-row>
    <b-row style='align-items: center;' class="py-1 accounts border border-dark rounded" :key='socials' v-for="socials in socialsList">
    <b-col lg="1"><i style='padding-left:0;' :class="'fab fa-' + socials + ' no-hover py-1'"></i></b-col>
    <b-col lg="10" style='align-items: center;'>
      <!--Not ideal, not sure a way around it though zzz-->
      <b-form-input class='mx-2 my-1' v-if="socials == 'twitch'" v-model='twitch' :placeholder="'Your ' + socials.replace(/^\w/, c => c.toUpperCase())"></b-form-input>
      <b-form-input class='mx-2' v-if="socials == 'youtube'" v-model='youtube' :placeholder="'Your ' + socials.replace(/^\w/, c => c.toUpperCase())"></b-form-input>
      <b-form-input class='mx-2' v-if="socials == 'discord'" v-model='discord' :placeholder="'Your ' + socials.replace(/^\w/, c => c.toUpperCase())"></b-form-input>
      <b-form-input class='mx-2' v-if="socials == 'patreon'" v-model='patreon' :placeholder="'Your ' + socials.replace(/^\w/, c => c.toUpperCase())"></b-form-input>
      <b-form-input class='mx-2' v-if="socials == 'twitter'" v-model='twitter' :placeholder="'Your ' + socials.replace(/^\w/, c => c.toUpperCase())"></b-form-input>
      </b-col>
      <b-col style='text-align:left;padding:.4rem;' lg="1">
         <i style="font-size:24px;" :value='socials' class="fas fa-trash-alt red delete" v-on:click="deleteRow(socials, 'social')"></i>
      </b-col>
         </b-row>
  </b-container>
  </div>
            

    <b-row class='py-2'>
  
    <b-col lg="2"  style="text-align:left;"><label for="yourroles">Your Roles:</label></b-col>
    <b-col style="text-align:left;">
      <b-form-checkbox-group
        id="yourroles"
        v-model="selectedRoles"
        :options="roleOptions"
        name="yourroles"
      ></b-form-checkbox-group>
    </b-col>
  </b-row>
<b-row style='align-items: center;'>
    <b-col lg="2" style="text-align:left;"><label for="yourlang">Language(s):</label></b-col>
    <b-col lg="2" style="text-align:left;">
       <b-form-select id='yourlang' v-on:change='addLang(selectedLang)' v-model="selectedLang" :options="languageOptions">
        <template v-slot:first>
          <option disabled :value="null">Language</option>
        </template>
        </b-form-select>
    </b-col>
    <b-col lg="8" style='text-align:left;'><b-badge v-on:click='removeLang(l)' class='mx-1 lang' :key='l' v-for='l in languages' variant='primary'>{{l.toUpperCase()}}</b-badge></b-col>
  </b-row>

  <!--Mentor-->
  <span v-if="mentor=='mentor'">
  <b-row>
    <b-col lg="12" style="text-align:left;"><h2>Mentor Stuff</h2></b-col>
    </b-row>
  <b-row>
    <b-col lg="2" style="text-align:left;"><label for="aboutme">Your Bio:</label></b-col>
    <b-col><b-form-textarea
        id="aboutme"
        rows="5"
        v-model='aboutMe'
        placeholder="Hello I'm K3Vx and I once solo killed Faker..."
      ></b-form-textarea>
      </b-col>
  </b-row>
  <b-row class="py-2">
    <b-col lg="2" style="text-align:left;"><label for="aboutme">Your Achievements <i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="Seperate achievements by comma"></i></label></b-col>
    <b-col><b-form-textarea
        id="aboutme"
        v-model='achievements'
        rows="5"
        placeholder="Dabbed on Uzi(please seperate by comma),
Beat Doublelift in arm wrestling"
      ></b-form-textarea>
      </b-col>
  </b-row>
  <b-row>
  <b-col lg="2" style="text-align:left;"><label for="yourreview">Review Types:</label></b-col>
    <b-col style="text-align:left;">
      <b-form-checkbox-group
        id="yourreview"
        v-model="selectedReview"
        :options="reviewOptions"
        name="yourreview"
      ></b-form-checkbox-group>
    </b-col>
  </b-row>

  <b-row>
  <b-col lg="2" style="text-align:left;"><label for="yourmoney">Free/Paid:</label></b-col>
    <b-col style="text-align:left;">
      <b-form-checkbox-group
        id="yourmoney"
        v-model="selectedMoney"
        :options="moneyOptions"
        name="yourmoney"
      ></b-form-checkbox-group>
    </b-col>
  </b-row>

  <b-row>
  <b-col lg="2" style="text-align:left;"><label for="yourreq">Add Requirement:</label></b-col>
    <b-col lg="3" style="text-align:left;">
      <b-form-select id='yourreq' v-model="selectedReq" v-on:change='addReq' :options="reqOptions">
        <template v-slot:first>
          <option disabled :value="null">Requirement</option>
        </template>
        </b-form-select>
    </b-col>
  </b-row>
  <b-row style='width:55%;align-items: center;' class='py-1'><b-col lg='12' class='border border-dark rounded'>
      <h5>Your Requirements</h5>
    </b-col></b-row>
  <span :key='key' v-for='(value, key) in requirements'>
  <b-row v-if="value != null && (value == true || value.enabled == true)" style="width:55%;text-align:left;"  class="py-1 accounts border border-dark rounded">
    <b-col v-if="key=='roleMatch' && value==true">Role Match<i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="If any roles match - pass."></i> <i style="font-size:24px;" :value='key' class="fas fa-trash-alt red delete" v-on:click="deleteReq(key)"></i></b-col>
    <b-col v-if="key=='serverMatch' && value==true">Server Match<i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="If any servers match - pass."></i><i style="font-size:24px;" :value='key' class="fas fa-trash-alt red delete" v-on:click="deleteReq(key)"></i></b-col>
    <b-col v-if="key=='champMatch' && value==true">Champ Match<i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="If any champs match - pass."></i><i style="font-size:24px;" :value='key' class="fas fa-trash-alt red delete" v-on:click="deleteReq(key)"></i></b-col>
    <b-col v-if="key=='langMatch' && value==true">Language Match<i class="fas fa-question-circle textIcon" v-b-tooltip.hover title="If any languages match - pass."></i><i style="font-size:24px;" :value='key' class="fas fa-trash-alt red delete" v-on:click="deleteReq(key)"></i></b-col>
    <b-col v-if="key=='gamesPlayed' && value != null && value.enabled==true" lg="12">
      <b-form inline>
      <label for='totalGames'>Student has played</label>
      <b-form-input class='mx-2' style='width:12.5%;' v-model='totalGames' placeholder='10'></b-form-input>
       <label for='days'>+ games in the last</label>
      <b-form-select class='mx-2' id='days' v-model="days"  :options="daysOptions"></b-form-select>
      <i style="font-size:24px;" :value='key' class="fas fa-trash-alt red delete" v-on:click="deleteReq(key)"></i>
        </b-form>
        </b-col>
    <b-col lg="12" v-if="key=='rank' && value != null && value.enabled==true">
      <b-form inline>
        <label for='minmax'>Student is</label>
      <b-form-select class='mx-2' id='minmax' v-model="minmax"  :options="minmaxOptions"></b-form-select>
        <b-form-select class='mx-2' id='rank' v-model="rank" :options="rankOptions"></b-form-select>
        <i style="font-size:24px;" :value='key' class="fas fa-trash-alt red delete" v-on:click="deleteReq(key)"></i>
    </b-form>
    </b-col>
    </b-row>
    </span>
  </span>

  <b-row v-if="mentor=='student'">
    <b-col lg="2" style="text-align:left;"><label for="yourgoals">Your Goals:</label></b-col>
    <b-col style='text-align:left'>[placeholder]</b-col>
  </b-row>
  <b-row class="py-2"><b-col>
    <b-button v-if="this.$route.query.new == '1'" v-on:click='setData' variant="info" block>Create your Profile</b-button>
    <b-button v-if="this.$route.query.new != '1'" v-on:click='setData' variant="info" block>Update Information</b-button>
    </b-col></b-row>
  </b-container>
</div>
</template>
<script>
import axios from 'axios'
import router from '../router'
export default {
  name: 'EditPage',
  props: ['p'],
  data() {
      return {
         reviewOptions: [
		  { value: 'live', text: 'Live' },
          { value: 'private', text: 'Private' },
          { value: 'written', text: 'Written' },
	      ],
      	moneyOptions: [
		 { value: 'free', text: 'Free' },
          { value: 'paid', text: 'Paid' },
          ],
          regionOptions: [
		  { value: 'na', text: 'NA' },
          { value: 'euw', text: 'EUW' },
          { value: 'eune', text: 'EUNE' },
          { value: 'br', text: 'BR' },
          { value: 'kr', text: 'KR' },
          { value: 'lan', text: 'LAN'},
          { value: 'las', text: 'LAS'},
          { value: 'oce', text: 'OCE'},
          { value: 'ru', text: 'RU'},
          { value: 'tr', text: 'TR'},
          { value: 'jp', text: 'JP'},
          { value: 'cn', text: 'CN'},
		      { value: 'garena', text: 'Garena'}
      ],
      reqOptions: [,
          { value: 'gamesPlayed', text: 'Games Played' },
          { value: 'rank', text: 'Rank' },
          { value: 'roleMatch', text: 'Role Match' },
          { value: 'serverMatch', text: 'Server Match' },
          { value: 'champMatch', text: 'Champ Match'},
          { value: 'langMatch', text: 'Language Match'}
      ],
	       languageOptions: [
		  { value: 'english', text: 'English' },
          { value: 'korean', text: 'Korean' },
          { value: 'spanish', text: 'Spanish' },
          { value: 'mandarin', text: 'Chinese (Mandarin)'},
          { value: 'cantonese', text: 'Chinese (Cantonese)'},
          { value: 'danish', text: 'Danish'},
          { value: 'russian', text: 'Russian'},
          { value: 'portuguese', text: 'Portuguese'},
          { value: 'french', text: 'French'},
          { value: 'japanese', text: 'Japanese'},
          { value: 'german', text: 'German'},
          { value: 'italian', text: 'Italian'},
      ],
       roleOptions: [
          { value: 'top', text: 'Top' },
          { value: 'jungle', text: 'Jungle' },
          { value: 'middle', text: 'Middle' },
          { value: 'adc', text: 'ADC'},
          { value: 'support', text: 'Support'},
          { value: 'teams', text: 'Teams/Competitive'}
        ],
        minmaxOptions: [
          { value: 'min', text: 'at least' },
          { value: 'max', text: 'at most' }
        ],
        daysOptions: [
          { value: 31, text: 'Month' },
          { value: 7, text: 'Week' },
          { value: 0, text: 'Season' }
        ],
        	rankOptions: [
          { value: 'iron', text: 'Iron' },
          { value: 'bronze', text: 'Bronze' },
		      { value: 'silver', text: 'Silver'},
          { value: 'gold', text: 'Gold' },
          { value: 'platinum', text: 'Platinum' },
          { value: 'diamond', text: 'Diamond' },
		      { value: 'master', text: 'Master'},
          { value: 'grandmaster', text: 'Grandmaster' },
          { value: 'challenger', text: 'Challenger'},
		      { value: 'professional', text: 'Professional', disabled: true }
        ],
        selectedMoney: [],
        selectedReview: [],
        selectedLang: null,
        selectedReq: null,
        minmax: 'min',
        days: 7,
        rank: 'gold',
        totalGames: 10,
        aboutMe: '',
        achievements:'',
        socialsOptions: ['twitch', 'youtube', 'discord', 'twitter', 'patreon'],
        twitch:'',
        youtube:'',
        discord:'',
        twitter:'',
        patreon:'',
        goals: '',
        languages: [],
          requirements: {
            "serverMatch":  false,
            "roleMatch":  false,
            "langMatch":  false,
            "champMatch": false,
            "gamesPlayed": null,
            "rank": null
          },
          champions: this.championsList(),
          removedChamps: [],
          main: null,
          champs: null,
          region: null,
          account: null,
          accountList: [],
          mainAccount: {},
          socials: '',
          socialName: '',
          socialsList: [],
          socialMedia: '',
          finalSocial: {},
          selectedRoles: [],
          regionList: [],
          userData: {},
          skinList: null,
      }
    },
  components: {
    
  },
  methods: {
  redirect: function(p1) {
    console.log(p1);
    if(p1.loggedIn == false) {
      router.push({ name: "Login"})
    }
  },
	championsList: function() {	
	var vm = this;
  var championList = [];
  console.log(this.$parent);
	for (const [key, value] of Object.entries(this.$parent.$parent.champions)) {
		championList.push(value.name);
	}
	  return championList;
  },
    updateList: function() {
        if(this.removedChamps.length == 0){
          this.main = this.champs
        }
        var perfectName = this.champs.toLowerCase().split(' ').map((s) => s.charAt(0).toUpperCase() + s.substring(1)).join(' ');
        if(this.removedChamps.length <= 5 && this.champions.includes(perfectName) && !this.removedChamps.includes(this.champs)) {
          this.removedChamps.push(perfectName);
        }
        else if(this.removedChamps.length == 6) {
          this.makeToast('Warning', 'You may only add up to six champions.', "warning")
        } else if(this.removedChamps.includes(this.champs)) {
          this.makeToast('Error', 'You cannot add the same champion twice.', "danger")
        }
        this.champs = null;
    },
    deleteRow: function(c, type) {
        if(type =='champ') {
          var index = this.removedChamps.indexOf(c);
          this.removedChamps.splice(index, 1);
        } else if(type == 'account') {
          var index = this.accountList.indexOf(c);
          this.accountList.splice(index, 1);
        } else if(type == 'social') {
          console.log(c);
          var index = this.socialsList.indexOf(c);
          this.socialsList.splice(index, 1);
        }
    },
    deleteReq: function(r) {
      if(r == 'roleMatch' || r == 'champMatch' || r == 'serverMatch' || r == 'langMatch') {
        this.requirements[r] = false;
      }  else if(r == 'gamesPlayed' || r == 'rank') {
        this.requirements[r].enabled = false;
      } 
    },
    makeToast(title, content, variant = null) {
        this.$bvToast.toast(content, {
          title: `${title}`,
          variant: variant,
          solid: true,
          toaster: 'b-toaster-top-center'
        })
      },
    updateAccounts: function() {
      var vm = this;
      var dupe = false;
      var l = vm.accountList.length;
      if(this.accountList.length <= 1){
          this.mainAccount = 0;
        }
      if(this.account && this.region) {
        for(let x of this.accountList){
          console.log(x);
          console.log(this.account);
          console.log(this.region);
          if(x.region == this.region && x.name.toLowerCase() == this.account.toLowerCase()) {
               this.makeToast('Error', 'You cannot add the same account twice.', "danger")
               dupe = true;
               break;
          }
        }
          if(!dupe) {
            this.accountList.push({'id': l, 'name': this.account, 'region': this.region});
          }
        this.account = null;
        this.region = null;
      }
      console.log(this.accountList);
    },
    socialsAdd: function(sm){
        if(this.socialsList.includes(sm)) {
          this.makeToast('Error', 'You can only have one of each social media.', 'danger');
        } else {
        this.socialsList.push(sm);
        }
        console.log(this.socialsList);
  },
  setMain: function(newMain){
    this.main = newMain;
  },
  setMainAccount: function(newMain){
    this.mainAccount = newMain;
  },
  addLang: function(lang) {
    if(!this.languages.includes(lang)){
      this.languages.push(lang);
    } else {
      this.makeToast('Error', 'You cannot add the same language twice.', 'danger')
    }
    this.selectedLang = null;
  },
  removeLang: function(lang){
    var index = this.languages.indexOf(lang);
    this.languages.splice(index, 1);
  },
  addReq: function() {
    if(this.requirements[this.selectedReq] == true || this.requirements[this.selectedReq].enabled == true) {
      this.makeToast('Warning', 'You already added this requirement.', 'warning')
    } else {
    if(this.selectedReq == 'roleMatch' || this.selectedReq == 'champMatch' || this.selectedReq == 'serverMatch' || this.selectedReq == 'langMatch') {
      this.requirements[this.selectedReq] = true;
    } else if(this.selectedReq == 'gamesPlayed') {
      this.requirements[this.selectedReq] = {'enabled': true, 'games': this.totalGames, 'days': this.days}
    } else if(this.selectedReq == 'rank') {
      this.requirements[this.selectedReq] = {'enabled': true, 'minmax': this.minmax, 'rank': this.rank}
    }
    }
  },
   setData: function() {
    var vm = this;
    this.accountList.forEach(function(x) {
      vm.regionList.push(x.region);
    })
    this.socialsList.forEach(function(x){
      vm.finalSocial[x] = vm[x];
    })
    //const path = 'http://localhost:5000/api/profileInfo/' + this.$parent.$parent.profileData.did;
    const path = '/api/profileInfo/' + this.$parent.$parent.profileData.did;
    const data = {
      'did': this.$parent.$parent.profileData.did, //should be cookie
      'champs': this.removedChamps,
      'socials': this.finalSocial,
      'roles': this.selectedRoles,
      'region': [...new Set(this.regionList)],
      'accounts': this.accountList,
      'main': this.main,
      'mainAccount': this.mainAccount,
      'languages': this.language,
    };
    let data2 = {};
    //mentor student
    if(this.$parent.$parent.profileData.type == "mentor") {
      if(this.requirements.gamesPlayed && this.requirements.gamesPlayed.enabled == true) {
        this.requirements.gamesPlayed = {'enabled': true, 'games': this.totalGames, 'days': this.days}
      } else {
        this.requirements.gamesPlayed = {'enabled': false, 'games': this.totalGames, 'days': this.days}
      }
      if(this.requirements.rank && this.requirements.rank.enabled == true) {
        this.requirements.rank = {'enabled': true, 'minmax': this.minmax, 'rank': this.rank}
      } else {
        this.requirements.rank = {'enabled': false, 'minmax': this.minmax, 'rank': this.rank}
      }
      data2 = {
        'bio': this.aboutMe,
        'achievements': (this.achievements).split(","),
        'reviewType': this.selectedReview,
        'moneyType': this.selectedMoney,
        'requirements': this.requirements
      }
    } else {
      data2 = {
        'goals': ''
      }
    }
    axios.post(path, Object.assign({}, data, data2))
    .then(response => {
      console.log(response);
      window.scrollTo(0, 0);
      this.makeToast('Updated', 'You have saved your profile.', 'success')
    })
    .catch(error => {
      this.makeToast('Error', "Err - there's been an error in the back. Try again or report it - thank you!", 'danger');
      console.log(error)
    })
  },
  getData:function() {
    //const path = 'http://localhost:5000/api/profileInfo/' + this.$parent.$parent.profileData.did;
    const path = '/api/profileInfo/' + this.$parent.$parent.profileData.did;
    axios.get(path)
    .then(response => {
      this.removedChamps = response.data.champs;
      this.main = response.data.main;
      this.accountList = response.data.accounts;
      this.selectedRoles = response.data.roles;
      this.mainAccount = response.data.mainAccount;
      this.languages = response.data.languages;
      this.socialsList = Object.keys(response.data.socials)
      this.mentor = response.data.type;
      for(const[k,v] of Object.entries(response.data.socials)) {
        this[k]=v; 
      }
      this.aboutMe = response.data.bio;
      this.selectedMoney = response.data.moneyType;
      this.selectedReview = response.data.reviewType;
      this.achievements = response.data.achievements.join(',');
      this.requirements = response.data.requirements;
      this.totalGames = response.data.requirements.gamesPlayed.games;
      this.rank = response.data.requirements.rank.rank;
      this.minmax = response.data.requirements.rank.minmax;
      this.days = response.data.requirements.gamesPlayed.days;
      console.log(response);
    })
    .catch(error => {
      this.makeToast('Error', "Err - there's been an error in the back. Try again or report it - thank you!", 'danger');
      console.log(error)
    })
  }
  },
  mounted: async function(){
    this.p = await this.$parent;
    await this.$parent;
    this.redirect(this.$parent.$parent);
    if(this.$route.query.new != '1') {
      this.getData();
    }
  }
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

.deleteChamp {
position:absolute;
top:.2rem;
right:.2rem;
opacity:.75;
}

.badgeChamp {
position:absolute;
bottom:.2rem;
left:.2rem;
opacity:1;
}

.delete:hover, .deleteChamp:hover{
color:red;
}
h5 {
  font-size:18px;
}
.fab {
  font-size: 24px;
}
.no-hover{
  cursor:default;
  font-size:36px;
}

label {
  font-size:17px!important;
}

.accounts {
  background-color:#636d7b;
  cursor:pointer;
}
.accounts:hover{
    background-color:#3f464e;
}
.img-holder {position: relative; display: inline-block;cursor:pointer;}
.img-holder img {display: block;}
.lang {
  cursor: pointer;
}
.lang:hover {
background-color:#dc3545;
}
</style>