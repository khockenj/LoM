<template>
  <b-card
  text-variant="white"
  bg-variant="dark"
    no-body
    style="max-width:15rem;min-width:15rem;border:1px solid white;"
	:img-src="main? '/static/squareicons/' + main.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png': 'data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII='"
    img-alt="Image"
    img-top
  >
    <template v-slot:header>
      <h4 class="mb-0" :to="'/profile/' + name">{{name}} <img class="rankIcon" :src="'/static/ranks/' + rank + '.png'" /></h4>
    </template>

    <b-list-group flush>
      <b-list-group-item style="padding:.75rem 1rem;background-color:inherit;" >
        <img class='smallChamps' :key='c' v-for='c in champs' :src="'/static/squareicons/' + c.toLowerCase() + '_square.png'" :alt='c' />
        <span v-if='champs.length == 0'>None Available</span>
        </b-list-group-item>
	  <b-list-group-item style="background-color:inherit;">
      <b-badge class='badge' v-for='r in roles' :key='r' :variant='switchVariant(r)'>{{r.toUpperCase()}}</b-badge>
      <b-badge v-if='roles.length == 0'>NONE</b-badge></b-list-group-item>
    </b-list-group>

    <b-card-body class="mx-auto">
      <b-button variant='success' :to="'/profile/' + did">View Mentor</b-button>
		<!--<router-link class="card-link" :to="'/profile/' + name">View Mentor</router-link>-->
    </b-card-body>
  </b-card>
</template>
<style scoped>
.rankIcon {
	max-width:48px;
	max-height:48px;
	vertical-align: middle;
}
.smallChamps {
  max-width:2rem;
  margin:.05rem;
}
.badge {
  margin:.1rem;
}
</style>

<script>
export default {
  name: 'SearchCard',
  props: ['id', 'name', 'main', 'rank', 'champs', 'roles', 'did'],
methods: {
  switchVariant: function(r) {
    if(r == "adc") {
      return "danger"
    } else if(r == "middle") {
      return "primary"
    } else if(r == "jungle") {
      return "success" 
    } else if(r == "support") {
      return "warning"
    } else if (r == "top") {
      return "light"
    } else if(r == "teams"){
      return "info"
    }
  }
}
}
</script>