"use client";

export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            GOLFMATH
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
              Golf Handicap & Course API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Your handicap ignores wind. Here&rsquo;s one that doesn&rsquo;t.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              GOLFMATH gives golfers and course operators instant access to
              handicap calculations, weather adjustments, and scorecard
              analysis — via API.
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
              &ldquo;Your USGA handicap index doesn&rsquo;t account for 30mph
              headwinds at Pinehurst. Neither do most apps.&rdquo;
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
                {/* Input */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-3 uppercase tracking-wider">
                    Input
                  </p>
                  <div className="bg-cream-code border border-cream-border rounded p-4">
                    <div className="space-y-2 text-body-sm text-ink">
                      <div className="flex gap-3">
                        <span className="text-ink-muted font-mono"> handicap</span>
                        <span className="font-mono">12.4</span>
                      </div>
                      <div className="flex gap-3">
                        <span className="text-ink-muted font-mono"> temp</span>
                        <span className="font-mono">92°F</span>
                      </div>
                      <div className="flex gap-3">
                        <span className="text-ink-muted font-mono"> wind</span>
                        <span className="font-mono">25mph headwind</span>
                      </div>
                      <div className="flex gap-3">
                        <span className="text-ink-muted font-mono"> elevation</span>
                        <span className="font-mono">5,800ft</span>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Divider */}
                <div className="flex items-center gap-3 py-2">
                  <div className="flex-1 h-px bg-cream-border" />
                  <span className="text-body-sm text-ink-muted">API response</span>
                  <div className="flex-1 h-px bg-cream-border" />
                </div>

                {/* Output */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-3 uppercase tracking-wider">
                    Output
                  </p>
                  <div className="bg-cream-code border border-cream-border rounded p-4">
                    <div className="space-y-3">
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Adjusted handicap
                        </span>
                        <span className="text-body-sm text-ink font-medium font-mono">
                          10.8
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Wind cost you
                        </span>
                        <span className="text-body-sm text-terracotta font-medium font-mono">
                          1.4 strokes
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Heat cost you
                        </span>
                        <span className="text-body-sm text-ink font-medium font-mono">
                          0.3 strokes
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2">
                        <span className="text-body-sm text-ink-muted">
                          Expected score
                        </span>
                        <span className="text-body-sm text-ink font-medium font-mono">
                          +9 to +11
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <p className="text-body-sm text-ink-muted text-center">
                Live on the API &mdash; all inputs affect the adjusted handicap
                in real time.
              </p>
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
                  title: "Send conditions",
                  desc: "Post handicap index, weather, wind, elevation, and course rating. We handle the math.",
                },
                {
                  step: "2",
                  title: "Engine calculates",
                  desc: "Our model applies USGA slope adjustments, wind coefficients, heat factors, and altitude corrections.",
                },
                {
                  step: "3",
                  title: "Get adjusted score",
                  desc: "Receive a weather-adjusted handicap, per-factor breakdown, and expected score range.",
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
                  title: "Golf apps",
                  desc: "Give users a handicap that actually reflects course conditions, not just a number from 6 months ago.",
                },
                {
                  title: "Course booking platforms",
                  desc: "Surface difficulty-aware tee time recommendations based on current weather and player skill.",
                },
                {
                  title: "Fantasy golf tools",
                  desc: "Model player performance under real-world conditions — wind, heat, and altitude all move the needle.",
                },
                {
                  title: "Golf instructors",
                  desc: "Give students a handicap that accounts for the conditions they actually played in, not ideal ones.",
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
                  calls: "50 calls/day",
                  feature: "Full API access",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$14",
                  calls: "10,000 calls/month",
                  feature: "All endpoints + support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$39",
                  calls: "100,000 calls/month",
                  feature: "Priority throughput + SLA",
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
              One call, adjusted handicap
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Request */}
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl -X POST https://api.golfmath.io/v1/adjust \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "handicap_index": 12.4,
    "conditions": {
      "temperature_f": 92,
      "wind_speed_mph": 25,
      "wind_direction": "headwind",
      "elevation_ft": 5800
    }
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
  "adjusted_handicap": 10.8,
  "breakdown": {
    "wind_cost": 1.4,
    "heat_cost": 0.3,
    "altitude_bonus": -0.2
  },
  "expected_score": "+9 to +11",
  "conditions": "challenging"
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
            <span className="font-serif text-lg text-ink">GOLFMATH</span>
            <nav className="flex items-center gap-6">
              <a
                href="#how-it-works"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Docs
              </a>
              <a
                href="#pricing"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Pricing
              </a>
              <a
                href="#"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Privacy
              </a>
            </nav>
          </div>
          <p className="text-body-sm text-ink-muted">
            &copy; 2026 GOLFMATH. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
