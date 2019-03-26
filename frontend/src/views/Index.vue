<template>
    <div class="index">
        <keep-alive>
            <AdSearch :isloggedin="isloggedin" v-on:ad-search="adSearch"></AdSearch>@
        </keep-alive>
        <Ad v-bind:ads="ads"></Ad>
    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import AdSearch from './ad/AdSearch'
    import {Api, User} from "../api";


    export default {
        name: "Index",
        components: {
            Ad,
            AdSearch
        },
        data() {
            return {
                ads: [],
                "isloggedin":false
            }
        },
        created() {
            Api.get('/auctions/ads/')
                    .then(res => this.ads = res.data
                    )
                    .catch((err) => {
                        if(err.response.status === 401) {
                            localStorage.removeItem("token")
                            location.reload();
                        }
                    } );
           User.isLoggedIn()
               .then(()=>{
                   this['isloggedin']=true
               })
        },
        methods: {
            adSearch(params) {
                Api.get('/auctions/ads/?search='+params.query+'&filter='+params.filter)
                        .then(res => this.ads = res.data)
                        .catch(() => {
                        });
            },

        }
    }

</script>

<style scoped>
    .index {
        height: 100%;
    }

</style>
