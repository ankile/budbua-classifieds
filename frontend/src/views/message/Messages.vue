<template>
  <div class="outer">

    <div class="inbox">
      <div :key="message.userId" v-for="message in allMessages">
        <div class="inbox-box" :class="{active: message.isActive}" v-on:click="boxClicked(message.userId)">
          <h3 :class="{active: message.isActive}">{{message.name}}</h3>
          <p>{{message.latestMessage}}</p>
        </div>
      </div>
    </div>

    <div class="content">
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus asperiores, aspernatur consectetur dicta doloremque dolores eaque est excepturi facere illum in itaque magnam maxime minima mollitia nam omnis perspiciatis praesentium quidem rem repellendus reprehenderit sed tempore tenetur veniam vero voluptas?</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut earum officiis quisquam sapiente temporibus. Animi assumenda atque blanditiis delectus eos nostrum odio quaerat recusandae suscipit ut? Ab alias aut cumque deserunt dolorem dolores doloribus, ducimus facilis fugit illo ipsam iste laboriosam modi necessitatibus, non nulla officia officiis perspiciatis quos recusandae sapiente, sequi similique sint sit veritatis voluptatem voluptatibus? Alias at consequatur deleniti distinctio ducimus enim eos, esse fugit hic impedit iure laboriosam maiores molestiae nam nemo numquam officia officiis qui ratione rerum sapiente sequi sunt voluptate. Ab consequuntur, doloremque expedita explicabo ipsa, iure nemo praesentium quae, quia quis repellat sit?</p>
    </div>

  </div>
</template>

<script>
    export default {
        name: "Messages",
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
                      isActive: false
                    },
                    {
                        userId: 3,
                        name: 'Ivar Myrstad',
                        latestMessage: 'Ka, ka, ka, ka e det som skjer?',
                        isActive: true
                    },
                    {
                        userId: 4,
                        name: 'Postman Pat',
                        latestMessage: 'Jeg har en svart og hvit katt',
                        isActive: false
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

  .outer {
    height: 75vh;
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
  }

  .inbox-box:hover {
    background: white;
    cursor: pointer;
  }

  .active {
    background: white;

  }

  .content {
    overflow-y: auto;
    overflow-x: hidden;
    background: white;
    padding-left: 10px;

  }
</style>

