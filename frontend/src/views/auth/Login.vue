<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template>
    <div>
        <Input_Text
                v-model="usernameInput"
                v-bind:variant="'text-input--large'"
                v-bind:placeholder="'Skriv ditt brukernavn'"
        />

        <Input_Text
                v-model="passwordInput"
                v-bind:variant="'text-input--large'"
                v-bind:placeholder="'Skriv ditt passord'"
        />
        <Button
        v-bind:variant="'button--small'"
        v-bind:text="'Logg inn'">
            </Button>

    </div>
</template>

<script>
    import Input_Text from "../../components/Input_Text";
    import Button from "../../components/Button";

    export default {

        data() {
            return {
                usernameInput: '',
                passwordInput: ''
            }
        },

        components: {
            Input_Text,
            Button
        },

        methods: {
            submitLogin() {

            }

        }

    }

</script>

<style lang="scss" scoped>

</style>
