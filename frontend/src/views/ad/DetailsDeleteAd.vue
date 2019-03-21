<!--
  For deleting the ad
  Only visible to owner of ad
  Contains delete button, and verificaion?

-->

<template>
  <div>
    <sui-button negative fluid size="big" icon="trash alternate outline" v-on:click="deleteAd">Slett Annonse</sui-button>
    <sui-divider></sui-divider>
  </div>
</template>

<script>
    import router from '../../router'
    import {Api} from "../../api";

    export default {
        name: "DetailsDeleteAd",
        props: ["ad"],
        methods: {
            deleteAd() {
                let confirmationPopup = confirm("Du er i ferd med å slette annonsen din. Dette kan ikke angres. \nVil du slette den?");
                if(confirmationPopup) {
                    const url = '/auctions/ads/' + this.ad.id;
                    Api.delete(url)
                      .then(() => {
                          alert("Annonsen er slettet");
                          router.push('/');
                        })
                      .catch((e) => {
                          alert("Noe gikk galt. Annonsen ble ikke slettet");
                          console.log(e);
                      });
                }

            }
        }
    }
</script>
