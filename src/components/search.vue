<template>
<div class="search">
<div class="overlay"></div>
	<mentor-search/>
</div>
</template>
<script>
import MentorSearch from './MentorSearch'
import SearchCard from './SearchCard'
export default {
  name: 'SearchPage',
  components: {
   'mentor-search': MentorSearch,
   'search-card': SearchCard,
   },
  methods: {
	championsList: function() {	
	var vm = this;
	console.log(this);
	var championList = [];
	for (const [key, value] of Object.entries(this.$parent.$parent.champions)) {
		championList.push({"text": value.name, "value": value.name.toLowerCase()});
	}
	console.log(championList);
	return championList;
	}
  }
  }
</script>
<style scoped>
.overlay {
  background-color: rgba(238, 238, 238, 0.5) !important;
  background-image:url('/static/backgrounds/zed.jpg');
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
</style>

