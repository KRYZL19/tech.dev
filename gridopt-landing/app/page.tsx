"use client";

import { useState } from "react";

const UTILITIES = [
  { id: "pge", name: "Pacific Gas & Electric (PG&E)", region: "California" },
  { id: "sce", name: "Southern California Edison", region: "California" },
  { id: "sdge", name: "San Diego Gas & Electric", region: "California" },
  { id: "coned", name: "Con Edison", region: "New York" },
  { id: "duke", name: "Duke Energy", region: "North Carolina" },
  { id: "eversource", name: "Eversource", region: "Connecticut" },
];

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [utility, setUtility] = useState("pge");
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl -X POST https://api.gridopt.io/v1/optimize \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "utility_id": "pge",
    "appliances": [
      {
        "id": "dishwasher",
        "duration_minutes": 120,
        "priority": 2,
        "latest_finish": "23:00",
        "earliest_start": "06:00"
      }
    ]
  }'`,
      response: `{
  "schedule": {
    "dishwasher": {
      "start": "02:00",
      "end": "04:00",
      "cost": 0.09,
      "peak_cost": 0.47,
      "savings": 0.38
    }
  },
  "total_savings": 0.38,
  "period": {
    "start": "2026-03-26T02:00:00Z",
    "end": "2026-03-26T04:00:00Z"
  }
}`,
    },
    python: {
      request: `import requests

response = requests.post(
    "https://api.gridopt.io/v1/optimize",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    json={
        "utility_id": "pge",
        "appliances": [
            {
                "id": "dishwasher",
                "duration_minutes": 120,
                "priority": 2,
                "latest_finish": "23:00",
                "earliest_start": "06:00",
            }
        ],
    },
)

schedule = response.json()
print(f"Run dishwasher at {schedule['schedule']['dishwasher']['start']}")`,
      response: `{
  "schedule": {
    "dishwasher": {
      "start": "02:00",
      "end": "04:00",
      "cost": 0.09,
      "peak_cost": 0.47,
      "savings": 0.38
    }
  },
  "total_savings": 0.38,
  "period": {
    "start": "2026-03-26T02:00:00Z",
    "end": "2026-03-26T04:00:00Z"
  }
}`,
    },
    javascript: {
      request: `const response = await fetch("https://api.gridopt.io/v1/optimize", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    utility_id: "pge",
    appliances: [
      {
        id: "dishwasher",
        duration_minutes: 120,
        priority: 2,
        latest_finish: "23:00",
        earliest_start: "06:00",
      },
    ],
  }),
});

const schedule = await response.json();
console.log(\`Run dishwasher at \${schedule.schedule.dishwasher.start}\`);`,
      response: `{
  "schedule": {
    "dishwasher": {
      "start": "02:00",
      "end": "04:00",
      "cost": 0.09,
      "peak_cost": 0.47,
      "savings": 0.38
    }
  },
  "total_savings": 0.38,
  "period": {
    "start": "2026-03-26T02:00:00Z",
    "end": "2026-03-26T04:00:00Z"
  }
}`,
    },
  };

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            GRIDOPT
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
              Energy Tariff API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              The electricity grid has off-peak hours. Your app should too.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              GRIDOPT gives developers the tariff data and optimization
              algorithms to build products that cut energy costs automatically.
              Built for Home Assistant, solar systems, and demand-flexibility
              apps.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#get-started"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Get Free API Key
              </a>
              <a
                href="#how-it-works"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                View Docs
              </a>
            </div>
            <p className="text-body-sm text-ink-muted mt-6">
              Free tier · No credit card · 500 calls/month
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;I spent 3 hours calculating when to run my dishwasher. The
              math isn&rsquo;t hard. The data is scattered across 300 utility
              websites in formats nobody can agree on.&rdquo;
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
                    Utility provider
                  </label>
                  <select
                    value={utility}
                    onChange={(e) => setUtility(e.target.value)}
                    className="w-full border border-cream-border rounded bg-cream-bg text-ink px-4 py-3 text-body-sm focus:outline-none focus:border-terracotta transition-colors"
                  >
                    {UTILITIES.map((u) => (
                      <option key={u.id} value={u.id}>
                        {u.name} — {u.region}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block text-body-sm text-ink-muted mb-2">
                    Appliance & constraints
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink-muted font-mono">
                    2-hour appliance, priority 2, flexible window 6am–11pm
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Optimal schedule
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Cheapest window
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        2:00am – 4:00am
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">Cost</span>
                      <span className="text-body-sm text-ink font-medium">
                        $0.09 <span className="text-ink-muted">vs $0.47 at peak</span>
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        You save
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        $0.38 per run
                      </span>
                    </div>
                  </div>
                </div>
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
                  title: "Query a utility tariff",
                  desc: "Tell us which utility company and we handle the rest. We normalize rate data from hundreds of providers.",
                },
                {
                  step: "2",
                  title: "POST your appliances",
                  desc: "Send your appliance list with duration, priority, and flexible time windows. The constraints are yours.",
                },
                {
                  step: "3",
                  title: "Get back optimal schedule",
                  desc: "Receive the cheapest window for each appliance, the cost at that time, and your projected savings.",
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
                  title: "Home automation",
                  desc: "Home Assistant, SmartThings, and any platform that schedules appliances.",
                },
                {
                  title: "Solar + battery dispatch",
                  desc: "Coordinate battery charging with off-peak rates and solar production windows.",
                },
                {
                  title: "Demand flexibility apps",
                  desc: "Help grid operators balance load with automated demand-response programs.",
                },
                {
                  title: "Energy management systems",
                  desc: "Enterprise EMS platforms that need real-time tariff-aware scheduling.",
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
                  calls: "500 calls/month",
                  feature: "All endpoints",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$9",
                  calls: "10,000 calls/month",
                  feature: "Priority support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$49",
                  calls: "100,000 calls/month",
                  feature: "Custom utilities",
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
              Starting at $0.00009 per call beyond your tier limit.
            </p>
          </div>
        </section>

        {/* Code Example */}
        <section className="py-24 px-6 border-t border-cream-border" id="get-started">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              Start optimizing in minutes
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
            <span className="font-serif text-lg text-ink">GRIDOPT</span>
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
            &copy; 2026 GRIDOPT. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
