"use client";

export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            CARBONCALC
          </span>
          <nav className="flex items-center gap-8">
            <a
              href="#demo"
              className="text-body-sm text-ink-muted hover:text-ink transition-colors"
            >
              Demo
            </a>
            <a
              href="#pricing"
              className="text-body-sm text-ink-muted hover:text-ink transition-colors"
            >
              Pricing
            </a>
          </nav>
        </div>
      </header>

      <main>
        {/* Hero */}
        <section className="pt-24 pb-32 px-6">
          <div className="max-w-prose mx-auto text-center">
            <p className="text-body-sm text-ink-muted uppercase tracking-widest mb-6">
              Carbon Footprint Shipping API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              A container from Shanghai to Rotterdam emits 1.5 tons of CO2.
              <br />
              <em className="not-italic text-ink-muted">
                Your logistics team doesn&apos;t know this.
              </em>
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              CARBONCALC gives logistics teams, developers, and sustainability
              officers instant carbon footprint calculations — without hiring a
              consultant.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#demo"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Try the Demo
              </a>
              <a
                href="#get-started"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                View Docs
              </a>
            </div>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;Your supply chain emits X tons of CO2. You don&apos;t know
              because there&apos;s no API for it.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Demo */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it — no signup required
              </h2>

              <div className="space-y-6 mb-10">
                {/* Input */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-3 uppercase tracking-wider">
                    Input
                  </p>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono space-y-1">
                    <div>
                      <span className="text-ink-muted">vessel_type: </span>
                      <span>&quot;container_ship&quot;</span>
                    </div>
                    <div>
                      <span className="text-ink-muted">distance_nm: </span>
                      <span>11,500</span>
                    </div>
                    <div>
                      <span className="text-ink-muted">cargo_tons: </span>
                      <span>20,000</span>
                    </div>
                  </div>
                </div>

                {/* Divider */}
                <div className="flex items-center gap-3">
                  <div className="flex-1 h-px bg-cream-border" />
                  <span className="text-body-sm text-ink-muted">→</span>
                  <div className="flex-1 h-px bg-cream-border" />
                </div>

                {/* Output */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-3 uppercase tracking-wider">
                    CO2 Output
                  </p>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Container ship
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        3,680 kg CO2
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Truck (same route)
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        34,076 kg CO2
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        Shipping saves
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        89% vs trucking
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              <div className="text-center">
                <a
                  href="#get-started"
                  className="inline-block text-body-sm text-terracotta hover:text-terracotta-hover transition-colors"
                >
                  Get your API key →
                </a>
              </div>
            </div>
          </div>
        </section>

        {/* How It Works */}
        <section className="py-24 px-6 border-t border-cream-border" id="how-it-works">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-16 text-center">
              How it works
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
              {[
                {
                  step: "1",
                  title: "Send voyage details",
                  desc: "POST vessel type, route distance, and cargo weight. We handle the emission factors and carrier-specific data.",
                },
                {
                  step: "2",
                  title: "Get CO2 in milliseconds",
                  desc: "Receive a precise CO2 estimate in kg, plus comparison benchmarks against road and air freight for the same route.",
                },
                {
                  step: "3",
                  title: "Build your report",
                  desc: "Integrate into dashboards, sustainability reports, or ESG pipelines. No consultant, no spreadsheets.",
                },
              ].map(({ step, title, desc }) => (
                <div key={step} className="text-center">
                  <div className="inline-flex items-center justify-center w-10 h-10 rounded-full border border-cream-border text-ink mb-5">
                    <span className="font-serif text-lg">{step}</span>
                  </div>
                  <h3 className="font-serif text-lg text-ink mb-3">{title}</h3>
                  <p className="text-body-sm text-ink-muted leading-relaxed">
                    {desc}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Use Cases */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              Built for
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {[
                {
                  title: "Logistics platforms",
                  desc: "Add carbon intelligence to freight booking, route planning, and carrier selection tools.",
                },
                {
                  title: "Supply chain dashboards",
                  desc: "Surface emissions data alongside cost, transit time, and reliability metrics.",
                },
                {
                  title: "Sustainability reporting",
                  desc: "Generate Scope 3 emissions estimates for shipments, legs, or entire supply chains.",
                },
                {
                  title: "ESG compliance",
                  desc: "Meet CSRD, CDP, and GHG Protocol requirements with auditable, API-sourced CO2 data.",
                },
              ].map(({ title, desc }) => (
                <div
                  key={title}
                  className="bg-cream-surface border border-cream-border rounded shadow-card p-6"
                >
                  <h3 className="font-serif text-lg text-ink mb-2">{title}</h3>
                  <p className="text-body-sm text-ink-muted leading-relaxed">
                    {desc}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Pricing */}
        <section className="py-24 px-6 border-t border-cream-border" id="pricing">
          <div className="max-w-prose mx-auto text-center">
            <h2 className="font-serif text-[1.75rem] text-ink mb-4">
              Simple pricing
            </h2>
            <p className="text-body-sm text-ink-muted mb-16">
              No surprise bills. Scale as you grow.
            </p>

            <div className="space-y-4 max-w-sm mx-auto text-left">
              {[
                {
                  tier: "Free",
                  price: "$0",
                  calls: "100 calls/day",
                  feature: "Basic emission factors",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "10,000 calls/day",
                  feature: "All vessel types + benchmarks",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$59",
                  calls: "100,000 calls/day",
                  feature: "ESG reports + audit trail",
                  cta: "Go production",
                },
              ].map(({ tier, price, calls, feature, cta }) => (
                <div
                  key={tier}
                  className="flex items-center justify-between bg-cream-surface border border-cream-border rounded p-5"
                >
                  <div>
                    <p className="font-serif text-lg text-ink">{tier}</p>
                    <p className="text-body-sm text-ink-muted">
                      {price}/mo · {calls} · {feature}
                    </p>
                  </div>
                  <a
                    href="#get-started"
                    className="text-body-sm text-terracotta hover:text-terracotta-hover transition-colors whitespace-nowrap ml-4"
                  >
                    {cta} →
                  </a>
                </div>
              ))}
            </div>

            <p className="text-body-sm text-ink-muted mt-8">
              Enterprise plans available. Contact us for custom volumes.
            </p>
          </div>
        </section>

        {/* Code Example */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="get-started"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              Start calculating in minutes
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Request */}
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl -X POST https://api.carboncalc.io/v1/ship \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "vessel_type": "container_ship",
    "distance_nm": 11500,
    "cargo_tons": 20000
  }'`}</code>
                </pre>
              </div>

              {/* Response */}
              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "co2_kg": 3680,
  "benchmarks": {
    "truck_kg": 34076,
    "air_kg": 98200
  },
  "savings_vs_truck_pct": 89,
  "savings_vs_air_pct": 96
}`}</code>
                </pre>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-cream-border py-8 px-6">
        <div className="max-w-prose mx-auto">
          <div className="flex items-center justify-between mb-6">
            <span className="font-serif text-lg text-ink">CARBONCALC</span>
            <nav className="flex items-center gap-6">
              <a
                href="#how-it-works"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Documentation
              </a>
              <a
                href="#"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Privacy
              </a>
              <a
                href="#"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Terms
              </a>
            </nav>
          </div>
          <p className="text-body-sm text-ink-muted">
            &copy; 2026 CARBONCALC. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
