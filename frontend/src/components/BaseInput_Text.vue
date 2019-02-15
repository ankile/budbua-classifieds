<!--

This is a already styled, reusable text-input field.

It accepts the props:
    value - the current text shown
    variant - the wanted styling, will be set as the buttons class
    placeholder - the wanted placeholder for the field


currently the following variants are accepted:
    text-input--small
    text-input--large


TODO: add support for different types of input, preventing having multiple files for inputs
-->

<template>
    <input
            type="text"
            :class="variant"
            :value="value"
            :placeholder="placeholder"
            v-on="listeners"
    >
</template>

<script>
    export default {
        props: {
            value: {
                type: String,
                default: '',
            },
            variant:{
                type:String,
                default:'text-input'
            },
            placeholder:{
                type:String,
                default:''
            }
        },
        computed: {
            listeners () {
                return {
                    ...this.$listeners,
                    input: event => this.$emit('input', event.target.value)
                }
            }
        }

    }
</script>

<style scoped>
    .text-input{
        border-radius: 5px;
    }
    .text-input--small{
        width:175px;
        height:40px;
        border-radius: 5px;
        border:1px solid #8f8f8f;
        padding:5px;
        font-size:1em;
        outline:none;
        -webkit-appearance: none;
    }

    .text-input--large{
        width:500px;
        height:50px;
        border-radius: 5px;
        border:1px solid #8f8f8f;
        padding:10px;
        font-size:1em;
        outline:none;
        -webkit-appearance: none;

    }
</style>
