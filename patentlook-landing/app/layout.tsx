import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "PATENTLOOK — Patent Search API", description: "Search patents by keyword, CPC code, or assignee. PATENLOOk gives researchers and investors access to patent data without a patent database subscription." };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>; }
