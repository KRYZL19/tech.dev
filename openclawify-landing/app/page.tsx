"use client";

import { useState } from "react";

export default function Home() {
  const [activeTab, setActiveTab] = useState<"curl" | "python" | "javascript">("curl");

  const codeExamples = {
    curl: {
      request: `curl -X POST https://api.openclawify.io/v1/generate \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "description": "Monitor server disk space and text me if it goes below 10%. Run every hour."
  }'`,
      response: `{
  "skill": {
    "name": "disk-space-monitor",
    "yaml_validated": true,
    "tools": ["exec", "session-send"],
    "trigger": { "cron": "0 * * * *" },
    "deploy_checklist": {
      "dependencies": 3,
      "permissions": 1,
      "setup_minutes": 10
    }
  }
}`,
    },
    python: {
      request: `import requests

response = requests.post(
    "https://api.openclawify.io/v1/generate",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    json={
        "description": "Monitor server disk space and text me if it goes below 10%. Run every hour."
    },
)

skill = response.json()
print(f"Skill generated: {skill['skill']['name']}")`,
      response: `{
  "skill": {
    "name": "disk-space-monitor",
    "yaml_validated": true,
    "tools": ["exec", "session-send"],
    "trigger": { "cron": "0 * * * *" },
    "deploy_checklist": {
      "dependencies": 3,
      "permissions": 1,
      "setup_minutes": 10
    }
  }
}`,
    },
    javascript: {
      request: `const response = await fetch("https://api.openclawify.io/v1/generate", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    description: "Monitor server disk space and text me if it goes below 10%. Run every hour.",
  }),
});

const { skill } = await response.json();
console.log(\`Skill generated: \${skill.name}\`);`,
      response: `{
  "skill": {
    "name": "disk-space-monitor",
    "yaml_validated": true,
    "tools": ["exec", "session-send"],
    "trigger": { "cron": "0 * * * *" },
    "deploy_checklist": {
      "dependencies": 3,
      "permissions": 1,
      "setup_minutes": 10
    }
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
            OPENCLAWIFY
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
              OpenClaw Skill Generator API
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Describe your workflow in plain English.
              <br />
              Get a working OpenClaw skill.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              OPENCLAWIFY generates OpenClaw skills from plain-English
              descriptions — ready to deploy, with YAML validation and
              deployment checklists.
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
              Free tier · No credit card · 20 calls/day
            </p>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <blockquote className="font-serif text-2xl text-ink leading-relaxed italic text-center max-w-2xl mx-auto">
              &ldquo;Writing a good OpenClaw skill requires knowing the SKILL.md
              format, tool patterns, and YAML structure. That&rsquo;s not
              automation — that&rsquo;s a learning curve.&rdquo;
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
                  <label className="block text-body-sm text-ink-muted mb-2 uppercase tracking-wider">
                    Your workflow description
                  </label>
                  <div className="bg-cream-bg border border-cream-border rounded p-4 text-body-sm text-ink font-mono leading-relaxed">
                    I want an agent that monitors my server and texts me if disk
                    space goes below 10%. It should run every hour.
                  </div>
                </div>

                <div className="border-t border-cream-border pt-6">
                  <p className="text-body-sm text-ink-muted mb-4 uppercase tracking-wider">
                    Generated skill
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Skill name
                      </span>
                      <span className="text-body-sm text-ink font-medium font-mono">
                        disk-space-monitor
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        YAML validated
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        ✅
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">Tools</span>
                      <span className="text-body-sm text-ink font-medium font-mono">
                        exec, session-send
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Trigger
                      </span>
                      <span className="text-body-sm text-ink font-medium font-mono">
                        cron(0 * * * *)
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        Deploy checklist
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        3 dependencies · 1 permission needed · ~10min setup
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
                  Generate your skill →
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
                  title: "Describe your workflow",
                  desc: "Write what you want in plain English. No format knowledge required — just describe the outcome.",
                },
                {
                  step: "2",
                  title: "We generate the skill",
                  desc: "OPENCLAWIFY produces a valid SKILL.md with the right tool calls, triggers, and YAML structure.",
                },
                {
                  step: "3",
                  title: "Deploy with confidence",
                  desc: "Get a deployment checklist with dependencies, permissions, and setup time before you start.",
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
                  title: "OpenClaw users building custom skills",
                  desc: "Skip the format docs. Describe what you need and get a working skill in seconds.",
                },
                {
                  title: "Automation consultants",
                  desc: "Rapidly prototype and deliver skill solutions for clients without deep OpenClaw knowledge.",
                },
                {
                  title: "DevOps teams",
                  desc: "Generate monitoring, alerting, and maintenance agents from plain operational requirements.",
                },
                {
                  title: "AI developers",
                  desc: "Integrate skill generation into AI-powered workflows and autonomous agent pipelines.",
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
                  calls: "20 calls/day",
                  feature: "All core features",
                  cta: "Get started",
                },
                {
                  tier: "Dev",
                  price: "$19",
                  calls: "1,000 calls/day",
                  feature: "Priority generation",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$49",
                  calls: "10,000 calls/day",
                  feature: "Custom templates",
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
              Start generating in minutes
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Tabs */}
              <div className="flex border-b border-cream-border">
                {(["curl", "python", "javascript"] as const).map((tab) => (
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
            <span className="font-serif text-lg text-ink">OPENCLAWIFY</span>
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
            &copy; 2026 OPENCLAWIFY. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
