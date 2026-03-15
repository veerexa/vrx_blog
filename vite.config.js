import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  // Multi-page application: list every HTML entry point
  build: {
    rollupOptions: {
      input: {
        // Root pages
        main: resolve(__dirname, 'index.html'),

        // Blog listing
        blogIndex: resolve(__dirname, 'blog/index.html'),

        // Blog articles
        blogBestSoftware: resolve(__dirname, 'blog/best-school-management-software-india.html'),
        blogErpHelps: resolve(__dirname, 'blog/how-school-erp-software-helps-schools.html'),
        blogFeatures: resolve(__dirname, 'blog/features-of-good-school-management-system.html'),
        blogBenefits: resolve(__dirname, 'blog/benefits-of-school-management-software.html'),
        blogDigitize: resolve(__dirname, 'blog/how-schools-can-digitize-administration.html'),

        // New article: Veerexa Indore / Madhya Pradesh
        blogIndoreMP: resolve(__dirname, 'blog/veerexa-school-inventory-software-indore-madhya-pradesh.html'),

        // City landing pages — High-Traffic SEO Strategy
        cityIndore: resolve(__dirname, 'blog/school-erp-indore.html'),
        cityBhopal: resolve(__dirname, 'blog/school-management-software-bhopal.html'),
        cityBarwani: resolve(__dirname, 'blog/school-erp-barwani.html'),
        cityThikri: resolve(__dirname, 'blog/school-software-thikri.html'),
        cityMP: resolve(__dirname, 'blog/school-erp-madhya-pradesh.html'),
      },
      output: {
        // Keep clean asset filenames in dist/
        assetFileNames: 'assets/[name]-[hash][extname]',
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
      }
    }
  },

  // Resolve paths relative to project root
  root: '.',

  // Dev server config
  server: {
    port: 5173,
    open: true,
  },

  // Preview server config
  preview: {
    port: 4173,
  }
})
