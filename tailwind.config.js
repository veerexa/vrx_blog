/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./education/**/*.{html,js}",
    "./space/**/*.{html,js}",
    "./tech/**/*.{html,js}",
    "./inventory/**/*.{html,js}",
    "./blog/**/*.{html,js}",
    "./assets/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        'brand-dark': '#06071a',
        'brand-surface': '#0d0f2b',
        'brand-primary': '#7c3aed',
        'brand-accent': '#06b6d4',
      },
      fontFamily: {
        display: ['Outfit', 'system-ui', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
