"use client";
import { useState } from "react";
export default function Home() {
  const [coffee, setCoffee] = useState(21);
  const [water, setWater] = useState(340);
  const [tds, setTds] = useState(1.38);
  const [result, setResult] = useState<any>(null);
  const run = () => {
    const dissolved = water * (tds / 100);
    const yield_pct = (dissolved / coffee) * 100;
    const ratio = water / coffee;
    setResult({
      yield_pct: yield_pct.toFixed(2),
      dissolved_g: dissolved.toFixed(2),
      status: yield_pct < 18 ? "under" : yield_pct > 22 ? "over" : "optimal",
      ratio: `1:${ratio.toFixed(1)}`,
    });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">BREWCRUNCH</div>
        <nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav>
      </header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Your refractometer says 1.38% TDS. Now what?</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">BREWCRUNCH converts your refractometer reading into the SCA extraction yield standard. It tells you whether your shot is under, over, or dialed in — and what to adjust.</p>
        <button onClick={run} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">"I got a refractometer because V60s were inconsistent. It sat on the bench for three weeks. I had no idea what to do with 1.4%."</p>
          <footer className="text-sm text-ink-muted mt-3">— Every specialty coffee professional</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">Try it — no signup</h2>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-3 gap-4 text-sm">
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Coffee (g)</label>
              <input type="number" value={coffee} onChange={e => setCoffee(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm" />
            </div>
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Water (ml)</label>
              <input type="number" value={water} onChange={e => setWater(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm" />
            </div>
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">TDS (%)</label>
              <input type="number" step="0.01" value={tds} onChange={e => setTds(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm" />
            </div>
          </div>
          <button onClick={run} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate extraction yield →</button>
          {result && (
            <div className="space-y-3">
              <div className="text-center">
                <span className="text-5xl font-bold font-serif">{result.yield_pct}%</span>
                <div className={`text-sm mt-1 px-3 py-0.5 rounded-full inline-block ${result.status === "optimal" ? "bg-green-100 text-green-700" : result.status === "under" ? "bg-yellow-100 text-yellow-700" : "bg-red-100 text-red-700"}`}>
                  {result.status === "optimal" ? "Optimal — 18-22% is ideal" : result.status === "under" ? "Under-extracted — grind finer or increase temp" : "Over-extracted — grind coarser or reduce time"}
                </div>
              </div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3 text-center">
                  <div className="text-xs text-ink-muted">Brew ratio</div>
                  <div className="font-medium">{result.ratio}</div>
                </div>
                <div className="bg-cream-50 rounded p-3 text-center">
                  <div className="text-xs text-ink-muted">Dissolved solids</div>
                  <div className="font-medium">{result.dissolved_g}g</div>
                </div>
              </div>
            </div>
          )}
        </div>
      </section>
      <section id="docs" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">API</h2>
        <div className="bg-ink text-cream-100 rounded-lg p-5 font-mono overflow-x-auto">
          <pre className="text-xs leading-relaxed">{`curl -X POST https://api.brewcrunch.io/v1/extract \\
  -H "Content-Type: application/json" \\
  -d '{"coffee_g":21,"water_ml":340,"tds_percent":1.38}'

# Response
{ "extraction_yield_percent": 20.8, "status": "optimal" }

# Grind recommendations
curl https://api.brewcrunch.io/v1/grind/v60`}</pre>
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <p className="text-sm text-ink-muted mb-6">Free tier is enough for personal use and development.</p>
        <div className="grid grid-cols-3 gap-4">
          {[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p => (
            <div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5">
              <div className="text-xs text-ink-muted uppercase">{p.tier}</div>
              <div className="text-2xl font-bold mt-1">{p.price}</div>
              <div className="text-xs text-ink-muted mt-1">{p.calls}</div>
            </div>
          ))}
        </div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">BREWCRUNCH</span><span>Built by KRYZL19</span>
      </footer>
    </main>
  );
}
