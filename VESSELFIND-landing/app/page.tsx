'use client'

export default function VesselFindLanding() {
  return (
    <main className="space-y-16">
      {/* Header */}
      <header className="space-y-4">
        <p className="text-sm tracking-widest text-terracotta uppercase">API for Maritime Data</p>
        <h1 className="text-4xl md:text-5xl leading-tight">
          VesselFind
        </h1>
        <p className="text-xl text-gray-600 leading-relaxed">
          That boat has three owners and a lien against it.<br />
          One API call tells you before you buy.
        </p>
      </header>

      {/* Demo */}
      <section className="bg-white/60 border border-gray-200 p-8 space-y-6">
        <h2 className="text-lg font-semibold text-terracotta">Live Demo</h2>
        <div className="font-mono text-sm space-y-3">
          <div className="flex gap-4">
            <span className="text-gray-500 w-28">Vessel ID:</span>
            <span className="font-semibold">VESSEL-2024-00047</span>
          </div>
          <div className="flex gap-4">
            <span className="text-gray-500 w-28">Status:</span>
            <span className="text-green-700">Active</span>
          </div>
          <div className="flex gap-4">
            <span className="text-gray-500 w-28">Lien:</span>
            <span className="text-terracotta font-semibold">YES — $22,000 remaining</span>
          </div>
          <div className="flex gap-4">
            <span className="text-gray-500 w-28">Owner:</span>
            <span>J. Martinez</span>
          </div>
          <div className="flex gap-4">
            <span className="text-gray-500 w-28">Prev owners:</span>
            <span>2</span>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="space-y-4">
        <h2 className="text-2xl">What you get</h2>
        <ul className="space-y-3 text-gray-700">
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Ownership chain & current owner verification</span>
          </li>
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Active liens, encumbrances & debt status</span>
          </li>
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Coast Guard documentation status</span>
          </li>
          <li className="flex gap-3">
            <span className="text-terracotta">→</span>
            <span>Previous owner history</span>
          </li>
        </ul>
      </section>

      {/* Pricing */}
      <section className="space-y-6">
        <h2 className="text-2xl">Pricing</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="border border-gray-300 p-6 text-center">
            <p className="text-3xl font-semibold">Free</p>
            <p className="text-gray-600 mt-1">100 lookups/day</p>
            <p className="text-sm text-gray-500 mt-2">No credit card</p>
          </div>
          <div className="border-2 border-terracotta p-6 text-center bg-white/80">
            <p className="text-3xl font-semibold text-terracotta">$19<span className="text-base font-normal">/mo</span></p>
            <p className="text-gray-600 mt-1">Dev</p>
            <p className="text-sm text-gray-500 mt-2">5,000 lookups/day</p>
          </div>
          <div className="border border-gray-300 p-6 text-center">
            <p className="text-3xl font-semibold">$49<span className="text-base font-normal">/mo</span></p>
            <p className="text-gray-600 mt-1">Pro</p>
            <p className="text-sm text-gray-500 mt-2">Unlimited lookups</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="text-center text-gray-500 text-sm pt-8 border-t border-gray-200">
        <p>VesselFind API · Maritime intelligence for buyers & brokers</p>
      </footer>
    </main>
  )
}
