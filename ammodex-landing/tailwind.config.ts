import type { Config } from "tailwindcss";
const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: { cream: { 50: "#FAF7F2", border: "#E8E2D9" }, ink: { DEFAULT: "#1A1A18", muted: "#6B6560" }, terracotta: { DEFAULT: "#B5451B", hover: "#9A3A16" } },
      fontFamily: { serif: ["Georgia", "serif"] },
      maxWidth: { prose: "720px" },
    },
  },
};
export default config;
