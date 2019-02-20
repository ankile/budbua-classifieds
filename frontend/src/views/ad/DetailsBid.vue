<!--
  Bid details in Details View
  Only visible to registered users (but not owner of ad)
  Contains bidding, name of person who has won?, reporting of ad/seller
-->

<template>
  <div>
    <form @submit="bid">
      <input type="text" v-model="bidAmount" name="bid" placeholder="Legg inn et bud...">
      <input type="submit" value="By" class="btn">
    </form>

    <div class="report">
      <button>Rapporter Selger</button>
      <button>Rapporter Annonse</button>
    </div>
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
                //todo: api call
                this.bidAmount = '';
            }
        }
    }
</script>

<style scoped>
  form {
    display: flex;
    min-height: 40px;
    margin: 1rem 0;
  }

  input[type="text"] {
    flex: 10;
    padding: 5px;
  }

  input[type="submit"] {
    flex: 2;
  }

  .report {
    display: flex;
    justify-content: flex-start;
  }
  button {
    padding: 1rem 3rem;
    margin-right: 1rem;
  }
</style>