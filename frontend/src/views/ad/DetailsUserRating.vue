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
                hasLeadingBid: this.user.id === this.ad.highestBidder.id,
                previouslyRated: false
            }
        },
        methods: {
            handleRate(evt, props) {
                this.value = props.rating;
                this.payload = props;

                const data = {
                    "rating": this.value
                };
                let url = '/rating/?ratingReceiver=';
                if(this.hasLeadingBid) {
                    url += this.ad.owner;
                }
                else {
                    url += this.user.id
                }
                if(!this.previouslyRated) {
                    Api.post(url, data)
                        .then(() => {
                            this.previouslyRated = true;
                        })
                        .catch(() => {
                            this.value = 0;
                            alert("Noe gikk galt");
                        });
                }
                else {
                    Api.put(url, data)
                        .catch(() => {
                            this.value = 0;
                            alert("Noe gikk galt");
                    })
                }
            },
        },
        created() {
            const timeremaining = timeleft.prettyGetTimeRemainng(this.ad.bidEndTime).timestring;
            if(timeremaining) {this.adActive = true;}

            let url = '/rating/?ratingReceiver=';
            if(this.hasLeadingBid) {
                 url += this.ad.owner;
            }
            else {
                url += this.user.id
            }
            Api.get(url)
                .then(res => {
                    if(res.status === 200) {
                        this.value = res.data.rating;
                        this.previouslyRated = true;
                    }
                });
        }
    }
</script>
