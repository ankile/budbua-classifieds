<template>
    <div class="index">
    <AdSearch></AdSearch>
    <Ad></Ad>
    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import AdSearch from './ad/AdSearch'

    export default {
        name: "Index",
        components: {
            Ad,
            AdSearch

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
