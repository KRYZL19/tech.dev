import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        cream: {
          bg: "#FAF7F2",
          surface: "#FFFFFF",
          border: "#E8E2D9",
          code: "#F0EBE3",
        },
        ink: {
          DEFAULT: "#1A1A18",
          muted: "#6B6560",
        },
        terracotta: {
          DEFAULT: "#B5451B",
          hover: "#8C3415",
        },
      },
      fontFamily: {
        serif: ["Georgia", "Times New Roman", "serif"],
        sans: [
          "-apple-system",
          "BlinkMacSystemFont",
          "system-ui",
          "sans-serif",
        ],
      },
      fontSize: {
        "body-lg": ["18px", { lineHeight: "1.75" }],
        "body-sm": ["14px", { lineHeight: "1.6" }],
      },
      maxWidth: {
        prose: "720px",
      },
      boxShadow: {
        card: "0 2px 12px rgba(0,0,0,0.06)",
      },
      borderRadius: {
        DEFAULT: "6px",
      },
    },
  },
  plugins: [],
};
export default config;
