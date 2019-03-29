<template>
    <div class="outer">

        <div class="inbox">
            <h2 is="sui-header" color="blue">
                <sui-header-content class="card--header">Meldinger</sui-header-content>
            </h2>
            <div :key="chat.id" v-for="chat in chats">
                <div class="inbox-box" :class="{active: currentChat.id===chat.id}"
                     v-on:click="boxClicked(chat.id)">
                    <h3 :class="{active: currentChat.id===chat.id}">{{chat.displayName||chat.id}}</h3>
                    <p>{{chat.message}}</p>
                    <p class="time">{{chat.updatedAt}}</p>
                </div>
            </div>
        </div>

        <div class="content">
            <div class="msg_history">
                <Message :key="msg.id" v-for="msg in currentChat.messages" v-bind:msg="msg"></Message>
            </div>
            <div class="type_msg">
                <div class="input_msg_write">
                    <input type="text" class="write_msg" v-model="currentInput" placeholder="Skriv en melding"/>
                    <button class="msg_send_btn" v-on:click="sendMessage" type="button">Send</button>
                </div>
            </div>
        </div>

    </div>
</template>


<script>
    import Message from "./Message";
    import {MessageApi} from "./../../api";
    import prettyTime from "./prettyTime"

    export default {
        name: "Messages",
        components: {Message},
        props: ["currentuserid"],
        methods: {
            boxClicked(id) {
                window.history.pushState("Navigated", "", "/messages?id="+id);
                MessageApi.getChat(id)
                    .then(messages => {
                        this.currentChat =
                            {
                                messages: messages.map((msg) => {
                                    return {...msg,
                                        type: (msg.sender === this.currentuserid) ? "out" : "in"
                                    }
                                }),
                                id: id
                            };
                        this.recieveMessage(id)
                    })
            },
            sendMessage(e){
                let id = new URL(window.location).searchParams.get("id");
                let message=this.currentInput;
                let createdAt=new Date();
                MessageApi.sendMessage(id, message, createdAt);
                this.currentInput="";
                this.currentChat.messages.push({id,message,createdAt,from:this.currentuserid, type:"out"})
            },
            recieveMessage(id){

                    window.clearInterval(this.interval_id);

                this.interval_id=setInterval(()=>{
                    MessageApi.fetchMessagesFromChat(id)
                        .then(msgs=>{
                            this.currentChat =
                                {
                                    messages: msgs.map((msg) => {
                                        return {...msg,
                                            type: (msg.sender === this.currentuserid) ? "out" : "in"
                                        }
                                    }),
                                    id: id
                                };

                        })
                }, 2000);
            }

        },
        created() {
            MessageApi.getAllChats()
                .then(chats => {
                    let id = new URL(window.location).searchParams.get("id");
                    this.chats = chats.map(chat=>{
                        return({...chat,updatedAt: prettyTime.getPrettyTime(chat.updatedAt, true)})
                    });
                    if (id!=undefined) {
                        this.boxClicked(id)
                    } else {
                        id=this.chats[0].id
                        this.boxClicked(id)
                    }
                    this.recieveMessage(id)

                })

        },
        data() {
            return {
                currentInput:"",
                currentChat: {},
                chats: [],
                interval_id:null

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

    .card--header {
        text-align: center;
        width: 100%;
        background: none !important;
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
        /*height: 20px;
        position: absolute;
        width: 40px;
        top: 5px;
        right: 5px;*/
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

