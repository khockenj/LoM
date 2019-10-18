<template>
  <div id="app">
    <router-view v-if='this.$parent.complete' />
  </div>
</template>

<script>
export default {
  name: 'App',
  props: ['loggedIn', 'profileData'],
  mounted: function() {
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
