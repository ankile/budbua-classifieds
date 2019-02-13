<template>
  <div id="singleblog">
    <h1>{{ad.title}}</h1>
    <article>{{ad.body}}</article>
  </div>
</template>


<script>
    import axios from "axios";

    export default {
        name: "Details",
        data() {
            return {
                id: this.$route.params.id,
                ad: {}
            }
        },
        created() {
            axios.get('https://jsonplaceholder.typicode.com/posts/' + this.id)
                .then(res => this.ad = res.data)
                .catch(err => console.log(err));
        }
    }
</script>


<style scoped>
  #singleblog {
    max-width: 700px;
    margin: 0 auto;
    text-align: left;
  }
</style>