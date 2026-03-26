"use client";
import { useState } from "react";
export default function Home() {
  const [call, setCall] = useState("W1ABC");
  const [result, setResult] = useState<any>(null);
  const calls: Record<string, any> = {
    "W1ABC": { callsign: "W1ABC", class: "Amateur Extra", frn: "0012345678", grid: "FN31", name: "John Smith", address: "Boston, MA", expiration: "2031-06-15", privileges: "All bands, all modes", since: 2015 },
    "K2XYZ": { callsign: "K2XYZ", class: "General", frn: "0023456789", grid: "FN20", name: "Jane Doe", address: "New York, NY", expiration: "2030-03-20", privileges: "HF + 6m/2m", since: 2019 },
    "KK4PQR": { callsign: "KK4PQR", class: "Amateur Extra", frn: "0045678901", grid: "EL87", name: "Alice Brown", address: "Miami, FL", expiration: "2032-01-10", privileges: "All bands, all modes", since: 2012 },
    "AI6ST": { callsign: "AI6ST", class: "General", frn: "0056789012", grid: "CM87", name: "Charlie Green", address: "San Francisco, CA", expiration: "2030-09-05", privileges: "HF + 6m/2m", since: 2017 },
  };
  const lookup = () => setResult(calls[call.toUpperCase()] || { error: "Not in demo database" });
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">FCCLOOKUP</div>
        <nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav>
      </header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Ham radio license lookup. No QRZ subscription needed.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">FCCLOOKUP gives antenna designers, propagation engineers, and DXers instant callsign lookup with license class, grid square, and band privileges. One call.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">"I need to verify a callsign for a contest log. My QRZ subscription expired. I'm not paying $30/yr to look up one call."</p>
          <footer className="text-sm text-ink-muted mt-3">— Every ham who values $30</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6">Try it — demo callsigns</h2>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-4 gap-2 text-xs">
            {Object.keys(calls).map(c => (
              <button key={c} onClick={() => { setCall(c); setResult(calls[c]); }} className="bg-cream-100 rounded px-2 py-1.5 text-center font-mono hover:border-terracotta border border-transparent transition-colors text-sm">{c}</button>
            ))}
          </div>
          {result && !result.error && (
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div><span className="text-xs text-ink-muted block">Callsign</span><span className="font-bold font-mono text-lg">{result.callsign}</span></div>
              <div><span className="text-xs text-ink-muted block">Class</span><span className="font-medium">{result.class}</span></div>
              <div><span className="text-xs text-ink-muted block">Grid</span><span className="font-mono">{result.grid}</span></div>
              <div><span className="text-xs text-ink-muted block">FRN</span><span className="font-mono text-xs">{result.frn}</span></div>
              <div><span className="text-xs text-ink-muted block">Privileges</span><span className="text-xs">{result.privileges}</span></div>
              <div><span className="text-xs text-ink-muted block">Expires</span><span className="text-xs">{result.expiration}</span></div>
            </div>
          )}
          {result?.error && <p className="text-sm text-red-600">{result.error}</p>}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">
          {[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p => (
            <div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5">
              <div className="text-xs text-ink-muted uppercase">{p.tier}</div>
              <div className="text-2xl font-bold mt-1">{p.price}</div>
              <div className="text-xs text-ink-muted mt-1">{p.calls}</div>
            </div>
          ))}
        </div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">FCCLOOKUP</span><span>Built by KRYZL19</span>
      </footer>
    </main>
  );
}
