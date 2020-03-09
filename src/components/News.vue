<template>
  <div class="news">
    <div class="overlay"></div>
<b-container style="max-width:1200px">
      <b-row>
        <b-col lg="12">
          <b-container>
            <b-row>
              <b-col lg="12">
                <b-card
                  no-body
                  border-variant="info"
                  header-bg-variant="info"
                  header-text-variant="white"
                  align="center"
                  header="Recent News"
                ></b-card>
              </b-col>
            </b-row>
            <b-row>
              <b-col lg="12">
                <b-card
                  v-for="p in newsData"
                  :key="p._id.$oid"
                  border-variant="dark"
                  :header="p.title"
                  header-bg-variant="dark"
                  header-text-variant="white"
                  align="center"
                >
                  <b-card-text>{{p.post}}</b-card-text>
                </b-card>
              </b-col>
            </b-row>
          </b-container>
        </b-col>
        
      </b-row>
    </b-container>
    </div>
</template>
<script>
import axios from "axios";

export default {
  name: "News",
  data() {
    return {
      newsData: null
    };
  },
  methods: {
    getNewsData: function() {
      const path = "http://localhost:5000/api/getNews";
      //const path = '/api/getNews'
      axios
        .get(path)
        .then(response => {
          this.newsData = response.data;
          console.log(this.newsData);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  mounted: async function() {
    await this.$parent;
    this.getNewsData();
  }
};
</script>

<style scoped>

.overlay {
/* background-color: rgba(0, 0, 0, 0.4) !important; */
  background-image: url("/static/kevin.png");
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0px;
  z-index: -1000;
}

</style>