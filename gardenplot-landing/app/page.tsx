"use client";
import { useState } from "react";
export default function Home() {
  const [location, setLocation] = useState("austin_tx");
  const [plant, setPlant] = useState("tomato");
  const [result, setResult] = useState<any>(null);
  const locs: Record<string,any> = {
    austin_tx: {zone:"8b",last_frost:"Mar 5",first_frost:"Nov 22",grow_days:261},
    denver_co: {zone:"5b",last_frost:"May 5",first_frost:"Oct 1",grow_days:149},
    chicago_il: {zone:"6a",last_frost:"Apr 20",first_frost:"Oct 20",grow_days:183},
    seattle_wa: {zone:"9a",last_frost:"Mar 15",first_frost:"Nov 15",grow_days:245},
    minneapolis_mn: {zone:"4b",last_frost:"May 10",first_frost:"Sep 25",grow_days:138},
  };
  const plants: Record<string,any> = {
    tomato:{days:80,spacing:24,yield:"10 lbs",hardiness:"frost tender"},
    pepper:{days:75,spacing:18,yield:"5 lbs",hardiness:"frost tender"},
    lettuce:{days:45,spacing:12,yield:"0.5 lbs",hardiness:"frost hardy"},
    kale:{days:55,spacing:18,yield:"2 lbs",hardiness:"frost hardy"},
    cucumber:{days:60,spacing:36,yield:"8 lbs",hardiness:"frost tender"},
  };
  const calc = () => {
    const l = locs[location], p = plants[plant];
    const canPlant = l.grow_days >= p.days + 21;
    setResult({ ...l, ...p, canPlant });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">GARDENPLOT</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Last frost March 5th. Plant tomatoes. Or lose the whole crop.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">GARDENPLOT gives garden apps and seed companies USDA hardiness zones, frost dates, and planting calendars by location — without scraping a dozen extension office websites.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Location</label>
              <select value={location} onChange={e=>setLocation(e.target.value)} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm">
                {Object.entries(locs).map(([k,v])=><option key={k} value={k}>{v.zone} — {k.replace("_"," ").toUpperCase()}</option>)}
              </select>
            </div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Plant</label>
              <select value={plant} onChange={e=>setPlant(e.target.value)} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm">
                {Object.entries(plants).map(([k,v])=><option key={k} value={k}>{k.charAt(0).toUpperCase()+k.slice(1)} ({v.days}d)</option>)}
              </select>
            </div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate planting dates →</button>
          {result && (
            <div className="space-y-3">
              <div className={`rounded p-3 text-center text-sm ${result.canPlant ? "bg-green-50 border border-green-200" : "bg-yellow-50 border border-yellow-200"}`}>
                <span className="font-medium">{result.canPlant ? "✓ Safe to plant now" : "✗ Too early or too late for this season"}</span>
              </div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">USDA Zone</div><div className="font-bold">{result.zone}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Last frost</div><div className="font-bold">{result.last_frost}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Days to maturity</div><div className="font-bold">{result.days}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Spacing</div><div className="font-bold">{result.spacing}"</div></div>
              </div>
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">GARDENPLOT</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
