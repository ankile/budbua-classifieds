<!--

Styled default link component

-->

<template>
    <a v-on="listeners" :class="variant">
        <slot/>
    </a>
</template>

<script>
    export default {
        props:{
            variant:{
                type:String,
                default:'link'
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
        text-decoration:underline;
        text-decoration-color: $primary;
    }
</style>
