<template>
    <header class="header">
    <h1>Budbua AS</h1>
    <div id="nav">
        <router-link to="/">Hjem</router-link>  |
        <router-link to="/about">Om Oss</router-link>  |
        <router-link to="/create">Lag annonse</router-link>
    </div>
    </header>
</template>


<script>
    export default {
        name: "Header"
    }
</script>


<style lang="scss" scoped>
    @import './../common.scss';

    .header {
        background-color: white !important;
        color: white;
        text-align: center;
        padding: 10px;
    }

    .header a {
        color: white;
        padding-right: 5px;
        text-decoration: none;
    }
    #nav{
        background-color: white !important;
    }

</style>
