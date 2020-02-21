<template>
    <div id='footer' class='navbar'>
      <div class='text'>Website by  <a href='https://www.kevhock.com/'
       target="_blank" rel="nofollow noopener">Kevin Hockenjos</a></div>
    </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
#footer {
  flex:none;
  margin-top:1rem;
  background-color:rgba(0,0,0,0.95);
  height:7%;
  width:100%;
  color: rgba(255,255,255,0.4);
  font-size:36px;
}
.text {
  font-size:18px;
}
</style>