<!--

This file wraps the Analytics.vue component

-->

<template>
    <div class="analytics-wrapper">
        <Analytics />
    </div>
</template>

<script>
    import Analytics from './Analytics'

    export default {
        components: {
            Analytics
        }

    }

</script>

<style lang="scss" scoped>
    @import './../../common.scss';

    .analytics-wrapper {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        margin: 3vh auto 10px;
        @include respond-to(wide) {
            max-width: 1000px;
        }
        @include respond-to(medium) {
            max-width:75vw;
        }
        @include respond-to(phone) {
            max-width:95%;
        }
    }

</style>
