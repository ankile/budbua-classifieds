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
        this.$emit('ad-search', this.searchQuery);
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
    outline: none;
    border: none;
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
    background-color: #1E639D;
    color: #fff;
    margin-left: 6px;
  }

  .btn:hover {
    background-color: #1c588f;
  }
</style>
