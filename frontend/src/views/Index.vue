<template>
    <div class="index">
    <AdSearch v-on:ad-search="adSearch"></AdSearch>
    <Ad v-bind:ads="ads"></Ad>
    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import AdSearch from './ad/AdSearch'
    import {Api} from "../api";


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
            Api.get('/auctions/ads/')
                    .then(res => this.ads = res.data
                    )
                    .catch((err) => {
                        if(err.response.status == 401) {
                            localStorage.removeItem("token")
                            location.reload();
                            console.log("ok")
                        }
                    } );
        },
        methods: {
            adSearch(query) {
                console.log("search!!" + query);
                Api.get('/auctions/ads/?search='+query)
                        .then(res => this.ads = res.data)
                        .catch(() => {
                        });
            }
        }
    }

</script>

<style scoped>
    .index {
        height: 100%;
    }

</style>
