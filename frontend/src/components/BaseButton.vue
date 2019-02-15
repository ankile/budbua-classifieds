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
       <slot />
    </button>

</template>

<script>

    export default{
        props:{
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

    .button--primary{
        background-color: $primary-dark;
        color:white;
    }
    .button-primary:active{
        background-color: $primary-light;
    }
    .button--small{
        width:160px;
        height:53px;
        border-radius: 5px;
        font-size:1.05em;
        font-family: gotham;
        z-index:100;
        outline:none;
    }
</style>
