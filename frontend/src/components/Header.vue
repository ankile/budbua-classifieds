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

    export default {
        name: "Header",
        components: {SuiTab, SuiHeader},
        data() {
            return {
                active: 'Hjem',
                items: ['Login'],
            };
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
                    case "Hjem":
                        router.push("/");
                }
            },
        },
    }

</script>


<style lang="scss" scoped>
    @import './../common.scss';

    .header{
        margin-bottom:30px;
    }

    .menu__header{
       font-weight: bold;
    }

</style>
