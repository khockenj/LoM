<template>
  <b-card
    border-variant="dark"
    header="Achievements"
    header-bg-variant="secondary"
    header-text-variant="white"
    align="center"
    style='border:0;'
  >
    <b-card-body class="mx-auto" style="padding:0!important;">
      <b-list-group flush>
        <b-list-group-item :key="a" v-for="a in achievements" draggable> 
           <b-input-group>
         <template v-slot:append>
      <b-input-group-text v-if='editingMode' v-on:click="achievements.splice(achievements.indexOf(a), 1)" style='background-color:#dc3545;'><i class="fas fa-times-circle red"></i></b-input-group-text>
    </template>
      <b-input
              :plaintext="!editingMode"
              :value="a"
            ></b-input>
      </b-input-group>
          
            </b-list-group-item>
      <b-list-group-item>
      <i v-if='editingMode' class="fas fa-plus-circle" v-on:click="achievements.push('')"></i>
      </b-list-group-item>
      </b-list-group>
    </b-card-body>
  </b-card>
</template>

  <script>
export default {
  name: "Achievements",
  props: ["achievements", "editingMode"],
  data: function() {
    return {
      achievements: this.achievements
    }
  }
};
</script>
<style scoped>
.card-body:not(.mx-auto) {
  border-right:1px solid black;
  padding-right:0;
}
.fas.fa-plus-circle:hover, .fas.fa-plus-circle  {
  color:rgba(0,0,0,.8);
}
 .fas.fa-times-circle.red {
  font-size:1.5rem;
  color:#fff;
}
.fas.fa-times-circle.red:hover {
  color:#BEBEBE;
}
</style>