<template>
<div class="nowlive">
<div class="overlay"></div>
<div class="searchContainer">
 <b-card-group deck>
  <b-card :key='mentor.user_id' v-for='mentor in live'
    :title="mentor.user_name"
    :img-src="mentor.thumbnail_url.replace('{width}', '300').replace('{height}', '200')"
    :img-alt="mentor.user_name"
    img-top
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      {{mentor.title}}
    </b-card-text>

    <b-button :href="'https://www.twitch.tv/' + mentor.user_name" variant="primary">Visit Stream</b-button>
  </b-card>
 </b-card-group>
</div>
</div>
</template>

<script>
export default {
  name: 'NowLive',
  components: {
   },
  methods: {
  },
  data: function() {
      return {
    live: [{'id': '36042780080', 'user_id': '51496027', 'user_name': 'loltyler1', 'game_id': '21779', 'type': 'live', 'title': 'me freak . BIG MAN . also haved swag ! LET GO !!!', 'viewer_count': 15996, 'started_at': '2019-10-22T21:50:58Z', 'language': 'en', 'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_loltyler1-{width}x{height}.jpg', 'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']}, {'id': '36043641600', 'user_id': '21673391', 'user_name': 'Aphromoo', 'game_id': '21779', 'type': 'live', 'title': 'SOLO DOLO', 'viewer_count': 1591, 'started_at': '2019-10-22T23:44:54Z', 'language': 'en', 'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_aphromoo-{width}x{height}.jpg', 'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']}]
      }
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

