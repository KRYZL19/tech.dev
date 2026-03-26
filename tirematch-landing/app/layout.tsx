import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "TIREMATCH — Tire Size API",
  description: "Compare tire sizes. Speedometer error calculator. Load index lookup. TIREMATCH gives tire retailers and automotive apps the math behind switching wheel sizes.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
