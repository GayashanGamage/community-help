export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['nuxt-icon', '@nuxt/icon', '@pinia/nuxt', '@nuxtjs/tailwindcss', '@nuxtjs/leaflet'],
  leaflet: {
    markerCluster: true
  },
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css'
  },
  runtimeConfig: {
    public: {
      url: process.env.NUXT_PUBLIC_URL || 'default_fallback_url',
    },
  },
})