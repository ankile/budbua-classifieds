<template lang="html">
    <div class="user-profile__container">
        <sui-grid centered vertical-align="middle">
            <sui-grid-column>
                <h2 is="sui-header" color="blue" image>
                    <sui-header-content class="card--header">Rediger din brukerinformasjon</sui-header-content>
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
                        <sui-button v-on:click="submitUpdate" size="large" color="blue" fluid>Oppdater</sui-button>
                    </sui-segment>
                </sui-form>

                <sui-message>
                    <sui-button v-on:click="submitDelete" size="large" color="red" fluid>Slett din bruker</sui-button>
                </sui-message>
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
                emailInput: ''

            }
        },

        created(){
            User.getCurrentUser().then(res=>{
                this.firstNameInput=res.data.firstName;
                this.lastNameInput=res.data.lastName;
                this.emailInput=res.data.email;
            })
        },

        components: {
        },

        methods: {
            submitUpdate(e){
                e.preventDefault();
                User.updateUserInfo(this.emailInput,this.firstNameInput, this.firstNameInput).then(
                    alert("Profil oppdatert")
                )
            },

            submitDelete(e){
                e.preventDefault();
                User.deleteUser().then(
                    router.push("/")
                )
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
