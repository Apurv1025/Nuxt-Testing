// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-05-15",
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      appwriteEndpoint: process.env.APPWRITE_ENDPOINT,
      appwriteProject: process.env.APPWRITE_PROJECT,
      appUrl: process.env.APP_URL,
    },
  },
  routeRules: {
    // Homepage pre-rendered at build time
    "/login": { ssr: false },
  },
  modules: [
    "@nuxt/icon",
    "@nuxt/image",
    "@nuxt/scripts",
    "@nuxt/ui",
    "@nuxt/fonts",
    "@nuxt/eslint",
    "@pinia/nuxt",
    "pinia-plugin-persistedstate/nuxt",
  ],
  css: ["./assets/css/main.css"],
});
