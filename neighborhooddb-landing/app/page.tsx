"use client";

import { useState } from "react";

const DEMO_ZIPS = [
  { zip: "78704", city: "Austin, TX" },
  { zip: "94110", city: "San Francisco, CA" },
  { zip: "60614", city: "Chicago, IL" },
  { zip: "30301", city: "Atlanta, GA" },
  { zip: "10001", city: "New York, NY" },
];

export default function Home() {
  const [selectedZip, setSelectedZip] = useState("78704");

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            NEIGHBORHOODDB
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
              Demographics &amp; Real Estate Comp Database
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Average days on market, price per sqft trend, median rent — by
              zip code. Updated monthly.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              NEIGHBORHOODDB gives real estate investors and developers instant
              access to neighborhood-level demographic and housing market data.
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
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;You need to analyze a zip code for a rental property
              investment. Zillow&rsquo;s API is expensive and their data isn&rsquo;t
              granular enough.&rdquo;
            </blockquote>
          </div>
        </section>

        {/* Demo Card */}
        <section className="py-24 px-6" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <h2 className="font-serif text-xl text-ink mb-2 text-center">
                Try it — no signup
              </h2>
              <p className="text-body-sm text-ink-muted text-center mb-8">
                Enter any US zip code. Get instant comp data.
              </p>

              <div className="space-y-6 mb-10">
                <div>
                  <label className="block text-body-sm text-ink-muted mb-2">
                    Zip code
                  </label>
                  <select
                    value={selectedZip}
                    onChange={(e) => setSelectedZip(e.target.value)}
                    className="w-full border border-cream-border rounded bg-cream-bg text-ink px-4 py-3 text-body-sm focus:outline-none focus:border-terracotta transition-colors"
                  >
                    {DEMO_ZIPS.map((z) => (
                      <option key={z.zip} value={z.zip}>
                        {z.zip} — {z.city}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    {selectedZip} —{" "}
                    {DEMO_ZIPS.find((z) => z.zip === selectedZip)?.city} data
                  </p>
                  <div className="space-y-3">
                    {[
                      { label: "Median home price", value: "$685,000" },
                      { label: "Days on market", value: "18" },
                      { label: "Price / sqft", value: "$524" },
                      { label: "Median rent", value: "$2,340/mo" },
                      { label: "YoY appreciation", value: "+8.2%", accent: true },
                      { label: "Cap rate estimate", value: "5.1%" },
                      { label: "School rating", value: "7/10" },
                    ].map(({ label, value, accent }) => (
                      <div
                        key={label}
                        className="flex justify-between items-center py-2 border-b border-cream-border"
                      >
                        <span className="text-body-sm text-ink-muted">
                          {label}
                        </span>
                        <span
                          className={`text-body-sm font-medium ${
                            accent ? "text-terracotta" : "text-ink"
                          }`}
                        >
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
                  title: "Real estate investors",
                  desc: "Evaluate rental property opportunities with granular neighborhood data before you sign a contract.",
                },
                {
                  title: "Property managers",
                  desc: "Benchmark portfolio performance against local comps and track market trends by zip code.",
                },
                {
                  title: "Mortgage lenders",
                  desc: "Pull comp data for appraisal support and stress-test collateral values against market shifts.",
                },
                {
                  title: "Zoning attorneys",
                  desc: "Ground rezoning arguments and variance requests in hard demographic and housing data.",
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

        {/* How It Works */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-16 text-center">
              How it works
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
              {[
                {
                  step: "1",
                  title: "Pick a zip code",
                  desc: "Query any US zip code. Data is refreshed from county assessor records, MLS feeds, and census sources every month.",
                },
                {
                  step: "2",
                  title: "Get comp data instantly",
                  desc: "Receive median sale price, days on market, rent estimates, appreciation trends, school ratings, and cap rate estimates.",
                },
                {
                  step: "3",
                  title: "Build your analysis",
                  desc: "Use the API to pull data into your own models, dashboards, or investor reports — no manual spreadsheet wrangling.",
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

        {/* Pricing */}
        <section className="py-24 px-6 border-t border-cream-border" id="pricing">
          <div className="max-w-prose mx-auto text-center">
            <h2 className="font-serif text-[1.75rem] text-ink mb-4">
              Simple pricing
            </h2>
            <p className="text-body-sm text-ink-muted mb-16">
              No surprise bills. No data resale. Your calls are yours.
            </p>

            <div className="space-y-4 max-w-sm mx-auto text-left">
              {[
                {
                  tier: "Free",
                  price: "$0",
                  calls: "100 calls/day",
                  feature: "All data fields",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$29",
                  calls: "10,000 calls/day",
                  feature: "Historical trends",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$99",
                  calls: "Unlimited calls",
                  feature: "Bulk export + API",
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
          </div>
        </section>

        {/* API Preview */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-12 text-center">
              One request. All the data.
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl https://api.neighborhooddb.io/v1/zip/78704 \\
  -H "Authorization: Bearer YOUR_API_KEY"`}</code>
                </pre>
              </div>

              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "zip": "78704",
  "median_home_price": 685000,
  "days_on_market": 18,
  "price_per_sqft": 524,
  "median_rent": 2340,
  "yoy_appreciation": 0.082,
  "cap_rate_estimate": 0.051,
  "school_rating": 7,
  "updated_at": "2026-03-01"
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
            <span className="font-serif text-lg text-ink">NEIGHBORHOODDB</span>
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
            &copy; 2026 NEIGHBORHOODDB. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
