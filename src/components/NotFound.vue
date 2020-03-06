<template>
  <div class="not-found" style="max-width:600px;">
    <div class="overlay"></div>
        <b-card class='card-holder' header-bg-variant="danger" border-variant="danger" header-text-variant="light">
       <template v-slot:header>
    Not Found
    </template>
     <img src="/static/logo.png" style="max-width:45%;padding-bottom:5%;" />
     <p>I hate to give you the bad news but this page doesn't exist. If you think this is an error please report it!</p>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "NotFound",
};
</script>

<style scoped>
.overlay {
  /* background-color: rgba(0, 0, 0, 0.5) !important; */
  background-image: url("/static/kevin.png");
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  /* 
   background-position: center; 
   filter: blur(2px);
  -webkit-filter: blur(2px);
  */
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1000;
 
}
.card-holder {
  max-width:600px;
  margin:auto;
  background-color:rgba(255,255,255,.85);
}
.card {
  border:5px solid inherit;
}
.not-found {
  margin: auto;
  padding-top: 5%;
}
.no-hover-header, .no-hover-header:hover {
  cursor:default;
  color:inherit;
}

.card-header {
  font-size:2rem;
}
</style>