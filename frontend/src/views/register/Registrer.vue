<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template lang="html">
    <div class="register-container">
        <sui-grid centered vertical-align="middle">
            <sui-grid-column>

                <h2 is="sui-header" color="blue" image>

                    <sui-header-content class="card--header">Log-in to your account</sui-header-content>
                </h2>

                <sui-form>
                    <sui-segment >
                        <sui-form-field>
                            <sui-input
                                    type="text"
                                    placeholder="Fornavn"
                                    icon="user"
                                    v-model="firstNameInput"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-form-field>
                            <sui-input
                                    type="text"
                                    placeholder="Etternavn"
                                    v-model="lastNameInput"
                                    icon="user"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-form-field>
                            <sui-input
                                    type="email"
                                    placeholder="Email"
                                    icon="mail"
                                    v-model="emailInput"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-divider />
                        <sui-form-field>
                            <sui-input
                                    type="password"
                                    placeholder="Passord"
                                    v-model="passwordInput"
                                    icon="lock"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-form-field>
                            <sui-input
                                    type="password"
                                    placeholder="Gjenta passord"
                                    v-model="password2Input"
                                    icon="lock"
                                    icon-position="left" />
                        </sui-form-field>
                        <sui-button v-on:click="submitRegister" size="large" color="blue" fluid>Registrer</sui-button>
                    </sui-segment>
                </sui-form>

                <sui-message>Eksisterende bruker? <router-link to="/login">Logg inn</router-link></sui-message>
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
                firstNameInput:'',
                lastNameInput:'',
                emailInput: '',
                passwordInput: '',
                password2Input:''

            }
        },

        components: {
        },

        methods: {
            submitRegister(e){
                e.preventDefault();
                User.register(
                    this.firstNameInput,
                    this.lastNameInput,
                    this.emailInput,
                    this.passwordInput,
                    this.password2Input)
                    .then(e=>router.push('/login'))
            }

        }

    }

</script>

<style lang="scss" scoped>
    @import './../../common.scss';

    .register-container{
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
