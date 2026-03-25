"use client";

export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            AMMODEX
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
              Ammunition Data API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Every reloader has a powder spreadsheet from 6 different PDF
              manuals. Stop.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              AMMODEX gives reloaders and ammunition researchers instant access
              to powder data, bullet specifications, and reloading calculations
              — via API.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#get-started"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Get Free API Key
              </a>
              <a
                href="#demo"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                Try the demo
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
              &ldquo;You need to check the max load for CFE Pistol in a 9mm.
              You have three PDF manuals and a spreadsheet. Nobody should need a
              spreadsheet for this.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Live Demo */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it — no signup required
              </h2>

              <div className="space-y-6 mb-10">
                {/* Input */}
                <div>
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Input
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                    .223 Rem, 55gr, Varget powder
                  </div>
                </div>

                {/* Arrow */}
                <div className="flex justify-center">
                  <div className="text-ink-muted text-lg">↓</div>
                </div>

                {/* Output */}
                <div>
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    API response
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded p-4">
                    <div className="space-y-3">
                      {[
                        { label: "Starting load", value: "24.0 gr" },
                        { label: "Max load", value: "26.5 gr" },
                        { label: "Est. velocity", value: "3,045 fps" },
                        {
                          label: "Optimal charge for 3,100 fps",
                          value: "25.2 gr",
                          highlight: true,
                        },
                      ].map(({ label, value, highlight }) => (
                        <div
                          key={label}
                          className="flex justify-between items-center py-2 border-b border-cream-border last:border-0"
                        >
                          <span className="text-body-sm text-ink-muted">
                            {label}
                          </span>
                          <span
                            className={`text-body-sm font-medium ${
                              highlight ? "text-terracotta" : "text-ink"
                            }`}
                          >
                            {value}
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Code snippet */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Or via API
                  </p>
                  <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded font-mono">
                    <code>{`curl https://api.ammodex.io/v1/load \\
  -d '{"caliber":".223 Rem","bullet":"55gr","powder":"Varget"}'`}</code>
                  </pre>
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
                  title: "Query powder data",
                  desc: "Search by caliber, bullet weight, and powder name. We normalize load data from authoritative reloading manuals.",
                },
                {
                  step: "2",
                  title: "Get load parameters",
                  desc: "Receive starting load, max load, optimal charge, and estimated velocity — instantly, without manual lookups.",
                },
                {
                  step: "3",
                  title: "Integrate anywhere",
                  desc: "REST API with JSON responses. Built for reloading apps, ballistic calculators, and firearms training platforms.",
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
                  title: "Reloading software",
                  desc: "Give users instant access to verified powder and bullet data inside your reloading app or spreadsheet.",
                },
                {
                  title: "Ammunition comparison tools",
                  desc: "Compare load data across calibers, powders, and bullet weights programmatically.",
                },
                {
                  title: "Ballistic calculators",
                  desc: "Feed accurate load parameters directly into your trajectory and energy calculators.",
                },
                {
                  title: "Firearms training platforms",
                  desc: "Help instructors and students look up load data without leaving the firing line.",
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
                  feature: "Full powder & bullet data",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "10,000 calls/month",
                  feature: "Priority support + rate limits",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$59",
                  calls: "100,000 calls/month",
                  feature: "Bulk access + historical data",
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
              Starting at $0.001 per call beyond your tier limit.
            </p>
          </div>
        </section>

        {/* Get Started / Code Example */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="get-started"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              Start in minutes
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded font-mono">
                  <code>{`curl https://api.ammodex.io/v1/load \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{"caliber":".223 Rem","bullet":"55gr","powder":"Varget"}'`}</code>
                </pre>
              </div>

              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded font-mono">
                  <code>{`{
  "caliber": ".223 Rem",
  "bullet": { "weight": "55gr" },
  "powder": "Varget",
  "starting_load": "24.0 gr",
  "max_load": "26.5 gr",
  "optimal_charge": "25.2 gr",
  "est_velocity": "3,045 fps"
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
            <span className="font-serif text-lg text-ink">AMMODEX</span>
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
            &copy; 2026 AMMODEX. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
