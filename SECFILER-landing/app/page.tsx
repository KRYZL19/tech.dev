'use client'

export default function SecFilerLanding() {
  return (
    <main className="space-y-16">
      {/* Header */}
      <header className="space-y-4">
        <p className="text-sm tracking-widest text-terracotta uppercase">API for SEC Intelligence</p>
        <h1 className="text-4xl md:text-5xl leading-tight">
          SecFiler
        </h1>
        <p className="text-xl text-gray-600 leading-relaxed">
          Alert me when any company in sector X files a Form 4 within 24 hours.
        </p>
      </header>

      {/* Demo */}
      <section className="bg-white/60 border border-gray-200 p-8 space-y-6">
        <h2 className="text-lg font-semibold text-terracotta">Live Demo</h2>
        <div className="space-y-4">
          <div className="flex gap-4 items-start">
            <span className="text-gray-500 w-20 shrink-0">Sector:</span>
            <span className="font-semibold">tech</span>
          </div>
          <div className="flex gap-4 items-start">
            <span className="text-gray-500 w-20 shrink-0">Alert:</span>
            <span>purchases over $500K</span>
          </div>
          <div className="border-t border-gray-200 pt-4 mt-4">
            <p className="text-sm text-gray-600 mb-2">Matched alert:</p>
            <div className="bg-terracotta/10 border border-terracotta/30 p-4 space-y-1">
              <p className="font-semibold text-terracotta">NVDA CFO purchased $1.2M options</p>
              <p className="text-sm text-gray-600">4 hours ago</p>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="space-y-4">
        <h2 className="text-2xl">What you get</h2>
        <ul className="space-y-3 text-gray-700">
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Sector-based Form 4 monitoring</span>
          </li>
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Threshold alerts ($100K to $10M+)</span>
          </li>
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Real-time webhook delivery</span>
          </li>
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Insider transaction tracking</span>
          </li>
        </ul>
      </section>

      {/* Pricing */}
      <section className="space-y-6">
        <h2 className="text-2xl">Pricing</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="border border-gray-300 p-6 text-center">
            <p className="text-3xl font-semibold">Free</p>
            <p className="text-gray-600 mt-1">100 alerts/day</p>
            <p className="text-sm text-gray-500 mt-2">No credit card</p>
          </div>
          <div className="border border-gray-300 p-6 text-center">
            <p className="text-3xl font-semibold">$49<span className="text-base font-normal">/mo</span></p>
            <p className="text-gray-600 mt-1">Dev</p>
            <p className="text-sm text-gray-500 mt-2">5,000 alerts/day</p>
          </div>
          <div className="border-2 border-terracotta p-6 text-center bg-white/80">
            <p className="text-3xl font-semibold text-terracotta">$149<span className="text-base font-normal">/mo</span></p>
            <p className="text-gray-600 mt-1">Pro</p>
            <p className="text-sm text-gray-500 mt-2">Unlimited alerts</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="text-center text-gray-500 text-sm pt-8 border-t border-gray-200">
        <p>SecFiler API · SEC intelligence for investors & traders</p>
      </footer>
    </main>
  )
}
