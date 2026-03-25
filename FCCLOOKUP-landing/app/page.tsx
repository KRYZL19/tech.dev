'use client'

export default function Home() {
  return (
    <main className="space-y-12">
      {/* Header */}
      <header className="text-center space-y-4">
        <p className="text-terracotta uppercase tracking-widest text-sm">API for Developers</p>
        <h1 className="text-4xl md:text-5xl leading-tight">
          Ham radio license lookup<br />in one call.
        </h1>
        <p className="text-xl text-gray-600 max-w-md mx-auto">
          Equipment certification. Frequency allocation.
        </p>
      </header>

      {/* Hook */}
      <section className="border-t border-b border-gray-300 py-8 text-center">
        <p className="text-lg md:text-xl text-gray-800">
          FCCLOOKUP gives radio operators instant access to license records and frequency data.
        </p>
      </section>

      {/* Demo */}
      <section className="bg-white/50 rounded-lg p-8 space-y-6">
        <div className="text-center">
          <p className="text-terracotta font-medium mb-2">Try it now</p>
          <code className="bg-gray-100 px-4 py-2 rounded text-lg">callsign=W1ABC</code>
        </div>
        
        <div className="text-center space-y-2">
          <p className="text-2xl font-semibold text-terracotta">W1ABC</p>
          <div className="grid grid-cols-2 gap-4 mt-6">
            <div className="bg-white p-4 rounded border border-gray-200">
              <p className="text-sm text-gray-500">License Class</p>
              <p className="text-xl font-semibold">Amateur Extra</p>
            </div>
            <div className="bg-white p-4 rounded border border-gray-200">
              <p className="text-sm text-gray-500">FRN</p>
              <p className="text-xl font-semibold">123456789</p>
            </div>
            <div className="bg-white p-4 rounded border border-gray-200">
              <p className="text-sm text-gray-500">Grid Square</p>
              <p className="text-xl font-semibold">FN31</p>
            </div>
            <div className="bg-white p-4 rounded border border-gray-200">
              <p className="text-sm text-gray-500">Expiration</p>
              <p className="text-xl font-semibold">2031</p>
            </div>
            <div className="col-span-2 bg-white p-4 rounded border border-gray-200">
              <p className="text-sm text-gray-500">Privileges</p>
              <p className="text-xl font-semibold">All bands, all modes</p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section className="space-y-6">
        <h2 className="text-2xl text-center">Simple, transparent pricing</h2>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="bg-white/50 p-6 rounded-lg border border-gray-200 text-center">
            <p className="text-sm text-gray-500 uppercase tracking-wider">Free</p>
            <p className="text-3xl font-semibold mt-2">$0</p>
            <p className="text-gray-500 mt-1">100 requests/day</p>
          </div>
          <div className="bg-white/50 p-6 rounded-lg border-2 border-terracotta text-center">
            <p className="text-terracotta text-sm uppercase tracking-wider">Dev</p>
            <p className="text-3xl font-semibold mt-2 text-terracotta">$9</p>
            <p className="text-gray-500 mt-1">per month</p>
          </div>
          <div className="bg-white/50 p-6 rounded-lg border border-gray-200 text-center">
            <p className="text-sm text-gray-500 uppercase tracking-wider">Pro</p>
            <p className="text-3xl font-semibold mt-2">$29</p>
            <p className="text-gray-500 mt-1">per month</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="text-center text-gray-500 text-sm pt-8 border-t border-gray-200">
        <p>&copy; 2026 FCCLOOKUP. Built for ham radio operators and repeater builders.</p>
      </footer>
    </main>
  )
}
