<!--
  Detailed view of an ad
  Wrapper for sub views
  Content depending on user status and bid status

-->

<template>
  <div is="sui-container" textAlign="left">
    <h3 v-if="loading">Laster inn...</h3>
    <div v-else>
      <DetailsGeneral v-bind:ad="ad" v-bind:user="user"></DetailsGeneral>
      <DetailsUserRating v-bind:ad="ad" v-bind:user="user" v-if="user"></DetailsUserRating>
      <DetailsBid v-bind:ad="ad" v-if="user && !owner"></DetailsBid>
      <DetailsMap v-bind:ad="ad" v-if="ad.zipCode"></DetailsMap>
      <DetailsReport v-bind:ad="ad" v-if="user && !owner"></DetailsReport>
      <DetailsUnregistered v-if="!user"></DetailsUnregistered>
      <DetailsDeleteAd v-bind:ad="ad" v-if="owner"></DetailsDeleteAd>
    </div>
  </div>
</template>


<script>
    import {Api} from '../../api'
    import DetailsGeneral from './DetailsGeneral'
    import DetailsBid from "./DetailsBid";
    import DetailsUnregistered from "./DetailsUnregistered";
    import DetailsDeleteAd from "./DetailsDeleteAd";
    import DetailsReport from "./DetailsReport";
    import DetailsUserRating from "./DetailsUserRating";
    import DetailsMap from "./DetailsMap";

    export default {
        name: "Details",
        components: {
            DetailsUserRating,
            DetailsMap,
            DetailsGeneral,
            DetailsBid,
            DetailsUnregistered,
            DetailsDeleteAd,
            DetailsReport
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
            Api.get('/auctions/ads/'+ this.id)
                .then(res => {
                    this.ad = res.data;
                    this.loading = false;
                    Api.get('/users/')
                        .then(res => {
                            this.user = res.data;
                            this.owner = this.user.id === this.ad.owner
                        })
                        .catch(() => this.user = null);
                });
        }
    }
</script>


<style scoped>
  div {
    max-width: 700px;
    margin: 0 auto;
    text-align: left;
  }

</style>
