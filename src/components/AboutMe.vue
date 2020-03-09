<template>
  <b-card
    border-variant="info"
    header="My Bio"
    header-bg-variant="info"
    header-text-variant="white"
    align="center"
  >
    <b-card-body style="padding:0!important;">
      <b-container>
        <b-row>
          <b-col lg="6">
            <h4>About Me</h4>
          </b-col>
          <b-col lg="6">
            <h4>League Info</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col lg="6">
            <b-form-textarea
              id="bio"
              :no-resize="!editingMode"
              :plaintext="!editingMode"
              v-model="bio2"
              oninput='this.style.height = ;this.style.height = this.scrollHeight + 50 + "px"'
            ></b-form-textarea>
          </b-col>

          <b-col lg="6">
            <b-container>
              <b-row>
                <b-col lg="4">
                  <h5>Champions:</h5>
                </b-col>
                <b-col>
                  <b-container>
                    <b-row>
                      <b-col class="h-container" v-for="m in this.champs" :key="m">
                        <b-img
                          :class="editingMode? 'smallChamp image': 'smallChamp'"
                          :alt="m"
                          :src="'/static/squareicons/' + m.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
                          v-b-tooltip.hover.top="{ variant: 'info' }"
                          :title="m"
                          rounded
                        />
                        <div class="middle" v-if='editingMode' v-on:click="champs.splice(champs.indexOf(m), 1)">
                          <div class="x-hover">
                            <i class="fas fa-times-circle"></i>
                          </div>
                        </div>
                      </b-col>
                      <b-col v-b-modal.addChamps class='h-container' v-if='editingMode && champs.length < 6'>
                       <b-img class='smallChamp' blank blank-color="rgba(0,0,0,.8)" rounded />
                        <div class="plus-button" v-on:click="alert('boop')">
                            <i class="fas fa-plus-circle"></i>
                          </div>
                        <!--<i class="fas fa-plus-square"></i>-->
                       </b-col>
                    </b-row>
                  </b-container>
                </b-col>
              </b-row>
              <hr />
              <b-row>
                <b-col lg="4">
                  <h5>Roles:</h5>
                </b-col>
                <b-col>
                  <img
                    :key="r"
                    class="smallChamp"
                    v-b-tooltip.hover
                    :title="r.replace(/^\w/, c => c.toUpperCase())"
                    :alt="r"
                    v-for="r in this.roles"
                    :src="r == 'teams'? '/static/roles/Clash.svg':'/static/roles/' + r.replace(/^\w/, c => c.toUpperCase()) + '.png'"
                    v-on:click="editingMode ? (roles.splice(roles.indexOf(r),1), sortRoles()): false"
                  />
                  <span v-if="editingMode">
                    <img
                      :key="r"
                      class="smallChamp"
                      v-b-tooltip.hover
                      :title="r.replace(/^\w/, c => c.toUpperCase())"
                      :alt="r"
                      v-for="r in this.roleOptions[0].filter(x => !this.roles.includes(x))"
                      :src="r == 'teams'? '/static/roles/fill.png':'/static/roles/' + r.replace(/^\w/, c => c.toUpperCase()) + '.png'"
                      style="opacity:.5;"
                      v-on:click="editingMode ? (roles.push(r), sortRoles()): false"
                    />
                  </span>
                </b-col>
              </b-row>
            </b-container>
          </b-col>
        </b-row>
      </b-container>
    </b-card-body>
    <b-modal size="xl" id="addChamps">
      <template v-slot:modal-title>Add Champions</template>
        <b-form-group>
        <b-container>
        <b-row>
<b-col>
   <multi-select
            :options="championOptions"
            :selected-options="champs"
            placeholder="Choose your Champions"
            hide-selected-options
            @select="onSelect"
          >
          <!--             -->
          </multi-select>
</b-col>
        </b-row>
        <b-row class="mx-auto" style="padding-top:1rem;text-align:center;">
          <b-col
            v-for="x in champs"
            :key="x"
            class="py-3"
            lg="2"
            style="max-width:100%;justify-content: space-between;position:relative;"
          >
            <div class="img-holder">
              <img
                v-on:click="main2 = x"
                style="max-width:128px;position:relative;"
                :src="'/static/squareicons/' + x.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
              />
              <i
                style="font-size:24px;"
                :value="x"
                class="fas fa-trash-alt deleteChamp"
                :v-model="x"
                v-on:click="x == main2 ? (champs.splice(champs.indexOf(x), 1), main2=champs[0]): champs.splice(champs.indexOf(x), 1)"
              ></i>
              <b-badge v-if="x == main2" class="badgeChamp" variant="success">MAIN</b-badge>
            </div>
          </b-col>
        </b-row>
        </b-container>
      </b-form-group>
    </b-modal>
  </b-card>
</template>
 <script>
 import { MultiSelect } from 'vue-search-select'
export default {
  name: "AboutMe",
  props: ["bio", "champs", "roles", "rank", "editingMode", "main"],
  components: { MultiSelect },
  methods: {
    makeToast(title, content, variant = null) {
      this.$bvToast.toast(content, {
        title: `${title}`,
        variant: variant,
        solid: true,
        toaster: "b-toaster-top-center"
      });
    },
    autoHeight: function() {
      let bioBox = document.getElementById("bio");
      bioBox.style.height = "";
      bioBox.style.height = bioBox.scrollHeight + 50 + "px";
    },
    sortRoles: function() {
      this.roles = this.roles.sort(
        (a, b) => this.roleSort[a] - this.roleSort[b]
      );
    },
    championsList: function() {
      var vm = this;
      var championList = [];
      console.log(this.$parent);
      for (const [key, value] of Object.entries(
        this.$parent.$parent.$parent.champions
      )) {
        championList.push(value.name);
      }
     
      return championList;
    },
    parseChampOptions: function() {
      var arr = [];
       for (const [key, value] of Object.entries(
        this.$parent.$parent.$parent.champions
      )) {
      arr.push({"text": value.name, "value": value.name});
      }
      return arr;
    },
    onSelect: function(c, lastSelectItem) {
       if (this.champs.length == 0) {
        this.main2 = lastSelectItem.value;
      }
      if (
        this.champs.length <= 5 &&
        this.champions.includes(lastSelectItem.value) &&
        !this.champs.includes(lastSelectItem.value)
      ) {
        this.champs.push(lastSelectItem.value);
      } else if (this.champs.length == 6) {
        this.makeToast(
          "Warning",
          "You may only add up to six champions.",
          "warning"
        );
      } else if (this.champs.includes(lastSelectItem.value)) {
        this.makeToast(
          "Error",
          "You cannot add the same champion twice.",
          "danger"
        );
      }
    }
  },
  data: function() {
    return {
      roleOptions: [["top", "jungle", "middle", "adc", "support", "teams"]],
      roleSort: {
        top: 0,
        jungle: 1,
        middle: 2,
        adc: 3,
        support: 4,
        teams: 5
      },
      roles: this.roles,
      champs: this.champs,
      bio2: this.bio2 ? this.bio2 : this.bio,
      main2: this.main2 ? this.main2 : this.main,
      champions: this.championsList(),
      championOptions: this.parseChampOptions(),
    };
  },

  updated: function() {
    this.autoHeight();
  }
};
</script>
<style scoped>
@media (min-width: 576px) {
  .smallChamp {
    width: 2.5rem;
    height: 2.5rem;
  }
}

@media (max-width: 575px) {
  .smallChamp {
    width: 1.5rem;
    height: 2.5rem;
  }
}

.h-container {
  position: relative;
  margin: 0vw;
  padding: 0;
  max-width:3rem;
}

.image {
  opacity: 1;
  display: block;
  transition: 0.5s ease;
  backface-visibility: hidden;
}

.middle {
  transition: 0.5s ease;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 45%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

.plus-button {
  position: absolute;
  top:10.5%;
  left:18%;
  text-align: center;
}
.fas.fa-plus-circle, fas.fa-plus-circle:hover {
  color:rgba(255,255,255,1);
}
.h-container:hover .image {
  opacity: 0.3;
}

.h-container:hover .middle {
  opacity: 1;
}

.x-hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.img-holder {
  position: relative;
  display: inline-block;
  cursor: pointer;
}
.img-holder img {
  display: block;
}

.deleteChamp {
  position: absolute;
  top: 0.2rem;
  right: 0.2rem;
  opacity: 0.75;
}

.badgeChamp {
  position: absolute;
  bottom: 0.2rem;
  left: 0.2rem;
  opacity: 1;
}
.fas.fa-trash-alt.deleteChamp {
  color:rgb(255, 0, 25)
}
.fas.fa-trash-alt.deleteChamp:hover {
  color:rgb(175, 0, 15)
}
</style>