<template>
  <div class="nowlive">
    <div class="overlay"></div>
    <div class="searchContainer">
      <b-card-group deck v-if="live">
        <b-card
          text-variant="white"
          :key="mentor.user_id"
          v-for="mentor in live"
          :img-src="mentor.thumbnail_url.replace('{width}', '300').replace('{height}', '200')"
          :img-alt="mentor.user_name"
          img-top
          style="max-width: 20rem;min-width: 20rem;background-color:transparent;border:2px solid steelblue;"
          no-body
        >
         <template v-slot:header>
      <h4 class="mb-0">
       {{mentor.user_name}}
      </h4>
    </template>
  <b-list-group flush>
      <b-list-group-item style="padding:.75rem 1rem;background-color:#343A40;">
       {{mentor.title}}
      </b-list-group-item>
      <b-list-group-item
        style="background-color:#343A40;margin:0;"
        class='footer-button'
      >
        
          <b-button
            :href="'https://www.twitch.tv/' + mentor.user_name"
            variant="primary"
          > <i class="fas fa-video textIcon"></i>Visit Stream</b-button>
          <b-button :to="'/profile/' + mentor.did" variant="success"><i class="fas fa-user textIcon"></i>View Profile</b-button>
      </b-list-group-item>
    </b-list-group>


        </b-card>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NowLive",
  components: {},
  data: function() {
    return {
      live: null
    };
  },
  methods: {
    getData: function() {
      const path = "http://localhost:5000/api/getStreams";
      //const path = '/api/getStreams'
      axios
        .get(path)
        .then(response => {
          this.live = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted: function() {
    this.getData();
  }
};
</script>
<style scoped>
.overlay {
  background-color: rgba(0, 0, 0, 0.4) !important;
  background-image: url("/static/backgrounds/zed.jpg");
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0%;
  left: 0px;
  z-index: -1000;
}
.searchContainer {
  margin-left:1rem;
  margin-right:1rem;
  padding-top:1rem;
}
.card-header{
  background-color:rgba(0,0,0,.8);
}
h4 {
  font-size:1.75rem;
}
.list-group-item {
   /* margin-bottom:.25rem; */
   border-bottom:2px solid black;
}
.card-img-top, .card-img {
  width: 100%;
  object-fit: cover;
}
.footer-button {
  padding:1rem;
  height:100%;
  background-color:#343A40;
  border-bottom-right-radius: calc(0.25rem - 1px);
  border-bottom-left-radius: calc(0.25rem - 1px);
}
.btn {
  font-size:1rem;
}
</style>

