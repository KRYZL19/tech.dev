import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "AQUARIGHT — Pool & Water Chemistry API", description: "FCI chlorine lockup, CSI saturation index, chemical dosing. AQUARIGHT gives pool professionals water chemistry calculations without a chemistry degree." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
