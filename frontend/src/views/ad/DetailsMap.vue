<template>
  <div class="mapouter">
      <div class="gmap_canvas">
        <iframe
                width="700"
                height="500"
                id="gmap_canvas"
                :src="'https://maps.google.com/maps?q=norge%20' + this.zipcode+ '&t=&z=13&ie=UTF8&iwloc=&output=embed'"
                frameborder="0"
                scrolling="no"
                marginheight="0"
                marginwidth="0">
        </iframe>
      </div>
  </div>
</template>

<script>
    export default {
        name: "DetailsMap",
        props: ["ad"],
        data() {
            return {
                zipcode: this.ad.zipCode
            }
        }
    }
</script>

<style scoped>
  .mapouter{
    text-align:right;

    margin-top: 2rem;
    margin-bottom: 2rem;

  }

  .gmap_canvas {
    overflow:hidden;
    background:none!important;
    height:500px;
    width:700px;
  }

</style>