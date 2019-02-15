<template>
    <div class="index">
       <authWrapper></authWrapper>
    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import AdSearch from './ad/AdSearch'
    import axios from 'axios';
    import authWrapper from './auth/authWrapper'

    export default {
        name: "Index",
        components: {
            authWrapper
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
    }

</style>
