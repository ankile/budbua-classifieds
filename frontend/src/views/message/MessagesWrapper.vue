<template>
  <div class="message-wrapper">
    <Messages v-bind:currentuserid="currentUserId"></Messages>
  </div>
</template>

<script>
    import Messages from './Messages'
    import {User} from './../../api'

    export default {
        name: "MessagesWrapper",
        components: {
            Messages
        },
        data(){
          return{
            currentUserId:null
          }
        },
        beforeMount() {
          User.getCurrentUser()
                  .then(user=>{
                    this.currentUserId=user.data.id
                  })
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
