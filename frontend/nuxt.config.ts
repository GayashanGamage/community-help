export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['nuxt-icon', '@nuxt/icon', '@pinia/nuxt', '@nuxtjs/tailwindcss'],
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css'
  }
  // css: ['./app/assets/css/main.css'],
  // css: ['app/assets/css/tailwind.css'],
  // vite: {
  //   plugins: [
  //     tailwindcss(),
  //   ],
  // },
})