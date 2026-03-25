import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "POOLCHEM — Water Chemistry Explained",
  description: "Instant pool water chemistry calculations for pool professionals.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-cream text-gray-900 font-serif antialiased">
        <div className="max-w-editorial mx-auto px-6 py-16">
          {children}
        </div>
      </body>
    </html>
  );
}
