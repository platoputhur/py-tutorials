<template>
  <v-container>
    <h1>Dashboard</h1>
    <p>
      Available products list.<br />
      Users can add, edit and delete products.
      <br /><br />
    </p>
    <ProductsList />
  </v-container>
</template>

<script>
import { defineComponent } from "vue";
import ProductsList from "@/components/ProductsList.vue";

export default defineComponent({
  components: { ProductsList },
});
</script>

<style scoped></style>
