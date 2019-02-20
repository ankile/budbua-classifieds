<template>
  <div id="singleblog">
    <h3 v-if="loading">Laster inn...</h3>
    <DetailsGeneral v-bind:ad="ad"></DetailsGeneral>
    <DetailsBid v-bind:ad="ad" v-if="user && !owner"></DetailsBid>
    <DetailsUnregistered v-if="!user"></DetailsUnregistered>
    <DetailsDeleteAd v-bind:ad="ad" v-if="owner"></DetailsDeleteAd>

    <h2 class='debug debug-top' v-if="user">Debug: user true</h2>
    <h2 class="debug" v-if="owner">Debug: owner true</h2>
    <h2 class="debug" v-if="user && !owner">User and not owner</h2>
  </div>
</template>


<script>
    import Api from '../api'
    import DetailsGeneral from './DetailsGeneral'
    import DetailsBid from "./DetailsBid";
    import DetailsUnregistered from "./DetailsUnregistered";
    import DetailsDeleteAd from "./DetailsDeleteAd";


    export default {
        name: "Details",
        components: {
            DetailsGeneral,
            DetailsBid,
            DetailsUnregistered,
            DetailsDeleteAd
        },
        data() {
            return {
                id: this.$route.params.id,
                ad: {},
                user: null, //current user viewing the ad
                loading: true,
                owner: false  // is owner of ad viewing the ad
            }
        },

        created() {
            Api.get('auctions/ads/'+ this.id)
                .then(res => {
                    this.ad = res.data;
                    this.loading = false;
                    Api.get('users/')
                        .then(res => {
                            this.user = res.data;
                            this.owner = this.user.id === this.ad.owner
                        })
                        .catch(err => console.log(err));
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


  .debug {
    color: red;
  }
  .debug-top {
    margin-top: 150px;
  }
</style>