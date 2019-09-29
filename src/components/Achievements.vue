<template>
<b-card
        border-variant="secondary"
        header="Achievements"
        header-bg-variant="secondary"
        header-text-variant="white"
        align="center"
      >
    <b-card-body class="mx-auto" style="padding:0!important;">
		  <b-list-group flush>
      <b-list-group-item :key=a v-for="a in achievements">{{a}}</b-list-group-item>
    </b-list-group>
    </b-card-body>
      </b-card>
  </template>

  <script>
export default {
  name: 'Achievements',
  props: ['achievements']
}
</script>
