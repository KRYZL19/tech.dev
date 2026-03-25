import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "NeighborhoodDB — Real Estate Data by Zip Code",
  description: "Average days on market, price per sqft trend, median rent — by zip code. Updated monthly.",
  icons: {
    icon: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-cream font-serif text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
