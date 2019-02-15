<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template>
    <div class="login-container">
        <BaseCard class="login-card">
            <div class="card-header"> <!--TODO: legg card-header inn i selve card komponenten -->
                Logg deg inn på Budbua!
            </div>
            <div class="input-group">
                <BaseInput_Text
                        v-model="usernameInput"
                        v-bind:variant="'text-input--large'"
                        v-bind:placeholder="'Skriv ditt brukernavn'"
                        class="input"
                />

                <BaseInput_Text
                        v-model="passwordInput"
                        v-bind:variant="'text-input--large'"
                        v-bind:placeholder="'Skriv ditt passord'"
                        class="input"
                />
            </div>

            <div class="input-group">
                <BaseButton
                        v-bind:variant="'button--small primary'"
                        v-bind:text="'Logg inn'">

                </BaseButton>
            </div>

        </BaseCard>

    </div>
</template>

<script>
    import BaseInput_Text from "../../components/BaseInput_Text";
    import BaseButton from "../../components/BaseButton";
    import BaseCard from "../../components/BaseCard";

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
            BaseCard
        },

        methods: {
            submitLogin() {

            }

        }

    }

</script>

<style lang="scss" scoped>

    .card-header{
        font-size:2em;

        border-bottom:1px solid #B7B7B7;
        padding:10px 0 25px 0;
        margin: 0 0 35px 0;
    }
    .login-card{
        padding:20px 0 20px 0;
    }
    .input{
        margin:10px;
    }
    button{
        margin:30px 0 10px 0; /*TODO: klasse her*/
    }
</style>
