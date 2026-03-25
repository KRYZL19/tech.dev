import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "PATENTLOOK — US Patent Database API",
  description:
    "PATENTLOOK gives researchers, inventors, and legal professionals full-text patent search across titles, abstracts, claims, and inventor names — without a patent lawyer's budget.",
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
