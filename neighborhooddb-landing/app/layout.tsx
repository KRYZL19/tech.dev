import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "NEIGHBORHOODDB — Demographics & Real Estate Comp Database",
  description: "Instant access to neighborhood-level demographic and housing market data by zip code. Updated monthly.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
