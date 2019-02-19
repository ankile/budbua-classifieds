<!--

A styled card-component meant for wrapping other components.

-->


<template>

    <div class="card">
        <div class="card__header">

            <slot name="header" class="card__header"/>

        </div>


        <div class="card__body">

            <slot />

        </div>
    </div>

</template>

<script>

    export default {
        props: {
            variant: {
                type: String,
                default: 'text-input--small'
            },
        },
    }

</script>

<style lang="scss" scoped>
    @import './../common.scss';


    .card {
        background-color: white;
        width: 100%;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    }

    .card--small {
        width: 50%;
    }

    .card--medium {
        width: 70%;
    }

    .card--fill {
        width: 100%;
    }

    .card__header {
        font-size: 2em;
        border-bottom: 1px solid #B7B7B7;
        padding: 25px 0 25px 0;
        margin: 0 0 35px 0;
    }
    .card__body{
        padding:20px;
    }


</style>
