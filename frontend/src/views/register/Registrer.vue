<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template>
    <div class="login-container">
        <BaseCard class="card__login">

            <template slot="header"> <!--TODO: legg card-header inn i selve card komponenten -->
                Registrer deg på Budbua!
            </template>

            <template>
                <div class="login__input">
                    <BaseInput_Text
                            v-model="usernameInput"
                            v-bind:variant="'text-input--large'"
                            v-bind:placeholder="'Brukernavn'"
                            class="text-input__login"
                    />
                    <BaseInput_Text
                            v-model="emailInput"
                            v-bind:variant="'text-input--large'"
                            v-bind:placeholder="'Email'"
                            class="text-input__login"
                    />
                    <BaseInput_Text
                            v-model="passwordInput"
                            v-bind:variant="'text-input--large'"
                            v-bind:placeholder="'Passord'"
                            class="text-input__login"
                    />
                </div>
                <div class="login__footer">
                    <BaseButton
                            v-bind:variant="'button--small button--primary'"
                            class="footer__button"
                    >
                        Register deg
                    </BaseButton>

                    <BaseLink to="/login" class="footer__link">
                        Logg inn
                    </BaseLink>
                </div>
            </template>

        </BaseCard>

    </div>
</template>

<script>
    import BaseInput_Text from "../../components/BaseInput_Text";
    import BaseButton from "../../components/BaseButton";
    import BaseCard from "../../components/BaseCard";
    import BaseLink from "../../components/BaseLink";

    export default {

        data() {
            return {
                usernameInput: '',
                emailInput: '',
                passwordInput: ''
            }
        },

        components: {
            BaseInput_Text,
            BaseButton,
            BaseCard,
            BaseLink
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
