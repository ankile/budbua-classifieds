<!--

This file wraps the CreateAd.vue component

-->

<template>
  <div class="create-wrapper">
    <CreateAd></CreateAd>
  </div>
</template>

<script>
    import CreateAd from "./CreateAd";

    export default {
        name: "CreateAdWrapper",
        components: {
            CreateAd
        }
    }
</script>

<style lang="scss" scoped>
  @import './../../common.scss';

  .create-wrapper{
    width: 100%;
    height: 100%;
    margin: 20px auto 10px auto;
    display: flex;
    justify-content: center;
    margin-top: 3vh;
    @include respond-to(wide) {
      max-width: 700px;
    }
    @include respond-to(medium) {
      max-width:75vw;
    }
    @include respond-to(phone) {
      max-width:95%;
    }


  }

</style>