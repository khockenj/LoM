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
                  no-body
                  border-variant="primary"
                  header-bg-variant="primary"
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
        <b-col lg="3">
          <b-card
            border-variant="primary"
            header="Recents"
            header-bg-variant="primary"
            header-text-variant="white"
            align="center"
          >
            <b-list-group flush>
              <!--bg yellow to represent accepted, incomplete, bg green to represent accepted complete, red to declined-->
              <b-list-group-item
                href="#"
                :key="session._id.$oid"
                v-for="session in coachingData"
                @click="$bvModal.show(session._id.$oid)"
                :variant="
      (session.status=='complete' && session.complete) ? 'success'
         : (session.status=='declined' && session.complete) ? 'danger'
         : (Date.now() > session.dt) ? 'danger'
         : 'warning'
         "
              >
                <b-badge v-if="session.status == 'pending'" variant="info">PENDING</b-badge>
                <b-badge v-if="session.status == 'declined'" variant="danger">DECLINED</b-badge>
                <b-badge v-if="session.status == 'reschedule'" variant="warning">RESCHEDULE</b-badge>
                <b-badge v-if="session.status == 'accepted'" variant="primary">ACCEPTED</b-badge>
                <b-badge v-if="session.status == 'complete'" variant="success">COMPLETE</b-badge>
                {{session.studentName}} (
                <i>{{new Date(session.dt.$date).toLocaleDateString()}}</i>)
              </b-list-group-item>
            </b-list-group>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-modal :key="session._id.$oid" v-for="session in coachingData" :id="session._id.$oid">
      <template v-slot:modal-title>Session Information</template>
      <label for="status">Status</label>
      <b-form-select class="mx-2" id="status" v-model="status" :options="statusOptionsMentor"></b-form-select>only if session marked as complete by mentor
      <b-button variant="success" v-on:click="completeSession = true">Complete Session</b-button>
      <div class="reviewSection" v-if="completeSession==true">
        <div class="container">
          <div class="starrating risingstar d-flex justify-content-center flex-row-reverse">
            <input type="radio" id="star5" name="rating" value="5" />
            <label for="star5" title="5 stars"></label>
            <input type="radio" id="star4" name="rating" value="4" />
            <label for="star4" title="4 stars"></label>
            <input type="radio" id="star3" name="rating" value="3" />
            <label for="star3" title="3 stars"></label>
            <input type="radio" id="star2" name="rating" value="2" />
            <label for="star2" title="2 stars"></label>
            <input type="radio" id="star1" name="rating" value="1" />
            <label for="star1" title="1 star"></label>
          </div>
        </div>
        <label for="title">Title</label>
        <b-form-input id="title" class="my-2" v-model="title"></b-form-input>
        <label for="review">Review</label>
        <b-form-textarea id="review" rows="5" v-model="review" placeholder class="my-2"></b-form-textarea>
      </div>
    </b-modal>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Dashboard",
  data() {
    return {
      status: "",
      review: "",
      title: "",
      completeSession: false,
      statusOptionsMentor: [
        ,
        { value: "pending", text: "Pending" },
        { value: "accepted", text: "Accepted" },
        { value: "declined", text: "Declined" },
        { value: "reschedule", text: "Reschedule" },
        { value: "complete", text: "Complete" },
        { value: "incomplete", text: "Incomplete" }
      ],
      coachingData: null,
      newsData: null
    };
  },
  methods: {
    getCoachingData: function() {
      //this.$route.params.user
      const path =
        "http://localhost:5000/api/getCoaching/" + "175387337054879744";
      //const path = '/api/getCoaching/' + this.$route.params.user
      axios
        .get(path)
        .then(response => {
          this.coachingData = response.data;
          console.log(this.coachingData);
        })
        .catch(error => {
          console.log(error);
        });
    },
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
    saveData: function() {
      const path = "http://localhost:5000/api/profileInfo/" + this.p.name;
      //const path = '/api/profileInfo/' + this.$parent.$parent.profileData.name;

      axios
        .post(path, {
          did: this.$parent.$parent.profileData.did,
          bg: this.profileData.bg
        })
        .then(response => {
          console.log(response);
          this.makeToast("Updated", "Updated background", "success");
          this.selectedChamp = null;
          this.selectedBG = null;
        })
        .catch(error => {
          this.makeToast(
            "Error",
            "Err - there's been an error in the back. Try again or report it - thank you!",
            "danger"
          );
          console.log(error);
        });
    }
  },
  mounted: async function() {
    await this.$parent;
    console.log(this.$parent);
    this.getCoachingData();
    this.getNewsData();
  }
};
</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

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

.starrating > input {
  display: none;
} /* Remove radio buttons */

.starrating > label:before {
  content: "\f005"; /* Star */
  margin: 2px;
  font-size: 2em;
  font-family: FontAwesome;
  display: inline-block;
}

.starrating > label {
  color: #222222; /* Start color when not clicked */
}

.starrating > input:checked ~ label {
  color: #ffc107;
} /* Set yellow color when star checked */

.starrating > input:hover ~ label {
  color: #ffc107;
} /* Set yellow color when star hover */
</style>

