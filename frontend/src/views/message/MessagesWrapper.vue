<template>
  <div class="message-wrapper">
    <Messages></Messages>
  </div>
</template>

<script>
    import Messages from './Messages'

    export default {
        name: "MessagesWrapper",
        components: {
            Messages
        }
    }
</script>


<style lang="scss" scoped>
  @import './../../common.scss';

  .message-wrapper{
    width: 100%;
    height: 100%;
    margin:20px auto 10px auto;
    margin-top:3vh;
    @include respond-to(wide) {
      max-width: 900px;
    }
    @include respond-to(medium) {
      max-width:75vw;
    }
    @include respond-to(phone) {
      max-width:95%;
    }

  }

</style>