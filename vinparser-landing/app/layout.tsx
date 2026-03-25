import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "VINPARSER — Motorcycle VIN Decoder API",
  description:
    "Decode any motorcycle VIN to full specs, ownership history, and recall data before you buy.",
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
