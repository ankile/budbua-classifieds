<template>
  <div class="outgoing_msg">
    <div class="sent_msg">
      <p>Test which is a new approach to have all
        solutions</p>
      <span class="time_date">{{timeDate}}</span>
    </div>
  </div>
</template>

<script>
    import prettyTime from "./prettyTime";

    export default {
        name: "OutgoingMessage",
        data() {
            return {
                timeDate: prettyTime.getPrettyTime(new Date())
            }
        }
    }
</script>

<style scoped>
  .outgoing_msg{
    overflow:hidden;
    margin:26px 0 26px;
  }

  .sent_msg {
    float: right;
    width:55%;
    text-align: left;
  }

  .sent_msg p {
    background: #1E639C none repeat scroll 0 0;
    border-radius: 3px;
    font-size: 14px;
    margin: 0;
    color:#fff;
    padding: 5px 10px 5px 12px;
    width:100%;

  }

  .time_date {
    color: #747474;
    display: block;
    font-size: 12px;
    margin: 8px 0 0;
  }
</style>