import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "STORMTRACK — Hurricane & Historical Storm Database",
  description:
    "STORMTRACK gives insurance agents, real estate developers, and emergency planners instant access to hurricane track data, return period analysis, and risk summaries — via API.",
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
