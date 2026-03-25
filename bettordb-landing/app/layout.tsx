import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BETTORDB — Casino Probability API",
  description:
    "Probability data for casino game developers and betting system researchers. No NumPy. No local simulations. Just answers.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
