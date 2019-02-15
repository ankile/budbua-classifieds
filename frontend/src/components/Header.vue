<template>
    <header class="header">
    <h1>Budbua AS</h1>
    <div id="nav">
        <router-link to="/">Hjem</router-link>  |
        <router-link to="/about">Om Oss</router-link>
    </div>
    </header>
</template>


<script>
    export default {
        name: "Header"
    }
</script>


<style scoped>
    .header {
        background: #333;
        color: white;
        text-align: center;
        padding: 10px;
    }

    .header a {
        color: white;
        padding-right: 5px;
        text-decoration: none;
    }

</style>