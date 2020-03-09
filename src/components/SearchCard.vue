<template>
  <b-card
    text-variant="white"
    no-body
    style="max-width:18.1rem;min-width:18.1rem;background-color:transparent;"
    img-top
    :img-src="main? '/static/tiles/' + main.replace(/[^A-Z0-9]/ig, '') + '_0.jpg': 'data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII='"
  >
    <template v-slot:header>
      <h4 class="mb-0" :id='name'>
        <span v-if='name.length <= 10' v-b-tooltip.hover.top="{ variant: 'danger' }" :title='name'>{{name}}</span>
        <span style='font-size:.8rem;' v-if='name.length > 10' v-b-tooltip.hover.top="{ variant: 'danger' }" :title='name'>{{name}}</span>
        <img class="rankIcon" :src="'/static/ranks/' + rank + '.png'" v-b-tooltip.hover.top="{ variant: 'warning' }" :title="(rank[0].toUpperCase() + rank.slice(1)).replace(/_/g, ' ')" />
      </h4>
    </template>

    <b-list-group flush>
      <b-list-group-item style="padding:.75rem 1rem;background-color:#343A40;">
        <b-img
          style='max-width:2.5rem;'
          :id='c'
          :src="'/static/squareicons/' + c.toLowerCase().replace(/[^A-Z0-9]/ig, '') + '_square.png'"
          :alt="c"
          v-for="c in champs" :key="c"
          class='smallChamps'
          v-b-tooltip.hover.top="{ variant: 'info' }"
          :title='c'
          rounded
        />
        <span v-if="champs.length == 0"><img
          class="smallChamps"
          style='width:2.5rem'
          src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII="
          v-b-tooltip.hover.top="'Unknown'"
        /></span>

      </b-list-group-item>
      <b-list-group-item
        style="padding:.75rem 1rem;background-color:#343A40;"
      >
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
          style='width:2.5rem'
          src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mOs/A8AAfcBeguDlP0AAAAASUVORK5CYII="
          v-b-tooltip.hover.top="'Unknown'"
        /></span>
      </b-list-group-item>
    </b-list-group>

    <div class="footer-button">
      <!--Using hidden button to retain the space-->
      <b-button style='visibility: hidden;'><i class="textIcon"></i></b-button>
      <b-button style='position:absolute;bottom:1rem;left:4.6rem;' variant="success" :to="'/profile/' + did"><i class="fas fa-search textIcon"></i>View Mentor</b-button>
    </div>
  </b-card>
</template>
<style scoped>
.rankIcon {
  max-width: 48px;
  max-height: 48px;
  vertical-align: middle;
}
.smallChamps {
  max-width: 2.5rem;
  margin: 0.07rem;
}
.badge {
  margin: 0.1rem;
}
.card-img-top, .card-img {
  width: 100%;
  object-fit: cover;
}
.footer-button {
  padding:1rem;
  height:100%;
  background-color:#343A40;
  border-bottom-right-radius: calc(0.25rem - 1px);
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card-header{
  background-color:rgba(0,0,0,.8);
}
h4 {
  font-size:1.75rem;
}
.list-group-item {
   margin-bottom:.25rem;
}
</style>

<script>
export default {
  name: "SearchCard",
  props: ["id", "name", "main", "rank", "champs", "roles", "did"],
  methods: {
    //No longer in use - switched it for icons
    switchVariant: function(r) {
      if (r == "adc") {
        return "danger";
      } else if (r == "middle") {
        return "primary";
      } else if (r == "jungle") {
        return "success";
      } else if (r == "support") {
        return "warning";
      } else if (r == "top") {
        return "light";
      } else if (r == "teams") {
        return "info";
      }
    },
    cutName: function(name) {
      //No longer in use, but will cut name after 10 characters if > 10
      return name.length > 10 ? name.substring(name,10) + "..." : name
    }
  },

};
</script>