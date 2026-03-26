import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "SAWMILL — Board Foot & Lumber Calculator API",
  description: "Board feet, linear feet, cubic footage, lumber pricing. SAWMILL gives sawyers and contractors lumber math without a scratch pad and a calculator.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
