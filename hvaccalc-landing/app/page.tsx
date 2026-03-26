"use client";
import { useState } from "react";
export default function Home() {
  const [sqft, setSqft] = useState(2100);
  const [zone, setZone] = useState("4");
  const [result, setResult] = useState<any>(null);
  const zones: Record<string,any> = {"1":{n:"Zone 1",heat:30,cool:95},2:{n:"Zone 2",heat:10,cool:100},3:{n:"Zone 3",heat:5,cool:95},4:{n:"Zone 4",heat:0,cool:93},5:{n:"Zone 5",heat:-10,cool:91},6:{n:"Zone 6",heat:-20,cool:89},7:{n:"Zone 7",heat:-30,cool:86},8:{n:"Zone 8",heat:-40,cool:83}};
  const calc = () => { const z=zones[zone]; const cool=(sqft/13)*(z.cool-75)*1.08; const heat=(sqft/13)*(75-z.heat)*1.08; const tons=cool/12000; setResult({sqft,zone:z.n,cool_btu:+cool.toFixed(0),heat_btu:+heat.toFixed(0),tons:+tons.toFixed(1),warn:tons>5}); };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">HVACCALC</div></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Manual J is required by code. Nobody does it by hand.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">HVACCALC gives contractors and inspectors Manual J residential load calculations — simplified ACCA method, zone-based — without a $500/year software subscription or a mechanical engineering degree.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Floor area (sqft)</label><input type="number" value={sqft} onChange={e=>setSqft(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Climate zone</label><select value={zone} onChange={e=>setZone(e.target.value)} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm">{Object.entries(zones).map(([k,v])=><option key={k} value={k}>{k} — {v.n}</option>)}</select></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate load →</button>
          {result && (
            <div className="space-y-3">
              {result.warn&&<div className="bg-yellow-50 border border-yellow-200 rounded p-3 text-xs text-yellow-700">Possible oversizing — consider Manual J full calculation before specifying equipment.</div>}
              <div className="grid grid-cols-3 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">Cooling</div><div className="font-bold text-lg">{result.cool_btu.toLocaleString()}</div><div className="text-xs text-ink-muted">BTU/h</div></div>
                <div className="bg-cream-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">Equipment</div><div className="font-bold text-lg">{result.tons}</div><div className="text-xs text-ink-muted">tons AC</div></div>
                <div className="bg-cream-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">Heating</div><div className="font-bold text-lg">{result.heat_btu.toLocaleString()}</div><div className="text-xs text-ink-muted">BTU/h</div></div>
              </div>
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20"><h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2><div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"50/day"},{tier:"Dev",price:"$19",calls:"10,000/day"},{tier:"Pro",price:"$49",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div></section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">HVACCALC</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
