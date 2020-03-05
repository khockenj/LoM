<template>
  <div class="profile">
    <div class="overlay" :style="setBG"></div>
    <b-container>
    <b-row>
    <b-col class='my-0 py-0'>
      <b-jumbotron
        style="padding:1rem 1rem;margin-bottom:0;margin-top:1rem;background-color:#000;border-top-left-radius:1rem;border-top-right-radius:1rem;"
bg-variant="dark"
        text-variant="white"
        header-level="4"
        fluid
      >
        <div style="display:flex;">
          <div style="flex-grow:12;" class='starHolder' v-on:click="scrollToReviews">
            <div v-if="profileData.type == 'mentor'">
            <i class="fas fa-star star" :key='' v-for="s in Math.floor(profileData.score)"></i>
            <i
              class="fas fa-star-half-alt star"
              v-for="s in customRound(profileData.score-Math.floor(profileData.score))[0]"
            ></i>
            <i
              class="far fa-star star"
              v-for="s in 5-Math.ceil(profileData.score)+customRound(profileData.score-Math.floor(profileData.score))[1]"
            ></i>
          </div>
          </div>
          <div class="champHolder" style="flex-grow:0">
            <img
              :key="m"
              class="smallChamp"
              :alt="m"
              v-for="m in profileData.champs"
              :src="'/static/squareicons/' + m.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
               v-b-tooltip.hover.top="{ variant: 'info' }"
          :title='m'
            />
          </div>
          <div class="iconHolder" style="flex-grow:0;">
            <a
              v-if="profileData.socials.twitch"
              :href="'https://www.twitch.tv/' + profileData.socials.twitch"
            >
              <i class="fab fa-twitch profileSocial"></i>
            </a>
            <a
              v-if="profileData.socials.youtube"
              :href="'https://www.youtube.com/user/' + profileData.socials.youtube"
            >
              <i class="fab fa-youtube profileSocial"></i>
            </a>
            <i
              v-if="profileData.socials.discord"
              v-b-tooltip.hover
              :title="profileData.socials.discord"
              class="fab fa-discord profileSocial"
            ></i>
            <a
              v-if="profileData.socials.twitter"
              :href="'https://www.twitter.com/' + profileData.socials.twitter"
            >
              <i class="fab fa-twitter profileSocial"></i>
            </a>
            <a
              v-if="profileData.socials.patreon"
              :href="'https://www.patreon.com/' + profileData.socials.patreon"
            >
              <i class="fab fa-patreon profileSocial"></i>
            </a>
          </div>
        </div>
        <span v-if="$parent.$parent.profileData">
          <i
            v-if="$parent.$parent.profileData.did == profileData.did"
            class="fas fa-image"
            style="position: absolute;right:4.2rem;top:1.55rem;"
            v-b-modal.settings
            v-b-tooltip.hover.bottomleft="{ variant: 'info' }"
            title='Change Background'
          ></i>
        </span>
        <i
          class="fas fa-sync-alt"
          style="position: absolute;right:1.6rem;top:1.55rem;"
          v-b-tooltip.hover.bottomleft="{ variant: 'warning' }"
          title='Update Information'
          v-on:click="pullRiotInfo"
        ></i>
        <i
          class="fas fa-info-circle"
          style="position:absolute; left:1.6rem; top:1.55rem;"
          v-b-modal.info
        ></i>
        <template v-slot:header>
          {{profileData.name}}
          <img class="rankIcon" :src="'/static/ranks/' + profileData.rank + '.png'" />
        </template>
      </b-jumbotron>
  </b-col>
  </b-row>
      <b-row class="mb-0">
        <b-col lg="12">
          <Plotly
            v-if="profileData.type == 'student'"
            style="height:100%;"
            :data="graphdata"
            :layout="layout"
            :displayModeBar="true"
          />
          <about-me
            :bio="profileData.bio"
            :champs="profileData.champs"
            :roles="profileData.roles"
            :rank="profileData.rank == 'default' || !profileData.rank ? 'challenger':profileData.rank"
            v-if="profileData.type == 'mentor'"
            style="height:100%;"
          />
        </b-col>
      </b-row>
      <b-row>
        <b-col lg="8" style='padding-right:0;'>
          <goals v-if="profileData.type == 'student'" :goalProgress='profileData.goalProgress' style="height:100%;" />
          <achievements
            :achievements="profileData.achievements"
            v-if="profileData.type == 'mentor'"
            style="height:100%;"
          />
        </b-col>
        <b-col lg="4" style='padding-left:0;'>
          <stats v-if="profileData.type == 'student'" style="height:100%;" />
          <requirements
            :champs="profileData.champs"
            :servers="profileData.region"
            :langs="profileData.languages"
            :roles="profileData.roles"
            :requirements="profileData.requirements"
            :did="profileData.did"
            v-if="profileData.type == 'mentor'"
            style="height:100%;"
          />
        </b-col>
      </b-row>
      <div v-if="profileData.type == 'mentor'">
      <b-row>
        <b-col class='my-0 py-0'>
          <b-jumbotron
            style="padding-top:1rem;padding-bottom:1rem;margin-bottom:0;"
            bg-variant="dark"
            text-variant="white"
            header-level="4"
            fluid
          >
            <template v-slot:header>Reviews</template>
          </b-jumbotron>
        </b-col>
        </b-row>
        <b-row v-for='r in reviews' :key='r._id'>
          <b-col>
            <b-card>
               <template v-slot:header>
                  <b>{{r.reviewTitle}}</b> <small>posted by <b-link :to="'/profile/' + r.student">{{r.studentName}}</b-link></small>
          </template>
          <b-card-title><i class="fas fa-star star no-hover" v-for="s in Math.floor(r.rating)"></i><i
              class="far fa-star star no-hover"
              v-for="s in 5-Math.ceil(r.rating)+customRound(r.rating-Math.floor(r.rating))[1]"
            ></i>
          </b-card-title>
          <b-card-text>{{r.reviewText}}</b-card-text>
          </b-card>
          </b-col>
        </b-row>
        <b-calendar 
        class="border rounded p-2 custom-calendar" 
        readonly='true' 
        :date-info-fn="dateFilled" 
        :date-disabled-fn="dateDisabled" 
        label-no-date-selected='General Availability'
        label-help='Green - typically available, Red - typically unavailable. Contact mentor for more info.'></b-calendar>
        </div>
    </b-container>

    <b-modal @ok="saveBG" id="settings" ok-title="Save">
      <template v-slot:modal-title>Settings</template>
      <b-container>
        <b-row class="py-2">
          <b-col lg="3">
            <label for="champ">Champion:</label>
          </b-col>
          <b-col lg="9">
            <b-form-select id="champ" v-on:change="filterList" v-model="selectedChamp">
              <option :key="k" v-for="(v,k) in skinList" :value="k">{{k}}</option>
            </b-form-select>
          </b-col>
        </b-row>
        <b-row>
          <b-col lg="3">
            <label for="yourbg">Splash:</label>
          </b-col>
          <b-col lg="9">
            <b-form-select id="yourbg" v-model="selectedBG">
              <option :key="s.id" v-for="s in filteredList" :value="s.id">{{s.name}}</option>
            </b-form-select>
          </b-col>
        </b-row>

      </b-container>
             

    </b-modal>

    <b-modal id="info">
      <template v-slot:modal-title>Information</template>
      info
    </b-modal>

    <b-modal id="shareGoals">
      <template v-slot:modal-title>Share Goals</template>
      share
    </b-modal>

    <b-modal id="changeGoals">
      <template v-slot:modal-title>Change Goals</template>
      change
    </b-modal>

    <b-modal id="bookSession" @ok='bookSession'>
      <template v-slot:modal-title>Book Session</template>
      <b-container>
      <b-row>
      <b-col>
      <b-form-datepicker  class="border rounded" 
        v-model="date" 
        :date-disabled-fn="dateDisabled" 
        label-no-date-selected='Select up to 3 dates and times'
        @input="addDate"
      reset-button
      close-button
        >
        </b-form-datepicker>
      </b-col>
      </b-row>
      <b-row v-for='(d, index) in dates' :key='index' class='py-1'>
      <b-col lg='3'>
        <h5 style='padding-top:.35rem;font-size:1rem;'>{{d.date}}</h5>
      </b-col>
      <b-col>
         <b-form-timepicker v-model="d.time"       
      now-button
      reset-button
      label-no-time-selected='All time is in your local time'></b-form-timepicker>
      </b-col>
      <b-col lg='1' style='text-align:left;'>
      <i class="fas fa-minus-circle red" style='font-size:1.5rem;padding-top:.3rem;' v-on:click='removeDate(index)'></i>
      </b-col>
      </b-row>
      <b-row>
      <b-col>
        <b-form-textarea
      class='my-2'
      id="textarea"
      v-model="studentMessage"
      :placeholder="profileData.mentorMessage"
      rows="3"
    ></b-form-textarea>
      </b-col>
      </b-row>
      </b-container>
    </b-modal>
  </div>
</template>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
import { Plotly } from "vue-plotly";
import Goals from "./Goals";
import ProfileStats from "./ProfileStats";
import ProfileChampionCard from "./ProfileChampionCard";
import AboutMe from "./AboutMe";
import Achievements from "./Achievements";
import Requirements from "./Requirements";
import axios from "axios";
import skinlist from "../../static/skinList.json";
export default {
  name: "ProfilePage",
  components: {
    Plotly,
    goals: Goals,
    stats: ProfileStats,
    "profile-champion": ProfileChampionCard,
    "about-me": AboutMe,
    requirements: Requirements,
    achievements: Achievements
  },
  props: ["p"],
  data: function() {
    return {
      selectedChamp: null,
      selectedBG: null,
      filteredList: null,
      skinList: skinlist,
      graphdata: [],
      layout: {},
      profileData: {},
      reviews: null,
      date: null,
      dates: [],
      studentMessage: null,
      rankGraphInfo: {
        "challenger_1": 26,
        "grandmaster_1": 25,
        "master_1": 24,
        "diamond_1": 23,
        "diamond_2": 22,
        "diamond_3": 21,
        "diamond_4": 20,
        "platinum_1": 19,
        "platinum_2": 18,
        "platinum_3": 17,
        "platinum_4": 16,
        "gold_1": 15,
        "gold_2": 14,
        "gold_3": 13,
        "gold_4": 12,
        "silver_1": 11,
        "silver_2": 10,
        "silver_3": 9,
        "silver_4": 8,
        "bronze_1": 7,
        "bronze_2": 6,
        "bronze_3": 5,
        "bronze_4": 4,
        "iron_1": 3,
        "iron_2": 2,
        "iron_3": 1,
        "iron_4": 0
      }
    };
  },
  methods: {
    addDate: function() {
      if(this.dates.length < 3) {
        this.dates.push({date: this.date, time: null});
        this.date = null;
      } else {
        this.date = null;
        this.makeToast("Error", "Cannot add more than 3 times", "warning");
      }
    },
    removeDate: function(date) {
      this.dates.splice(date, 1);
    },
    bookSession: function() {
      alert('hi');
    },
    dateDisabled(ymd, date) {
        // Disable weekends (Sunday = `0`, Saturday = `6`) and
        // disable days that fall on the 13th of the month
        const weekday = date.getDay()
        const day = date.getDate()
        // Return `true` if the date should be disabled
        return weekday != 0 && weekday != 6
      },
      dateFilled(ymd, date) {
        // Disable weekends (Sunday = `0`, Saturday = `6`) and
        // disable days that fall on the 13th of the month
        const weekday = date.getDay()
        const day = date.getDate()
        // Return `true` if the date should be disabled
        return weekday === 0 || weekday === 6  ?  'table-success' : 'table-danger'
      },
    makeToast(title, content, variant = null) {
      this.$bvToast.toast(content, {
        title: `${title}`,
        variant: variant,
        solid: true,
        toaster: "b-toaster-top-center"
      });
    },
    scrollToReviews: function() {
      window.scrollTo(0, 950);
    },
    graphRank: function(rank) {
      return this.rankGraphInfo[rank];
    },
    saveBG: function() {
      this.profileData.bg = this.selectedChamp + "_" + this.selectedBG;

      const path = "http://localhost:5000/api/profileInfo/" + this.$parent.$parent.profileData.name;
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
    },
    filterList: function() {
      this.filteredList = this.skinList[this.selectedChamp];
      console.log(this.filteredList);
    },
    customRound: function(n) {
      if (n >= 0.4) {
        return [1, 0];
      } else if (n != 0) {
        return [0, 1];
      } else {
        return [0, 0];
      }
    },
    pullRiotInfo: function() {
      const path = "http://localhost:5000/api/riotApi"
      //const path = '/api/riotApi'
      axios
        .post(path, {
          did: this.profileData.did,
          region: this.profileData.accounts[this.profileData.mainAccount-1].region,
          accountName: this.profileData.accounts[this.profileData.mainAccount-1].name
        })
        .then(response => {
          console.log(response);
          this.makeToast("Updated", "Updated profile", "success");
          this.profileData.rank = response.data.rank;
          this.profileData.rankTimeline.push(response.data)
          this.profileData.goals = response.data.goals;
        })
        .catch(error => {
          this.makeToast(
            "Error",
            "Err - there's been an error in the back. Try again or report it - thank you!",
            "danger"
          );
          console.log(error);
        });
    },
    getData: function() {
      const path =
        "http://localhost:5000/api/profileInfo/" + this.$route.params.user;
      //const path = '/api/profileInfo/' + this.$route.params.user
      axios
        .get(path)
        .then(response => {
          this.profileData = response.data;
          this.graphdata = [{
            x: this.profileData.rankTimeline.map(a => new Date(a.time*1000).toDateString()),
            y: this.profileData.rankTimeline.map(a => this.graphRank(a.rank)),
          type: "scatter"
        }]
        this.layout = {
       
        title: "Rank Graph",
        xaxis: {
    autorange: true,
    rangeselector: {
      buttons: [
        {
          count: 1,
          label: '1m',
          step: 'month',
          stepmode: 'backward'
        },
        {
          count: 6,
          label: '6m',
          step: 'month',
          stepmode: 'backward'
        },
        {step: 'all'}
      ]},
      },
      yaxis: {
         tickvals: this.profileData.rankTimeline.map(a => this.graphRank(a.rank)),
        ticktext: this.profileData.rankTimeline.map(a => (a.rank[0].toUpperCase() + a.rank.slice(1)).replace(/_/g, ' '))
      }
        }
          console.log(this.profileData);
        })
        .catch(error => {
          console.log(error);
        });
        const path2 =
        "http://localhost:5000/api/getCoaching/" + this.$route.params.user + "?complete=1";
        //const path2 = '/api/getCoaching/' + this.$route.params.user + "?complete=1";
      axios
        .get(path2)
        .then(response => {
          console.log(response.data);
          this.reviews = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
    
  },
  mounted: async function() {
    await this.$parent;
    console.log(this.$parent);
    this.getData();
  },
  updated: function() {},
  watch: {
    $route(to, from) {
      this.getData();
    }
  },
  computed: {
    setBG: function() {
      return {
        "--bg":
          "url('/static/backgrounds/splash/" + this.profileData.bg + ".jpg')"
      };
    }
  }
};
</script>

<style scoped>
.overlay {
  background-color: rgba(0, 0, 0, 0.4) !important;
  background-image: var(--bg);
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-size: cover;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0px;
  z-index: -1000;
}
.starHolder {
  min-height: calc(12px + 1vw);
}
.rankIcon {
  max-width: 96px;
  max-height: 96px;
  vertical-align: middle;
}

.iconHolder {
  text-align: right;
  font-size: calc(12px + 1vw);
  position: absolute;
  right: 2%;
}

.champHolder {
  text-align: left;
  font-size: calc(12px + 1vw);
  position: absolute;
  left: 2%;
}

@media (min-width: 576px) {
.smallChamp {
  width:2.5rem;
  margin: 0.1vw;
}

.custom-calendar {
  position:fixed;
  right:2.5%;
  top:26%;
  z-index:1040;
  background-color:#fff;
}
}

@media (max-width: 575px) {
.smallChamp {
  width:1.5rem;
  margin: 0.1vw;
}
.custom-calendar {
  background-color:#fff;
}
}

.profileSocial {
  padding: 0;
}

.no-hover {
  cursor:auto;
}

.card {
  margin:0;
}
.fas.fa-minus-circle:hover {
color:rgb(156,0,6);
font-size:1.5rem;
}
</style>
