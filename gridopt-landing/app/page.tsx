'use client'

export default function Home() {
  return (
    <main className="min-h-screen">
      {/* Header */}
      <header className="max-w-prose mx-auto px-6 py-8 flex items-center justify-between">
        <span className="font-serif text-2xl font-bold tracking-tight text-cream-text">GRIDOPT</span>
        <nav className="flex gap-6 text-sm text-cream-muted">
          <a href="#docs" className="hover:text-cream-text transition-colors">Documentation</a>
          <a href="#pricing" className="hover:text-cream-text transition-colors">Pricing</a>
        </nav>
      </header>

      {/* Hero */}
      <section className="max-w-prose mx-auto px-6 pt-16 pb-24">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight text-cream-text mb-6">
          The electricity grid has off-peak hours.<br />
          Your app should too.
        </h1>
        <p className="text-lg text-cream-muted leading-relaxed">
          GRIDOPT gives developers the tariff data and optimization algorithms to build products that cut energy costs automatically.
        </p>
      </section>

      {/* Problem */}
      <section className="max-w-prose mx-auto px-6 pb-24">
        <blockquote className="border-l-4 border-cream-accent pl-6 py-2 text-cream-muted italic">
          "I spent 3 hours calculating when to run my dishwasher. The math isn't hard. The data is scattered across 300 utility websites."
        </blockquote>
      </section>

      {/* Demo */}
      <section className="max-w-prose mx-auto px-6 pb-24">
        <div className="bg-cream-surface border border-cream-border rounded-xl p-8 shadow-sm">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-xs font-medium text-cream-accent uppercase tracking-wider">Try it — no signup</span>
          </div>
          <div className="space-y-4">
            <div className="text-sm text-cream-muted">
              <span className="font-medium text-cream-text">PG&E</span> · Dishwasher · 2hr · Priority 2
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-cream-bg rounded-lg p-4">
                <div className="text-xs text-cream-muted uppercase tracking-wider mb-1">Optimized</div>
                <div className="font-serif text-2xl text-cream-text">2–4 AM</div>
                <div className="text-sm text-cream-muted">$0.09</div>
              </div>
              <div className="bg-cream-bg rounded-lg p-4">
                <div className="text-xs text-cream-muted uppercase tracking-wider mb-1">Peak Rate</div>
                <div className="font-serif text-2xl text-cream-accent">4–9 PM</div>
                <div className="text-sm text-cream-muted">$0.47</div>
              </div>
            </div>
            <div className="text-sm text-cream-muted">
              <span className="text-green-600 font-medium">81% savings</span> — automatically scheduled
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="max-w-prose mx-auto px-6 pb-24">
        <h2 className="font-serif text-2xl text-cream-text mb-8">How It Works</h2>
        <div className="space-y-6">
          {[
            { step: '1', title: 'Query the tariff', desc: 'Fetch time-of-use periods for any of 10+ US utilities.' },
            { step: '2', title: 'Submit your devices', desc: 'Tell us what needs to run, for how long, and its priority.' },
            { step: '3', title: 'Get an optimized schedule', desc: 'Our greedy algorithm finds the cheapest hours automatically.' },
          ].map(({ step, title, desc }) => (
            <div key={step} className="flex gap-4">
              <span className="flex-shrink-0 w-8 h-8 rounded-full bg-cream-accent text-white flex items-center justify-center font-medium text-sm">
                {step}
              </span>
              <div>
                <h3 className="font-medium text-cream-text">{title}</h3>
                <p className="text-sm text-cream-muted">{desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Use Cases */}
      <section className="max-w-prose mx-auto px-6 pb-24">
        <h2 className="font-serif text-2xl text-cream-text mb-8">Use Cases</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            { title: 'Smart Home Apps', desc: 'Automatically run dishwasher, washer, dryer during off-peak hours.' },
            { title: 'EV Charging', desc: 'Schedule vehicle charging to minimize overnight electricity costs.' },
            { title: 'HVAC Optimization', desc: 'Pre-cool or pre-heat your home when rates are lowest.' },
            { title: 'Commercial Building Management', desc: 'Shift load away from peak demand windows.' },
          ].map(({ title, desc }) => (
            <div key={title} className="bg-cream-surface border border-cream-border rounded-xl p-6 shadow-sm">
              <h3 className="font-medium text-cream-text mb-2">{title}</h3>
              <p className="text-sm text-cream-muted">{desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Pricing */}
      <section className="max-w-prose mx-auto px-6 pb-24" id="pricing">
        <h2 className="font-serif text-2xl text-cream-text mb-8">Pricing</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { name: 'Free', price: '$0', req: '500/mo', desc: 'For hobby projects and exploration.' },
            { name: 'Dev', price: '$9', req: '10,000/mo', desc: 'For apps in active development.' },
            { name: 'Pro', price: '$49', req: '100,000/mo', desc: 'For production applications.' },
          ].map(({ name, price, req, desc }) => (
            <div key={name} className="bg-cream-surface border border-cream-border rounded-xl p-6 shadow-sm">
              <div className="text-sm font-medium text-cream-muted mb-1">{name}</div>
              <div className="font-serif text-3xl text-cream-text mb-1">{price}<span className="text-lg text-cream-muted">/mo</span></div>
              <div className="text-xs text-cream-muted mb-3">{req}</div>
              <p className="text-sm text-cream-muted">{desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Code Example */}
      <section className="max-w-prose mx-auto px-6 pb-24" id="docs">
        <h2 className="font-serif text-2xl text-cream-text mb-8">Quick Start</h2>
        <div className="bg-cream-surface border border-cream-border rounded-xl p-6 overflow-x-auto">
          <pre className="text-sm text-cream-muted"><code>{`$ curl -X POST https://api.gridopt.dev/v1/optimize/schedule \\
  -H "Content-Type: application/json" \\
  -d '{
    "utility_id": "pge",
    "devices": [
      {"name": "dishwasher", "duration_hours": 2, "priority": 2}
    ]
  }'

{
  "utility_id": "pge",
  "scheduled_devices": [
    {
      "name": "dishwasher",
      "start_time": "02:00",
      "end_time": "04:00",
      "duration_hours": 2,
      "cost": 0.09,
      "priority": 2
    }
  ],
  "total_cost": 0.09,
  "flat_rate_cost": 0.47,
  "savings_percent": 80.9
}`}</code></pre>
        </div>
      </section>

      {/* Footer */}
      <footer className="max-w-prose mx-auto px-6 py-12 border-t border-cream-border">
        <div className="flex items-center justify-between text-sm text-cream-muted">
          <span className="font-serif font-medium text-cream-text">GRIDOPT</span>
          <span>© 2026</span>
        </div>
      </footer>
    </main>
  )
}
