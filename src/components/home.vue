<template>
<div class="home">
<div class="overlay"></div>
</div>
</template>
<script>
export default {
  name: 'HomePage'
  }
</script>

<style scoped>
.overlay {
  background-color: rgba(238, 238, 238, 0.5) !important;
  background-image:url('/static/backgrounds/cassiopeia.jpg');
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position:fixed;
  width:100%;
  height:100%;
  top:5%;
  left:0px;
  z-index:-1000;
}
</style>

