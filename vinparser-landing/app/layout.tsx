import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "VINPARSER — Vehicle Identification Number Decode API",
  description: "Parse any 17-character VIN. Validation, country of origin, model year, assembly plant, serial number. VINPARSER gives dealers and automotive platforms instant vehicle identification.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-cream-50 text-ink antialiased min-h-screen">{children}</body></html>;
}
