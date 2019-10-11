<template>
  <div id="mentorSearch">
  
  <div class="searchBarContainer">
  <b-input-group>

    <b-form-input size='lg' v-model.trim="search" v-on:input="searchFunction" placeholder="Search Mentors"></b-form-input>

    <template v-slot:append>
	<b-form-select class="btn" style="color:#6c757d!important;width:240%;" size='lg' v-model="champFilter" :options="champOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Champion</option>
      </template>
	  </b-form-select>

	  <b-form-select class="btn" style="color:#6c757d!important;width:100%;" size='lg' v-model="roleFilter" :options="roleOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Role</option>
      </template>
	  </b-form-select>

	  <b-form-select class="btn" style="color:#6c757d!important;width:200%;" size='lg' v-model="rankFilter" :options="rankOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Rank</option>
      </template>
	  </b-form-select>
	 
	 <b-form-select class="btn" style="color:#6c757d!important;width:110%;" size='lg' v-model="regionFilter" :options="regionOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Region</option>
      </template>
	  </b-form-select>
	  
	  <b-form-select class="btn" style="color:#6c757d!important;width:150%;" size='lg' v-model="languageFilter" :options="languageOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Language</option>
      </template>
	  </b-form-select>
	  
	  <b-form-select class="btn" style="color:#6c757d!important;width:110%;" size='lg' v-model="reviewFilter" :options="reviewOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Type</option>
      </template>
	  </b-form-select>
	  
	  <b-form-select class="btn" style="color:#6c757d!important;width:70%" size='lg' v-model="moneyFilter" :options="moneyOptions" v-on:input="searchFunction" variant="outline-secondary">
	  <template v-slot:first>
        <option :value="null">Cost</option>
      </template>
	  </b-form-select>
    </template>
  </b-input-group>
  </div>
  
  <div class="searchContainer">
  
   <b-card-group deck>
  <search-card v-for="m in mentors" v-bind:key="m.id" :name="m.name" :main="m.main" :rank="m.rank" :champs="m.champs"/>
  </b-card-group>

  </div>
  </div>
  </div>
</template>
<script>
import SearchCard from './SearchCard'
import axios from 'axios'
export default {
  name: 'MentorSearch',
   components: {
    SearchCard
  },
	props: ['champions'],
	data: function() {
	return {
	search: '',
	mentors: [],
	list: [],
	rankFilter: null,
	champFilter: null,
	languageFilter: null,
	reviewFilter: null,
	regionFilter: null,
	moneyFilter: null,
	roleFilter: null,
	
	rankOptions: [
          { value: 'platinum', text: 'Platinum' },
          { value: 'diamond', text: 'Diamond' },
		  { value: 'master', text: 'Master'},
          { value: 'grandmaster', text: 'Grandmaster' },
          { value: 'challenger', text: 'Challenger'},
		  { value: 'professional', text: 'Professional', disabled: true }
        ],
    champOptions: this.$parent.championsList(),
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
		            { value: 'danish', text: 'Danish'},
		  { value: 'russian', text: 'Russian'},
		  { value: 'portuguese', text: 'Portuguese'},
		  { value: 'french', text: 'French'},
		  { value: 'japanese', text: 'Japanese'},
		  { value: 'german', text: 'German'},
		  { value: 'italian', text: 'Italian'},
	],
	reviewOptions: [
		  { value: 'live', text: 'Live' },
          { value: 'private', text: 'Private' },
          { value: 'written', text: 'Written' },
	],
	moneyOptions: [
		  { value: 'free', text: 'Free' },
          { value: 'paid', text: 'Paid' },
	],
	roleOptions: [
		  { value: 'top', text: 'Top' },
          { value: 'jungle', text: 'Jungle' },
          { value: 'middle', text: 'Middle' },
          { value: 'adc', text: 'ADC'},
		  { value: 'support', text: 'Support'},
		  { value: 'teams', text: 'Teams'}	
	]
  }
  },
  methods: {
  convertRank: function(r) {
	var rf = 0;
	if(r != null) {
	r = r.toLowerCase();

	
  	if(r.search("platinum") >= 0){
		rf = 1;
	} else if(r.search("diamond") >= 0) {
		rf = 2;
	} else if(r.search("master") >= 0) {
		rf = 3;
	} else if(r.search("grandmaster") > 0) {
		rf = 4;
	} else if(r.search("challenger") >= 0) {
		rf = 5;
	} else if(r.search("professional") >= 0) {
		rf = 6;
	}
	}
	return rf;
  },
  searchFunction: function() {
    var vm = this;

	var ret = [];
	vm.list.forEach(function(x) {
		if(
		(x.name.toLowerCase().search(vm.search.toLowerCase()) >= 0)
		&& (vm.convertRank(x.rank) >= vm.convertRank(vm.rankFilter))
		&& ((vm.regionFilter == null) || (x.region.includes(vm.regionFilter)))
		&& ((vm.languageFilter == null) || (x.languages.includes(vm.languageFilter)))
		&& ((vm.moneyFilter == null) || (x.moneyType.includes(vm.moneyFilter)))
		&& ((vm.reviewFilter == null) || (x.reviewType.includes(vm.reviewFilter)))
		&& ((vm.champFilter == null) || (x.champs.includes(vm.champFilter)))
		&& ((vm.roleFilter == null) || (x.roles.includes(vm.roleFilter)))
		) {
			ret.push(x);
		}
	})
	this.mentors = ret;
  },
    getData: function() {
	//const path = 'http://localhost:5000/api/profileInfo/' + "MENTORS"
    const path = '/api/profileInfo/' + "MENTORS"
    axios.get(path)
    .then(response => {
	  this.list = response.data;
	  this.mentors = response.data;
    })
    .catch(error => {
      console.log(error)
    })
  }
  },
  computed: {
  
  },
  ready: function(){
  }, 
  watch: {},
  mounted: function() {
	  this.getData();
  }
}

</script>

