import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "OPENCLAWIFY — OpenClaw Skill Generator API",
  description:
    "Describe your workflow in plain English. Get a working OpenClaw skill. YAML validated, ready to deploy.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
