"use client";
import { useState } from "react";
export default function Home() {
  const [thickness, setThickness] = useState(2);
  const [width, setWidth] = useState(6);
  const [length, setLength] = useState(96);
  const [qty, setQty] = useState(10);
  const [priceBf, setPriceBf] = useState(4.50);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    const bfPerPiece = (thickness * width * length) / 144;
    const totalBf = bfPerPiece * qty;
    const linearFt = (length / 12) * qty;
    const cost = totalBf * priceBf;
    setResult({ bfPerPiece: bfPerPiece.toFixed(2), totalBf: totalBf.toFixed(1), linearFt: linearFt.toFixed(1), cost: cost.toFixed(2) });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">SAWMILL</div>
        <nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav>
      </header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">
          Board foot math. Without the scratch pad.
        </h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">
          SAWMILL gives sawyers and contractors board foot calculations, linear footage, and pricing estimates — without a scratch pad and a $4 calculator from Home Depot.
        </p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">
          Try it →
        </button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">
            "Customer wants a quote on 20 pieces of 2×6×8西部红柏. I don't have a board foot calculator on my phone. I use my head. Then I get it wrong."
          </p>
          <footer className="text-sm text-ink-muted mt-3">— Every sawyer, eventually</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">Board foot calculator</h2>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-3 gap-4 text-sm">
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Thickness (inches)</label>
              <select value={thickness} onChange={e => setThickness(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm">
                {[1,2,3,4,5,6,8,10,12].map(t => <option key={t} value={t}>{t}"</option>)}
              </select>
            </div>
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Width (inches)</label>
              <select value={width} onChange={e => setWidth(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm">
                {[2,3,4,5,6,8,10,12].map(w => <option key={w} value={w}>{w}"</option>)}
              </select>
            </div>
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Length (inches)</label>
              <input type="number" value={length} onChange={e => setLength(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Quantity</label>
              <input type="number" value={qty} onChange={e => setQty(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/>
            </div>
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Price per board foot ($)</label>
              <input type="number" step="0.01" value={priceBf} onChange={e => setPriceBf(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/>
            </div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">
            Calculate →
          </button>
          {result && (
            <div className="grid grid-cols-3 gap-3 text-sm">
              <div className="bg-cream-50 rounded p-3 text-center">
                <div className="text-xs text-ink-muted">Per piece</div>
                <div className="font-bold text-lg">{result.bfPerPiece} bd ft</div>
              </div>
              <div className="bg-cream-50 rounded p-3 text-center">
                <div className="text-xs text-ink-muted">Total board feet</div>
                <div className="font-bold text-lg">{result.totalBf}</div>
              </div>
              <div className="bg-cream-50 rounded p-3 text-center">
                <div className="text-xs text-ink-muted">Total cost</div>
                <div className="font-bold text-lg text-terracotta">${result.cost}</div>
              </div>
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <p className="text-sm text-ink-muted mb-6">Board foot math is simple. Your API shouldn't cost $50/mo.</p>
        <div className="grid grid-cols-3 gap-4">
          {[
            { tier: "Free", price: "$0", calls: "100/day" },
            { tier: "Dev", price: "$9", calls: "10,000/day" },
            { tier: "Pro", price: "$29", calls: "100,000/day" },
          ].map(p => (
            <div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5">
              <div className="text-xs text-ink-muted uppercase tracking-wide">{p.tier}</div>
              <div className="text-3xl font-bold mt-1">{p.price}</div>
              <div className="text-xs text-ink-muted mt-1">{p.calls}</div>
            </div>
          ))}
        </div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex items-center justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">SAWMILL</span>
        <span>Built by KRYZL19</span>
      </footer>
    </main>
  );
}
