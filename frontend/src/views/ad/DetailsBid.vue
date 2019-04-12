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
        <sui-input v-if="timeremaining"
              type="text"
              placeholder="Legg inn et bud..."
              v-model="bidAmountInput"
              icon="money bill alternate outline"
              icon-position="left"
              />

        <sui-input v-else
                   type="text"
                   placeholder="denne annonsen er ikke aktiv..."
                   v-model="bidAmountInput"
                   icon="money bill alternate outline"
                   icon-position="left"
                   disabled />
      </sui-form-field>
      <sui-button v-if="timeremaining" primary type="submit">By</sui-button>
      <sui-button v-else disabled primary type="submit">By</sui-button>
    </sui-form>


  </div>
</template>

<script>
    import {Api} from "../../api";
    import timeleft from "./timer";

    export default {
        name: "DetailsBid",
        props: ['ad'],
        data() {
            return {
                bidAmountInput: "",
            }
        },
        methods: {
            bid() {
                let minBid = 0;
                if (this.ad.maximumBid) {
                    minBid = this.ad.maximumBid + 1;
                }
                else {
                    minBid = this.ad.minimumBid
                }
                this.bidAmountInput = Number(this.bidAmountInput);
                if(this.bidAmountInput <= this.ad.maximumBid){
                    alert("Budet må være større enn nåværende bud")
                } else {
                    let confirmationPopup = confirm("Du er i ferd med å legge inn et bud på: "+this.bidAmountInput+" NOK. Dette budet er bindende. \nVil du legge inn bud?")
                    if(confirmationPopup == true){
                        if (!isNaN(this.bidAmountInput) && this.bidAmountInput >= minBid) { // if the bid is accepted
                            const data = {
                                "value": this.bidAmountInput
                            };
                            const path = '/auctions/ads/'+this.ad.id +'/bid/';
                            Api.post(path, data)
                                .then(() => {
                                    this.bidAmountInput = '';
                                })
                                .catch( () => {});
                        }
                    }

                }


            }
        },
        created(){
            this.timeremaining = timeleft.prettyGetTimeRemainng(this.ad.bidEndTime).timestring;
        }
    }
</script>

<style scoped>

</style>