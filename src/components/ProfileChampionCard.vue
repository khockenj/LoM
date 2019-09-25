<template>
  <b-card
  text-variant="white"
  bg-variant="dark"
    no-body
    style="max-width: 20rem;border:1px solid white;"
	:img-src="'/static/squareicons/' + champ.toLowerCase() + '_square.png'"
    img-alt="Image"
    img-top
  >
    <template v-slot:header>
      <h4 class="mb-0">{{champ}}</h4>
    </template>
  </b-card>
</template>
<script>
export default {
  name: 'ProfileChampionCard',
  props: ['champ']
}
</script>