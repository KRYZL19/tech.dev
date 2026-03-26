import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "FCCLOOKUP — Ham Radio Callsign API",
  description: "Ham radio license lookup in one call. Callsign class, FRN, grid square, band privileges, expiration. FCCLOOKUP gives ham operators and antenna designers instant access to license data.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
