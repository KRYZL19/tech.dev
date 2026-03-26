import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "STORMTRACK — Severe Weather API",
  description: "Wind chill, heat index, tornado threat, hurricane category. STORMTRACK gives weather apps and safety platforms NWS-standard calculations without building the math yourself.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
