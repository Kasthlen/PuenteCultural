/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eff3fc',
          100: '#d8e8f7',
          500: '#134da5',
          600: '#0f2185',
          700: '#1e0d69',
        },
      },
    },
  },
  plugins: [],
}

