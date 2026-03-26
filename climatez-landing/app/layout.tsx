import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "CLIMATEZ — Historical Weather & Climate API",
  description: "Frost date history, 30-year normals, growing season, precipitation. CLIMATEZ gives agricultural developers and insurance actuaries access to NOAA climate data by zip code.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
