import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CLINICALTRL — Clinical Trial Results Database",
  description:
    "Instant access to clinical trial data — without ClinicalTrials.gov's terrible UI.",
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
