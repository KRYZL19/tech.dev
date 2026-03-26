"use client";
import { useState } from "react";
export default function Home() {
  const [city, setCity] = useState("austin_tx");
  const [result, setResult] = useState<any>(null);
  const cities: Record<string,any> = {
    austin_tx:{city:"Austin, TX",code:"IBC 2021",adopted:"March 2022",amendments:7,permits:["residential","commercial","mechanical","electrical","plumbing"],setback:5,max_height:35},
    los_angeles_ca:{city:"Los Angeles, CA",code:"IBC 2022",adopted:"Jan 2024",amendments:15,permits:["residential","commercial","fire"],setback:5,max_height:45},
    new_york_ny:{city:"New York, NY",code:"NYC Building Code 2022",adopted:"July 2022",amendments:22,permits:["new building","alteration","demolition"],setback:10,max_height:210},
    chicago_il:{city:"Chicago, IL",code:"IBC 2021",adopted:"Nov 2022",amendments:11,permits:["new construction","renovation","electrical","plumbing"],setback:5,max_height:80},
    denver_co:{city:"Denver, CO",code:"IBC 2021",adopted:"Aug 2023",amendments:9,permits:["residential","commercial","accessory structure"],setback:5,max_height:35},
  };
  const lookup = () => setResult(cities[city]);
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">BUILDINGCODE</div></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">What version of the IBC does your city use? What did they adopt and when?</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">BUILDINGCODE gives contractors and architects instant access to IBC adoption dates, local amendments, permit types, and zoning setbacks — without calling the building department.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase block mb-1">City</label><select value={city} onChange={e=>setCity(e.target.value)} className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm">{Object.entries(cities).map(([k,v])=><option key={k} value={k}>{v.city}</option>)}</select></div>
          <button onClick={lookup} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Lookup →</button>
          {result && (
            <div className="space-y-3">
              <div className="text-sm font-medium mb-2">{result.city}</div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Code version</div><div className="font-bold">{result.code}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Adopted</div><div className="font-bold">{result.adopted}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Local amendments</div><div className="font-bold">{result.amendments}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Max height</div><div className="font-bold">{result.max_height} ft</div></div>
              </div>
              <div className="text-xs text-ink-muted">Permit types: {result.permits.join(", ")}</div>
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20"><h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2><div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"50/day"},{tier:"Dev",price:"$29",calls:"10,000/day"},{tier:"Pro",price:"$79",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div></section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">BUILDINGCODE</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
