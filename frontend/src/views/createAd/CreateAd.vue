<template>
  <div class="create-container">
    <sui-grid centered vertical-align="middle">
      <sui-grid-column>

        <h2 is="sui-header" color="blue" image>

          <sui-header-content class="card--header">Lag en ny annonse</sui-header-content>
        </h2>

        <sui-form>
          <sui-segment >
            <sui-form-field required>
              <label>Tittel</label>
              <sui-input
                      type="text"
                      placeholder="Tittel"
                      icon="heading"
                      v-model="titleInput"
                      icon-position="left"/>
            </sui-form-field>
            <sui-form-field>
              <label>Beskrivelse</label>
              <textarea v-model="descriptionInput" rows="10" placeholder="Beskrivelse"></textarea>
            </sui-form-field>
            <sui-form-field>
              <label>Bilde</label>
              <input type="file" accept="image/*" @change="onFileSelected">
              <div v-if="selectedFile">
                <label>Forhåndsvisning av bilde: <br> </label>
                <img v-bind:src="this.selectedFile" alt="Annonsebilde">
              </div>
            </sui-form-field>
            <sui-form-field required>
              <label>Sluttid</label>
              <sui-input
                      type="datetime-local"
                      placeholder="Sluttid"
                      icon="calendar alternate outline"
                      v-model="bidEndTimeInput"
                      icon-position="left" />
            </sui-form-field>
            <sui-divider />
            <sui-form-field>
              <label>Minste godtatte bud</label>
              <sui-input
                      type="text"
                      placeholder="Minste godtatte bud"
                      v-model="minimumBidInput"
                      icon="money bill alternate outline"
                      icon-position="left" />
            </sui-form-field>
            <!--<sui-form-field>
              <sui-input
                      type="text"
                      placeholder="Postkode"
                      v-model="zipcodeInput"
                      icon="map marker alternate"
                      icon-position="left" />
            </sui-form-field>-->
            <sui-button v-on:click="submitAd" size="large" color="blue" fluid>Lag Annonse</sui-button>
          </sui-segment>
        </sui-form>
      </sui-grid-column>
    </sui-grid>

  </div>
</template>

<script>
    import {Api} from "../../api";

    function getBase64(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => resolve(reader.result);
            reader.onerror = error => reject(error);
        });
    }

    export default {
        name: "CreateAd",
        data() {
            return {
                titleInput: '',
                descriptionInput: '',
                bidEndTimeInput: '',
                minimumBidInput: 0,
                zipcodeInput: '',
                selectedFile: null //image file base64
            }
        },
        methods: {
            onFileSelected(event) {
                const file = event.target.files[0];
                getBase64(file)
                    .then(data => {
                        this.selectedFile = data;
                    })
                    .catch(err => console.log(err));
            },

            submitAd(e) {
                e.preventDefault();
                let data = {
                    "title": this.titleInput,
                    "description": this.descriptionInput,
                    "bidEndTime": new Date(this.bidEndTimeInput).toISOString(),
                    "imageString": this.selectedFile
                    //"zipCode": this.zipcodeInput
                };
                let minimumBid = Number(this.minimumBidInput);
                if (!isNaN(minimumBid)) { // add minimumbid field if it's a number
                    data.minimumBid = minimumBid;
                }

                Api.post('/auctions/ads/', data)
                    .then(() => {
                        console.log('Ad created');
                        this.titleInput = '';
                        this.descriptionInput = '';
                        this.minimumBidInput = 0;
                        this.bidEndTimeInput = '';
                        this.zipcodeInput = '';
                    })
                    .catch(err => console.log(err))
                 this.$router.push("/")
            }
        }
    }
</script>


<style lang="scss" scoped>
  @import './../../common.scss';

  .create-container{
    margin-top:10px;
    width:90%;
    text-align: center;
    height:100%;

  @include respond-to(wide) {
    width:500px;
  }
  @include respond-to(medium) {
    max-width:400px;
  }
  @include respond-to(phone) {
    max-width:300em;
  }
  }
  .card--header{
    text-align: center;
    width:100%;
  }

  img {
    max-width: 100%;
    max-height: 100%;
  }
</style>
