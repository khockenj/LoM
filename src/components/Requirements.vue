<template>
<b-card
        border-variant="warning"
        header="Requirements"
        header-bg-variant="warning"
        header-text-variant="white"
        align="center"
      >

      <b-list-group flush>
      <b-list-group-item>Season Games: <span class="red">105/700</span></b-list-group-item>
      <b-list-group-item>Weekly Games: <span class="green">100/5</span></b-list-group-item>
      <b-list-group-item>Language: <span class="green">English</span></b-list-group-item>
      <b-list-group-item>Rank: <span class="yellow">Diamond 4/Diamond 2</span></b-list-group-item>
      <b-list-group-item>Role: <span class="red">Middle/ADC</span></b-list-group-item>
      <b-list-group-item>Champs: <span class="red">No Champions in common</span></b-list-group-item>
    </b-list-group>

    <template v-slot:footer>
    <b-card-body class="mx-auto" style="padding:0!important;">
		 <b-button block v-b-modal.bookSession variant="success">Book a session</b-button>
    </b-card-body>
    </template>
      </b-card>
  </template>

  <script>
export default {
  name: 'Requirements',
}
</script>
