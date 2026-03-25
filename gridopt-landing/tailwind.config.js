/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        cream: {
          bg: '#FAF7F2',
          surface: '#FFFFFF',
          border: '#E8E2D9',
          text: '#1A1A18',
          muted: '#6B6560',
          accent: '#B5451B',
        },
      },
      fontFamily: {
        serif: ['Georgia', 'Cambria', 'Times New Roman', 'serif'],
        sans: ['system-ui', '-apple-system', 'sans-serif'],
      },
      maxWidth: {
        prose: '720px',
      },
    },
  },
  plugins: [],
}
