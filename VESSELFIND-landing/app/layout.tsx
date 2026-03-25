import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'VesselFind - Vessel Ownership & Lien Lookup API',
  description: 'Instant vessel ownership records, liens, and history before you buy.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-cream font-serif text-gray-900 antialiased">
        <div className="max-editorial mx-auto px-6 py-16">
          {children}
        </div>
      </body>
    </html>
  )
}
