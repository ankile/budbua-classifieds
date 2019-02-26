<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template lang="html">
    <div class="login-container">
        <sui-grid centered vertical-align="middle">
            <sui-grid-column>

                <h2 is="sui-header" color="blue" image>

                    <sui-header-content class="card--header">Logg inn på din brukerkonto</sui-header-content>
                </h2>

                <sui-form>
                    <sui-segment >
                        <sui-form-field>
                            <sui-input
                                    type="email"
                                    placeholder="Email"
                                    icon="user"
                                    v-model="emailInput"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-form-field>
                            <sui-input
                                    type="password"
                                    placeholder="Passord"
                                    v-model="passwordInput"
                                    icon="lock"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-button v-on:click="submitLogin" size="large" color="blue" fluid>Login</sui-button>
                    </sui-segment>
                </sui-form>

                <sui-message>Ny bruker? <router-link to="/register">Registrer</router-link></sui-message>
            </sui-grid-column>
        </sui-grid>
    </div>
</template>

<script>
    import {Api, User} from '../../api'
    import router from '../../router'

    export default {

        data() {
            return {
                emailInput: '',
                passwordInput: ''
            }
        },

        components: {
        },

        methods: {
            submitLogin(e){
                e.preventDefault();
                User.login(this.emailInput, this.passwordInput)
                    .then(e => {
                        router.push('/?login=true')
                        document.location.reload()
                    })
            }

        }

    }

</script>

<style lang="scss" scoped>
    @import './../../common.scss';

    .login-container{
        margin-top:10px;
        width:90%;
        text-align: center;
        height:100%;

        @include respond-to(wide) {
            width:500px;
        }
        @include respond-to(medium) {
            max-width:400px;
        }
        @include respond-to(phone) {
            max-width:300em;
        }
    }
    .card--header{
        text-align: center;
        width:100%;
    }
</style>
