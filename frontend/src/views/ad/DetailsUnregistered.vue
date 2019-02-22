<!--
  For ungeristered users in Details View
  Only visible to users that are not registered/logged in
  Contains log in message link to log-in site

-->

<template>
  <div class="wrap">
    <sui-segment raised color="blue">
      <h3>Du er ikke logget inn. For å kunne by på en annonse må du være logget inn. Hvis du ikke har en bruker fra før av så kan du registrere en ny bruker. </h3>
      <sui-button primary @click="$router.push('/login')">Log Inn</sui-button>
    </sui-segment>

  </div>
</template>

<script>
    export default {
        name: "DetailsUnregistered"
    }
</script>

<style scoped>
  .wrap {
    margin-bottom: 2rem;
  }

  button {
    padding: 1rem 3rem;
  }
</style>