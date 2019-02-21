<!--
  Report details in Details View
  Only visible to registered users (but not owner of ad)
  Contains reporting of ad and seller
-->

<template>
  <div class="report">
    <sui-divider hidden></sui-divider>
    <sui-button-group size="large" attached="bottom">
      <sui-button negative content="Rapporter Selger"/>
      <sui-button-or text=" "/>
      <sui-button negative content="Rapporter Annonse"/>
    </sui-button-group>
  </div>
</template>

<script>
    export default {
        name: "DetailsReport",
        props: ["ad"]
    }
</script>

<style scoped>
  .report {
    margin-bottom: 2rem;
  }
</style>