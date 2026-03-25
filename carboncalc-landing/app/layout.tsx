import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CARBONCALC — Carbon Footprint Shipping API",
  description:
    "Instant carbon footprint calculations for logistics teams, developers, and sustainability officers. No consultant required.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
