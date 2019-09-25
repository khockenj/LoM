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
      <b-list-group-item>Average Control Wards Bought: <span class="yellow">3.7</span></b-list-group-item>
      <b-list-group-item>Change since last coaching session: <span class="red">-370LP</span></b-list-group-item>
    </b-list-group>
    <b-card-body class="mx-auto" style="padding-bottom:0rem!important;">
		<a href="#" class="card-link">Find a Mentor</a>
    </b-card-body>
      </b-card>
  </template>

  <script>
export default {
  name: 'ProfileStats',
}
</script>
