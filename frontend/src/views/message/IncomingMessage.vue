<template>
  <div class="incoming_msg">
    <div class="received_msg">
      <p>Test which is a new approach to have all
        solutions</p>
      <span class="time_date">{{dateTime}}</span>
    </div>
  </div>
</template>

<script>
    import prettyTime from "./prettyTime";

    export default {
        name: "ReceivedMessage",
        data() {
            return {
                dateTime: prettyTime.getPrettyTime(new Date(), true)
            }
        }
    }
</script>

<style scoped>
  .incoming_msg {
    margin:26px 0 26px;
    overflow: hidden;
    width: 92%;
  }

  .received_msg {
    float: left;
    width: 55%;
    text-align: left;
  }

  .received_msg p {
    background: #ebebeb none repeat scroll 0 0;
    border-radius: 3px;
    color: #646464;
    font-size: 14px;
    margin: 0;
    padding: 5px 10px 5px 12px;
    width: 100%;
  }

  .time_date {
    color: #747474;
    display: block;
    font-size: 12px;
    margin: 8px 0 0;
  }
</style>