"use client";
import { useState } from "react";
export default function Home() {
  const [sizeA, setSizeA] = useState("245/45R18");
  const [sizeB, setSizeB] = useState("235/45R18");
  const [result, setResult] = useState<any>(null);
  const parse = (s: string) => {
    const m = s.match(/(\d+)\/(\d+)R(\d+)/);
    if (!m) return null;
    const w = parseInt(m[1]), a = parseInt(m[2]), r = parseInt(m[3]);
    const sw = (a/100)*w/25.4;
    const diam = 2*sw + r;
    return { width_mm:w, aspect:a, rim_in:r, sidewall_in:+sw.toFixed(2), diam_in:+diam.toFixed(2) };
  };
  const compare = () => {
    const a = parse(sizeA), b = parse(sizeB);
    if (!a || !b) { setResult({error:"Invalid size — use format: 245/45R18"}); return; }
    const diff = b.diam_in - a.diam_in;
    const err_pct = (diff / a.diam_in) * 100;
    setResult({ a, b, diff: diff.toFixed(2), err_pct: err_pct.toFixed(2), compatible: Math.abs(diff) < 0.5 });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">TIREMATCH</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Your speedometer says 60. You're doing 58.7. That's not a GPS error.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">Switching from 245/45R18 to 235/45R18 drops your diameter by 0.35 inches. TIREMATCH tells you exactly how much that throws off your speedometer — before your customer finds out.</p>
        <button onClick={compare} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try the demo →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Original tire</label><input type="text" value={sizeA} onChange={e => setSizeA(e.target.value)} placeholder="245/45R18" className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm font-mono"/></div>
            <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">New tire</label><input type="text" value={sizeB} onChange={e => setSizeB(e.target.value)} placeholder="235/45R18" className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm font-mono"/></div>
          </div>
          <button onClick={compare} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Compare →</button>
          {result && !result.error && (
            <div className="space-y-3">
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Original diameter</div><div className="font-bold">{result.a.diam_in}"</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">New diameter</div><div className="font-bold">{result.b.diam_in}"</div></div>
              </div>
              <div className={`rounded p-3 text-center text-sm ${result.compatible ? "bg-green-50 border border-green-200" : "bg-yellow-50 border border-yellow-200"}`}>
                <div className="font-medium">{result.compatible ? "✓ Compatible" : "⚠ Check Speedo calibration"}</div>
                <div className="text-xs text-ink-muted mt-1">Diameter diff: {result.diff > 0 ? "+" : ""}{result.diff}" ({result.err_pct > 0 ? "+" : ""}{result.err_pct}%)</div>
                {!result.compatible && <div className="text-xs mt-1">At 60mph indicated → {+(60*(1+parseFloat(result.err_pct)/100)).toFixed(1)}mph actual</div>}
              </div>
            </div>
          )}
          {result?.error && <p className="text-sm text-red-600">{result.error}</p>}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p => (<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">TIREMATCH</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
