import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "VESSELFIND — US Boat & Ship Registration Lookup",
  description:
    "VESSELFIND gives boat buyers and marine dealers instant access to USCG vessel documentation, ownership history, and lien status.",
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
