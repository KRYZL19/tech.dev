import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "GARDENPLOT — Planting Calendar API",
  description: "USDA hardiness zones, frost dates, spacing calculators. GARDENPLOT gives garden apps and seed companies planting calendars by location — updated for the current season.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
