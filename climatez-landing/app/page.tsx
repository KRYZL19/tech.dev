"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl https://api.climatez.io/v1/zip/78701 \\
  -H "Authorization: Bearer YOUR_API_KEY"`,
      response: `{
  "zip": "78701",
  "location": {
    "city": "Austin",
    "state": "TX",
    "lat": 30.2672,
    "lon": -97.7431
  },
  "frost_dates": {
    "last_spring": "2024-03-15",
    "last_spring_std": 7,
    "first_fall": "2024-11-22",
    "first_fall_std": 6
  },
  "growing_season_days": 251,
  "climate_normals": {
    "precipitation_inches": 34.2,
    "wettest_month": "May",
    "heat_zone": "USDA Zone 8b"
  }
}`,
    },
    python: {
      request: `import requests

response = requests.get(
    "https://api.climatez.io/v1/zip/78701",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)
data = response.json()
print(f"Growing season: {data['growing_season_days']} days")`,
      response: `{
  "zip": "78701",
  "location": {
    "city": "Austin",
    "state": "TX",
    "lat": 30.2672,
    "lon": -97.7431
  },
  "frost_dates": {
    "last_spring": "2024-03-15",
    "last_spring_std": 7,
    "first_fall": "2024-11-22",
    "first_fall_std": 6
  },
  "growing_season_days": 251,
  "climate_normals": {
    "precipitation_inches": 34.2,
    "wettest_month": "May",
    "heat_zone": "USDA Zone 8b"
  }
}`,
    },
    javascript: {
      request: `const response = await fetch(
  "https://api.climatez.io/v1/zip/78701",
  {
    headers: {
      "Authorization": "Bearer YOUR_API_KEY",
    },
  }
);

const data = await response.json();
console.log(\`Growing season: \${data.growing_season_days} days\`);`,
      response: `{
  "zip": "78701",
  "location": {
    "city": "Austin",
    "state": "TX",
    "lat": 30.2672,
    "lon": -97.7431
  },
  "frost_dates": {
    "last_spring": "2024-03-15",
    "last_spring_std": 7,
    "first_fall": "2024-11-22",
    "first_fall_std": 6
  },
  "growing_season_days": 251,
  "climate_normals": {
    "precipitation_inches": 34.2,
    "wettest_month": "May",
    "heat_zone": "USDA Zone 8b"
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
            CLIMATEZ
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
              Historical Weather &amp; Climate API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Frost date history for this zip code. 30-year normals. One query.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              CLIMATEZ gives agricultural developers and insurance actuaries
              instant access to climate normals, frost dates, and precipitation
              data by location.
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
              Free tier · 100 calls/day · No credit card
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;Your planting app needs the last frost date for zip 78701
              (Austin). The NOAA normals exist. The structured access
              doesn&rsquo;t.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Demo Card */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-8 text-center">
                Try it — no signup required
              </h2>

              <div className="space-y-6 mb-10">
                <div>
                  <label className="block text-body-sm text-ink-muted mb-2">
                    Zip code
                  </label>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                    Zip: 78701 (Austin, TX)
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Response
                  </p>
                  <div className="space-y-3">
                    {[
                      {
                        label: "Last spring frost",
                        value: "March 15 (±7 days)",
                      },
                      {
                        label: "First fall frost",
                        value: "November 22",
                      },
                      {
                        label: "Growing season",
                        value: "251 days",
                      },
                      {
                        label: "Avg precipitation",
                        value: "34.2 in/year",
                      },
                      {
                        label: "Wettest month",
                        value: "May",
                      },
                      {
                        label: "Heat zone",
                        value: "USDA Zone 8b",
                      },
                    ].map(({ label, value }) => (
                      <div
                        key={label}
                        className="flex justify-between items-center py-2 border-b border-cream-border last:border-0"
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
                  title: "Planting calendars",
                  desc: "Give gardeners and farmers precise frost dates and growing season lengths for their exact location.",
                },
                {
                  title: "Agricultural insurance",
                  desc: "Actuaries need 30-year normals and frost probability data to price crop and weather derivatives.",
                },
                {
                  title: "HVAC sizing",
                  desc: "Heat load calculations require historical temperature extremes and design day data by location.",
                },
                {
                  title: "Solar installers",
                  desc: "Irradiance patterns, precipitation data, and seasonal variation inform system design and output estimates.",
                },
                {
                  title: "Real estate disclosures",
                  desc: "Property disclosures increasingly require historical weather and climate risk data at the zip code level.",
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
                  feature: "All endpoints",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$29",
                  calls: "100,000 calls/day",
                  feature: "Bulk queries + exports",
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
              One call. All the data.
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
            <span className="font-serif text-lg text-ink">CLIMATEZ</span>
            <nav className="flex items-center gap-6">
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
            &copy; 2026 CLIMATEZ. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
