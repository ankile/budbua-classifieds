<!--

A styled card-component meant for wrapping other components.

-->


<template>

    <div class="card">
        <slot></slot> <!--en <slot> komponent lar deg sende andre komponenter som argumenter-->
    </div>

</template>

<script>

    export default {
        props: {
            variant:{
                type:String,
                default:'text-input--small'
            },
        },
    }

</script>

<style>

    .card{
        background-color:white;
        width:900px;
        border-radius: 5px;
        min-height:200px;
    }

</style>
