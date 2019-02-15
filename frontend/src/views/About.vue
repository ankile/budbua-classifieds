<template>
  <div>
    <h1>Om oss</h1>
    <p>
      Budbua AS er norges eldste og største auksjonsselskap og ble stiftet i 1869. Vi har nå bestemt
      oss for å gå digitalt og lage norges beste auksjonsapplikasjon.
    </p>
    <p class="box_warning">
      Merk: Denne nettsiden er et studentprosjekt, og ikke en ekte applikasjon. Budbua AS er et fiktivt selskap,
      og annonsene på denne nettsiden er ikke ekte.
    </p>
  </div>
</template>



<script>
    export default {
        name: "About"
    }
</script>



<style scoped>
  div {
    text-align: left;
    padding: 3rem;
  }

  .box_warning {
    background: red;
    color: #fff;
  }

  p {
    padding: 3rem;
  }
</style>