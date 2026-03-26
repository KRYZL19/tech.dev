import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "NEIGHBORHOODDB — Real Estate Demographics API",
  description: "Median home price, cap rate, days on market, rent, walk score — by zip code. Updated monthly. NEIGHBORHOODDB gives real estate investors instant access to neighborhood-level data.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
