import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "MARINEDB — Boat Specifications API",
  description: "Sea Ray, Boston Whaler, Jeanneau — specs for 7 boat models. MARINEDB gives marine developers and boat dealers instant access to vessel data: fuel burn, dry weight, insurance quotes.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
