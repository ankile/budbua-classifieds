<!--
  For deleting the ad
  Only visible to owner of ad
  Contains delete button, and verificaion?

-->

<template>
  <div>
    <sui-button negative fluid size="big" icon="trash alternate outline" v-on:click="deleteAd">Slett Annonse</sui-button>
  </div>
</template>

<script>
    export default {
        name: "DetailsDeleteAd",
        props: ["ad"],
        methods: {
            deleteAd(e) {
                e.preventDefault();
                //todo: api call

            }
        }
    }
</script>

<style scoped>
  button {
    padding: 1rem 3rem;
  }
</style>