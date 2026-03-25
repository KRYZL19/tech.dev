import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        cream: "#FAF7F2",
        terracotta: "#B5451B",
      },
      fontFamily: {
        serif: ["Georgia", "Times New Roman", "serif"],
      },
      maxWidth: {
        editorial: "720px",
      },
    },
  },
  plugins: [],
};
export default config;
