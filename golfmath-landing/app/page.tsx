"use client";
import { useState } from "react";
export default function Home() {
  const [scores, setScores] = useState("82,78,88,76,90,84,79,91,77,85");
  const [par, setPar] = useState(72);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    const list = scores.split(",").map(s => parseInt(s.trim())).filter(s => !isNaN(s) && s > 0);
    if (list.length < 3) { setResult({error:"Need at least 3 scores"}); return; }
    const diffs = list.slice(-20).map(s => Math.max(s - par, 0) * 1.0).sort((a,b) => a-b);
    const n = diffs.length;
    const use = n >= 9 ? 8 : n >= 5 ? 5 : 3;
    const avg = diffs.slice(0, use).reduce((a,b) => a+b, 0) / use;
    const hi = +(avg * 0.96).toFixed(1);
    setResult({ hi, rounds: list.length, used: use, scores: list.slice(-use) });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">GOLFMATH</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Your handicap is 10.4. Here's how we got there.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">GOLFMATH calculates your USGA handicap index from your last 3-20 rounds. The math is public. We just implemented it cleanly.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Calculate handicap →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Scores (comma-separated)</label><input type="text" value={scores} onChange={e=>setScores(e.target.value)} className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm font-mono"/></div>
          <div className="grid grid-cols-2 gap-4">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Course par</label><input type="number" value={par} onChange={e=>setPar(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate →</button>
          {result && !result.error && (
            <div className="text-center">
              <div className="text-6xl font-bold font-serif text-terracotta mb-2">{result.hi}</div>
              <div className="text-sm text-ink-muted mb-4">Handicap Index · {result.rounds} rounds · best {result.used} differentials</div>
              <div className="text-xs text-ink-muted">{result.hi <= 0 ? "Scratch or better" : `${result.hi}-handicap player`}</div>
            </div>
          )}
          {result?.error && <p className="text-sm text-red-600">{result.error}</p>}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"50/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">GOLFMATH</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
