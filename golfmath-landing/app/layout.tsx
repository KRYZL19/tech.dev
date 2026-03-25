import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "GOLFMATH — Golf Handicap & Course API",
  description:
    "GOLFMATH gives golfers and course operators instant access to handicap calculations, weather adjustments, and scorecard analysis — via API.",
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
