<template>
<b-card
        border-variant="warning"
        header="Requirements"
        header-bg-variant="warning"
        header-text-variant="white"
        align="center"
      >
     
      <b-list-group flush>
      <span :key='key' v-for='(value, key) in requirements'>
        <span v-if="value != null && (value == true || value.enabled == true)">
      <b-list-group-item v-if="key=='gamesPlayed'">Games during the last: {{value.days}}</b-list-group-item>
      <b-list-group-item v-if="key=='langMatch'">Language: {{value}}</b-list-group-item>
      <b-list-group-item v-if="key=='rank'">{{value.minmax}} - {{value.rank.replace(/^\w/, c => c.toUpperCase())}}</b-list-group-item>
      <b-list-group-item v-if="key=='roleMatch'">{{value}}</b-list-group-item>
      <b-list-group-item v-if="key=='champMatch'">Champs: {{value}}</b-list-group-item>
      <b-list-group-item v-if="key=='champMatch'">Server: {{value}}</b-list-group-item>
      </span>
      </span>
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
  props: ['requirements']
}
</script>
