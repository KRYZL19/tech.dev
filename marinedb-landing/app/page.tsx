"use client";

export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            MARINEDB
          </span>
          <nav className="flex items-center gap-8">
            <a
              href="#docs"
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
              Marine Navigation API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Tides don&rsquo;t care about your schedule. Neither should your
              autopilot.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              MARINEDB gives marine developers and navigation app builders
              instant access to tide predictions, port data, and route
              calculations — without maintaining their own harmonic constant
              databases.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#get-started"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Get Free API Key
              </a>
              <a
                href="#docs"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                View Docs
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
              &ldquo;Tide harmonic constants are published by NOAA. Getting
              them into your app means downloading shapefiles, parsing arcane
              data formats, and maintaining update schedules. Or one API
              call.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Live Demo */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it — no signup
              </h2>

              <div className="space-y-6 mb-10">
                <div>
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Input
                  </label>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                    San Francisco Bay, next 3 days
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Output
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Next high tide
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        5:42am, 5.8ft
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Next low tide
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        12:15pm, 1.2ft
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        Slack water
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        8:30am, 2:45pm
                      </span>
                    </div>
                  </div>
                </div>
              </div>
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
                  title: "Autopilot software",
                  desc: "Feed real-time tide data to navigation systems for precise course adjustments at lock gates and drawbridges.",
                },
                {
                  title: "Fishing apps",
                  desc: "Surface tide predictions with slack-water windows so anglers hit prime fishing conditions every trip.",
                },
                {
                  title: "Sailing trackers",
                  desc: "Give sailors current flow data and tide heights for safe harbor entries and tricky channel transits.",
                },
                {
                  title: "Marine logistics",
                  desc: "Schedule cargo operations around tidal windows to avoid grounding in shallow ports and estuaries.",
                },
                {
                  title: "Charter boat booking",
                  desc: "Build availability systems that automatically block out unsafe windows based on predicted conditions.",
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
                  feature: "All endpoints",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "Unlimited calls",
                  feature: "All endpoints + support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$49",
                  calls: "Unlimited calls + SLA",
                  feature: "Custom ports & routes",
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

        {/* API Example */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="get-started"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              One call to tidal data
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Request */}
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl -X GET "https://api.marinedb.io/v1/tides?\\
  port=San_Francisco_Bay&days=3" \\
  -H "Authorization: Bearer YOUR_API_KEY"`}</code>
                </pre>
              </div>

              {/* Response */}
              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "port": "San Francisco Bay",
  "tides": [
    {
      "time": "2026-03-26T05:42:00Z",
      "type": "high",
      "height_ft": 5.8
    },
    {
      "time": "2026-03-26T12:15:00Z",
      "type": "low",
      "height_ft": 1.2
    }
  ],
  "slack_water": ["08:30", "14:45"]
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
            <span className="font-serif text-lg text-ink">MARINEDB</span>
            <nav className="flex items-center gap-6">
              <a
                href="#docs"
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
            &copy; 2026 MARINEDB. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
