import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "AIRCRAFTDB — FAA Aircraft Registry API", description: "N-number lookup, airworthiness status, useful load, owner history. AIRCRAFTDB gives FBO management and aviation insurance platforms FAA registry data." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
