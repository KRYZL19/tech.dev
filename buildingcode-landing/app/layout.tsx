import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "BUILDINGCODE — IBC Code Lookup API", description: "What version of the IBC does your city use? What did they adopt and when? BUILDINGCODE gives contractors and architects building code lookup by city." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
