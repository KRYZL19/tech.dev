import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "GRIDOPT — Energy Tariff Optimization API",
  description: "Cut energy costs with off-peak scheduling. GRIDOPT gives developers the tariff data and optimization algorithms to build products that run appliances when the grid is cheapest.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet" />
      </head>
      <body className="bg-cream-50 text-ink antialiased min-h-screen">
        {children}
      </body>
    </html>
  );
}
