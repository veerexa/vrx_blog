import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        
        // Category Index Pages
        education: resolve(__dirname, 'education/index.html'),
        space: resolve(__dirname, 'space/index.html'),
        inventory: resolve(__dirname, 'inventory/index.html'),

        // Space Blogs
        spaceChandrayaan: resolve(__dirname, 'space/chandrayaan-3-success.html'),
        spaceGaganyaan: resolve(__dirname, 'space/gaganyaan-mission-updates.html'),

        // Education Blogs
        blogBestSoftware: resolve(__dirname, 'education/best-school-management-software-india.html'),
        blogErpHelps: resolve(__dirname, 'education/how-school-erp-software-helps-schools.html'),
        blogFeatures: resolve(__dirname, 'education/features-of-good-school-management-system.html'),
        blogBenefits: resolve(__dirname, 'education/benefits-of-school-management-software.html'),
        blogDigitize: resolve(__dirname, 'education/how-schools-can-digitize-administration.html'),
        blogIndoreMP: resolve(__dirname, 'education/veerexa-school-inventory-software-indore-madhya-pradesh.html'),
        cityIndore: resolve(__dirname, 'education/school-erp-indore.html'),
        cityBhopal: resolve(__dirname, 'education/school-management-software-bhopal.html'),
        cityBarwani: resolve(__dirname, 'education/school-erp-barwani.html'),
        cityThikri: resolve(__dirname, 'education/school-software-thikri.html'),
        cityMP: resolve(__dirname, 'education/school-erp-madhya-pradesh.html'),

        // Inventory Blogs
        inventoryIndoreMP: resolve(__dirname, 'inventory/inventory-management-software-indore-madhya-pradesh.html'),
        inventoryRoi: resolve(__dirname, 'inventory/roi-inventory-management-software-sme.html'),

        // Tech Blogs
        techCustomDev: resolve(__dirname, 'tech/custom-software-development-advantages-india.html'),
        techSeo: resolve(__dirname, 'tech/seo-marketing-strategies-indore-2026.html'),
      },
      output: {
        assetFileNames: 'assets/[name]-[hash][extname]',
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
      }
    }
  },
  root: '.',
  server: {
    port: 5173,
    open: true,
  },
  preview: {
    port: 4173,
  }
})
