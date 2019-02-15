<template>
   <div>
     <div v-bind:key="ad.id" v-for="ad in ads">
       <AdItem v-bind:ad="ad"></AdItem>
     </div>

   </div>
</template>


<script>
  import AdItem from './AdItem'
  import axios from 'axios'

  export default {
      name: "Ad",
      components: {
          AdItem
      },
      data() {
        return {
            ads: []
        }
      },
      created() {
          axios.get('https://jsonplaceholder.typicode.com/posts?_limit=10')
              .then(res => this.ads = res.data)
              .catch(err => console.log(err));
      }
  }
</script>