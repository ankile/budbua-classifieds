<template>
  <div>
    <form @submit="searchAd">
      <input type="text" v-model="searchQuery" name="search" placeholder="Søk i annonser ...">
      <input type="submit" value="Søk" class="btn">
    </form>
  </div>
</template>

<script>
  export default {
    name: "AdSearch",
    data() {
      return {
          searchQuery: ''
      }
    },
    methods: {
      searchAd(e) {
        e.preventDefault();
        console.log(this.searchQuery);

        this.searchQuery = '';
      }
    }
  }

</script>

<style scoped>
  form {
    display: flex;
    min-height: 40px;
  }

  input[type="text"] {
    flex: 10;
    padding: 5px;
  }

  input[type="submit"] {
    flex: 2;
  }

  div {
    max-width: 700px;
    margin: 1rem auto;
  }

  .btn {
    background: #1E639D;
    color: #fff;
  }

  .btn:hover {
    background: #41AAA1;
    color: #000;
  }
</style>