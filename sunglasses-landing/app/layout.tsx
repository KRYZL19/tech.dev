import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SUNGLASSES — Aviation Incident Report Database",
  description: "Instant access to NASA ASRS aviation incident data. Laser illuminations, wildlife strikes, operational incidents — one query.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
