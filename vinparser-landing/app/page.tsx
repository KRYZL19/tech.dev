"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl -X GET "https://api.vinparser.io/v1/decode/JYARNH10E1NA002347" \\
  -H "Authorization: Bearer YOUR_API_KEY"`,
      response: `{
  "vin": "JYARNH10E1NA002347",
  "valid": true,
  "make": "Yamaha",
  "model": "MT-09",
  "year": 2021,
  "engine": "889cc",
  "horsepower": 119,
  "wet_weight_lbs": 442,
  "frame_type": "Aluminum Deltabox",
  "assembly_plant": "Japan",
  "serial": "002347"
}`,
    },
    python: {
      request: `import requests

response = requests.get(
    "https://api.vinparser.io/v1/decode/JYARNH10E1NA002347",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

bike = response.json()
print(f"{bike['year']} {bike['make']} {bike['model']}")`,
      response: `{
  "vin": "JYARNH10E1NA002347",
  "valid": True,
  "make": "Yamaha",
  "model": "MT-09",
  "year": 2021,
  "engine": "889cc",
  "horsepower": 119,
  "wet_weight_lbs": 442,
  "frame_type": "Aluminum Deltabox",
  "assembly_plant": "Japan",
  "serial": "002347"
}`,
    },
    javascript: {
      request: `const response = await fetch(
  "https://api.vinparser.io/v1/decode/JYARNH10E1NA002347",
  {
    headers: { "Authorization": "Bearer YOUR_API_KEY" },
  }
);

const bike = await response.json();
console.log(\`\${bike.year} \${bike.make} \${bike.model}\`);`,
      response: `{
  "vin": "JYARNH10E1NA002347",
  "valid": true,
  "make": "Yamaha",
  "model": "MT-09",
  "year": 2021,
  "engine": "889cc",
  "horsepower": 119,
  "wet_weight_lbs": 442,
  "frame_type": "Aluminum Deltabox",
  "assembly_plant": "Japan",
  "serial": "002347"
}`,
    },
  };

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            VINPARSER
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
              Motorcycle VIN Decoder API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              The VIN on that 2019 vs 2021 MT-09 looks identical. One character
              tells you everything.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              VINPARSER decodes any motorcycle VIN to full specs, ownership
              history, and recall data — before you buy.
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
              Free tier · No credit card · 100 calls/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;You can&rsquo;t tell a 2019 MT-09 from a 2021 by looking at
              the frame. The VIN tells you everything — if you know how to
              read it.&rdquo;
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
                  <label className="block text-body-sm text-ink-muted mb-2">
                    VIN
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded px-4 py-3 text-body-sm text-ink font-mono">
                    JYARNH10E1NA002347
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Decoded
                  </p>
                  <div className="space-y-3">
                    {[
                      { label: "Make", value: "Yamaha" },
                      { label: "Model", value: "MT-09" },
                      { label: "Year", value: "2021" },
                      { label: "Engine", value: "889cc" },
                      { label: "HP", value: "119" },
                      { label: "Wet weight", value: "442 lbs" },
                      { label: "Frame type", value: "Aluminum Deltabox" },
                      { label: "Plant", value: "Japan" },
                    ].map(({ label, value }) => (
                      <div
                        key={label}
                        className="flex justify-between items-center py-2 border-b border-cream-border"
                      >
                        <span className="text-body-sm text-ink-muted">
                          {label}
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          {value}
                        </span>
                      </div>
                    ))}
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
                  title: "Motorcycle dealers",
                  desc: "Instantly verify bikes on the lot. Pull specs and history before the customer asks.",
                },
                {
                  title: "Insurance companies",
                  desc: "Quote accurately by spec, not by frame photos. Eliminatevin mismatch claims.",
                },
                {
                  title: "Buyer inspection apps",
                  desc: "Give buyers the full picture — specs, recall status, and ownership chain — in one tap.",
                },
                {
                  title: "Recall tracking tools",
                  desc: "Monitor your fleet or customer base for open recalls by VIN, make, or model year.",
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
                  price: "$14",
                  calls: "5,000 calls/day",
                  feature: "Full history & recall data",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$39",
                  calls: "50,000 calls/day",
                  feature: "Webhook delivery & bulk",
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

        {/* Code Example */}
        <section
          className="py-24 px-6 border-t border-cream-border"
          id="get-started"
        >
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              One request, full specs
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
            <span className="font-serif text-lg text-ink">VINPARSER</span>
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
            &copy; 2026 VINPARSER. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
