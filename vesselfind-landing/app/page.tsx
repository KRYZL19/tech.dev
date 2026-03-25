"use client";

import { useState } from "react";

export default function Home() {
  const [demoDone, setDemoDone] = useState(false);

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            VESSELFIND
          </span>
          <nav className="flex items-center gap-8">
            <a
              href="#demo"
              className="text-body-sm text-ink-muted hover:text-ink transition-colors"
            >
              Demo
            </a>
            <a
              href="#use-cases"
              className="text-body-sm text-ink-muted hover:text-ink transition-colors"
            >
              Use Cases
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
              USCG Vessel Documentation API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              That boat has three owners and a lien against it.
              <br />
              One API call tells you before you buy.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              VESSELFIND gives boat buyers and marine dealers instant access to
              USCG vessel documentation, ownership history, and lien status.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#demo"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Try the Demo
              </a>
              <a
                href="#pricing"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                View Pricing
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
            <h2 className="font-serif text-[1.75rem] text-ink mb-10 text-center">
              The problem
            </h2>
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;You found a 2019 Sea Ray on Craigslist. The seller says
              there&rsquo;s no lien. You don&rsquo;t know if the documentation
              is even current.&rdquo;
            </blockquote>
            <p className="text-body-lg text-ink-muted text-center mt-8 max-w-xl mx-auto">
              Boat fraud is real. Liens survive ownership transfers. Without
              USCG documentation data, you&rsquo;re buying blind.
            </p>
          </div>
        </section>

        {/* Demo Card */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it — no signup required
              </h2>

              {!demoDone ? (
                <div className="space-y-6 mb-10">
                  <div>
                    <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                      Vessel ID
                    </label>
                    <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                      VESSEL-2024-00047
                    </div>
                  </div>

                  <button
                    onClick={() => setDemoDone(true)}
                    className="w-full bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
                  >
                    Look up vessel
                  </button>
                </div>
              ) : (
                <div className="space-y-6 mb-10">
                  <div>
                    <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                      Vessel ID
                    </label>
                    <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                      VESSEL-2024-00047
                    </div>
                  </div>

                  <div className="border-t border-cream-border pt-6">
                    <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                      Response
                    </p>
                    <div className="space-y-3">
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Status
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          Active
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Length
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          31 ft
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Hull
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          Fiberglass
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Owner
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          J. Martinez (current)
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Lien
                        </span>
                        <span className="text-body-sm text-terracotta font-medium">
                          YES — $22,000 remaining
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-cream-border">
                        <span className="text-body-sm text-ink-muted">
                          Lien holder
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          US Bank
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2">
                        <span className="text-body-sm text-ink-muted">
                          Previous owners
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          2
                        </span>
                      </div>
                    </div>
                  </div>

                  <button
                    onClick={() => setDemoDone(false)}
                    className="w-full text-body-sm text-ink-muted hover:text-ink transition-colors py-2"
                  >
                    Try another →
                  </button>
                </div>
              )}
            </div>
          </div>
        </section>

        {/* Use Cases */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="use-cases"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              Built for
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {[
                {
                  title: "Boat dealers",
                  desc: "Verify liens and ownership before you close. One lookup saves a six-figure mistake.",
                },
                {
                  title: "Marine insurance",
                  desc: "Underwrite with confidence. Know the vessel&rsquo;s documentation history and any encumbrances.",
                },
                {
                  title: "Coast Guard documentation",
                  desc: "Automate documentation lookups for compliance workflows and regulatory reporting.",
                },
                {
                  title: "Buyer due diligence",
                  desc: "Private buyers deserve the same data dealers have. VESSELFIND makes it available to everyone.",
                },
              ].map(({ title, desc }) => (
                <div
                  key={title}
                  className="bg-cream-surface border border-cream-border rounded shadow-card p-6"
                >
                  <h3 className="font-serif text-lg text-ink mb-2">{title}</h3>
                  <p
                    className="text-body-sm text-ink-muted leading-relaxed"
                    dangerouslySetInnerHTML={{ __html: desc }}
                  />
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
                  feature: "Full vessel lookup",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "10,000 calls/month",
                  feature: "Priority support + bulk",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$49",
                  calls: "100,000 calls/month",
                  feature: "Webhooks + team access",
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
                    href="#demo"
                    className="text-body-sm text-terracotta hover:text-terracotta-hover transition-colors whitespace-nowrap ml-4"
                  >
                    {cta} →
                  </a>
                </div>
              ))}
            </div>

            <p className="text-body-sm text-ink-muted mt-8">
              Enterprise plans available. Contact us for volume pricing.
            </p>
          </div>
        </section>

        {/* API Snippet */}
        <section className="py-24 px-6 border-t border-cream-border" id="api">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              One call. Full vessel picture.
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl https://api.vesselfind.io/v1/vessel \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{"vessel_id": "VESSEL-2024-00047"}'`}</code>
                </pre>
              </div>

              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "vessel_id": "VESSEL-2024-00047",
  "status": "Active",
  "length": "31 ft",
  "hull": "Fiberglass",
  "owner": "J. Martinez",
  "owner_current": true,
  "lien": true,
  "lien_amount": 22000,
  "lien_currency": "USD",
  "lien_holder": "US Bank",
  "previous_owners": 2
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
            <span className="font-serif text-lg text-ink">VESSELFIND</span>
            <nav className="flex items-center gap-6">
              <a
                href="#demo"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                Demo
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
            &copy; 2026 VESSELFIND. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
