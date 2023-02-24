<script setup>
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";
import { computed, onMounted, ref } from "vue";
import { signOut, getAuth, onAuthStateChanged } from "firebase/auth";
const theme = ref("dark");
const router = useRouter();
const snackbar = ref(false);
const auth = getAuth();
const authStore = useAuthStore();
let snackBarText = "";
const isLoggedIn = computed(() => {
  return authStore.isLoggedIn;
});

function logout() {
  signOut(auth).then(() => {
    snackbar.value = true;
    snackBarText = "Logged out!";
    authStore.logout();
    router.push("/");
  });
}

onMounted(() => {
  onAuthStateChanged(auth, (user) => {
    if (user) {
      snackbar.value = true;
      snackBarText = "Logged in!";
      authStore.login();
      router.push("/dashboard");
    }
  });
});
</script>

<template>
  <v-app :theme="theme">
    <v-app-bar>
      <v-app-bar-nav-icon to="/">
        <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="32" />
      </v-app-bar-nav-icon>
      <v-app-bar-title to="/">
        <p>AuthDemo - CyberMalayali</p>
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn to="/">Home</v-btn>
      <v-btn to="/dashboard" v-if="isLoggedIn">Dashboard</v-btn>
      <v-btn to="/login" v-if="isLoggedIn === false">Login</v-btn>
      <v-btn @click="logout" v-if="isLoggedIn === true">Logout</v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
    <v-snackbar v-model="snackbar">
      {{ snackBarText }}
      <template v-slot:actions>
        <v-btn color="pink" variant="text" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<style scoped></style>
