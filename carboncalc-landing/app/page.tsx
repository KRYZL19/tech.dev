"use client";
import { useState } from "react";
export default function Home() {
  const [cbm, setCbm] = useState(20);
  const [dist, setDist] = useState(11000);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    const cargo = cbm * 0.5;
    const co2 = cargo * dist * 10 / 1000;
    const truck = dist * 1.852 * 0.271;
    setResult({cbm, dist, cargo: cargo.toFixed(1), co2_kg: co2.toFixed(1), co2_lbs: (co2*2.20462).toFixed(1), truck_kg: truck.toFixed(1), savings: ((1-co2/truck)*100).toFixed(1)});
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">CARBONCALC</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Shanghai to Rotterdam emits 1.1 tons of CO2. The truck emits 5.5 tons. One query.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">CARBONCALC gives logistics platforms and ESG reporters real CO2 calculations using IMO and ICAO formulas — without maintaining emissions databases or building the math yourself.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Cargo volume (cbm)</label><input type="number" value={cbm} onChange={e=>setCbm(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Distance (nm)</label><input type="number" value={dist} onChange={e=>setDist(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate CO2 →</button>
          {result && (
            <div className="space-y-3">
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">CO2 by ship</div><div className="font-bold text-lg">{result.co2_kg} kg</div><div className="text-xs text-ink-muted">{result.co2_lbs} lbs</div></div>
                <div className="bg-cream-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">CO2 by truck</div><div className="font-bold text-lg">{result.truck_kg} kg</div><div className="text-xs text-ink-muted">same route</div></div>
              </div>
              <div className="bg-green-50 border border-green-200 rounded p-3 text-center text-sm">
                <span className="text-green-700 font-medium">Shipping saves {result.savings}% vs trucking</span>
              </div>
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">CARBONCALC</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
