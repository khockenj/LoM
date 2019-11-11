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
      <b-list-group-item variant='warning' href="#" v-b-modal.test><b-badge variant='info'>PENDING</b-badge>Doublelift (<i>11/16/19@2pm</i>)</b-list-group-item>
      <b-list-group-item variant='warning' href="#"><b-badge variant='primary'>ACCEPTED</b-badge>Milk Shake (<i>11/4/19@7pm</i>)</b-list-group-item>
      <b-list-group-item variant='danger' href="#"><b-badge variant='danger'>DECLINED</b-badge>Sneaky (<i>12/30/19@5pm</i>)</b-list-group-item>
      <b-list-group-item variant='warning' href="#"><b-badge variant='warning'>RESCHEDULE</b-badge>Sneaky (<i>12/31/19@1pm</i>)</b-list-group-item>
      <b-list-group-item variant='success' href="#"><b-badge variant='success'>ACCEPTED</b-badge>George (<i>9/16/19@9am</i>)</b-list-group-item>
    </b-list-group>
      </b-card>
      </b-col>
      </b-row>
</b-container>
<b-modal id="test">   
   <template v-slot:modal-title>
      Session Information
    </template>
    <label for='status'>Status</label>
     <b-form-select class='mx-2' id='status' v-model="status"  :options="statusOptionsMentor"></b-form-select>
     only if session marked as complete by mentor
     <b-button variant='success' v-on:click="completeSession = true">Complete Session</b-button>
<div class="reviewSection" v-if="completeSession==true">
<div class="container">
        <div class="starrating risingstar d-flex justify-content-center flex-row-reverse">
            <input type="radio" id="star5" name="rating" value="5" /><label for="star5" title="5 stars"></label>
            <input type="radio" id="star4" name="rating" value="4" /><label for="star4" title="4 stars"></label>
            <input type="radio" id="star3" name="rating" value="3" /><label for="star3" title="3 stars"></label>
            <input type="radio" id="star2" name="rating" value="2" /><label for="star2" title="2 stars"></label>
            <input type="radio" id="star1" name="rating" value="1" /><label for="star1" title="1 star"></label>
        </div>
  </div>	
    <label for='title'>Title</label>
    <b-form-input id='title' class='my-2' v-model='title'></b-form-input>
    <label for='review'>Review</label>
    <b-form-textarea
        id="review"
        rows="5"
        v-model='review'
        placeholder=""
        class="my-2"
      ></b-form-textarea>
      </div>
    </b-modal>
</div>

</template>
<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      status: '',
      review: '',
      title: '',
      completeSession: false,
      statusOptionsMentor: [,
          { value: 'pending', text: 'Pending' },
          { value: 'accepted', text: 'Accepted' },
          { value: 'declined', text: 'Declined' },
          { value: 'reschedule', text: 'Reschedule' },
          { value: 'complete', text: 'Complete'},
          { value: 'incomplete', text: 'Incomplete'}
      ],
    }
  }
  }
</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

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

.starrating > input {display: none;}  /* Remove radio buttons */

.starrating > label:before { 
  content: "\f005"; /* Star */
  margin: 2px;
  font-size: 2em;
  font-family: FontAwesome;
  display: inline-block; 
}

.starrating > label
{
  color: #222222; /* Start color when not clicked */
}

.starrating > input:checked ~ label
{ color: #ffc107 ; } /* Set yellow color when star checked */

.starrating > input:hover ~ label
{ color: #ffc107 ;  } /* Set yellow color when star hover */

</style>

