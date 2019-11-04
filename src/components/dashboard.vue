<template>
<div class="home">
<div class="overlay"></div>
<b-container style="max-width:1200px">
  <b-row> 
    <b-col lg="9">
      <b-container>
        <b-row>
          <b-col lg="12">
      <b-card
        border-variant="dark"
        header="Sofia perma-banned from server!"
        header-bg-variant="dark"
        header-text-variant="white"
        align="center"
      >
        <b-card-text>k3vx will reign as new supreme king now. read more.</b-card-text>
      </b-card>
      </b-col>
        </b-row>
        <b-row>
          <b-col lg="12">
      <b-card
        border-variant="dark"
        header="Faker joins the mentoring team"
        header-bg-variant="dark"
        header-text-variant="white"
        align="center"
      >
        <b-card-text>SKT T1 player Faker will be joining our mentoring staff as of his latest defeat at Worlds 2019. He is taking some time off from professional League to coach prime NA talent.</b-card-text>
      </b-card>
      </b-col>
        </b-row>
         <b-row>
          <b-col lg="12">
      <b-card
        border-variant="dark"
        header="LoM tournament for $100k"
        header-bg-variant="dark"
        header-text-variant="white"
        align="center"
      >
        <b-card-text>On Feb. 29th 2021, League of Mentoring will be hosting a tournament for $100k USD!</b-card-text>
      </b-card>
      </b-col>
        </b-row>
        <b-row>
          <b-col lg="12">
      <b-card
        border-variant="dark"
        header="garbage cans invade my soloq games...surprise!"
        header-bg-variant="dark"
        header-text-variant="white"
        align="center"
      >
        <b-card-text>yeah whatever bro</b-card-text>
      </b-card>
      </b-col>
        </b-row>
      </b-container>
    </b-col>
      <b-col lg="3">
      <b-card
        border-variant="info"
        header="Recents"
        header-bg-variant="info"
        header-text-variant="white"
        align="center"
      >
     <b-list-group flush>
       <!--bg yellow to represent accepted, incomplete, bg green to represent accepted complete, red to declined-->
      <b-list-group-item variant='warning' href="#"><b-badge variant='info'>PENDING</b-badge>Doublelift (<i>11/16/19@2pm</i>)</b-list-group-item>
      <b-list-group-item variant='warning' href="#"><b-badge variant='primary'>ACCEPTED</b-badge>Milk Shake (<i>11/4/19@7pm</i>)</b-list-group-item>
      <b-list-group-item variant='danger' href="#"><b-badge variant='danger'>DECLINED</b-badge>Sneaky (<i>12/30/19@5pm</i>)</b-list-group-item>
      <b-list-group-item variant='warning' href="#"><b-badge variant='warning'>RESCHEDULE</b-badge>Sneaky (<i>12/31/19@1pm</i>)</b-list-group-item>
      <b-list-group-item variant='success' href="#"><b-badge variant='success'>ACCEPTED</b-badge>George (<i>9/16/19@9am</i>)</b-list-group-item>
    </b-list-group>
      </b-card>
      </b-col>
      </b-row>
</b-container>
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

