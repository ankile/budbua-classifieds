<template>

    <div class="header">
        <sui-menu pointing secondary>

            <sui-menu-item>
                <p class="menu__header">BudBua</p>
            </sui-menu-item>

            <sui-menu-menu position="right">
                <router-link is="sui-menu-item" to="/">Hjem</router-link>
                <router-link is="sui-menu-item" to="/login">Login</router-link>
            </sui-menu-menu>
        </sui-menu>

    </div>
</template>


<script>
    import SuiHeader from "semantic-ui-vue/dist/commonjs/elements/Header/Header";
    import SuiTab from "semantic-ui-vue/dist/commonjs/modules/Tab/Tab";
    export default {
        name: "Header",
        components: {SuiTab, SuiHeader}
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
