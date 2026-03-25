"use client";

import { useState } from "react";

type Tab = "curl" | "python" | "javascript";

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>("curl");

  const codeExamples: Record<Tab, { request: string; response: string }> = {
    curl: {
      request: `curl -X POST https://api.ruffcheck.io/v1/lint \\
  -H "Content-Type: application/json" \\
  -d '{
    "code": "def unused_func(): pass",
    "language": "python"
  }'`,
      response: `[
  {
    "line": 1,
    "column": 1,
    "rule": "F401",
    "severity": "error",
    "message": "unused_func is imported but unused",
    "fix": "remove this import"
  }
]`,
    },
    python: {
      request: `import requests

response = requests.post(
    "https://api.ruffcheck.io/v1/lint",
    json={
        "code": "def unused_func(): pass",
        "language": "python",
    },
)
print(response.json())`,
      response: `[
  {
    "line": 1,
    "column": 1,
    "rule": "F401",
    "severity": "error",
    "message": "unused_func is imported but unused",
    "fix": "remove this import"
  }
]`,
    },
    javascript: {
      request: `const response = await fetch("https://api.ruffcheck.io/v1/lint", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    code: "def unused_func(): pass",
    language: "python",
  }),
});

const issues = await response.json();
console.log(JSON.stringify(issues, null, 2));`,
      response: `[
  {
    "line": 1,
    "column": 1,
    "rule": "F401",
    "severity": "error",
    "message": "unused_func is imported but unused",
    "fix": "remove this import"
  }
]`,
    },
  };

  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            RUFFCHECK
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
              Code Quality Linter API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Run ESLint, Ruff, or golangci-lint without installing anything.
              Just POST your code.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              RUFFCHECK gives CI/CD pipelines and code review tools instant lint
              feedback — no binaries, no config files, no local setup.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#demo"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Try the Demo
              </a>
              <a
                href="#get-started"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                View Docs
              </a>
            </div>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;Your lint check requires{' '}
              <code className="not-italic bg-cream-code px-1 rounded">
                npm install eslint
              </code>
              ,{' '}
              <code className="not-italic bg-cream-code px-1 rounded">
                pip install ruff
              </code>
              ,{' '}
              <code className="not-italic bg-cream-code px-1 rounded">
                brew install golangci-lint
              </code>{' '}
              — and they&rsquo;re all the wrong version.&rdquo;
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
                    Language
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded px-4 py-3 text-body-sm text-ink">
                    Python via Ruff
                  </div>
                </div>

                <div>
                  <label className="block text-body-sm text-ink-muted mb-2">
                    Code input
                  </label>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono">
                    def unused_func(): pass
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Lint result
                  </p>
                  <div className="bg-cream-code border border-cream-border rounded p-4 text-body-sm text-ink font-mono overflow-x-auto">
                    <span className="text-terracotta">&#91;</span>
                    {"\n"}
                    {"  "}
                    <span className="text-terracotta">&#123;</span>
                    {"\n"}
                    {"    "}
                    <span className="text-ink-muted">&quot;line&quot;</span>
                    {": 1, "}
                    <span className="text-ink-muted">&quot;column&quot;</span>
                    {": 1, "}
                    <span className="text-ink-muted">&quot;rule&quot;</span>
                    {": "}
                    <span className="text-ink-muted">&quot;F401&quot;</span>
                    {",\n    "}
                    <span className="text-ink-muted">&quot;severity&quot;</span>
                    {": "}
                    <span className="text-ink-muted">&quot;error&quot;</span>
                    {",\n    "}
                    <span className="text-ink-muted">&quot;message&quot;</span>
                    {": "}
                    <span className="text-ink-muted">
                      &quot;unused_func is imported but unused&quot;
                    </span>
                    {",\n    "}
                    <span className="text-ink-muted">&quot;fix&quot;</span>
                    {": "}
                    <span className="text-ink-muted">
                      &quot;remove this import&quot;
                    </span>
                    {"\n  "}
                    <span className="text-terracotta">&#125;</span>
                    {"\n"}
                    <span className="text-terracotta">&#93;</span>
                  </div>
                </div>
              </div>

              <div className="text-center">
                <a
                  href="#get-started"
                  className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
                >
                  Get API Key →
                </a>
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
                  title: "POST your code",
                  desc: "Send your source code and specify the language. We handle the rest — no SDK, no install.",
                },
                {
                  step: "2",
                  title: "We run the linter",
                  desc: "RUFFCHECK executes ESLint, Ruff, or golangci-lint in a sandboxed environment. Any version, any config.",
                },
                {
                  step: "3",
                  title: "Get structured results",
                  desc: "Receive a clean JSON array of issues with rule IDs, severity, line numbers, and suggested fixes.",
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
                  title: "CI/CD pipelines",
                  desc: "Add lint checks to GitHub Actions, GitLab CI, or any pipeline with a single POST request.",
                },
                {
                  title: "Code review bots",
                  desc: "Hook into pull requests and get lint results as comments — without installing anything on your server.",
                },
                {
                  title: "Editor integrations",
                  desc: "Power LSP plugins and browser-based IDEs that need lint results without local tooling.",
                },
                {
                  title: "Pre-commit hook replacements",
                  desc: "Replace brittle pre-commit setups with a fast API call that works in any environment.",
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
                  calls: "50 calls/day",
                  feature: "All linters",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "50,000 calls/month",
                  feature: "Priority queue",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$59",
                  calls: "200,000 calls/month",
                  feature: "Custom configs + webhooks",
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
              Start linting in minutes
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
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded font-mono">
                  <code>{codeExamples[activeTab].request}</code>
                </pre>
              </div>

              {/* Response */}
              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded font-mono">
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
            <span className="font-serif text-lg text-ink">RUFFCHECK</span>
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
            &copy; 2026 RUFFCHECK. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
