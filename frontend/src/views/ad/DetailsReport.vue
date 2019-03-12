<!--
  Report details in Details View
  Only visible to registered users (but not owner of ad)
  Contains reporting of ad and seller
-->

<template>
  <div class="report">
    <sui-divider hidden></sui-divider>
    <sui-button-group size="large" attached="bottom">
      <sui-button v-on:click="reportSeller" v-bind:disabled="reportSellerDisabled" negative content="Rapporter Selger"/>
      <sui-button-or text=" "/>
      <sui-button v-on:click="reportAd" v-bind:disabled="reportAdDisabled" negative content="Rapporter Annonse"/>
    </sui-button-group>
  </div>
</template>

<script>
    import {Api} from "../../api";

    export default {
        name: "DetailsReport",
        props: ["ad"],
        data() {
          return {
              reportSellerDisabled: false,
              reportAdDisabled: false
            }
        },
        methods: {
            reportSeller() {
                console.log("report seller");
                let confirmationPopup = confirm("Du er i ferd med å rapportere selger. Dette kan ikke angres. \nVil du rapportere?")
                if (confirmationPopup) {
                    console.log("slettet");
                    // API call here
                    //alert("Selger er rapportert");
                    this.reportSellerDisabled = true;

                }
            },
            reportAd() {
                console.log("report ad");
                let confirmationPopup = confirm("Du er i ferd med å rapportere denne annonsen. Dette kan ikke angres. \nVil du rapportere?")
                if (confirmationPopup) {
                    console.log("slettet");
                    // API call here
                    //alert("Budet er rapportert");
                    this.reportAdDisabled = true;

                }
            }
        }
    }
</script>

<style scoped>
  .report {
    margin-bottom: 2rem;
  }
</style>