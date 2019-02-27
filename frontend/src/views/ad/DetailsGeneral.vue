<!--
  General details for Details View
  Contains: ad title, image, description, remaining bid time, seller name, higest bid

-->

<template>
  <div class="general">
    <h1 is="sui-header" class="title">{{ad.title}}</h1>
    <img v-bind:src="this.ad.imageString" alt="Annonsebilde">
    <article>{{ad.description}}</article>
    <sui-divider section></sui-divider>

    <sui-grid :columns="3" divided stackable>
        <sui-grid-column>
            <h3 v-if="timeremaining">
                <sui-loader v-if="timeremaining.includes('NaNd')" active centered inline />
                <div v-else> Utløper om:
                {{timeremaining}}
                </div>
            </h3>
            <h3 class="expired" v-else>Utløpt</h3>
        </sui-grid-column>
        <sui-grid-column>
          <h3>Selger: {{ad.firstName}} {{ad.lastName}}</h3>
        </sui-grid-column>
        <sui-grid-column>
          <h3 class="highest-bid" v-if="ad.maximumBid">
              <div v-if="ad.highestBidder.id == user.id">
                  Du leder budet!<br/>
                  Høyeste bud: {{ad.maximumBid}} kr.
              </div>
              <div v-else>
                  Leder av budet: {{ad.highestBidder.name}}<br/>
                  Høyeste bud: {{ad.maximumBid}} kr.
              </div>
          </h3>
          <h3 class="highest-bid" v-else>Ingen bud lagt inn <br>
            Minimum bud: {{ad.minimumBid}} kr</h3>
        </sui-grid-column>
    </sui-grid>
  </div>
</template>


<script>
    import timeleft from "./timer";
    import SuiDivider from "semantic-ui-vue/dist/commonjs/elements/Divider/Divider";
    import SuiGrid from "semantic-ui-vue/dist/commonjs/collections/Grid/Grid";
    import SuiGridRow from "semantic-ui-vue/dist/commonjs/collections/Grid/GridRow";
    import SuiGridColumn from "semantic-ui-vue/dist/commonjs/collections/Grid/GridColumn";
    import {Api} from '../../api'

    export default {
        name: "DetailsGeneral",
        components: {SuiGridColumn, SuiGridRow, SuiGrid, SuiDivider},
        props: ["ad"],
        data() {
            return {
                timeremaining: undefined

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

            Api.get('/users/')
                .then(res => {
                    this.user = res.data;
                })
                .catch(err => console.log(err));
        }

    }
</script>



<style scoped>

  .general {
    padding: 3rem 0;
  }

  img {
    max-width: 100%;
    max-height: 100%;
    box-shadow: 0 0 8px #1e639d;
  }

  article {
    margin-top: 2rem;
  }

  .expired {
    color: red;
  }

</style>