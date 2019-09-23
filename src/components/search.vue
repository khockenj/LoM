<template>
<div class="search">
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

