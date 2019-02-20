<!--

Styled default link component

-->

<template>
    <router-link :to="to" v-on="listeners" :class="variant">
        <slot/>
    </router-link>
</template>

<script>
    export default {
        props:{
            variant:{
                type:String,
                default:'link'
            },
            to:{
                type:String,
                default:'/'
            }
        },
        computed: {
            listeners() {
                return {
                    ...this.$listeners,
                    input: event => this.$emit('link', event.target.value)
                }
            }
        }
    }

</script>
<style lang="scss" scoped>
    @import './../common.scss';

    .link {
        color: $primary;
        text-underline:$primary;
        text-decoration-color: $primary;
    }
</style>
