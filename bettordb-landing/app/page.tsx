"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");
  const [system, setSystem] = useState("martingale");
  const [baseBet, setBaseBet] = useState("10");
  const [bankroll, setBankroll] = useState("1000");
  const [bets, setBets] = useState("100");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl -X POST https://api.bettordb.io/v1/simulate \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "system": "martingale",
    "base_bet": 10,
    "bankroll": 1000,
    "num_bets": 100,
    "num_simulations": 100000
  }'`,
      response: `{
  "system": "martingale",
  "num_simulations": 100000,
  "prob_doubling": 0.312,
  "prob_ruin": 0.688,
  "median_ending_bankroll": 0,
  "mean_ending_bankroll": 487.20,
  "p10_bankroll": 0,
  "p90_bankroll": 1090
}`,
    },
    python: {
      request: `import requests

response = requests.post(
    "https://api.bettordb.io/v1/simulate",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    json={
        "system": "martingale",
        "base_bet": 10,
        "bankroll": 1000,
        "num_bets": 100,
        "num_simulations": 100000,
    },
)

result = response.json()
print(f"Probability of doubling: {result['prob_doubling']:.1%}")`,
      response: `{
  "system": "martingale",
  "num_simulations": 100000,
  "prob_doubling": 0.312,
  "prob_ruin": 0.688,
  "median_ending_bankroll": 0,
  "mean_ending_bankroll": 487.20,
  "p10_bankroll": 0,
  "p90_bankroll": 1090
}`,
    },
    javascript: {
      request: `const response = await fetch("https://api.bettordb.io/v1/simulate", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    system: "martingale",
    base_bet: 10,
    bankroll: 1000,
    num_bets: 100,
    num_simulations: 100000,
  }),
});

const result = await response.json();
console.log(\`Probability of doubling: \${(result.prob_doubling * 100).toFixed(1)}%\`);`,
      response: `{
  "system": "martingale",
  "num_simulations": 100000,
  "prob_doubling": 0.312,
  "prob_ruin": 0.688,
  "median_ending_bankroll": 0,
  "mean_ending_bankroll": 487.20,
  "p10_bankroll": 0,
  "p90_bankroll": 1090
}`,
    },
  };

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            BETTORDB
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
              Casino Probability API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              The math proves the martingale always loses.
              <br />
              Now prove it to your users.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              BETTORDB gives casino game developers and betting system
              researchers the probability data they need — without installing
              NumPy or running simulations locally.
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
              Free tier · No credit card · 1,000 sims/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;Every gambling system researcher runs the same 10
              simulations manually. Martingale, Fibonacci, D&rsquo;Alembert —
              the math is known. The data isn&rsquo;t easily accessible via
              API.&rdquo;
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
                    Betting system
                  </label>
                  <select
                    value={system}
                    onChange={(e) => setSystem(e.target.value)}
                    className="w-full border border-cream-border rounded bg-cream-bg text-ink px-4 py-3 text-body-sm focus:outline-none focus:border-terracotta transition-colors"
                  >
                    <option value="martingale">Martingale — double after loss</option>
                    <option value="fibonacci">Fibonacci — follow the sequence</option>
                    <option value="dalembert">D&rsquo;Alembert — raise after loss</option>
                    <option value="flat">Flat — same bet every time</option>
                  </select>
                </div>

                <div className="grid grid-cols-3 gap-4">
                  <div>
                    <label className="block text-body-sm text-ink-muted mb-2">
                      Base bet
                    </label>
                    <div className="flex items-center border border-cream-border rounded bg-cream-bg px-4 py-3">
                      <span className="text-body-sm text-ink-muted mr-1">$</span>
                      <input
                        type="number"
                        value={baseBet}
                        onChange={(e) => setBaseBet(e.target.value)}
                        className="bg-transparent text-ink text-body-sm w-full focus:outline-none"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-body-sm text-ink-muted mb-2">
                      Bankroll
                    </label>
                    <div className="flex items-center border border-cream-border rounded bg-cream-bg px-4 py-3">
                      <span className="text-body-sm text-ink-muted mr-1">$</span>
                      <input
                        type="number"
                        value={bankroll}
                        onChange={(e) => setBankroll(e.target.value)}
                        className="bg-transparent text-ink text-body-sm w-full focus:outline-none"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-body-sm text-ink-muted mb-2">
                      Number of bets
                    </label>
                    <input
                      type="number"
                      value={bets}
                      onChange={(e) => setBets(e.target.value)}
                      className="w-full border border-cream-border rounded bg-cream-bg text-ink px-4 py-3 text-body-sm focus:outline-none focus:border-terracotta transition-colors"
                    />
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Simulation result — 100,000 runs
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Probability of doubling
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        31.2%
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Probability of ruin
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        68.8%
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        Median ending bankroll
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        $0
                      </span>
                    </div>
                  </div>
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
                  title: "Choose a betting system",
                  desc: "Martingale, Fibonacci, D&rsquo;Alembert, Paroli, or flat betting. We handle the math behind each one.",
                },
                {
                  step: "2",
                  title: "Set your parameters",
                  desc: "Base bet, bankroll, number of bets, and number of simulations. POST to the API.",
                },
                {
                  step: "3",
                  title: "Get probability data",
                  desc: "Receive ruin probability, doubling odds, median ending bankroll, and percentiles — ready to display to users.",
                },
              ].map(({ step, title, desc }) => (
                <div key={step} className="text-center">
                  <div className="inline-flex items-center justify-center w-10 h-10 rounded-full border border-cream-border text-ink mb-5">
                    <span className="font-serif text-lg">{step}</span>
                  </div>
                  <h3
                    className="font-serif text-lg text-ink mb-3"
                    dangerouslySetInnerHTML={{ __html: title }}
                  />
                  <p
                    className="text-body-sm text-ink-muted leading-relaxed"
                    dangerouslySetInnerHTML={{ __html: desc }}
                  />
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
                  title: "Casino game developers",
                  desc: "Show players the true odds before they bet. Embed real probability data into your game UI.",
                },
                {
                  title: "Betting system researchers",
                  desc: "Run thousands of simulations in seconds. Compare systems without installing a single library.",
                },
                {
                  title: "Poker training software",
                  desc: "Feed probability data into training tools. Give students the numbers behind bankroll management.",
                },
                {
                  title: "Casino affiliate sites",
                  desc: "Publish credible, data-backed gambling content. Stand out from sites making up odds.",
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
                  sims: "1,000 sims/day",
                  feature: "All betting systems",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$49",
                  sims: "100,000 sims/day",
                  feature: "Priority support",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$199",
                  sims: "Unlimited simulations",
                  feature: "Custom system config",
                  cta: "Go production",
                },
              ].map(({ tier, price, sims, feature, cta }) => (
                <div
                  key={tier}
                  className="flex items-center justify-between bg-cream-surface border border-cream-border rounded p-5"
                >
                  <div>
                    <p className="font-serif text-lg text-ink">{tier}</p>
                    <p className="text-body-sm text-ink-muted">
                      {price}/mo · {sims} · {feature}
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
              Starting at $0.00002 per simulation beyond your tier limit.
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
              Start in minutes
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
            <span className="font-serif text-lg text-ink">BETTORDB</span>
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
            &copy; 2026 BETTORDB. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
