import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "DRONEWING — Drone Airspace API", description: "LAANC authorization, airspace classification, max altitude. DRONEWING gives drone operators instant airspace compliance checks without the FAA's broken portal." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
