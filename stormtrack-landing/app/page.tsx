"use client";
import { useState } from "react";
export default function Home() {
  const [temp, setTemp] = useState(95);
  const [rh, setRh] = useState(70);
  const [wind, setWind] = useState(10);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    // Heat index (NWS)
    let hi = temp >= 80 ? -42.379 + 2.04901523*temp + 10.14333127*rh - 0.22475541*temp*rh - 0.00683783*temp*temp - 0.05481717*rh*rh + 0.00122874*temp*temp*rh + 0.00085282*temp*rh*rh - 0.00000199*temp*temp*rh*rh : temp;
    // Wind chill
    let wc = temp <= 50 && wind >= 3 ? 35.74 + 0.6215*temp - 35.75*Math.pow(wind,0.16) + 0.4275*temp*Math.pow(wind,0.16) : temp;
    setResult({ hi: Math.round(hi), wc: Math.round(wc), danger: (hi as number) >= 103 || (wc as number) <= -25 });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">STORMTRACK</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Feels like 122°F. That's not a guess. That's the NWS formula.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">STORMTRACK gives weather apps and safety platforms NWS-standard heat index and wind chill calculations — plus tornado threat and hurricane category — without implementing the math yourself.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try the demo →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-3 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Temp (°F)</label><input type="number" value={temp} onChange={e => setTemp(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">RH (%)</label><input type="number" value={rh} onChange={e => setRh(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Wind (mph)</label><input type="number" value={wind} onChange={e => setWind(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate →</button>
          {result && (
            <div className="grid grid-cols-2 gap-4">
              <div className={`rounded p-4 text-center ${result.hi >= 103 ? "bg-red-50 border border-red-200" : "bg-cream-50"}`}><div className="text-xs text-ink-muted">Heat index</div><div className="text-3xl font-bold font-serif">{result.hi}°F</div><div className="text-xs text-ink-muted mt-1">{result.hi >= 130 ? "Extreme danger" : result.hi >= 103 ? "Danger" : result.hi >= 90 ? "Extreme caution" : "Caution"}</div></div>
              <div className={`rounded p-4 text-center ${result.wc <= 0 ? "bg-blue-50 border border-blue-200" : "bg-cream-50"}`}><div className="text-xs text-ink-muted">Wind chill</div><div className="text-3xl font-bold font-serif">{result.wc}°F</div><div className="text-xs text-ink-muted mt-1">{result.wc <= -25 ? "Extreme danger" : result.wc <= 0 ? "Danger" : "Caution"}</div></div>
            </div>
          )}
        </div>
      </section>
      <section id="docs" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">API</h2>
        <div className="bg-ink text-cream-100 rounded-lg p-5 font-mono overflow-x-auto"><pre className="text-xs leading-relaxed">{`curl "https://api.stormtrack.io/v1/heatindex?temp_f=95&rh_percent=70"
curl "https://api.stormtrack.io/v1/windchill?temp_f=10&wind_mph=15"
curl "https://api.stormtrack.io/v1/hurricane?wind_mph=145"
curl "https://api.stormtrack.io/v1/tornado?ef_scale=2&distance_mi=8&duration_min=3"`}</pre></div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p => (<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">STORMTRACK</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
