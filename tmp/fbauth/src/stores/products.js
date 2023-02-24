import { ref } from "vue";
import { defineStore } from "pinia";

export const useProductsStore = defineStore("products", () => {
  const products = ref([
    {
      productId: crypto.randomUUID(),
      productName: "Product Item #1",
      productCover: "",
      productStock: 10,
    },
    {
      productId: crypto.randomUUID(),
      productName: "Product Item #2",
      productCover:
        "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d",
      productStock: 10,
    },
    {
      productId: crypto.randomUUID(),
      productName: "Product Item #3",
      productCover: "",
      productStock: 10,
    },
    {
      productId: crypto.randomUUID(),
      productName: "Product Item #4",
      productCover: "",
      productStock: 10,
    },
    {
      productId: crypto.randomUUID(),
      productName: "Product Item #5",
      productCover: "",
      productStock: 10,
    },
  ]);
  function addProduct(id, name, stock, cover) {
    products.value.push({
      productId: id,
      productName: name,
      productStock: stock,
      productCover: cover,
    });
  }

  function removeProduct(id) {
    console.log(id);
    products.value = products.value.filter((item) => item.productId !== id);
  }

  function updateProduct(id, name, stock, cover) {
    products.value = products.value.map((item) => {
      if (item.productId === id) {
        return {
          productId: item.productId,
          productName: name ? name : item.productName,
          productStock: stock ? stock : item.productStock,
          productCover: cover ? cover : item.productCover,
        };
      }
      return item;
    });
  }

  return { products, addProduct, removeProduct, updateProduct };
});
