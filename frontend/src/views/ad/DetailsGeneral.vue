<!--
  General details for Details View
  Contains: ad title, image, description, remaining bid time, seller name, higest bid

-->

<template>
  <div>
    <h1 class="title">{{ad.title}}</h1>
    <img src="https://images.pexels.com/photos/1751731/pexels-photo-1751731.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="Annonsebilde">
    <article>{{ad.description}}</article>

    <h3 v-if="timeremaining">Utløper om: {{timeremaining}}</h3>
    <h3 class="expired" v-else>Utløpt</h3>

    <h3>Selger: {{ad.firstName}} {{ad.lastName}}</h3>

    <h3 class="highest-bid" v-if="ad.maximumBid">Høyeste bud: {{ad.maximumBid}} kr</h3>
    <h3 class="highest-bid" v-else>Ingen bud lagt inn <br>
      Minimum bud: {{ad.minimumBid}} kr</h3>

  </div>
</template>
<script>
    import timeleft from "./timer";

    export default {
        name: "DetailsGeneral",
        props: ["ad"],
        data() {
            return {
                timeremaining: null
            }
        },
        created() {
            this.timeremaining = timeleft.prettyGetTimeRemainng(this.ad.bidEndTime).timestring;
            let timeinterval = setInterval(() => {
                let time = timeleft.prettyGetTimeRemainng(this.ad.bidEndTime);
                this.timeremaining = time.timestring;
                if (!time.shouldCount) {
                    clearInterval(timeinterval);
                }
                //console.log("timeintervallid" + this.ad.id);
            }, 1000);
        }

    }
</script>



<style scoped>
  div {
    margin: 1rem auto;
    max-width: 700px;
  }

  .title {
    margin-top: 2rem;
  }

  img {
    max-width: 100%;
    max-height: 100%;
    box-shadow: 0 0 8px #1e639d;
  }

  article {
    margin-top: 1rem;
  }

  .expired {
    color: red;
  }

  h3 {
    background: #eee;
    padding: 1rem;
  }
</style>