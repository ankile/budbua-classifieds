<template>
  <div class="outer">

    <div class="inbox">
      <h2 is="sui-header" color="blue">
        <sui-header-content class="card--header">Meldinger</sui-header-content>
      </h2>
      <div :key="message.userId" v-for="message in allMessages">
        <div class="inbox-box" :class="{active: message.isActive}" v-on:click="boxClicked(message.userId)">
          <h3 :class="{active: message.isActive}">{{message.name}}</h3>
          <p>{{message.latestMessage}}</p>
          <p class="time">{{message.dateTime}}</p>
        </div>
      </div>
    </div>

    <div class="content">
      <div class="msg_history">
        <OutgoingMessage></OutgoingMessage>
        <IncomingMessage></IncomingMessage>
        <IncomingMessage></IncomingMessage>
        <OutgoingMessage></OutgoingMessage>
        <OutgoingMessage></OutgoingMessage>
        <IncomingMessage></IncomingMessage>
        <IncomingMessage></IncomingMessage>
        <OutgoingMessage></OutgoingMessage>
      </div>
      <div class="type_msg">
        <div class="input_msg_write">
          <input type="text" class="write_msg" placeholder="Skriv en melding" />
          <button class="msg_send_btn" type="button">Send</button>
        </div>
      </div>
    </div>

  </div>
</template>


<script>
    import OutgoingMessage from "./OutgoingMessage";
    import IncomingMessage from "./IncomingMessage"
    import prettyTime from "./prettyTime";

    export default {
        name: "Messages",
        components: {OutgoingMessage, IncomingMessage},
        methods: {
            boxClicked(userId) {
                console.log(userId);
                this.allMessages.forEach((message) => {
                    message.isActive = message.userId === userId;
                })
            }
        },
        data() {
            return {
                allMessages: [ //temoprary, waiting for api
                    {
                      userId: 1,
                      name: 'Jo Nesbø',
                      latestMessage: 'Passer det å møtes i morgen kl 12?',
                      isActive: true,
                      dateTime: prettyTime.getPrettyTime(new Date(), false)
                    },
                    {
                        userId: 3,
                        name: 'Ivar Myrstad',
                        latestMessage: 'Ka, ka, ka, ka e det som skjer?',
                        isActive: false,
                        dateTime: prettyTime.getPrettyTime(new Date(), false)
                    },
                    {
                        userId: 4,
                        name: 'Postman Pat',
                        latestMessage: 'Jeg har en svart og hvit katt',
                        isActive: false,
                        dateTime: prettyTime.getPrettyTime(new Date(), false)
                    }
                ],

            }
        }
    }
</script>


<style scoped>
  h3 {
    margin: 0;
    text-align: left;
  }

  p {
    text-align: left;
  }

  .card--header{
    text-align: center;
    width:100%;
    background: none!important;
  }

  .outer {
    height: 85vh;
    display: grid;
    grid-template-columns: 1fr 2fr;

  }

  .inbox {
    overflow-y: auto;
    overflow-x: hidden;
    padding-right: 10px;
  }

  .inbox-box {
    padding: 5px;
    position: relative;
  }

  .time {
    height: 20px;
    position: absolute;
    width: 40px;
    top: 5px;
    right: 5px;

  }

  .inbox-box:hover {
    background: white;
    cursor: pointer;
  }

  .active {
    background: white;

  }

  .content {
    overflow: hidden;
    background: white;
  }

  .msg_history {
    height: calc(85vh - 48px);
    overflow-y: auto;
    padding-left: 10px;
    padding-right: 10px;
  }

  .type_msg {
    border-top: 1px solid #c4c4c4;
    position: relative;
    padding-left: 10px;
    padding-right: 10px;
  }

  .input_msg_write input {
    background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
    border: medium none;
    color: #4c4c4c;
    font-size: 15px;
    min-height: 48px;
    width: 86%;
    float: left;

  }

  .input_msg_write input:focus {
    outline-width: 0;
  }


  .msg_send_btn {
    background: #1E639C none repeat scroll 0 0;
    border: medium none;
    border-radius: 3px;
    color: #fff;
    cursor: pointer;
    font-size: 17px;
    height: 33px;
    position: absolute;
    right: 10px;
    top: 8px;
    width: 70px;
  }
</style>

