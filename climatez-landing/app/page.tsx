"use client";
import { useState } from "react";
export default function Home() {
  const [zip, setZip] = useState("78701");
  const [result, setResult] = useState<any>(null);
  const data: Record<string,any> = {
    "78701":{city:"Austin, TX",zone:"8b",last_frost:"Mar 5",first_frost:"Nov 22",grow_days:261,precip:34.2,wettest:"May",avg_high:79,avg_low:58},
    "10001":{city:"New York, NY",zone:"7b",last_frost:"Apr 10",first_frost:"Nov 5",grow_days:209,precip:49.9,wettest:"Sep",avg_high:64,avg_low:49},
    "60601":{city:"Chicago, IL",zone:"6a",last_frost:"Apr 20",first_frost:"Oct 20",grow_days:183,precip:38.0,wettest:"Jul",avg_high:59,avg_low:44},
    "98101":{city:"Seattle, WA",zone:"9a",last_frost:"Mar 15",first_frost:"Nov 15",grow_days:245,precip:37.4,wettest:"Nov",avg_high:60,avg_low:46},
    "33101":{city:"Miami, FL",zone:"10b",last_frost:null,first_frost:null,grow_days:365,precip:61.9,wettest:"Aug",avg_high:83,avg_low:72},
    "80301":{city:"Boulder, CO",zone:"5b",last_frost:"May 5",first_frost:"Oct 1",grow_days:149,precip:20.1,wettest:"May",avg_high:62,avg_low:36},
  };
  const lookup = () => setResult(data[zip] || { error: "Zip not in demo database" });
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">CLIMATEZ</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Frost date history for this zip. 30-year normals. One query.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">CLIMATEZ gives agricultural developers and insurance actuaries instant access to NOAA climate normals, frost dates, and precipitation data — without scraping the NOAA website or managing a 50GB dataset.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">"Your planting app needs the last frost date for zip 78701. The NOAA normals exist. The structured access doesn't."</p>
          <footer className="text-sm text-ink-muted mt-3">— Every developer who's tried to use climate data</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="flex gap-3"><input type="text" value={zip} onChange={e => setZip(e.target.value)} placeholder="Zip code" className="border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm flex-1"/><button onClick={lookup} className="bg-terracotta text-white px-5 py-2 rounded font-medium text-sm">Lookup</button></div>
          <div className="grid grid-cols-5 gap-2 text-xs">{Object.keys(data).map(z => <button key={z} onClick={()=>{setZip(z);setResult(data[z])}} className="bg-cream-100 rounded px-2 py-1.5 text-center font-mono hover:border-terracotta border border-transparent">{z}</button>)}</div>
          {result && !result.error && (
            <div>
              <div className="text-sm font-medium mb-3">{result.city} · Zone {result.zone}</div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Last frost (spring)</div><div className="font-bold">{result.last_frost || "None"}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">First frost (fall)</div><div className="font-bold">{result.first_frost || "None"}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Growing season</div><div className="font-bold">{result.grow_days} days</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Avg precipitation</div><div className="font-bold">{result.precip}"/year</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Wettest month</div><div className="font-bold">{result.wettest}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Avg high/low</div><div className="font-bold">{result.avg_high}°F / {result.avg_low}°F</div></div>
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
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">CLIMATEZ</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
