export default function Home() {
  return (
    <div className="min-h-screen bg-cream-bg">
      {/* Header */}
      <header className="border-b border-cream-border">
        <div className="max-w-prose mx-auto px-6 py-5 flex items-center justify-between">
          <span className="font-serif text-xl tracking-wide text-ink">
            CLINICALTRL
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
            <a
              href="#use-cases"
              className="text-body-sm text-ink-muted hover:text-ink transition-colors"
            >
              Use Cases
            </a>
          </nav>
        </div>
      </header>

      <main>
        {/* Hero */}
        <section className="pt-24 pb-32 px-6">
          <div className="max-w-prose mx-auto text-center">
            <p className="text-body-sm text-ink-muted uppercase tracking-widest mb-6">
              Clinical Trial Results Database
            </p>
            <h1 className="font-serif text-[2.5rem] leading-tight text-ink mb-8">
              Find all phase 3 trials for semaglutide with positive results.
              One query.
            </h1>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto mb-10">
              CLINICALTRL gives researchers and investors instant access to
              clinical trial data — without ClinicalTrials.gov&apos;s terrible UI.
            </p>
            <div className="flex items-center justify-center gap-6 flex-wrap">
              <a
                href="#demo"
                className="inline-block bg-terracotta text-white font-sans text-body-sm px-6 py-3 rounded hover:bg-terracotta-hover transition-colors"
              >
                Try the Demo
              </a>
              <a
                href="#api"
                className="text-body-sm text-ink-muted underline underline-offset-4 hover:text-ink transition-colors"
              >
                API Docs
              </a>
            </div>
          </div>
        </section>

        {/* The Problem */}
        <section className="py-24 px-6 border-t border-cream-border">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8 mb-10">
              <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                The Problem
              </p>
              <p className="font-serif text-xl text-ink leading-relaxed italic">
                &ldquo;You&apos;re researching which GLP-1 drugs completed phase 3
                with positive results. ClinicalTrials.gov returns 847 results.
                Nobody has time for that.&rdquo;
              </p>
            </div>
            <p className="text-body-lg text-ink-muted max-w-xl mx-auto text-center">
              CLINICALTRL is a queryable database of clinical trial outcomes —
              structured, filtered, and actually usable.
            </p>
          </div>
        </section>

        {/* Demo Card */}
        <section className="py-24 px-6 border-t border-cream-border" id="demo">
          <div className="max-w-prose mx-auto">
            <div className="bg-cream-surface border border-cream-border rounded shadow-card p-8">
              <div className="text-center mb-10">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-2">
                  Try it — no signup
                </p>
                <p className="font-serif text-xl text-ink">
                  Instant clinical trial search
                </p>
              </div>

              <div className="space-y-6">
                {/* Input */}
                <div>
                  <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                    Query
                  </p>
                  <div className="bg-cream-code rounded p-4 space-y-2">
                    {[
                      { label: "Drug", value: "semaglutide" },
                      { label: "Phase", value: "3" },
                      { label: "Results", value: "positive" },
                      { label: "Status", value: "completed" },
                    ].map(({ label, value }) => (
                      <div
                        key={label}
                        className="flex items-center gap-3"
                      >
                        <span className="text-body-sm text-ink-muted min-w-[60px]">
                          {label}:
                        </span>
                        <span className="text-body-sm text-ink font-mono">
                          {value}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Arrow */}
                <div className="flex justify-center">
                  <div className="text-terracotta text-2xl leading-none">↓</div>
                </div>

                {/* Output */}
                <div>
                  <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                    Results
                  </p>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Trials found
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        12 trials
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Most recent
                      </span>
                      <span className="text-body-sm text-ink font-mono">
                        NCT04657055
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Title
                      </span>
                      <span className="text-body-sm text-ink font-medium text-right max-w-[280px]">
                        Semaglutide 2.4mg for obesity
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Result
                      </span>
                      <span className="text-body-sm text-terracotta font-medium">
                        Positive
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Sponsor
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        Novo Nordisk
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2 border-b border-cream-border">
                      <span className="text-body-sm text-ink-muted">
                        Enrollment
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        1,700
                      </span>
                    </div>
                    <div className="flex justify-between items-center py-2">
                      <span className="text-body-sm text-ink-muted">
                        Completion
                      </span>
                      <span className="text-body-sm text-ink font-medium">
                        March 2025
                      </span>
                    </div>
                  </div>
                </div>
              </div>
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
                  title: "Pharma researchers",
                  desc: "Track competing drug pipelines and filter trials by outcome, phase, and sponsor in seconds.",
                },
                {
                  title: "Biotech investors",
                  desc: "Due diligence without reading 847 unstructured records. Know exactly which trials succeeded.",
                },
                {
                  title: "Medical writers",
                  desc: "Source accurate trial data for publications, press releases, and regulatory documents.",
                },
                {
                  title: "Clinical operations",
                  desc: "Monitor competitor enrollment status and completion timelines across therapeutic areas.",
                },
                {
                  title: "Patient advocacy groups",
                  desc: "Track which treatments are furthest along and what results they&apos;ve shown.",
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

        {/* API Overview */}
        <section className="py-24 px-6 border-t border-cream-border" id="api">
          <div className="max-w-prose mx-auto">
            <h2 className="font-serif text-[1.75rem] text-ink mb-16 text-center">
              Simple REST API
            </h2>

            <div className="bg-cream-surface border border-cream-border rounded shadow-card overflow-hidden">
              {/* Request */}
              <div className="p-6 border-b border-cream-border">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Request
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`curl -X GET \\
  "https://api.clinicaltrl.com/v1/trials?`}{`\\
    drug=semaglutide&`}{`\\
    phase=3&`}{`\\
    result=positive&`}{`\\
    status=completed" \\
  -H "Authorization: Bearer YOUR_API_KEY"`}</code>
                </pre>
              </div>

              {/* Response */}
              <div className="p-6">
                <p className="text-body-sm text-ink-muted uppercase tracking-wider mb-4">
                  Response
                </p>
                <pre className="bg-cream-code text-ink text-body-sm overflow-x-auto p-4 rounded">
                  <code>{`{
  "trials": [
    {
      "nct_id": "NCT04657055",
      "title": "Semaglutide 2.4mg for obesity",
      "phase": 3,
      "result": "positive",
      "sponsor": "Novo Nordisk",
      "enrollment": 1700,
      "completion": "2025-03",
      "conditions": ["Obesity", "Overweight"],
      "interventions": ["Semaglutide 2.4mg"]
    }
  ],
  "total": 12,
  "page": 1,
  "per_page": 20
}`}</code>
                </pre>
              </div>
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
                  feature: "All filters & fields",
                  cta: "Get API Key",
                },
                {
                  tier: "Dev",
                  price: "$49",
                  calls: "10,000 calls/day",
                  feature: "Full history access",
                  cta: "Start building",
                },
                {
                  tier: "Pro",
                  price: "$149",
                  calls: "Unlimited calls",
                  feature: "Bulk export + webhooks",
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
                    href="#"
                    className="text-body-sm text-terracotta hover:text-terracotta-hover transition-colors whitespace-nowrap ml-4"
                  >
                    {cta} →
                  </a>
                </div>
              ))}
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-cream-border py-8 px-6">
        <div className="max-w-prose mx-auto">
          <div className="flex items-center justify-between mb-6">
            <span className="font-serif text-lg text-ink">CLINICALTRL</span>
            <nav className="flex items-center gap-6">
              <a
                href="#api"
                className="text-body-sm text-ink-muted hover:text-ink transition-colors"
              >
                API Docs
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
            &copy; 2026 CLINICALTRL. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
