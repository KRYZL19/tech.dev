"use client";
import { useState } from "react";
export default function Home() {
  const [boat, setBoat] = useState("boston_whaler_380");
  const [hours, setHours] = useState(6);
  const [result, setResult] = useState<any>(null);
  const boats: Record<string, any> = {
    boston_whaler_380: { make: "Boston Whaler", model: "380 Realm", year: 2022, fuel_gal: 445, burn_gph: 8.5, hull_speed_knots: 46 },
    sea_ray_320: { make: "Sea Ray", model: "320 Sundancer", year: 2021, fuel_gal: 200, burn_gph: 12, hull_speed_knots: 28.5 },
    grady_white_370: { make: "Grady-White", model: "Express 370", year: 2023, fuel_gal: 402, burn_gph: 9, hull_speed_knots: 43 },
    jeanneau_379: { make: "Jeanneau", model: "379 Deck Salon", year: 2019, fuel_gal: 53, burn_gph: 2.5, hull_speed_knots: 7.2 },
    sabrett_450: { make: "Sabrett", model: "450 Convertible", year: 2021, fuel_gal: 902, burn_gph: 22, hull_speed_knots: 34 },
  };
  const run = () => {
    const b = boats[boat];
    const burn = hours * b.burn_gph;
    const range = (b.fuel_gal - burn) / b.burn_gph * b.hull_speed_knots;
    setResult({ ...b, hours, fuel_used: burn.toFixed(1), fuel_remaining: (b.fuel_gal - burn).toFixed(1), range_nm: range.toFixed(0) });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">MARINEDB</div>
        <nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav>
      </header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">The data you'd spend an hour digging through boat forums. One call.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">Sea Ray's website has specs for the 320 Sundancer. Boston Whaler's site has the 380 Realm. MARINEDB gives you both — with fuel burn estimates and insurance quotes built in.</p>
        <button onClick={run} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try the demo →</button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">"I need fuel burn for a 6-hour run to the Dry Tortugas. I have a 380 Whaler. I called my dealer and left a message."</p>
          <footer className="text-sm text-ink-muted mt-3">— Every boat owner who's tried to plan a serious trip</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">Fuel burn calculator</h2>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Boat</label>
              <select value={boat} onChange={e => setBoat(e.target.value)} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm">
                {Object.entries(boats).map(([id, b]) => <option key={id} value={id}>{b.make} {b.model}</option>)}
              </select>
            </div>
            <div>
              <label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">Run duration (hours)</label>
              <input type="number" value={hours} onChange={e => setHours(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm" />
            </div>
          </div>
          <button onClick={run} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate →</button>
          {result && (
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Fuel used</div><div className="font-bold text-lg">{result.fuel_used} gal</div></div>
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Remaining</div><div className="font-bold text-lg">{result.fuel_remaining} gal</div></div>
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Est. range</div><div className="font-bold">{result.range_nm} nm</div></div>
              <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Hull speed</div><div className="font-bold">{result.hull_speed_knots} kts</div></div>
            </div>
          )}
        </div>
      </section>
      <section id="docs" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">API</h2>
        <div className="bg-ink text-cream-100 rounded-lg p-5 font-mono overflow-x-auto">
          <pre className="text-xs leading-relaxed">{`curl https://api.marinedb.io/v1/boat/boston_whaler_380

curl -X POST https://api.marinedb.io/v1/fuel-calc \\
  -d '{"boat_id":"boston_whaler_380","hours_run":6}'

curl -X POST https://api.marinedb.io/v1/insurance \\
  -d '{"boat_id":"boston_whaler_380","value_usd":480000}'`}</pre>
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <p className="text-sm text-ink-muted mb-6">7 boat models included. Adding yours on request.</p>
        <div className="grid grid-cols-3 gap-4">
          {[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$19",calls:"10,000/day"},{tier:"Pro",price:"$49",calls:"100,000/day"}].map(p => (
            <div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5">
              <div className="text-xs text-ink-muted uppercase">{p.tier}</div>
              <div className="text-2xl font-bold mt-1">{p.price}</div>
              <div className="text-xs text-ink-muted mt-1">{p.calls}</div>
            </div>
          ))}
        </div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">MARINEDB</span><span>Built by KRYZL19</span>
      </footer>
    </main>
  );
}
