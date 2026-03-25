import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'SecFiler - SEC Form 4 Alerting API',
  description: 'Get alerts when companies in your sector file Form 4 within 24 hours.',
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
