<template>
    <div class="index">

    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import AdSearch from './ad/AdSearch'
    import axios from 'axios';

    export default {
        name: "Index",
        components: {

        },
        data() {
            return {
                ads: []
            }
        },
        created() {
            axios.get('https://jsonplaceholder.typicode.com/posts?_limit=10')
                .then(res => this.ads = res.data)
                .catch(err => console.log(err));
        }
    }

</script>

<style scoped>
    .index {
        height: 100vh;
        width:100vw;
    }

</style>
