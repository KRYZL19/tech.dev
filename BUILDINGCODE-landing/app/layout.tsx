import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BuildingCode — IBC Adoption by City",
  description: "What version of the IBC does your city use? What did they adopt and when?",
  icons: {
    icon: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-cream font-serif text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
