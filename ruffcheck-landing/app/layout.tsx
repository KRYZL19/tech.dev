import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "RUFFCHECK — Code Quality Linter API",
  description:
    "Run ESLint, Ruff, or golangci-lint without installing anything. Just POST your code.",
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
      <body className="bg-cream-bg text-ink antialiased">{children}</body>
    </html>
  );
}
