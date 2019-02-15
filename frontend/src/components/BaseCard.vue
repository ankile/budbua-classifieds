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
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    }

</style>
