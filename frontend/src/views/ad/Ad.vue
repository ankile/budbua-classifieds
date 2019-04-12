<template>
   <div>
     <div v-bind:key="ad.id" v-for="ad in ads">
       <AdItem v-bind:ad="ad"></AdItem>
     </div>

   </div>
</template>


<script>
  import AdItem from './AdItem'

  export default {
      name: "Ad",
      components: {
          AdItem
      },
      props: ["ads"],
      created() {

      }
  }
</script>