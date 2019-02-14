<template>
  <div id="aditem">
    <router-link v-bind:to="'/details/'+ad.id">
      <h3>{{ad.title}}</h3>
    </router-link>
    <router-link v-bind:to="'/details/'+ad.id">
      <img  alt="Annonsebilde">
    </router-link>
  </div>
</template>


<script>

  export default {
      name: "AdItem",
      props: ["ad"]
  }

</script>


<style scoped>
  #aditem {
    background: #f4f4f4;
    box-shadow: 0 0 8px #1e639d;
    max-width: 700px;
    /* border: 2px solid #41aaa1; */
    display: grid;
    grid-gap: 30px;
    grid-template-columns: 2fr 1fr;
    padding: 2rem 3rem;
    margin: 1rem auto;
    text-align: left;
  }

  #aditem:hover {
    box-shadow: 0 0 10px #41aaa1;
    transition-duration: 0.3s;
  }

  img {
    max-width: 100%;
  }

  a {
    text-decoration: none;
    color: inherit;
  }
</style>
