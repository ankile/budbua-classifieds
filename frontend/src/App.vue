
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  font-family: gotham_light;
  letter-spacing: 1.1px;
  color: #2c3e50;
  margin-top: 60px;
}
@font-face {
  font-family: gotham_light;
  src: url('./../public/fonts/GothamRounded-Light.otf');
}



</style>

