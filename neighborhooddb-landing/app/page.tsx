"use client";
import { useState } from "react";
export default function Home() {
  const [zip, setZip] = useState("78704");
  const [result, setResult] = useState<any>(null);
  const zips: Record<string, any> = {
    "78704": { zip: "78704", city: "Austin, TX", median_price: 685000, median_rent: 2340, dom: 18, price_sqft: 524, yoy: 0.082, cap_rate: 0.051, schools: 7, walk: 72, crime: 42 },
    "94110": { zip: "94110", city: "San Francisco, CA", median_price: 1350000, median_rent: 3800, dom: 22, price_sqft: 1050, yoy: 0.041, cap_rate: 0.038, schools: 6, walk: 98, crime: 55 },
    "60614": { zip: "60614", city: "Chicago, IL (Lincoln Park)", median_price: 620000, median_rent: 2650, dom: 31, price_sqft: 415, yoy: 0.053, cap_rate: 0.058, schools: 8, walk: 91, crime: 38 },
    "30301": { zip: "30301", city: "Atlanta, GA", median_price: 445000, median_rent: 2100, dom: 14, price_sqft: 295, yoy: 0.091, cap_rate: 0.062, schools: 6, walk: 68, crime: 51 },
    "98101": { zip: "98101", city: "Seattle, WA (Downtown)", median_price: 895000, median_rent: 3200, dom: 12, price_sqft: 725, yoy: 0.034, cap_rate: 0.044, schools: 7, walk: 99, crime: 48 },
  };
  const lookup = () => setResult(zips[zip] || { error: "Zip not in demo database" });
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">NEIGHBORHOODDB</div>
        <nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav>
      </header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Average days on market, price per sqft, cap rate. By zip code. Updated monthly.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">NEIGHBORHOODDB gives real estate investors, property managers, and lenders instant access to neighborhood-level demographic and housing market data — without scraping Zillow or paying $500/mo for a full subscription.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">"I'm analyzing a rental property in 78704. I need cap rate, days on market, and school ratings. I've got four browser tabs open and two spreadsheets running."</p>
          <footer className="text-sm text-ink-muted mt-3">— Every real estate investor who's spent 2 hours on research</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">Try it</h2>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="flex gap-3">
            <input type="text" value={zip} onChange={e => setZip(e.target.value)} placeholder="Zip code" className="border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm flex-1" />
            <button onClick={lookup} className="bg-terracotta text-white px-5 py-2 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Lookup</button>
          </div>
          <div className="grid grid-cols-5 gap-2 text-xs">
            {["78704","94110","60614","30301","98101"].map(z => (
              <button key={z} onClick={() => { setZip(z); setResult(zips[z]); }} className="bg-cream-100 rounded px-2 py-1.5 text-center hover:border-terracotta border border-transparent transition-colors font-mono">{z}</button>
            ))}
          </div>
          {result && !result.error && (
            <div>
              <div className="text-sm font-medium mb-3">{result.city} · ZIP {result.zip}</div>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Median price</div><div className="font-bold text-base">${result.median_price.toLocaleString()}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Median rent</div><div className="font-bold">${result.median_rent.toLocaleString()}/mo</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Days on market</div><div className="font-bold">{result.dom}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">$/sqft</div><div className="font-bold">${result.price_sqft}</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">YoY change</div><div className={`font-bold ${result.yoy > 0 ? "text-green-600" : "text-red-600"}`}>+{(result.yoy*100).toFixed(1)}%</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Cap rate</div><div className="font-bold">{(result.cap_rate*100).toFixed(1)}%</div></div>
              </div>
            </div>
          )}
          {result?.error && <p className="text-sm text-red-600">{result.error}</p>}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">
          {[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$29",calls:"10,000/day"},{tier:"Pro",price:"$99",calls:"100,000/day"}].map(p => (
            <div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5">
              <div className="text-xs text-ink-muted uppercase">{p.tier}</div>
              <div className="text-2xl font-bold mt-1">{p.price}</div>
              <div className="text-xs text-ink-muted mt-1">{p.calls}</div>
            </div>
          ))}
        </div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">NEIGHBORHOODDB</span><span>Built by KRYZL19</span>
      </footer>
    </main>
  );
}
