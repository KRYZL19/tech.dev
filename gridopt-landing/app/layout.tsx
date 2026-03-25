import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'GRIDOPT — Time-of-Use Energy Tariff API',
  description: 'GRIDOPT gives developers the tariff data and optimization algorithms to build products that cut energy costs automatically.',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="font-sans antialiased">{children}</body>
    </html>
  )
}
