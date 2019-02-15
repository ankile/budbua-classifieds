<!--

This component contains logic, styling and structure for a user to log into their existing account on the site.

Components used:
    - Input_Text

-->

<template>
    <div class="login-container">
        <Card class="login-card">
            <div class="card-header"> <!--TODO: legg card-header inn i selve card komponenten -->
                Logg deg inn på Budbua!
            </div>
            <div class="input-group">
                <Input_Text
                        v-model="usernameInput"
                        v-bind:variant="'text-input--large'"
                        v-bind:placeholder="'Skriv ditt brukernavn'"
                        class="input"
                />

                <Input_Text
                        v-model="passwordInput"
                        v-bind:variant="'text-input--large'"
                        v-bind:placeholder="'Skriv ditt passord'"
                        class="input"
                />
            </div>

            <div class="input-group">
                <Button
                        v-bind:variant="'button--small'"
                        v-bind:text="'Logg inn'">

                </Button>
            </div>

        </Card>

    </div>
</template>

<script>
    import Input_Text from "../../components/Input_Text";
    import Button from "../../components/Button";
    import Card from "../../components/Card";

    export default {

        data() {
            return {
                usernameInput: '',
                passwordInput: ''
            }
        },

        components: {
            Input_Text,
            Button,
            Card
        },

        methods: {
            submitLogin() {

            }

        }

    }

</script>

<style scoped>

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
