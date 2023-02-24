<template>
  <v-row>
    <v-spacer></v-spacer>
    <v-col>
      <v-form>
        <v-card>
          <v-card-title>Login/Signup Here</v-card-title>
          <v-card-item>
            <section id="firebaseui-auth-container"></section>
          </v-card-item>
        </v-card>
      </v-form>
    </v-col>
    <v-spacer></v-spacer>
  </v-row>
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { getAuth } from "firebase/auth";
import { useRouter } from "vue-router"; // import router
import { auth as uiAuth } from "firebaseui";
import "firebaseui/dist/firebaseui.css";
import firebase from "firebase/compat/app";
import { onMounted } from "vue";
import { useHead } from "@vueuse/head";

useHead({
  title: "Login - AuthDemo CyberMalayali",
});

const authStore = useAuthStore();
const router = useRouter();
const auth = getAuth();
onMounted(() => {
  if (authStore.isLoggedIn) {
    router.push("/");
  } else {
    let ui = uiAuth.AuthUI.getInstance();
    if (!ui) {
      ui = new uiAuth.AuthUI(auth);
    }
    let uiConfig = {
      signInSuccessUrl: "/dashboard",
      signInOptions: [firebase.auth.GoogleAuthProvider.PROVIDER_ID],
    };
    ui.start("#firebaseui-auth-container", uiConfig);
  }
});
</script>

<style scoped></style>
