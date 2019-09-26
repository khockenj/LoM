<template>
  <b-card
  text-variant="white"
  bg-variant="dark"
    no-body
    style="max-width:15rem;min-width:15rem;border:1px solid white;"
	:img-src="'/static/squareicons/' + main + '_square.png'"
    img-alt="Image"
    img-top
  >
    <template v-slot:header>
      <h4 class="mb-0">{{name}} <img class="rankIcon" :src="'/static/ranks/' + rank + '.png'" /></h4>
    </template>

    <b-list-group flush>
      <b-list-group-item style="background-color:inherit;" >Main Champs</b-list-group-item>
	  <b-list-group-item style="background-color:inherit;">Rank</b-list-group-item>
    </b-list-group>

    <b-card-body class="mx-auto">
		<router-link class="card-link" :to="'/profile/' + name">View Mentor</router-link>
		<a href="#" class="card-link">Check Availability</a>
    </b-card-body>


  </b-card>
</template>
<style scoped>
.rankIcon {
	max-width:48px;
	max-height:48px;
	vertical-align: middle;
}
</style>

<script>
export default {
  name: 'SearchCard',
  props: ['id', 'name', 'main', 'rank']
}
</script>