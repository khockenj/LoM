<template>
  <b-card
    no-body
    style="max-width: 20rem;"
	:img-src="'/static/squareicons/' + main + '_square.png'"
    img-alt="Image"
    img-top
  >
    <template v-slot:header>
      <h4 class="mb-0">{{name}} <img class="rankIcon" :src="'/static/ranks/' + rank + '.png'" /></h4>
    </template>

    <b-list-group flush>
      <b-list-group-item>Main Champs</b-list-group-item>
	  <b-list-group-item>Rank</b-list-group-item>
    </b-list-group>

    <b-card-body class="mx-auto">
		<a href="#" class="card-link">View Mentor</a>
		<a href="#" class="card-link">Check Availability</a>
    </b-card-body>


  </b-card>
</template>

<script>
export default {
  name: 'SearchCard',
  props: ['id', 'name', 'main', 'rank']
}
</script>
