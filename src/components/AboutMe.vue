<template>
<b-card
        border-variant="info"
        header="About Me"
        header-bg-variant="info"
        header-text-variant="white"
        align="center"
      >
    <b-card-body style="padding:0!important;">
      {{ bio }}
    </b-card-body>
      </b-card>
  </template>

  <script>
export default {
  name: 'AboutMe',
  props: ['bio']
}
</script>
