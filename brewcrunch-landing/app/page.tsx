"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

const codeExamples: Record<Tab, { request: string; response: string }> = {
  curl: {
    request: `curl -X POST https://api.brewcrunch.io/v1/calculate \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "og": 1.065,
    "fg": 1.015,
    "hops": [{ "name": "Cascade", "amount_oz": 5.2, "aa_pct": 5.5, "boil_minutes": 60 }],
    "batch_size_gal": 5
  }'`,
    response: `{
  "abv": "6.5%",
  "ibu": 42.3,
  "attenuation": "76.9%",
  "bjcp_match": {
    "style": "American IPA",
    "score": "38/50",
    "notes": "Notable citrus floral hops, caramel backbone"
  }
}`,
  },
  python: {
    request: `import requests

response = requests.post(
    "https://api.brewcrunch.io/v1/calculate",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    json={
        "og": 1.065,
        "fg": 1.015,
        "hops": [
            {
                "name": "Cascade",
                "amount_oz": 5.2,
                "aa_pct": 5.5,
                "boil_minutes": 60,
            }
        ],
        "batch_size_gal": 5,
    },
)

result = response.json()
print(f"ABV: {result['abv']}  |  IBU: {result['ibu']}")`,
    response: `{
  "abv": "6.5%",
  "ibu": 42.3,
  "attenuation": "76.9%",
  "bjcp_match": {
    "style": "American IPA",
    "score": "38/50",
    "notes": "Notable citrus floral hops, caramel backbone"
  }
}`,
  },
  javascript: {
    request: `const response = await fetch("https://api.brewcrunch.io/v1/calculate", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    og: 1.065,
    fg: 1.015,
    hops: [
      {
        name: "Cascade",
        amount_oz: 5.2,
        aa_pct: 5.5,
        boil_minutes: 60,
      },
    ],
    batch_size_gal: 5,
  }),
});

const result = await response.json();
console.log(\`ABV: \${result.abv}  |  IBU: \${result.ibu}\`);`,
    response: `{
  "abv": "6.5%",
  "ibu": 42.3,
  "attenuation": "76.9%",
  "bjcp_match": {
    "style": "American IPA",
    "score": "38/50",
    "notes": "Notable citrus floral hops, caramel backbone"
  }
}`,
  },
};

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            BREWCRUNCH
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
              Beer Calculator API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              ABV, IBU, OG — none of this needs an ad-supported calculator app.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              BREWCRUNCH gives homebrewers and craft breweries instant access to
              recipe calculations, BJCP style checking, and ingredient data —
              via API.
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
                Try the Demo
              </a>
            </div>
            <p className="text-body-sm text-ink-muted mt-6">
              Free tier · No credit card · 200 calls/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;You spent more time doing math than brewing. ABV, IBU, OG,
              attenuation — every calculator app has ads and asks for a
              subscription.&rdquo;
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
                <div>
                  <p className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Your input
                  </p>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono leading-relaxed">
                    OG 1.065, FG 1.015
                    <br />
                    5.2oz Cascade hops at 5.5% AA
                    <br />
                    60min boil, 5gal batch
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Calculated output
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">ABV</span>
                      <span className="text-body-sm text-ink font-medium">
                        6.5%
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">IBU</span>
                      <span className="text-body-sm text-ink font-medium">
                        42.3
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Attenuation
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        76.9%
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        BJCP match
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        American IPA (Score: 38/50)
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
                  title: "Homebrew recipe apps",
                  desc: "Give your users professional-grade calculations without building the math yourself.",
                },
                {
                  title: "Brewery inventory systems",
                  desc: "Track hop bills, OG/FG targets, and style compliance across every batch.",
                },
                {
                  title: "Beer judging software",
                  desc: "Score entries against BJCP guidelines automatically and stay consistent.",
                },
                {
                  title: "Brew day automation",
                  desc: "Trigger strike temps, boil timers, and hop additions from a single API call.",
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
              No ads. No subscriptions. Just the math.
            </p>

            <div className="space-y-4 max-w-sm mx-auto text-left">
              {[
                {
                  tier: "Free",
                  price: "$0",
                  calls: "200 calls/day",
                  feature: "All endpoints",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$9",
                  calls: "50,000 calls/month",
                  feature: "Rate limit bypass",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$29",
                  calls: "200,000 calls/month",
                  feature: "Priority support",
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
              Per-call pricing available for high-volume workloads.
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
              {/* Tabs */}
              <div className="flex border-b border-cream-border">
                {(["curl", "python", "javascript"] as Tab[]).map((tab) => (
                  <button
                    key={tab}
                    onClick={() => setActiveTab(tab)}
                    className={`px-5 py-3 text-body-sm transition-colors ${
                      activeTab === tab
                        ? "text-ink border-b-2 border-terracotta -mb-px"
                        : "text-ink-muted hover:text-ink"
                    }`}
                  >
                    {tab}
                  </button>
                ))}
              </div>

              {/* Request */}
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{codeExamples[activeTab].request}</code>
                </pre>
              </div>

              {/* Response */}
              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{codeExamples[activeTab].response}</code>
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
            <span className="font-serif text-lg text-ink">BREWCRUNCH</span>
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
            &copy; 2026 BREWCRUNCH. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
