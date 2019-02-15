<!--

This file wraps the Register.vue and Login.vue components into a single view.

-->

<template>
    <div class="authWrapper-container">
        <Login />
    </div>
</template>

<script>
   import Login from './Login'

    export default {

        data() {
            return {
                usernameInput: '',
                passwordInput: ''
            }
        },

        components: {
           Login
        }

    }

</script>

<style scoped>

.authWrapper-container{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    margin-top:100px;
}

</style>
