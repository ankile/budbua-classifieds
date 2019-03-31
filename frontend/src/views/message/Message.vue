



<template>
    <div class="msg">
        <div class="msg__container" v-bind:class="{'msg__type--in':msg.type=='in', 'msg__type--out':msg.type=='out'}">
            <p class="msg__text">{{msg.message}}</p>
            <span class="msg__timestamp">{{timeDate}}</span>
        </div>
    </div>
</template>

<script>
    import prettyTime from "./prettyTime";
    export default {
        props:["msg"],
        name: "Message",
        data() {
            return {
                timeDate: ""
            }
        },
        created() {
            console.log(this.msg.message+"     "+this.msg.createdAt)
           this.timeDate= prettyTime.getPrettyTime(this.msg.createdAt, true)
        }
    }
</script>

<style scoped>
    .msg{
        overflow:hidden;
        margin:26px 0 26px;
    }

    .msg__container {
        float: right;
        width:55%;
        text-align: left;
    }

    .msg__text {
        overflow-wrap: break-word;
    }

    .msg__timestamp {
        color: #747474;
        display: block;
        font-size: 12px;
        margin: 8px 0 0;
    }

    .msg__type--in{
        float: left;
        width: 55%;
        text-align: left;
    }
    .msg__type--in .msg__text{
        background: #ebebeb none repeat scroll 0 0;
        border-radius: 3px;
        color: #646464;
        font-size: 14px;
        margin: 0;
        padding: 5px 10px 5px 12px;
        width: 100%;
    }

    .msg__type--out{
        float: right;
        width:55%;
        text-align: left;
    }
    .msg__type--out .msg__text{
        background: #1E639C none repeat scroll 0 0;
        border-radius: 3px;
        font-size: 14px;
        margin: 0;
        color:#fff;
        padding: 5px 10px 5px 12px;
        width:100%;
    }
</style>
