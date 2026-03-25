import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'FCCLOOKUP - Ham Radio License Lookup',
  description: 'Instant access to license records and frequency data for radio operators.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-cream font-serif text-gray-900 antialiased">
        <div className="max-w-reading mx-auto px-6 py-12">
          {children}
        </div>
      </body>
    </html>
  )
}
