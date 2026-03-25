export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            SUNGLASSES
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
              Aviation Incident Database
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              That airport has 12 laser incidents reported in the last year.&nbsp;
              <em>One query.</em>
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              SUNGLASSES gives pilots and airport operators instant access to
              NASA ASRS aviation incident data — laser illuminations, wildlife
              strikes, operational incidents.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#demo"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Try the Demo
              </a>
              <a
                href="#api"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                View API Docs
              </a>
            </div>
            <p className="text-body-sm text-ink-muted mt-6">
              Free tier · No credit card · 100 calls/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;A pilot reported a green laser at 2,000ft over KATL last
              Tuesday. How many incidents like this happen at&nbsp;this&nbsp;airport?&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Demo Card */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it — no signup required
              </h2>

              <div className="space-y-6 mb-10">
                {/* Input */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Query
                  </p>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono space-y-1">
                    <p>Airport: <span className="text-terracotta">KLAX</span></p>
                    <p>Year: <span className="text-terracotta">2024</span></p>
                    <p>Radius: <span className="text-terracotta">5 miles</span></p>
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
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Response
                  </p>
                  <div className="bg-cream-code text-ink text-body-sm font-mono rounded p-4 leading-relaxed">
                    <p className="mb-3 font-serif text-base">14 incidents in 2024</p>
                    <div className="space-y-1 text-ink-muted">
                      <p>Laser: <span className="text-ink">8</span> <span className="text-xs">(most common)</span></p>
                      <p>Wildlife: <span className="text-ink">4</span></p>
                      <p>Operational: <span className="text-ink">2</span></p>
                    </div>
                    <div className="mt-4 pt-4 border-t border-cream-border">
                      <p className="text-ink-muted">
                        Most recent: <span className="text-ink">October 3rd</span> — pilot reported green laser from ground at 3,000ft. Crew&nbsp;unaffected.
                      </p>
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
                  title: "Query an airport",
                  desc: "Specify an airport code, year, and radius. We normalize NASA ASRS incident reports into a clean, structured API.",
                },
                {
                  step: "2",
                  title: "Filter by incident type",
                  desc: "Laser illuminations, wildlife strikes, operational incidents — filter by what matters to your safety review.",
                },
                {
                  step: "3",
                  title: "Get structured incident data",
                  desc: "Receive parsed incident records with date, altitude, description, crew impact, and reporter narrative.",
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
                  title: "Pilots",
                  desc: "Research incident history at your home airport or destination before a flight. Know what others have reported at altitude.",
                },
                {
                  title: "Airport safety officers",
                  desc: "Monitor laser illumination trends, wildlife strike patterns, and operational incidents across your airspace.",
                },
                {
                  title: "Aviation researchers",
                  desc: "Access a clean API layer over NASA ASRS data for academic research, safety studies, and statistical analysis.",
                },
                {
                  title: "Flight training academies",
                  desc: "Give instructors and students real incident data for scenario-based training and safety awareness programs.",
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

        {/* API Example */}
        <section className="py-24 px-6 border-t border-cream-border" id="api">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              One request, one response
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Request */}
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl https://api.sunglasses.dev/v1/incidents \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d "airport=KLAX&year=2024&radius=5"`}</code>
                </pre>
              </div>

              {/* Response */}
              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "airport": "KLAX",
  "total_incidents": 14,
  "by_type": {
    "laser": 8,
    "wildlife": 4,
    "operational": 2
  },
  "incidents": [
    {
      "date": "2024-10-03",
      "type": "laser",
      "description": "Green laser from ground at 3,000ft",
      "altitude_ft": 3000,
      "crew_affected": false
    }
  ]
}`}</code>
                </pre>
              </div>
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
                  feature: "All incident types",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "10,000 calls/day",
                  feature: "Historical data back to 2020",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$49",
                  calls: "100,000 calls/day",
                  feature: "Bulk export + webhooks",
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
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-cream-border py-8 px-6">
        <div className="max-w-prose mx-auto">
          <div className="flex items-center justify-between mb-6">
            <span className="font-serif text-lg text-ink">SUNGLASSES</span>
            <nav className="flex items-center gap-6">
              <a
                href="#api"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                API Docs
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
            Data sourced from NASA ASRS. &copy; 2026 SUNGLASSES.
          </p>
        </div>
      </footer>
    </div>
  );
}
