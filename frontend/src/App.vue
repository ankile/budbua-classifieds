<template>
  <div id="app">
    <Header></Header>
    <router-view/>
  </div>
</template>


<script>
  import Header from './components/Header'

  export default {
    name: "App",
    components: {
      Header
    },
    created() {
        document.title = 'Budbua';
    }
  }
</script>



<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    font-family: gotham_light;
    letter-spacing: 1.1px;
    color: #2c3e50;

  }
  @font-face {
    font-family: gotham_light;
    src: url('./../public/fonts/GothamRounded-Light.otf');
  }



</style>

