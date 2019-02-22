<!--
  Bid details in Details View
  Only visible to registered users (but not owner of ad)
  Contains bidding, name of person who has won?,
-->

<template>
  <div>
    <sui-form @submit="bid">
      <sui-form-field>
        <h3>Bud</h3>
        <input placeholder="Legg inn et bud..." >
      </sui-form-field>
      <sui-button primary type="submit">By</sui-button>
    </sui-form>


  </div>
</template>

<script>
    export default {
        name: "DetailsBid",
        props: ['ad'],
        data() {
            return {
                bidAmount: ''
            }
        },
        methods: {
            bid(e) {
                e.preventDefault();
                //todo: api call, issue #7
                this.bidAmount = '';
            }
        }
    }
</script>

<style scoped>

</style>