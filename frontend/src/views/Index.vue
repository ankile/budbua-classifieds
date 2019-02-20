<template>
    <div class="index">
        <AdSearch></AdSearch>
        <Ad></Ad>
    </div>
</template>


<script>
    import Ad from './ad/Ad'
    import AdSearch from './ad/AdSearch'

    export default {
        name: "Index",
        components: {
            Ad,
            AdSearch
        }
    }

</script>

<style scoped>
    .index {
        height: 100%;
    }

</style>
