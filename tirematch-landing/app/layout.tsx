import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "TIREMATCH — Vehicle Tire Fitment API",
  description:
    "One API call tells you if a tire size fits your vehicle before you buy. Tire fitment data for tire shops, wheel size apps, and automotive websites.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-cream-bg text-ink antialiased">{children}</body>
    </html>
  );
}
