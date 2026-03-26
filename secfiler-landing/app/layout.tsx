import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "SECFILER — SEC EDGAR Filings API", description: "Form 4 insider trades, 8-K events, 10-Q filings. SECFILER gives investors and financial platforms real-time SEC EDGAR data without scraping." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
