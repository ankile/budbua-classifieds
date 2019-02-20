<template>
  <div id="singleblog">
    <h3 v-if="loading">Laster inn...</h3>

    <h1>{{ad.title}}</h1>
    <article>{{ad.description}}</article>
    <h2 v-if="userId">Testing testing</h2>
  </div>
</template>


<script>
    import {Api} from '../../api'

    export default {
        name: "Details",
        data() {
            return {
                id: this.$route.params.id,
                ad: {},
                userId: null,
                loading: true
            }
        },
        created() {
            Api.get('auctions/ads/'+ this.id)
                .then(res => {
                    this.ad = res.data;
                    this.loading = false;
                })
                .catch(err => console.log(err));
        }
    }
</script>


<style scoped>
  #singleblog {
    max-width: 700px;
    margin: 0 auto;
    text-align: left;
  }
</style>
