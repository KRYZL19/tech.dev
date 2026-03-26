import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "VESSELFIND — USCG Vessel Documentation API", description: "Boat lien status, owner history, documentation renewal dates. VESSELFIND gives boat dealers and marine insurance platforms USCG vessel documentation data." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
