<template>

    <div class="header">
        <sui-menu pointing secondary>

            <sui-menu-item>
                <router-link to="/" class="menu__header">BudBua</router-link>
            </sui-menu-item>

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
        </sui-menu>

    </div>
</template>


<script>
    import SuiHeader from "semantic-ui-vue/dist/commonjs/elements/Header/Header";
    import SuiTab from "semantic-ui-vue/dist/commonjs/modules/Tab/Tab";
    import router from  './../router'
    import {User} from './../api'

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
                this.items=['Lag annonse', "Profil", 'Logg ut']
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

</style>
