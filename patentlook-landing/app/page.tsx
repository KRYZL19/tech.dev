"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl -X GET "https://api.patentlook.io/v1/search" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d "q=solid-state+battery" \\
  -d "filed_after=2020-01-01" \\
  -d "cpc_class=H01M" \\
  -d "limit=10"`,
      response: `{
  "total": 847,
  "patents": [
    {
      "id": "US20240114682A1",
      "title": "Solid-state electrolyte with lithium superionic conductivity",
      "assignee": "Toyota Motor Corporation",
      "filed": "2023-09-14",
      "abstract": "A solid-state electrolyte exhibiting lithium ion conductivity..."
    },
    {
      "id": "US20240078921A1",
      "title": "All-solid-state battery with sulfide-based electrolyte",
      "assignee": "Samsung SDI Co., Ltd.",
      "filed": "2023-07-03",
      "abstract": "An all-solid-state battery comprising a positive electrode..."
    }
  ],
  "top_assignee": "Toyota"
}`,
    },
    python: {
      request: `import requests

response = requests.get(
    "https://api.patentlook.io/v1/search",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    params={
        "q": "solid-state battery",
        "filed_after": "2020-01-01",
        "cpc_class": "H01M",
        "limit": 10,
    },
)

data = response.json()
print(f"Found {data['total']} patents")
print(f"Top assignee: {data['top_assignee']}")`,
      response: `{
  "total": 847,
  "patents": [
    {
      "id": "US20240114682A1",
      "title": "Solid-state electrolyte with lithium superionic conductivity",
      "assignee": "Toyota Motor Corporation",
      "filed": "2023-09-14",
      "abstract": "A solid-state electrolyte exhibiting lithium ion conductivity..."
    },
    {
      "id": "US20240078921A1",
      "title": "All-solid-state battery with sulfide-based electrolyte",
      "assignee": "Samsung SDI Co., Ltd.",
      "filed": "2023-07-03",
      "abstract": "An all-solid-state battery comprising a positive electrode..."
    }
  ],
  "top_assignee": "Toyota"
}`,
    },
    javascript: {
      request: `const response = await fetch(
  "https://api.patentlook.io/v1/search" +
  "?q=solid-state+battery" +
  "&filed_after=2020-01-01" +
  "&cpc_class=H01M" +
  "&limit=10",
  {
    headers: { "Authorization": "Bearer YOUR_API_KEY" },
  }
);

const data = await response.json();
console.log(\`Found \${data.total} patents\`);
console.log(\`Top assignee: \${data.top_assignee}\`);`,
      response: `{
  "total": 847,
  "patents": [
    {
      "id": "US20240114682A1",
      "title": "Solid-state electrolyte with lithium superionic conductivity",
      "assignee": "Toyota Motor Corporation",
      "filed": "2023-09-14",
      "abstract": "A solid-state electrolyte exhibiting lithium ion conductivity..."
    },
    {
      "id": "US20240078921A1",
      "title": "All-solid-state battery with sulfide-based electrolyte",
      "assignee": "Samsung SDI Co., Ltd.",
      "filed": "2023-07-03",
      "abstract": "An all-solid-state battery comprising a positive electrode..."
    }
  ],
  "top_assignee": "Toyota"
}`,
    },
  };

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            PATENTLOOK
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
              US Patent Database API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Search 50 years of patents by technical claim, not just keyword.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              PATENTLOOK gives researchers, inventors, and legal professionals
              full-text patent search across titles, abstracts, claims, and
              inventor names — without a patent lawyer&apos;s budget.
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
              Free tier · No credit card · 50 calls/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto text-center">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic max-w-2xl mx-auto">
              &ldquo;Google Patents is free but searching by specific technical
              claims is painful. The USPTO bulk data exists. The structured
              access doesn&rsquo;t.&rdquo;
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
                {/* Input */}
                <div>
                  <p className="text-body-sm text-ink-muted mb-3 uppercase tracking-wider">
                    Query
                  </p>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono leading-relaxed">
                    <div className="text-ink-muted">// Search request</div>
                    <div>q: &quot;solid-state battery&quot;</div>
                    <div>filed_after: 2020-01-01</div>
                    <div>cpc_class: H01M</div>
                  </div>
                </div>

                {/* Output */}
                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Results
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Matching patents
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        847
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Top assignee
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        Toyota
                      </span>
                    </div>
                    <div className="py-2 border-b border-cream-border">
                      <div className="flex justify-between items-center mb-1">
                        <span className="text-body-sm text-ink-muted">
                          Most recent
                        </span>
                        <span className="text-body-sm text-ink font-medium">
                          US20240114682A1
                        </span>
                      </div>
                      <p className="text-body-sm text-ink-muted italic font-serif">
                        &ldquo;Solid-state electrolyte with lithium superionic
                        conductivity&rdquo;
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <div className="text-center">
                <a
                  href="#get-started"
                  className="inline-block text-body-sm text-terracotta hover:text-terracotta-hover transition-colors"
                >
                  Run this query with your API key →
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
                  title: "Query full-text fields",
                  desc: "Search across patent titles, abstracts, claims, and inventor names with structured filters for date, CPC class, and assignee.",
                },
                {
                  step: "2",
                  title: "Get structured results",
                  desc: "Receive clean JSON with patent IDs, filing dates, assignee names, and claim snippets — no HTML parsing required.",
                },
                {
                  step: "3",
                  title: "Build your product",
                  desc: "Integrate in minutes with SDKs for Python, JavaScript, and cURL. No patent law expertise needed on your end.",
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
                  title: "Patent attorneys",
                  desc: "Freedom-to-operate searches and prior art identification without the manual PTO portal grind.",
                },
                {
                  title: "Tech researchers",
                  desc: "Track emerging technologies across 50 years of filings by claim language, not just title keywords.",
                },
                {
                  title: "Investors doing due diligence",
                  desc: "Assess a company&apos;s patent portfolio and competitive moat before making investment decisions.",
                },
                {
                  title: "R&D teams",
                  desc: "Avoid duplicating existing work. Search by technical claim to see what&apos;s already been disclosed.",
                },
                {
                  title: "Journalists",
                  desc: "Research patent activity around breaking stories in EVs, biotech, semiconductors, and AI.",
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
                  calls: "50 calls/day",
                  feature: "Full-text search",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$29",
                  calls: "10,000 calls/month",
                  feature: "Priority support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$99",
                  calls: "100,000 calls/month",
                  feature: "Bulk export",
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
              Start searching in minutes
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
            <span className="font-serif text-lg text-ink">PATENTLOOK</span>
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
            &copy; 2026 PATENTLOOK. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
