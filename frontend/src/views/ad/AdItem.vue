<template>
  <div id="aditem">
    <div class="info">
      <router-link v-bind:to="'/details/'+ad.id">
        <h2>{{ad.title}}</h2>
      </router-link>

      <h4 class="highest-bid" v-if="ad.maximumBid">Høyeste bud: {{ad.maximumBid}} kr</h4>
      <h4 class="highest-bid" v-else>Ingen bud lagt inn <br>
        Minimum bud: {{ad.minimumBid}} kr</h4>
      <h5 v-if="timeremaining">Utløper om: {{timeremaining}}</h5>
      <h5 class="expired" v-else>Utløpt</h5>
    </div>
    <router-link v-bind:to="'/details/'+ad.id">
      <img v-bind:src="this.ad.imageString" alt="Annonsebilde">
    </router-link>
  </div>
</template>


<script>
  import timeleft from "./timer";

  export default {
      name: "AdItem",
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
          }, 1000);

      }
  }

</script>


<style scoped>
  #aditem {
    background-color: white;
    max-width: 700px;
    /* border: 2px solid #41aaa1; */
    display: grid;
    grid-gap: 30px;
    grid-template-columns: 2fr 1fr;
    padding: 2rem 3rem;
    margin: 1rem auto;
    text-align: left;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  }

  #aditem:hover {
    box-shadow: 0 7px 14px rgba(0,0,0,0.25), 0 5px 5px rgba(0,0,0,0.22);
    transition-duration: 0.3s;
  }

  img {
    max-width: 100%;
    max-height: 100%;
    float: right;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  a:hover {
    font-weight: revert;
  }
  .highest-bid {
    margin-top: 80px;
  }

  h5 {
    margin-top: 20px;
  }

  .expired {
    color: red;
  }
</style>
