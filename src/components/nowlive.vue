<template>
<div class="nowlive">
<div class="overlay"></div>
<div class="searchContainer">
 <b-card-group deck v-if='live'>
  <b-card :key='mentor.user_id' v-for='mentor in live'
    :img-src="mentor.thumbnail_url.replace('{width}', '300').replace('{height}', '200')"
    :img-alt="mentor.user_name"
    img-top
    style="max-width: 20rem;"
    class="mb-2"
  >
  <b-card-title>{{mentor.user_name}}</b-card-title>
    <b-card-text>
      {{mentor.title}}
    </b-card-text>

    <b-button :href="'https://www.twitch.tv/' + mentor.user_name" variant="primary">Visit Stream</b-button>
    <b-button :to="'/profile/' + mentor.did" variant='success'>View Profile</b-button>
  </b-card>
 </b-card-group>
</div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NowLive',
  components: {
   },
  data: function() {
      return {
    live: null,
      }
  },
  methods: {
      getData: function() {
    //const path = 'http://localhost:5000/api/getStreams'
    const path = '/api/getStreams'
    axios.get(path)
    .then(response => {
      this.live = response.data;
    })
    .catch(error => {
      console.log(error)
    })
  },
  },
  mounted: function() {
    this.getData();
  }
}

</script>
<style scoped>
.overlay {
  background-color: rgba(0,0,0, 0.4) !important;
  background-image:url('/static/backgrounds/zed.jpg');
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position:fixed;
  width:100%;
  height:100%;
  top:0%;
  left:0px;
  z-index:-1000;
}
</style>

