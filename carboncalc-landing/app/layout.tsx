import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "CARBONCALC — Carbon Footprint API", description: "CO2 emissions for shipping and flights. IMO and ICAO formulas. CARBONCALC gives logistics platforms and sustainability reporters carbon footprint calculations." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
