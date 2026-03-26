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
        cream: {
          50: "#FAF7F2",
          100: "#F5F0E8",
          200: "#EDE5D8",
          300: "#E0D4C4",
          border: "#E8E2D9",
        },
        ink: {
          DEFAULT: "#1A1A18",
          muted: "#6B6560",
          light: "#3D3D3A",
        },
        terracotta: {
          DEFAULT: "#B5451B",
          hover: "#9A3A16",
          light: "#D4633A",
        },
      },
      fontFamily: {
        serif: ["Georgia", "Cambria", "Times New Roman", "serif"],
      },
      maxWidth: {
        prose: "720px",
      },
    },
  },
  plugins: [],
};
export default config;
