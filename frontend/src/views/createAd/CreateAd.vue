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
            <sui-form-field required>
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
            <sui-form-field>
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
            <sui-form-field>
              <sui-input
                      type="text"
                      placeholder="Postkode"
                      v-model="zipcodeInput"
                      icon="map marker alternate"
                      icon-position="left" />
            </sui-form-field>
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
   Date.prototype.toDatetimeLocal =
  function toDatetimeLocal() {
    var
      date = this,
      ten = function (i) {
        return (i < 10 ? '0' : '') + i;
      },
      YYYY = date.getFullYear(),
      MM = ten(date.getMonth() + 1),
      DD = ten(date.getDate()),
      HH = ten(date.getHours()),
      II = ten(date.getMinutes())
    ;
    return YYYY + '-' + MM + '-' + DD + 'T' +
             HH + ':' + II;
  };


    export default {
        name: "CreateAd",
        data() {

            var today = new Date();
            today.setHours(today.getHours() + 2);

            return {
                titleInput: '',
                descriptionInput: '',
                bidEndTimeInput: today.toDatetimeLocal(),
                minimumBidInput: 100,
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
                    .catch(() => {});
            },

            submitAd(e) {
                e.preventDefault();
                let data = {
                    "title": this.titleInput,
                    "description": this.descriptionInput,
                    "bidEndTime": new Date(this.bidEndTimeInput).toISOString(),
                    "imageString": this.selectedFile
                };
                let minimumBid = Number(this.minimumBidInput);
                if (!isNaN(minimumBid)) { // add minimumbid field if it's a number
                    data.minimumBid = minimumBid;
                }
                if(this.zipcodeInput !== '') {
                    data.zipCode = this.zipcodeInput;
                }

                let errormsg = "";
                if(data.title === '' || data.description == undefined) {
                    errormsg = "Du må ha tittel på annonsen\n"
                }
                if(data.description === '' || data.description == undefined) {
                    errormsg += "Du må ha en beskrivelse i annonsen\n"
                }

                if(errormsg !== ""){
                    alert(errormsg)
                }
                else {
                    Api.post('/auctions/ads/', data)
                        .then(() => {
                            this.titleInput = '';
                            this.descriptionInput = '';
                            this.minimumBidInput = 0;
                            this.bidEndTimeInput = '';
                            this.zipcodeInput = '';
                            this.$router.push("/")
                        })
                        .catch(()=> {
                            alert("Woops, her er det noe trøbbel. Prøv igjen senere. ")
                        })
                }

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
