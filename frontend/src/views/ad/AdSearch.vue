<template>
  <div>
    <form @submit="searchAd">
      <input type="text" v-on:keyup="updateQuery" name="search" placeholder="Søk i annonser ...">
    </form>
    <div class="adfilter__tabs">
      <sui-button active v-on:click="e=>updateFilter(e, 'ALL_ADS')">Alle annonser</sui-button>
      <sui-button v-on:click="e=>updateFilter(e, 'MY_ADS')">Mine annonser</sui-button>
      <sui-button v-on:click="e=>updateFilter(e, 'MY_BIDS')">Mine bud</sui-button>
    </div>
  </div>
</template>

<script>

  export default {
    name: "AdSearch",
    data() {
      return {
          query: '',
          filter: 'ALL_ADS',
      }
    },
    methods: {
      updateQuery(e){
        e.preventDefault();
        this.query=e.target.value;
        this.searchAd();
      },

      updateFilter(e, filter){
        this.filter=filter;
        this.searchAd();
        e.target.parentNode.childNodes.forEach(child=>{
          if(child===e.target){
            e.target.classList.add("active")
          }else{
            child.classList.remove("active")
          }
        });
      },

      searchAd() {
        this.$emit('ad-search', {filter:this.filter, query:this.query});
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

  .adfilter__tabs{
    margin:0 auto;
    margin-top: 10px;
    display: flex;
    justify-content: space-evenly;
    max-width: 700px;
  }

  .adfilter__tabs__button{
    padding:30px;
  }

  .adfilter__tabs__active{

  }
</style>
