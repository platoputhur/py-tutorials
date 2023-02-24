<template>
  <v-form
    @submit.prevent="props.editMode ? updateProduct() : addProduct()"
    validate-on="submit"
  >
    <v-card class="mx-auto" max-width="344" min-width="344">
      <v-card-title class="my-2">
        {{ props.editMode ? "Update" : "New" }} Product
      </v-card-title>
      <v-card-text>
        <v-text-field
          density="compact"
          :rules="nameRules"
          v-model="name"
          :counter="10"
          label="Product Name"
          required
        ></v-text-field>
        <v-text-field
          density="compact"
          :rules="stockRules"
          v-model="stock"
          label="Stock Count"
          required
        ></v-text-field>
        <v-file-input
          density="compact"
          clearable
          label="Cover Image"
          prepend-icon=""
          prepend-inner-icon="mdi-paperclip"
        ></v-file-input>
      </v-card-text>
      <v-card-actions class="float-right">
        <div v-if="props.editMode">
          <v-btn icon="mdi-content-save" color="green" type="submit"></v-btn>
          <v-btn
            icon="mdi-close"
            color="error"
            type="cancel"
            @click="$emit('cancelEditMode')"
          ></v-btn>
        </div>
        <div v-else>
          <v-btn icon="mdi-plus" color="green" type="submit"></v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script setup>
import { computed, ref } from "vue";
import { useProductsStore } from "@/stores/products";
const props = defineProps({
  productId: String,
  productName: String,
  productStock: Number,
  productCover: String,
  editMode: {
    default: false,
    type: Boolean,
  },
});

const productsStore = useProductsStore();
const name = ref(props.productName ? props.productName : "");
const stock = ref(props.productStock ? props.productStock : 0);
const cover = ref("");

const nameRules = ref([
  (value) => {
    if (value) return true;
    return "You must enter a product name.";
  },
]);
const stockRules = ref([
  (value) => {
    if (isNaN(+value)) return "You must enter a number.";
    return true;
  },
]);

const isValid = computed(() => {
  return !!(name.value && !isNaN(+stock.value));
});

const emit = defineEmits(["cancelEditMode"]);

function addProduct() {
  if (isValid.value) {
    productsStore.addProduct(
      crypto.randomUUID(),
      name.value,
      +stock.value,
      cover.value
    );
    name.value = "";
    stock.value = 0;
    cover.value = "";
  }
}

function updateProduct() {
  if (isValid.value) {
    productsStore.updateProduct(
      props.productId,
      name.value,
      +stock.value,
      cover.value
    );
    emit("cancelEditMode");
  }
}
</script>

<style scoped></style>
