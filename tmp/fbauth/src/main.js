import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

// Vuetify
import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { initializeApp } from "firebase/app";
import { createHead } from "@vueuse/head";

const vuetify = createVuetify({
  components,
  directives,
});

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCN5w52qFS2-ZmVeGFhB3l3tdj0i3Z_awM",
  authDomain: "cybermalayali-tutorials.firebaseapp.com",
  projectId: "cybermalayali-tutorials",
  storageBucket: "cybermalayali-tutorials.appspot.com",
  messagingSenderId: "143881002283",
  appId: "1:143881002283:web:4e1bc940237438a838b96e",
};

const app = createApp(App);
const head = createHead();

// Initialize Firebase
initializeApp(firebaseConfig);

app.use(createPinia());
app.use(router);
app.use(vuetify);
app.use(head);
app.mount("#app");
