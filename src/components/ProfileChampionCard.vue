<template>
 <div class='img-holder'>
       
  <b-badge v-if="champ == main" class='badgeChamp' variant='success'>MAIN</b-badge>
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
  </div>
</template>
<script>
export default {
  name: 'ProfileChampionCard',
  props: ['champ', 'main']
}
</script>

<style scoped>
.img-holder {position: relative; display: inline-block;}
.img-holder img {display: block;}
.lang {
  cursor: pointer;
}
.badgeChamp {
position:absolute;
top:.3rem;
right:0rem;
opacity:1;
z-index:99;
}
</style>