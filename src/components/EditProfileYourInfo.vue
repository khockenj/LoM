<template>
<span>
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
    <b-form-input id='yourchamps' v-on:change='updateList' list="champions" v-model="champs"></b-form-input>
    <datalist autocomplete='off' id="champions">
    <option :key='c' v-for="c in champions" :value='c'>{{c}}</option>
  </datalist>
        </b-col>
     </b-row>
     <b-form-group>

       <b-row v-if="removedChamps.length > 0">
         <b-col lg="3" style='padding:12px;'>Champion</b-col>
         <b-col style='padding:12px;'>Main</b-col>
         <b-col style='padding:12px;'>Remove</i></b-col>
         </b-row>

     <b-row v-for="x in removedChamps" :key=x>
         <b-col lg="1"><img style="max-width:48px":src="'/static/squareicons/' + x.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'" /></b-col>
         <b-col lg="2">{{x}}</b-col>
         <b-col style='padding:12px;'><b-form-radio v-model="main" :value='x'></b-form-radio></b-col>
         <b-col style='padding:12px;'><i style="font-size:24px;" :value='x' class="fas fa-trash-alt red delete" :v-model='x' v-on:click="deleteRow(x, 'champ')"></i></b-col>
         </b-row>
            </b-form-group>
<b-form-group>
  <b-row>
    <b-col lg="2" style="text-align:left;"><label for="youracc">Your Accounts:</label></b-col>
    <b-col lg="4"><b-form-input id='youracc' v-model="account" placeholder="Account Name"></b-form-input></b-col>
    <b-col lg="2">
      <b-form-select id='youracc' v-model="region" :options="regionOptions">
        <template v-slot:first>
          <option disabled :value="null">Region</option>
        </template>
        </b-form-select>
        </b-col>
    <b-col lg="4"><b-button variant="success" block v-on:click='updateAccounts'>Add</b-button></b-col>
  </b-row>
  <b-row v-if="accountList.length > 0">
         <b-col lg="3" style='padding:12px;'>Account</b-col>
         <b-col style='padding:12px;'>Region</b-col>
         <b-col style='padding:12px;'>Main?</b-col>
         <b-col style='padding:12px;'>Remove</i></b-col>
         </b-row>
  
  <b-row :key='a.id' v-for='a in accountList'>
         <b-col>{{a.name}}</b-col>
         <b-col>{{a.region.toUpperCase()}}</b-col>
         <b-col style='padding:12px;'><b-form-radio v-model="mainAccount" :value='a.id'></b-form-radio></b-col>
         <b-col style='padding:12px;'><i style="font-size:24px;" :value='a.id' class="fas fa-trash-alt red delete" :v-model='a.id' v-on:click="deleteRow(a, 'account')"></i></b-col>
         </b-row>
            </b-form-group>

    <b-row>
  
    <b-col lg="2" style="text-align:left;"><label for="yourroles">Your Roles:</label></b-col>
    <b-col style="text-align:left;">
      <b-form-checkbox-group
        id="yourroles"
        v-model="selectedRoles"
        :options="roleOptions"
        name="yourroles"
      ></b-form-checkbox-group>
    </b-col>
  </b-row>
<b-row>
    <b-col lg="2" style="text-align:left;"><label for="yourlang">Language(s):</label></b-col>
    <b-col style="text-align:left;">
      [placeholder]
    </b-col>
  </b-row>
  <b-row>
    <b-col lg="2" style="text-align:left;"><label for="yoursocials">Your Socials:</label></b-col>
    <b-col>
      <i v-on:click='socialsAdd(social)' v-for="social in socialsOptions" :class="'fab fa-' + social" :id='social'></i>
    </b-col>
  </b-row>
  <b-row class="p-1" :key='socials' v-for="socials in socialsList">
    <b-col lg="1"><i :class="'fab fa-' + socials + ' no-hover'"></i></b-col>
    <b-col><b-form-input :placeholder="'Your ' + socials.replace(/^\w/, c => c.toUpperCase())"></b-form-input></b-col>
    <b-col lg="1"><i style="font-size:24px;" :value='socials' class="fas fa-trash-alt red delete" v-on:click="deleteRow(socials, 'social')"></i></b-col>
  </b-row>
  </span>
  </template>

<script>
export default {
  name: 'EditProfileYourInfo',
  data() {
      return {
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
	       languageOptions: [
		  { value: 'english', text: 'English' },
          { value: 'korean', text: 'Korean' },
          { value: 'spanish', text: 'Spanish' },
          { value: 'mandarin', text: 'Chinese (Mandarin)'},
          { value: 'cantonese', text: 'Chinese (Cantonese)'},
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
		      { value: 'support', text: 'Support'}	
        ],
        socialsOptions: ['twitch', 'youtube', 'discord', 'twitter', 'patreon'],
      
          champions: this.championsList(),
          removedChamps: [],
          main: null,
          champs: null,
          region: null,
          account: null,
          accountList: [],
          mainAccount: null,
          socials: '',
          socialName: '',
          socialsList: [],
          socialMedia: '',
}
  },
  methods: {
	championsList: function() {	
	var vm = this;
	var championList = [];
	for (const [key, value] of Object.entries(this.$parent.$parent.$parent.champions)) {
		championList.push(value.name);
	}
	console.log(championList);
	return championList;
  },
    updateList: function() {
        if(this.removedChamps.length == 0){
          this.main = this.champs
        }
        var perfectName = this.champs.toLowerCase().replace(/^\w/, c => c.toUpperCase());
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
      var l = vm.accountList.length-1;
      if(this.removedChamps.length <= 1){
          this.mainAccount = 0;
          l = l+1;
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
    },
    socialsAdd: function(sm){
        if(this.socialsList.includes(sm)) {
          this.makeToast('Error', 'You can only have one of each social media.', 'danger');
        } else {
        this.socialsList.push(sm);
        }
    },
  }
}
</script>

<style scoped>
.delete:hover{
color:red;
}
h5 {
  font-size:18px;
}
.fab {
  font-size: 24px;
  float:left;
}
.no-hover{
  cursor:default;
  font-size:36px;
}
.no-hover:hover{
  color:#BEBEBE;
  cursor:default;
}

label {
  font-size:17px!important;
}
</style>