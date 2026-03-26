import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "SEPTICODER — Septic System Sizing API", description: "Drain field sizing, tank capacity, percolation-based loading rates. SEPTICODER gives contractors and inspectors septic system calculations without memorizing the NRCS tables." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
