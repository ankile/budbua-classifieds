<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template lang="html">
    <div class="background">
        <sui-grid centered vertical-align="middle">
            <sui-grid-column>

                <h2 is="sui-header" color="blue" image>

                    <sui-header-content>Log-in to your account</sui-header-content>
                </h2>

                <sui-form>
                    <sui-segment stacked>
                        <sui-form-field>
                            <sui-input
                                    type="email"
                                    placeholder="E-mail address"
                                    icon="user"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-form-field>
                            <sui-input
                                    type="password"
                                    placeholder="Password"
                                    icon="lock"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-button size="large" color="blue" fluid>Login</sui-button>
                    </sui-segment>
                </sui-form>

                <sui-message>New to us? <router-link to="/register">Register</router-link></sui-message>
            </sui-grid-column>
        </sui-grid>
    </div>
</template>

<script>

    export default {

        data() {
            return {
                usernameInput: '',
                passwordInput: ''
            }
        },

        components: {
        },

        methods: {
            submitLogin() {


            }

        }

    }

</script>

<style lang="scss" scoped>

    .login-container{
        width:100%;
        height:100%;
    }

    .login__input{

    }
    .text-input__login{
        margin:0 0 25px 0;
    }

    .login__footer{
        margin:20px 0 20px 0;
        display: grid;
        grid-template-columns: auto;
        grid-gap: 20px;
        justify-items: center;

    }

</style>
