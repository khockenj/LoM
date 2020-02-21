<template>
<div style='min-height:100%;'>
  <div id="app">
    <router-view v-if="this.$parent.complete" />
  </div>
 <Footer />
      </div>
</template>

<script>
import Footer from "./Footer";
export default {
  name: "App",
  components: {Footer},
  props: ["loggedIn", "profileData"],
  mounted: function() {}
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height:100%;
}
</style>
