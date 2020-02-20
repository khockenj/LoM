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
          <b-col lg="6">{{ bio }}</b-col>
          <b-col lg="6">
            <b-container>
              <b-row>
                <b-col lg="4">
                  <h5>Champions:</h5>
                </b-col>
                <b-col>
                  <img
                    :key="m"
                    class="smallChamp"
                    :alt="m"
                    v-for="m in this.champs"
                    :src="'/static/squareicons/' + m.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
                     v-b-tooltip.hover.top="{ variant: 'info' }"
          :title='m'
                  />
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
                    :src="r == 'teams'? '/static/roles/fill.png':'/static/roles/' + r.replace(/^\w/, c => c.toUpperCase()) + '.png'"
                  />
                </b-col>
              </b-row>
            </b-container>
          </b-col>
        </b-row>
      </b-container>
    </b-card-body>
  </b-card>
</template>

  <script>
export default {
  name: "AboutMe",
  props: ["bio", "champs", "roles", "rank"],
};
</script>
<style scoped>
@media (min-width: 576px) {
.smallChamp {
  width:2.5rem;
  margin: 0.1vw;
    text-align: left;
}
}

@media (max-width: 575px) {
.smallChamp {
  width:1.5rem;
  margin: 0.1vw;
    text-align: left;
}
}
</style>