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



<style lang="scss">
  @import 'common.scss';


  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  @font-face {
    font-family: gotham_light;
    src: url('./../public/fonts/GothamRounded-Light.otf');
  }
  @font-face {
    font-family: gotham_bold;
    src: url('./../public/fonts/GothamRounded-Bold.otf');
  }
  @font-face {
    font-family: gotham;
    src: url('./../public/fonts/GothamRounded-Medium.otf');
  }

  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    font-family: gotham_light ;
    width:100vw;
    height:100%;
    letter-spacing: 1.1px;
    color: #2c3e50;
    background-color: $off-white;

  }


  body::-webkit-scrollbar {
  width: 0.7em;
  background: transparent;
  }
  body::-webkit-scrollbar-thumb {
  background: rgba(65,131,196, 0.5);
  border-radius: 10px;
  }

  ::-webkit-scrollbar-thumb:hover {
  background: rgba(65,131,196, 0.65);
  }



</style>

