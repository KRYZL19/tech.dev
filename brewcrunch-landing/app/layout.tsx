import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BREWCRUNCH — Homebrew Beer Calculator API",
  description:
    "ABV, IBU, OG calculations and BJCP style checking via API. No ads, no subscriptions.",
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
