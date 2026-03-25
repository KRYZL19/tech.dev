import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AQUARIGHT — Aquarium Water Chemistry API",
  description:
    "Nitrogen cycle tracking, water chemistry calculations, and stocking recommendations for aquarium apps — via API.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
      </head>
      <body className="antialiased">{children}</body>
    </html>
  );
}
