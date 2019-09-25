<template>
<b-card
        border-variant="success"
        header="Weekly Goals"
        header-bg-variant="success"
        header-text-variant="white"
        align="center"
        title="Successful"
      >
        <b-card-text>You're crushing your goals this week</b-card-text>
      <b-list-group flush>
      <b-list-group-item>Weekly Games: <span class="green">100/5</span></b-list-group-item>
      <b-list-group-item>KDA: <span class="yellow">2.85/3.00</span></b-list-group-item>
      <b-list-group-item>Total Champs Played: <span class="red">10/2</span></b-list-group-item>
    </b-list-group>
    <b-card-body class="mx-auto" style="padding-bottom:0rem!important;">
		<a href="#" class="card-link" >Change Goals</a>
		<a href="#" class="card-link">Share</a>
    </b-card-body>
      </b-card>
  </template>

  <script>
export default {
  name: 'Goals',
}
</script>