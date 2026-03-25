import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Sunglasses — Laser Incident Data by Airport",
  description: "That airport has 12 laser incidents reported in the last year. One query.",
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
