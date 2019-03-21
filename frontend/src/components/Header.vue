<template>

    <div class="header">
        <sui-menu class="menuH" pointing secondary>
            <a href="/">
                 <img class="headerimg" src="./../assets/budbua_text.png" />
            </a>
            <sui-menu-menu position="right">
                <a
                        is="sui-menu-item"
                        v-for="item in items"
                        :active="isActive(item)"
                        :key="item"
                        :content="item"
                        @click="select(item)"
                />
            </sui-menu-menu>
            <img class="logoheader" src="./../assets/logo_trans.png" />
        </sui-menu>

    </div>
</template>


<script>
    import SuiHeader from "semantic-ui-vue/dist/commonjs/elements/Header/Header";
    import SuiTab from "semantic-ui-vue/dist/commonjs/modules/Tab/Tab";
    import router from  './../router'
    import {User} from './../api'
    import budbua from './../assets/budbua_text.png'

    export default {
        name: "Header",
        components: {SuiTab, SuiHeader},
        state:{

        },
        data() {
            return {items: ['Registrer', 'Login']}
        },
        created(){
            User.isLoggedIn().then(()=>{
                this.items=['Lag annonse', 'Meldinger', "Profil", 'Logg ut']
            })
        },
        methods: {

            isActive(name) {
                return this.active === name;
            },
            select(name) {
                        switch(name){
                            case "Login":
                                router.push("/login");
                                break;
                            case "Registrer":
                                router.push("/register");
                                break;
                            case "Lag annonse":
                                router.push("/create");
                                break;
                            case "Meldinger":
                                router.push("/messages");
                                break;
                            case "Profil":
                                router.push("/profile");
                                break;
                            case "Logg ut":
                                localStorage.removeItem("token")
                                this.$router.push("/")
                                document.location.reload()
                                break;

                        }
            },
        },
    }

</script>


<style lang="scss" scoped>
    @import './../common.scss';

    .header{
        margin-bottom:30px;
        background-color: white;
    }

    .menu__header{
       font-weight: bold;
    }
    .menuH{
        max-height: 40px;
    }
    .headerimg {
        max-width: 142px;
    }
    .logoheader {
        max-width: 40px;
        max-width: 40px;
    }

</style>
