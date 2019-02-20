<!--

This file wraps the Login.vue component

-->

<template>
    <div class="login-wrapper">
        <Login />
    </div>
</template>

<script>
    import Login from './Login'

    export default {
        components: {
            Login
        }

    }

</script>

<style lang="scss" scoped>
    @import './../../common.scss';

    .login-wrapper{
        width: 100%;
        height: 100%;
        margin:20px auto 10px auto;
        display: flex;
        justify-content: center;
        margin-top:3vh;
        @include respond-to(wide) {
            max-width: 700px;
        }
        @include respond-to(medium) {
            max-width:75vw;
        }
        @include respond-to(phone) {
            max-width:95%;
        }


    }

</style>
