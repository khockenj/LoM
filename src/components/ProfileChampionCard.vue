<template>
  <b-card
  text-variant="white"
  bg-variant="dark"
    no-body
    style="max-width:10rem;min-width:10rem;border:1px solid white;"
	:img-src="'/static/squareicons/' + champ.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
    img-alt="Image"
    img-top
  >
    <template v-slot:header>
      <h5 class="mb-0">{{champ}}</h5>
    </template>
  </b-card>
</template>
<script>
export default {
  name: 'ProfileChampionCard',
  props: ['champ']
}
</script>