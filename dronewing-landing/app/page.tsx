"use client";
import { useState } from "react";
export default function Home() {
  const [lat, setLat] = useState(34.05);
  const [lon, setLon] = useState(-118.24);
  const [alt, setAlt] = useState(100);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    const airports: [string,number,number][] = [["LAX",33.9425,-118.4081],["JFK",40.6413,-73.7781],["ORD",41.9742,-87.9073],["ATL",33.6407,-84.4277],["DFW",32.8998,-97.0403],["DEN",39.8561,-104.6737],["SFO",37.6213,-122.3790],["MIA",25.7959,-80.2870]];
    let found: any = null;
    for (const [airport,a_lat,a_lon] of airports) {
      const dist = Math.sqrt((lat-a_lat)**2+(lon-a_lon)**2)*69;
      if (dist < 5) { found={airport,dist:+dist.toFixed(1),airspace:"B",laanc:true,max_alt:100}; break; }
      else if (dist < 30) { found={airport,dist:+dist.toFixed(1),airspace:"B",laanc:true,max_alt:100}; break; }
    }
    if (!found) found={airspace:"G",laanc:false,max_alt:400,note:"No Class B within 30nm"};
    setResult(found);
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">DRONEWING</div></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">LAANC authorization in 30 seconds. Grid ID in one call.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">DRONEWING gives drone operators instant airspace compliance checks — LAANC authorization status, max altitude, airspace class — without navigating the FAA's broken LAANC portal.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Check airspace →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-3 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Latitude</label><input type="number" step="0.001" value={lat} onChange={e=>setLat(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Longitude</label><input type="number" step="0.001" value={lon} onChange={e=>setLon(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Altitude (ft)</label><input type="number" value={alt} onChange={e=>setAlt(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Check →</button>
          {result && (
            <div className="space-y-3">
              {result.airport ? (
                <div className="space-y-2">
                  <div className="text-center">
                    <div className="text-xs text-ink-muted">Nearest Class B airport</div>
                    <div className="text-2xl font-bold font-serif">{result.airport}</div>
                    <div className="text-xs text-ink-muted">{result.dist} nm away</div>
                  </div>
                  <div className="grid grid-cols-2 gap-3 text-sm">
                    <div className="bg-red-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">Airspace</div><div className="font-bold">Class {result.airspace}</div></div>
                    <div className="bg-red-50 rounded p-3 text-center"><div className="text-xs text-ink-muted">Max altitude</div><div className="font-bold">{result.max_alt} ft AGL</div></div>
                  </div>
                  <div className="bg-yellow-50 border border-yellow-200 rounded p-3 text-xs text-yellow-700">LAANC authorization required. Submit at an FAA-approved LAANC provider (Aloft, AirMap, or Kittyhawk).</div>
                </div>
              ) : (
                <div className="text-center space-y-2">
                  <div className="text-2xl font-bold font-serif">Class G</div>
                  <div className="text-sm text-ink-muted">Uncontrolled airspace — no authorization needed below {result.max_alt}ft AGL</div>
                  <div className="text-xs text-green-600">✓ Fly free up to 400ft AGL</div>
                </div>
              )}
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20"><h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2><div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"50/day"},{tier:"Dev",price:"$19",calls:"10,000/day"},{tier:"Pro",price:"$59",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div></section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">DRONEWING</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
