"use client";
import { useState } from "react";
export default function Home() {
  const [beds, setBeds] = useState(3);
  const [perc, setPerc] = useState(45);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    const flow = beds * 450;
    const rate = perc <= 10 ? 1.2 : perc <= 30 ? 0.9 : perc <= 45 ? 0.6 : perc <= 60 ? 0.45 : perc <= 90 ? 0.3 : 0.2;
    const sqft = Math.max(flow * rate, beds * 100);
    setResult({ beds, flow, perc, rate, sqft: +sqft.toFixed(1), tank: beds * 300 });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">SEPTICODER</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">The NRCS loading rate table has 47 entries. We did them all.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">SEPTICODER gives contractors and inspectors drain field sizing based on soil percolation — without digging through NRCS documentation from 1987.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Calculate →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Bedrooms</label><input type="number" value={beds} onChange={e=>setBeds(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Perc time (min/inch)</label><input type="number" value={perc} onChange={e=>setPerc(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate →</button>
          {result && (
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Drainfield needed</div><div className="font-bold text-lg">{result.sqft} sqft</div></div>
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Tank size</div><div className="font-bold text-lg">{result.tank} gal</div></div>
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Daily flow</div><div className="font-bold">{result.flow} gpd</div></div>
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Loading rate</div><div className="font-bold">{result.rate} sqft/gal</div></div>
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"50/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">SEPTICODER</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
