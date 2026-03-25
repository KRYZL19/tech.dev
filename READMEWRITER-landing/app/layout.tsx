import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ReadmeWriter — README from Repo Structure",
  description: "Point it at a repo structure. Get a README that actually describes what the code does.",
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
