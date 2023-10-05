/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#202225',
        secondary: '#5865f2',
        gray: colors.trueGray,
        gray: {
         900: '#202225',
         800: '#2f3136',
         700: '#3639f',
         600: '#4f545c',
         400: '#d4d7dc',
         300: '#e3e5e8',
         200: '#ebedef',
         100: '#f2f3f5',
        },
}
      
    },
  },
  plugins: [],
}

