<template>
<b-card
        border-variant="info"
        header="Your Recent Stats"
        header-bg-variant="info"
        header-text-variant="white"
        align="center"
      >
      <b-list-group flush>
      <b-list-group-item style="padding-top:0;">Winrate: <span class="green">85%</span></b-list-group-item>
      <b-list-group-item>Games Played: <span class="green">100</span></b-list-group-item>
      <b-list-group-item>KDA: <span class="yellow">2.85</span></b-list-group-item>
      <b-list-group-item>CSPM: <span class="green">8.8</span></b-list-group-item>
      <b-list-group-item>Control Wards: <span class="yellow">3.7</span></b-list-group-item>
      <b-list-group-item>Change: <span class="red">-370LP</span></b-list-group-item>
      <b-list-group-item>9/19/19 - 9/26/19</b-list-group-item>
    </b-list-group>
    <template v-slot:footer>
    <b-card-body class="mx-auto" style="padding:0!important;">
		 <b-button block variant="info">Find a mentor</b-button>
    </b-card-body>
    </template>
      </b-card>
  </template>

  <script>
export default {
  name: 'ProfileStats',
}
</script>
