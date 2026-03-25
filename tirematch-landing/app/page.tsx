"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

const FITMENT_RESPONSE = {
  diameter_diff: "+4.2%",
  will_fit: "RUBBING LIKELY on full turn",
  speedo_error: "+0.8mph at 60mph",
  recommendation:
    "215/45R17 or 225/40R18 (fits without modification)",
};

const codeExamples: Record<Tab, { request: string; response: string }> = {
  curl: {
    request: `curl "https://api.tirematch.io/v1/fitment?\\
  vehicle=2019%20Honda%20Civic%20EX&\\
  tire_size=235%2F40R18"\\
  -H "Authorization: Bearer YOUR_API_KEY"`,
    response: `{
  "vehicle": {
    "year": 2019,
    "make": "Honda",
    "model": "Civic EX",
    "fitments": [
      {
        "tire_size": "215/45R17",
        "rim_range": "17x7-18x8.5"
      },
      {
        "tire_size": "225/40R18",
        "rim_range": "18x7.5-19x8.5"
      }
    ]
  },
  "query": {
    "tire_size": "235/40R18",
    "diameter_inches": 25.42
  },
  "analysis": {
    "diameter_diff": "+4.2%",
    "will_fit": "rubbing_likely",
    "speedo_error_mph": 0.8,
    "recommendations": [
      "215/45R17",
      "225/40R18"
    ]
  }
}`,
  },
  python: {
    request: `import requests

response = requests.get(
    "https://api.tirematch.io/v1/fitment",
    params={
        "vehicle": "2019 Honda Civic EX",
        "tire_size": "235/40R18",
    },
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

result = response.json()
print(result["analysis"]["will_fit"])
# rubbing_likely`,
    response: `{
  "vehicle": {
    "year": 2019,
    "make": "Honda",
    "model": "Civic EX",
    "fitments": [
      {
        "tire_size": "215/45R17",
        "rim_range": "17x7-18x8.5"
      },
      {
        "tire_size": "225/40R18",
        "rim_range": "18x7.5-19x8.5"
      }
    ]
  },
  "query": {
    "tire_size": "235/40R18",
    "diameter_inches": 25.42
  },
  "analysis": {
    "diameter_diff": "+4.2%",
    "will_fit": "rubbing_likely",
    "speedo_error_mph": 0.8,
    "recommendations": [
      "215/45R17",
      "225/40R18"
    ]
  }
}`,
  },
  javascript: {
    request: `const response = await fetch(
  \`https://api.tirematch.io/v1/fitment?
  vehicle=\${encodeURIComponent("2019 Honda Civic EX")}&
  tire_size=\${encodeURIComponent("235/40R18")}\`,
  {
    headers: {
      "Authorization": "Bearer YOUR_API_KEY",
    },
  }
);

const result = await response.json();
console.log(result.analysis.will_fit);
// rubbing_likely`,
    response: `{
  "vehicle": {
    "year": 2019,
    "make": "Honda",
    "model": "Civic EX",
    "fitments": [
      {
        "tire_size": "215/45R17",
        "rim_range": "17x7-18x8.5"
      },
      {
        "tire_size": "225/40R18",
        "rim_range": "18x7.5-19x8.5"
      }
    ]
  },
  "query": {
    "tire_size": "235/40R18",
    "diameter_inches": 25.42
  },
  "analysis": {
    "diameter_diff": "+4.2%",
    "will_fit": "rubbing_likely",
    "speedo_error_mph": 0.8,
    "recommendations": [
      "215/45R17",
      "225/40R18"
    ]
  }
}`,
  },
};

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");
  const [demoExpanded, setDemoExpanded] = useState(false);

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <svg
              width="28"
              height="28"
              viewBox="0 0 32 32"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle
                cx="16"
                cy="16"
                r="13"
                stroke="#B5451B"
                strokeWidth="2.5"
              />
              <circle cx="16" cy="16" r="5" fill="#B5451B" />
              <line
                x1="16"
                y1="3"
                x2="16"
                y2="8"
                stroke="#B5451B"
                strokeWidth="2"
                strokeLinecap="round"
              />
              <line
                x1="16"
                y1="24"
                x2="16"
                y2="29"
                stroke="#B5451B"
                strokeWidth="2"
                strokeLinecap="round"
              />
              <line
                x1="3"
                y1="16"
                x2="8"
                y2="16"
                stroke="#B5451B"
                strokeWidth="2"
                strokeLinecap="round"
              />
              <line
                x1="24"
                y1="16"
                x2="29"
                y2="16"
                stroke="#B5451B"
                strokeWidth="2"
                strokeLinecap="round"
              />
            </svg>
            <span className="font-serif text-xl tracking-wide text-ink">
              TIREMATCH
            </span>
          </div>
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
              Vehicle Tire Fitment API
            </p>
            <h1 className="font-serif text-[2.4rem] leading-tight text-ink mb-8">
              245/45R18 on a 1998 Honda Civic will rub.{" "}
              <span className="text-terracotta">
                One API call tells you before you buy.
              </span>
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              TIREMATCH gives tire shops, wheel size apps, and automotive
              websites instant access to vehicle fitment data — via API.
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
              &ldquo;You bought tires online, got them mounted, and they rubbed
              the fender. The forum thread was 47 pages long and nobody
              agreed.&rdquo;
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
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Vehicle
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded px-4 py-3 text-body-sm text-ink font-mono">
                    2019 Honda Civic EX
                  </div>
                </div>

                <div>
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Tire size
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded px-4 py-3 text-body-sm text-ink font-mono">
                    235/40R18
                  </div>
                </div>

                <button
                  onClick={() => setDemoExpanded(!demoExpanded)}
                  className="w-full text-body-sm text-terracotta hover:text-terracotta-hover transition-colors text-left flex items-center gap-2"
                >
                  <span>{demoExpanded ? "Hide" : "Show"} analysis</span>
                  <span>{demoExpanded ? "▲" : "▼"}</span>
                </button>

                {demoExpanded && (
                  <div className="border-t border-cream-border pt-6 space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Diameter diff
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        {FITMENT_RESPONSE.diameter_diff}
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Will fit
                      </span>
                      <span className="text-body-sm text-red-600 font-medium uppercase tracking-wide">
                        {FITMENT_RESPONSE.will_fit}
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Speedo error
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        {FITMENT_RESPONSE.speedo_error}
                      </span>
                    </div>
                    <div className="flex justify-between items-start py-2">
                      <span className="text-body-sm text-ink-muted">
                        Recommendation
                      </span>
                      <span className="text-body-sm text-ink font-medium text-right">
                        {FITMENT_RESPONSE.recommendation}
                      </span>
                    </div>
                  </div>
                )}
              </div>

              {!demoExpanded && (
                <div className="border-t border-cream-border pt-6">
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Diameter diff
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        +4.2%
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Will fit
                      </span>
                      <span className="text-body-sm text-red-600 font-medium uppercase tracking-wide">
                        Rubbing likely
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Speedo error
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        +0.8mph at 60mph
                      </span>
                    </div>
                    <div className="flex justify-between items-start py-2">
                      <span className="text-body-sm text-ink-muted">
                        Recommendation
                      </span>
                      <span className="text-body-sm text-ink font-medium text-right">
                        215/45R17 or 225/40R18
                      </span>
                    </div>
                  </div>
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
                  title: "Tire e-commerce sites",
                  desc: "Show fitment warnings at checkout before customers commit to the wrong size.",
                },
                {
                  title: "Wheel size calculators",
                  desc: "Give users accurate fitment data instead of generic tolerance ranges.",
                },
                {
                  title: "Automotive forums",
                  desc: "Replace 47-page threads with a single API call returning a definitive answer.",
                },
                {
                  title: "Aftermarket wheel retailers",
                  desc: "Help customers find wheels that actually fit — no more returns, no more rub.",
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
                  calls: "10,000 calls/day",
                  feature: "Priority support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$39",
                  calls: "100,000 calls/day",
                  feature: "SLA + custom data",
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
              Overage pricing available. Contact us for high-volume needs.
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
              One call. Any vehicle. Any tire size.
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
            <div className="flex items-center gap-2">
              <svg
                width="20"
                height="20"
                viewBox="0 0 32 32"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle
                  cx="16"
                  cy="16"
                  r="13"
                  stroke="#B5451B"
                  strokeWidth="2.5"
                />
                <circle cx="16" cy="16" r="5" fill="#B5451B" />
              </svg>
              <span className="font-serif text-lg text-ink">TIREMATCH</span>
            </div>
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
            &copy; 2026 TIREMATCH. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
