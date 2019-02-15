<!--

This is a already styled, default button component

It accepts the props:
    text - the current text of the button
    variant - the wanted styling, will be set as the buttons class

currently the following variants are accepted:
    button--small
    button--large

-->

<template>

    <button
            v-on="listeners"
            :class="variant"
    >
        {{text}}
    </button>

</template>

<script>

    export default{
        props:{
            text:{
                type:String,
                default:''
            },
            variant:{
                type:String,
                default:'button--small'
            }
        },

        computed: {
            listeners () {
                return {
                    ...this.$listeners,
                    input: event => this.$emit('button', event.target.value)
                }
            }
        }
    }

</script>

<style lang="scss" scoped>
    @import './../common.scss';

    .button--small{
        width:150px;
        border: 2px solid black;
        height:50px;
        border-radius: 5px;
        font-size:1em;
        font-family: gotham;
        z-index:100;
        outline:none;
    }
    .primary{
        border: 2px solid $primary !important;
    }
    .primary:active{
        background-color: $primary-light;
    }
</style>
