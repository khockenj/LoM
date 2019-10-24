<template>
<div class="home">
<div class="overlay"></div>
this will be your dashboard - sorry i got nothing rn.
</div>
</template>
<script>
export default {
  name: 'Dashboard'
  }
</script>

<style scoped>
.overlay {
  background-color: rgba(0,0,0, 0.4) !important;
  background-image:url('/static/backgrounds/cassiopeia.jpg');
  background-blend-mode: color;
  background-repeat: no-repeat;
   background-attachment: fixed;
  background-size: cover;
  position:fixed;
  width:100%;
  height:100%;
  top:0;
  left:0px;
  z-index:-1000;
}
</style>

