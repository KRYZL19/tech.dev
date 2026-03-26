import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "AMMODEX — Ballistic Properties API",
  description: "Muzzle energy, penetration depth, expansion diameter — for 14 calibers. AMMODEX gives ammunition developers and re-loaders NIST-standard ballistic data via one API call.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
