import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "BETTORDB — Casino Probability Engine API",
  description: "The math proves the martingale always loses. Now prove it to your users. BETTORDB gives gambling platforms and developers real probability calculations — house edge, Kelly criterion, betting system simulations.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
