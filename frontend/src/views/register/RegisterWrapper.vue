<!--

This file wraps the Login.vue component

-->

<template>
    <div class="register-wrapper">
        <Register />
    </div>
</template>

<script>
    import Register from './Registrer'

    export default {
        components: {
            Register
        }

    }

</script>

<style lang="scss" scoped>
    @import './../../common.scss';

    .register-wrapper{
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
