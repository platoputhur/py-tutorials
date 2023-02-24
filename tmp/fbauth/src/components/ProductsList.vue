<template>
  <v-container fluid>
    <v-row dense>
      <v-col cols="12" xs="12" sm="6" md="6" lg="3">
        <ProductAdd class="my-5" />
      </v-col>
      <TransitionGroup>
        <v-col
          v-for="item in productsStore.products"
          :key="item.productId"
          cols="12"
          xs="12"
          sm="6"
          md="6"
          lg="3"
        >
          <ProductShow
            :product-id="item.productId"
            :product-name="item.productName"
            :product-stock="item.productStock"
            :product-cover="item.productCover"
            class="my-5"
          />
        </v-col>
      </TransitionGroup>
    </v-row>
  </v-container>
</template>

<script setup>
import ProductShow from "@/components/ProductShow.vue";
import ProductAdd from "@/components/ProductAdd.vue";
import { useProductsStore } from "@/stores/products";
const productsStore = useProductsStore();
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.25s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
