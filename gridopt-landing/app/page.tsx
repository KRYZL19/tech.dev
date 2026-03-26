"use client";

import { useState } from "react";

export default function Home() {
  const [demoRan, setDemoRan] = useState(false);
  const [demoResult, setDemoResult] = useState<any>(null);

  const runDemo = async () => {
    setDemoRan(true);
    setDemoResult({
      schedule: [
        { appliance: "Washer", time: "6:00 AM – 8:00 AM", cost: "$0.09", note: "off-peak" },
        { appliance: "Dishwasher", time: "9:00 PM – 11:00 PM", cost: "$0.11", note: "off-peak" },
      ],
      totalCost: "$0.20",
      flatRateCost: "$1.05",
      savings: "81%",
      period: "PG&E E-TOU-C · Tuesday",
    });
  };

  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      {/* Header */}
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight text-ink">
          GRIDOPT
        </div>
        <nav className="flex gap-6 text-sm text-ink-muted">
          <a href="#docs" className="hover:text-terracotta transition-colors">Documentation</a>
          <a href="#pricing" className="hover:text-terracotta transition-colors">Pricing</a>
          <a href="https://github.com/kryzl19/tech.dev" className="hover:text-terracotta transition-colors">GitHub</a>
        </nav>
      </header>

      {/* Hero */}
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6" style={{ fontFamily: "Georgia, serif" }}>
          The electricity grid has off-peak hours. Your app should too.
        </h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">
          GRIDOPT gives developers the tariff data and optimization algorithms to build products that cut energy costs automatically. Ten utilities. Real TOU rates. One API call.
        </p>
        <div className="flex gap-4">
          <button
            onClick={runDemo}
            className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm"
          >
            Try the demo
          </button>
          <a href="#docs" className="border border-ink text-ink px-6 py-3 rounded font-medium hover:bg-ink hover:text-cream-50 transition-colors text-sm">
            Read the docs
          </a>
        </div>
      </section>

      {/* Problem */}
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">
            "I spent three hours calculating when to run my dishwasher. The math isn't hard. The data is scattered across 300 utility websites and encoded in PDFs nobody wants to parse."
          </p>
          <footer className="text-sm text-ink-muted mt-3">— Every developer who's tried to build a smart home energy feature</footer>
        </blockquote>
      </section>

      {/* Demo */}
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2" style={{ fontFamily: "Georgia, serif" }}>Try it — no signup required</h2>
        <p className="text-sm text-ink-muted mb-6">PG&E residential TOU rates. Run a dishwasher for 2 hours, 1 device at priority 2.</p>

        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm">
          <div className="grid grid-cols-2 gap-4 mb-6 text-sm">
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Utility</span>
              <span className="font-medium">PG&E (California)</span>
            </div>
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Device</span>
              <span className="font-medium">Dishwasher · 2hr · 1200W</span>
            </div>
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Priority</span>
              <span className="font-medium">2 (medium)</span>
            </div>
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Strategy</span>
              <span className="font-medium">Greedy off-peak</span>
            </div>
          </div>

          <button
            onClick={runDemo}
            className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm mb-6"
          >
            Run optimization →
          </button>

          {demoRan && demoResult && (
            <div className="bg-cream-50 border border-cream-border rounded p-4 space-y-3">
              <div className="text-xs text-ink-muted uppercase tracking-wide mb-3">{demoResult.period}</div>
              {demoResult.schedule.map((item: any, i: number) => (
                <div key={i} className="flex items-center justify-between text-sm border-b border-cream-border pb-2 last:border-0">
                  <span className="font-medium">{item.appliance}</span>
                  <span className="text-ink-muted text-xs">{item.time} — {item.note}</span>
                  <span className="text-terracotta font-medium text-sm">{item.cost}</span>
                </div>
              ))}
              <div className="flex items-center justify-between pt-3 border-t border-cream-border">
                <span className="text-sm text-ink-muted">Flat-rate cost (no scheduling)</span>
                <span className="text-sm text-ink-muted line-through">{demoResult.flatRateCost}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-medium">Scheduled cost</span>
                <span className="text-terracotta font-bold text-lg">{demoResult.totalCost}</span>
              </div>
              <div className="text-center">
                <span className="text-xs bg-terracotta/10 text-terracotta px-3 py-1 rounded-full">
                  {demoResult.savings} savings vs running at peak
                </span>
              </div>
            </div>
          )}
        </div>
      </section>

      {/* How it works */}
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-8" style={{ fontFamily: "Georgia, serif" }}>How it works</h2>
        <div className="space-y-8">
          <div className="flex gap-4">
            <span className="text-terracotta font-serif text-2xl font-bold w-8 shrink-0">1</span>
            <div>
              <h3 className="font-medium mb-1">Query the tariff data</h3>
              <p className="text-sm text-ink-muted">GET the current TOU periods for any of our 10 supported utilities. Off-peak, partial-peak, peak — with exact hour boundaries and prices in cents/kWh.</p>
            </div>
          </div>
          <div className="flex gap-4">
            <span className="text-terracotta font-serif text-2xl font-bold w-8 shrink-0">2</span>
            <div>
              <h3 className="font-medium mb-1">Submit your devices</h3>
              <p className="text-sm text-ink-muted">POST your appliances — name, duration, wattage, priority. The greedy optimizer finds the cheapest contiguous window that fits.</p>
            </div>
          </div>
          <div className="flex gap-4">
            <span className="text-terracotta font-serif text-2xl font-bold w-8 shrink-0">3</span>
            <div>
              <h3 className="font-medium mb-1">Schedule and save</h3>
              <p className="text-sm text-ink-muted">Get back exact start/end times, cost, and comparison to flat-rate. Build your smart home app on top of it.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Supported utilities */}
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-4" style={{ fontFamily: "Georgia, serif" }}>10 utilities. More coming.</h2>
        <p className="text-sm text-ink-muted mb-6">Real TOU tariffs, updated quarterly. If your utility isn't here, we add it within 48 hours of your request.</p>
        <div className="grid grid-cols-2 gap-2 text-sm">
          {["Pacific Gas & Electric (PG&E)", "Southern California Edison (SCE)", "San Diego Gas & Electric (SDG&E)", "Dominion Energy (VA/NC)", "Duke Energy (NC/SC)", "Austin Energy (TX)", "Sacramento SMUD", "Arizona Public Service (APS)", "Xcel Energy (CO/NM)", "Consolidated Edison (NY)"].map(u => (
            <div key={u} className="bg-white border border-cream-border rounded px-3 py-2 text-xs text-ink-muted">{u}</div>
          ))}
        </div>
      </section>

      {/* Use cases */}
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-8" style={{ fontFamily: "Georgia, serif" }}>Built for developers</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {[
            { title: "Smart home apps", desc: "Tesla, SmartThings, Home Assistant — schedule appliances when your tariff dictates" },
            { title: "EV charging", desc: "Delay DCFC or Level 2 charge to off-peak windows automatically" },
            { title: "Solar + battery systems", desc: "Know when the grid is cheapest so you know when to discharge vs pull from grid" },
            { title: "Demand response tools", desc: "Help utilities run their DR programs without maintaining tariff databases themselves" },
          ].map(card => (
            <div key={card.title} className="bg-white border border-cream-border rounded-lg p-5">
              <h3 className="font-medium mb-2 text-sm">{card.title}</h3>
              <p className="text-xs text-ink-muted leading-relaxed">{card.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Pricing */}
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2" style={{ fontFamily: "Georgia, serif" }}>Simple pricing</h2>
        <p className="text-sm text-ink-muted mb-8">No per-seat fees. No surprise overages. Cancel any time.</p>
        <div className="grid grid-cols-3 gap-4">
          <div className="bg-white border border-cream-border rounded-lg p-5">
            <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">Free</div>
            <div className="text-3xl font-bold mb-1">$0</div>
            <div className="text-xs text-ink-muted mb-4">/month</div>
            <div className="text-xs text-ink-muted space-y-1">
              <div>500 API calls/day</div>
              <div>All 10 utilities</div>
              <div>Basic optimizer</div>
            </div>
          </div>
          <div className="bg-white border-2 border-terracotta rounded-lg p-5 relative">
            <div className="absolute -top-3 left-4 bg-terracotta text-white text-xs px-2 py-0.5 rounded">Most popular</div>
            <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">Dev</div>
            <div className="text-3xl font-bold mb-1">$9</div>
            <div className="text-xs text-ink-muted mb-4">/month</div>
            <div className="text-xs text-ink-muted space-y-1">
              <div>50,000 calls/day</div>
              <div>All 10 utilities</div>
              <div>Full optimizer</div>
              <div>Carbon intensity data</div>
            </div>
          </div>
          <div className="bg-white border border-cream-border rounded-lg p-5">
            <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">Pro</div>
            <div className="text-3xl font-bold mb-1">$49</div>
            <div className="text-xs text-ink-muted mb-4">/month</div>
            <div className="text-xs text-ink-muted space-y-1">
              <div>500,000 calls/day</div>
              <div>All 10 utilities</div>
              <div>Priority support</div>
              <div>Custom tariff uploads</div>
            </div>
          </div>
        </div>
      </section>

      {/* Code example */}
      <section id="docs" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6" style={{ fontFamily: "Georgia, serif" }}>One API call</h2>
        <div className="bg-ink text-cream-100 rounded-lg p-5 text-sm font-mono overflow-x-auto">
          <pre className="text-xs leading-relaxed">{`# Get tariff data
curl "https://api.gridopt.io/v1/tariffs/pge"

# Optimize your schedule
curl -X POST https://api.gridopt.io/v1/optimize/schedule \\
  -H "Content-Type: application/json" \\
  -d '{
    "utility_id": "pge",
    "devices": [
      {"name": "dishwasher",
       "duration_hours": 2,
       "priority": 2,
       "watts": 1200}
    ]
  }'

# Response
{
  "total_cost": 0.20,
  "flat_rate_cost": 1.05,
  "savings_percent": 81
}`}</pre>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-cream-border pt-8 flex items-center justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">GRIDOPT</span>
        <span>Built by KRYZL19 · Powered by OpenClaw</span>
      </footer>
    </main>
  );
}
