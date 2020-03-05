<template>
  <b-card
    header="Requirements"
    header-bg-variant="warning"
    header-text-variant="white"
    align="center"
     style='border:0;'
  >
    <b-list-group flush>
      <span :key="key" v-for="(value, key) in requirements">
        <span v-if="value != null && (value == true || value.enabled == true)">
          <b-list-group-item
            v-if="key=='gamesPlayed'"
            :variant="switchBackgroundVariant(key)"
          >{{value.games}} games during the last {{value.days}} days</b-list-group-item>
          <b-list-group-item v-if="key=='langMatch'" :variant="switchBackgroundVariant(key)">
            Language Match
            <i class="fas fa-question-circle textIcon-color" id="langPopover"></i>
            <b-popover target="langPopover" triggers="hover" placement="top">
              <template v-slot:title>Language Match</template>
              Mentor requires you must match at least one of their languages listed:
              <br />
              <b-badge class="popover-badge" variant="primary" v-for="l in langs" :key="l">{{l}}</b-badge>
            </b-popover>
          </b-list-group-item>
          <b-list-group-item :variant="rankSwitchBgVariant(value.rank, value.minmax)" v-if="key=='rank'">
            <b-badge variant="primary" v-if="value.minmax == 'min'">MINIMUM</b-badge>
            <b-badge variant="warning" v-if="value.minmax == 'max'">MAXIMUM</b-badge>
            {{value.rank.replace(/^\w/, c => c.toUpperCase())}}
          </b-list-group-item>

          <b-list-group-item v-if="key=='roleMatch'" :variant="switchBackgroundVariant(key)">
            Role Match
            <i class="fas fa-question-circle textIcon-color" id="rolePopover"></i>
            <b-popover target="rolePopover" triggers="hover" placement="top">
              <template v-slot:title>Role Match</template>
              Mentor requires you must match at least one of their roles listed:
              <br />
       <img
                    :key="r"
                    class="smallChamps"
      
                    v-b-tooltip.hover
                    :title="r.replace(/^\w/, c => c.toUpperCase())"
                    :alt="r"
                    v-for="r in roles"
                    :src="r == 'teams'? '/static/roles/Clash.svg':'/static/roles/' + r.replace(/^\w/, c => c.toUpperCase()) + '.png'"
                  />
          <span v-if="roles.length == 0"><img
          class="smallChamps"
          src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII="
          v-b-tooltip.hover.top="'Unknown'"
        /></span>
            </b-popover>
          </b-list-group-item>
          <b-list-group-item v-if="key=='champMatch'" :variant="switchBackgroundVariant(key)">
            Champion Match
            <i class="fas fa-question-circle textIcon-color" id="champPopover"></i>
            <b-popover target="champPopover" triggers="hover" placement="top">
              <template v-slot:title>Champ Match</template>
              Mentor requires you must match at least one of their champions listed:
              <br />
              <img
                style="max-width:2.5rem;"
                :id="c"
                :src="'/static/squareicons/' + c.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
                :alt="c"
                v-for="c in champs"
                :key="c"
                class="smallChamps"
                v-b-tooltip.hover.top="{ variant: 'info' }"
                :title="c"
              />
              <span v-if="champs.length == 0">
                <img
                  class="smallChamps"
                  style="width:2.5rem"
                  src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII="
                  v-b-tooltip.hover.top="'Unknown'"
                />
              </span>
            </b-popover>
          </b-list-group-item>
          <b-list-group-item v-if="key=='serverMatch'" :variant="switchBackgroundVariant(key)">
            Server Match
            <i class="fas fa-question-circle textIcon-color" id="serverPopover"></i>
            <b-popover target="serverPopover" triggers="hover" placement="top">
              <template v-slot:title>Server Match</template>
              Mentor requires you must match at least one of their servers listed:
              <br />
              <b-badge
                class="popover-badge"
                v-for="s in servers"
                :key="s"
                variant="primary"
              >{{s.toUpperCase()}}</b-badge>
            </b-popover>
          </b-list-group-item>
        </span>
      </span>
    </b-list-group>

    <template v-slot:footer>
      <b-card-body class="mx-auto" style="padding:0!important;">
        <b-button
          block
          v-b-modal.bookSession
        >Book a session</b-button>
        <!--
          :variant="failed ? 'danger': 'success'"
          :disabled="failed  || $parent.$parent.$parent.profileData.did == did"
          -->
      </b-card-body>
    </template>
  </b-card>
</template>

  <script>
export default {
  name: "Requirements",
  props: ["requirements", "champs", "servers", "langs", "roles", "did"],
  data: function() {
    return {
      failed: false
    };
  },
  methods: {
    convertRank: function(r) {
      var rf = 0;
      if (r != null) {
        r = r.toLowerCase();

        if (r.search("platinum") >= 0) {
          rf = 1;
        } else if (r.search("diamond") >= 0) {
          rf = 2;
        } else if (r.search("master") >= 0) {
          rf = 3;
        } else if (r.search("grandmaster") > 0) {
          rf = 4;
        } else if (r.search("challenger") >= 0) {
          rf = 5;
        } else if (r.search("professional") >= 0) {
          rf = 6;
        }
      }
      return rf;
    },
    rankSwitchBgVariant: function(rank, mm) {
      let user = this.$parent.$parent.$parent.profileData;
      let rankNum = this.convertRank(rank);
      if (user) {
        let userRank = this.convertRank(user.rank);
        if (mm == "min") {
          if (userRank >= rankNum) {
            return "success";
          } else {
            this.failed = true;
            return "danger";
          }
        } else if (mm == "max") {
          if (userRank <= rankNum) {
            return "success";
          } else {
            this.failed = true;
            return "danger";
          }
        }
      } else {
        this.failed = true;
        return "light";
      }
    },
    switchBackgroundVariant: function(req) {
      let user = this.$parent.$parent.$parent.profileData;
      if (user) {
        if (req == "serverMatch") {
          if (
            user.region.filter(element => this.servers.includes(element))
              .length > 0
          ) {
            return "success";
          } else {
            this.failed = true;
            return "danger";
          }
        } else if (req == "champMatch") {
          if (
            user.champs.filter(element => this.champs.includes(element))
              .length > 0
          ) {
            return "success";
          } else {
            this.failed = true;
            return "danger";
          }
        } else if (req == "roleMatch") {
          if (
            user.roles.filter(element => this.roles.includes(element)).length >
            0
          ) {
            return "success";
          } else {
            this.failed = true;
            return "danger";
          }
        } else if (req == "langMatch") {
          if (
            user.languages.filter(element => this.langs.includes(element))
              .length > 0
          ) {
            return "success";
          } else {
            this.failed = true;
            return "danger";
          }
        }
      } else {
        this.failed = true;
        return "light";
      }
    }
  }
};
</script>

<style scoped>
.popover-badge {
  margin-left: 0.1rem;
  margin-right: 0.1rem;
}
.smallChamps {
  margin: 0.05rem;
  width:2.5rem;
}
</style>
