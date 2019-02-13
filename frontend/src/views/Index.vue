<template>
    <div class="index">
        <Ad v-bind:ads="ads"></Ad>
    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import axios from 'axios';

    export default {
        name: "Index",
        components: {
            Ad
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
