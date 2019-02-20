<!--
  For ungeristered users in Details View
  Only visible to users that are not registered/logged in
  Contains log in message link to log-in site

-->

<template>
  <div>
    <h3>Du er ikke logget inn. For å kunne by på en annonse må du være logget inn. Hvis du ikke har en bruker fra før av så kan du registrere en ny bruker. </h3>
    <router-link to="/login">
      <button>Logg inn</button>
    </router-link>
  </div>
</template>

<script>
    export default {
        name: "DetailsUnregistered"
    }
</script>

<style scoped>
  div {
    margin-bottom: 2rem;
  }

  button {
    padding: 1rem 3rem;
  }
</style>