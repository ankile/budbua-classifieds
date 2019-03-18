<template>
  <div v-if="!adActive && this.ad.maximumBid && (owner || hasLeadingBid)">
    <h3 v-if="hasLeadingBid">Vurder selger:</h3>
    <h3 v-else>Vurder kjøper:</h3>
    <sui-rating icon="star" :rating="value" :max-rating="5" @rate="handleRate" />
    <sui-divider hidden></sui-divider>
  </div>
</template>

<script>
    import timeleft from "./timer";
    import {Api} from "../../api";

    export default {
        name: "DetailsUserRating",
        props: ['ad', 'user'],
        data() {
            return {
                value: 0,
                payload: {},
                adActive: false,
                owner: this.user.id === this.ad.owner,
                hasLeadingBid: this.user.id === this.ad.highestBidder.id

            }
        },
        methods: {
            handleRate(evt, props) {
                this.value = props.rating;
                this.payload = props;
                console.log(this.payload.rating);
                /*Api.post(url, data)
                    .then(() => {

                    })
                    .catch(() => {

                    });*/

            },
        },
        created() {
            const timeremaining = timeleft.prettyGetTimeRemainng(this.ad.bidEndTime).timestring;
            if(timeremaining) {this.adActive = true;}


        }

    }
</script>

<style scoped>

</style>