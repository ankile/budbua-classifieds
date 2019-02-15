<!--

This component contains logic, styling and structure for registering a new, basic privileged, user on the site.

-->

<template>
    <div class="reg-container">
        <BaseCard class="card__reg">

            <template slot="header"> <!--TODO: legg card-header inn i selve card komponenten -->
                Logg deg inn på Budbua!
            </template>

            <template>
                <div class="reg__input">
                    <BaseInput_Text
                            v-model="usernameInput"
                            v-bind:variant="'text-input--large'"
                            v-bind:placeholder="'Skriv ditt brukernavn'"
                            class="text-input__reg"
                    />

                    <BaseInput_Text
                            v-model="passwordInput"
                            v-bind:variant="'text-input--large'"
                            v-bind:placeholder="'Skriv ditt passord'"
                            class="text-input__reg"
                    />
                </div>
                <div class="reg__footer">
                    <BaseButton
                            v-bind:variant="'button--small button--primary'"
                            class="footer__button"
                            v-on="submitRegister"
                    >
                        Register deg
                    </BaseButton>

                    <BaseLink class="footer__link">
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
