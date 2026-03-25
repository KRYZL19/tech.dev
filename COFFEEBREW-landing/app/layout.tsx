import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "COFFEEBREW — Extraction Calculated",
  description: "Instant coffee extraction calculations for specialty coffee professionals.",
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
