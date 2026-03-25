"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl -X POST https://api.aquaright.io/v1/analyze \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "day": 7,
    "ammonia": 2.0,
    "nitrite": 0.5,
    "nitrate": 5.0
  }'`,
      response: `{
  "phase": "Nitrite peak (week 1-2)",
  "explanation": "Nitrosomonas are converting ammonia to nitrite. Nitrobacter will colonize in 5-10 days.",
  "recommendation": "Do NOT water change — you will restart the cycle. Add dechlorinator only.",
  "next_check": "3 days"
}`,
    },
    python: {
      request: `import requests

response = requests.post(
    "https://api.aquaright.io/v1/analyze",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    json={
        "day": 7,
        "ammonia": 2.0,
        "nitrite": 0.5,
        "nitrate": 5.0,
    },
)

result = response.json()
print(f"Phase: {result['phase']}")
print(f"Recommendation: {result['recommendation']}")`,
      response: `{
  "phase": "Nitrite peak (week 1-2)",
  "explanation": "Nitrosomonas are converting ammonia to nitrite. Nitrobacter will colonize in 5-10 days.",
  "recommendation": "Do NOT water change — you will restart the cycle. Add dechlorinator only.",
  "next_check": "3 days"
}`,
    },
    javascript: {
      request: `const response = await fetch("https://api.aquaright.io/v1/analyze", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    day: 7,
    ammonia: 2.0,
    nitrite: 0.5,
    nitrate: 5.0,
  }),
});

const result = await response.json();
console.log(\`Phase: \${result.phase}\`);
console.log(\`Recommendation: \${result.recommendation}\`);`,
      response: `{
  "phase": "Nitrite peak (week 1-2)",
  "explanation": "Nitrosomonas are converting ammonia to nitrite. Nitrobacter will colonize in 5-10 days.",
  "recommendation": "Do NOT water change — you will restart the cycle. Add dechlorinator only.",
  "next_check": "3 days"
}`,
    },
  };

  const tabs: Tab[] = ["curl", "python", "javascript"];

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            AQUARIGHT
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
              Aquarium Water Chemistry API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Nitrogen cycle confusion kills more fish than anything. This fixes
              it.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              AQUARIGHT gives aquarium hobbyists and fishkeepers instant access
              to nitrogen cycle tracking, water chemistry calculations, and
              stocking recommendations — via API.
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
            <p className="text-body-sm text-ink-muted mt-6">
              Free tier &middot; No credit card &middot; 100 calls/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;Your ammonia spikes on day 3 and you don&rsquo;t know why.
              The nitrogen cycle takes 2-6 weeks. Most beginners give up before
              day 7.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Live Demo */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it &mdash; no signup required
              </h2>

              <div className="space-y-6 mb-10">
                {/* Input */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Input
                  </p>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                    Day 7, ammonia 2ppm, nitrite 0.5ppm, nitrate 5ppm
                  </div>
                </div>

                {/* Output */}
                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Output
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Phase
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        Nitrite peak (week 1-2)
                      </span>
                    </div>
                    <div className="flex justify-between items-start py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        What&rsquo;s happening
                      </span>
                      <span className="text-body-sm text-ink font-medium text-right max-w-[60%]">
                        Nitrosomonas converting ammonia&rarr;nitrite
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">Next</span>
                      <span className="text-body-sm text-ink font-medium">
                        Nitrobacter colonizes in 5-10 days
                      </span>
                    </div>
                    <div className="flex justify-between items-start py-2">
                      <span className="text-body-sm text-ink-muted">
                        Recommendation
                      </span>
                      <span className="text-body-sm text-terracotta font-medium text-right max-w-[60%]">
                        Do NOT water change &mdash; you&rsquo;ll restart the
                        cycle. Add dechlorinator only.
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              <div className="text-center">
                <a
                  href="#get-started"
                  className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
                >
                  Get Free API Key
                </a>
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
                  title: "POST your water readings",
                  desc: "Send ammonia, nitrite, nitrate, pH, temperature, and tank day. We normalize the data and run it against the nitrogen cycle model.",
                },
                {
                  step: "2",
                  title: "Get cycle phase + advice",
                  desc: "Receive the current cycle phase, what bacteria are active, and a plain-English recommendation — no marine biology degree required.",
                },
                {
                  step: "3",
                  title: "Integrate anywhere",
                  desc: "REST API. JSON responses. Built for Home Assistant, fish store POS, maintenance apps, and planted tank calculators.",
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
                  title: "Aquarium automation",
                  desc: "Home Assistant integration for automated dosing, water change reminders, and real-time tank monitoring.",
                },
                {
                  title: "Fish store POS systems",
                  desc: "Help store staff and customers understand the nitrogen cycle at point of sale — before they set up the tank.",
                },
                {
                  title: "Aquarium maintenance apps",
                  desc: "Give hobbyists cycle tracking, dosing calculators, and stocking alerts built on real water chemistry.",
                },
                {
                  title: "Planted tank calculators",
                  desc: "Combine nutrient dosing, CO2 injection, and cycle status to help planted tank enthusiasts dial in their setup.",
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
                  price: "$9",
                  calls: "10,000 calls/day",
                  feature: "All endpoints + support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$29",
                  calls: "Unlimited calls",
                  feature: "Priority support + webhooks",
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
              Start in minutes
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Tabs */}
              <div className="flex border-b border-cream-border">
                {tabs.map((tab) => (
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
            <span className="font-serif text-lg text-ink">AQUARIGHT</span>
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
            &copy; 2026 AQUARIGHT. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
