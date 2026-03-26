import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "HVACCALC — HVAC Sizing API", description: "Manual J residential load calculation. Cooling tons, heating BTU, zone-based. HVACCALC gives contractors HVAC sizing without ACCA software subscriptions." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
