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
        {{this.text}}
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
