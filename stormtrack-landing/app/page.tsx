"use client";

export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            STORMTRACK
          </span>
          <nav className="flex items-center gap-8">
            <a
              href="#how-it-works"
              className="text-body-sm text-ink-muted hover:text-ink transition-colors"
            >
              Documentation
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
              Hurricane &amp; Historical Storm Database
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              What&rsquo;s the hurricane history for this coastal address?{" "}
              <em className="not-italic text-terracotta">1950 to 2025.</em>
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              STORMTRACK gives insurance agents, real estate developers, and
              emergency planners instant access to hurricane track data,
              return period analysis, and risk summaries&mdash;via API.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#demo"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Try the Demo
              </a>
              <a
                href="#how-it-works"
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
              &ldquo;For a hurricane risk assessment on a coastal property, you
              need NOAA historical data, track files, and surge modeling. Most
              agents spend days assembling what should take one query.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Demo Card */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it &mdash; no signup required
              </h2>

              <div className="space-y-6 mb-10">
                <div>
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Input
                  </label>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                    Miami, FL (25.8, -80.2), radius 25 miles
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    API Response
                  </p>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono mb-6 overflow-x-auto">
                    {`{
  "location": "Miami, FL (25.8, -80.2)",
  "radius_miles": 25,
  "storms_found": 12,
  "most_recent": {
    "name": "Hurricane Ian",
    "year": 2022,
    "category": 4
  },
  "return_period_cat3plus_years": 7,
  "estimated_surge_ft": "8-12"
}`}
                  </div>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Storms found
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        12 storms
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Most recent
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        Hurricane Ian 2022 (Cat 4)
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Return period (Cat 3+)
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        Every 7 years
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        Estimated surge at property
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        8&ndash;12 ft
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* How It Works */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="how-it-works"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-16 text-center">
              How it works
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
              {[
                {
                  step: "1",
                  title: "Query a location",
                  desc: "Send coordinates or an address with a search radius. We match it against our NOAA-backed storm track database.",
                },
                {
                  step: "2",
                  title: "Get storm history",
                  desc: "Receive every storm that intersected your radius since 1950, with category, dates, and track geometry.",
                },
                {
                  step: "3",
                  title: "Risk summary in one call",
                  desc: "Return period, surge estimates, and risk tier delivered alongside raw data&mdash;ready for your app or report.",
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
                  title: "Insurance underwriters",
                  desc: "Instant hurricane risk data to quote coastal property policies with confidence.",
                },
                {
                  title: "Coastal real estate developers",
                  desc: "Assess historical exposure before acquiring, financing, or permitting coastal projects.",
                },
                {
                  title: "Emergency management",
                  desc: "Prioritize resources and evacuation planning with neighborhood-level storm history.",
                },
                {
                  title: "Property inspectors",
                  desc: "Include certified storm risk summaries in your inspection reports.",
                },
                {
                  title: "Wind mitigation contractors",
                  desc: "Reference historical storm data to support construction standards and upgrades.",
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
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="pricing"
        >
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
                  feature: "Basic storm queries",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$29",
                  calls: "5,000 calls/day",
                  feature: "Surge + return period",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$79",
                  calls: "50,000 calls/day",
                  feature: "Bulk + track geometry",
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
                      {price}/mo &middot; {calls} &middot; {feature}
                    </p>
                  </div>
                  <a
                    href="#get-started"
                    className="text-body-sm text-terracotta hover:text-terracotta-hover transition-colors whitespace-nowrap ml-4"
                  >
                    {cta} &rarr;
                  </a>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Code Example */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="get-started"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              One query, full risk picture
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl -X GET "https://api.stormtrack.io/v1/risk\\
  ?lat=25.8&lon=-80.2&radius=25"\\
  -H "Authorization: Bearer YOUR_API_KEY"`}</code>
                </pre>
              </div>

              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "storms_found": 12,
  "most_recent": {
    "name": "Hurricane Ian",
    "year": 2022,
    "category": 4
  },
  "return_period_cat3plus_years": 7,
  "estimated_surge_ft": [8, 12]
}`}</code>
                </pre>
              </div>
            </div>

            <div className="text-center mt-10">
              <a
                href="#"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Get Free API Key
              </a>
              <p className="text-body-sm text-ink-muted mt-4">
                Free tier &middot; No credit card &middot; 100 calls/day
              </p>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-cream-border py-8 px-6">
        <div className="max-w-prose mx-auto">
          <div className="flex items-center justify-between mb-6">
            <span className="font-serif text-lg text-ink">STORMTRACK</span>
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
            &copy; 2026 STORMTRACK. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
