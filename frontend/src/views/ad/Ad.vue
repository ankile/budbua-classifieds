<template>
   <div>
     <div v-bind:key="ad.id" v-for="ad in ads">
       <AdItem v-bind:ad="ad"></AdItem>
     </div>

   </div>
</template>


<script>
  import AdItem from './AdItem'
  import Api from '../../api'

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
          Api.get('auctions/ads/')
            .then(res => this.ads = res.data)
            .catch(err => console.log(err));

      }
  }
</script>
