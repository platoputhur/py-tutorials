<template>
  <Transition mode="out-in">
    <div v-if="!editMode">
      <v-card class="mx-auto" max-width="344" min-width="344">
        <v-img
          :src="
            productCover
              ? productCover
              : 'https://cdn.vuetifyjs.com/images/parallax/material.jpg'
          "
          height="200px"
          cover
        ></v-img>
        <v-card-title>
          {{ productName }}
        </v-card-title>
        <v-card-subtitle>
          {{ "Stock: " + productStock }}
        </v-card-subtitle>
        <v-card-actions class="float-right">
          <v-btn
            icon="mdi-pencil"
            :onclick="
              () => {
                setEditMode(productId);
              }
            "
          ></v-btn>
          <v-btn
            icon="mdi-trash-can"
            color="error"
            :onclick="
              () => {
                deleteProduct(productId);
              }
            "
          ></v-btn>
        </v-card-actions>
      </v-card>
    </div>
    <div v-else>
      <ProductForm
        :edit-mode="true"
        :product-stock="productStock"
        :product-name="productName"
        :product-id="productId"
        :product-cover="productCover"
        @cancel-edit-mode="
          () => {
            setEditMode(productId, false);
          }
        "
      />
    </div>
  </Transition>
</template>

<script setup>
import { useProductsStore } from "@/stores/products";
import { ref } from "vue";
import ProductForm from "@/components/ProductForm.vue";

const props = defineProps({
  productId: String,
  productName: String,
  productStock: Number,
  productCover: String,
});
const productsStore = useProductsStore();
const editMode = ref(false);

function setEditMode(productId, setEditMode = true) {
  if (props.productId === productId) {
    editMode.value = setEditMode;
  }
}
function deleteProduct(id) {
  productsStore.removeProduct(id);
}
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
