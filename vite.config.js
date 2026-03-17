import { resolve } from 'path'
import { defineConfig } from 'vite'
import { readdirSync } from 'fs'

// Helper to find all HTML files recursively
function getHtmlFiles(dir) {
  const result = {}
  const files = readdirSync(dir, { recursive: true })
  
  for (const file of files) {
    if (file.endsWith('.html') && !file.includes('node_modules') && !file.includes('dist')) {
      const name = file.replace(/\.html$/, '').replace(/[\\/]/g, '_')
      result[name] = resolve(dir, file)
    }
  }
  return result
}

const input = getHtmlFiles(__dirname)

export default defineConfig({
  build: {
    rollupOptions: {
      input,
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
