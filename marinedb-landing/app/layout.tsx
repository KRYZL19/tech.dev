import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MARINEDB — Marine Navigation API",
  description:
    "MARINEDB gives marine developers and navigation app builders instant access to tide predictions, port data, and route calculations — without maintaining their own harmonic constant databases.",
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
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
