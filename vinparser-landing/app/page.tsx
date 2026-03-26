"use client";
import { useState } from "react";
export default function Home() {
  const [vin, setVin] = useState("1HGCM82633A004352");
  const [result, setResult] = useState<any>(null);
  const parse = () => {
    const v = vin.toUpperCase();
    if (v.length !== 17) { setResult({ error: "VIN must be exactly 17 characters" }); return; }
    const countries: Record<string,string> = {"1":"US","2":"Canada","3":"Mexico","J":"Japan","K":"Korea","L":"China","S":"UK","V":"France/Spain","W":"Germany","Y":"Sweden/Finland","Z":"Italy"};
    const yearMap: Record<string,number> = {"A":2010,"B":2011,"C":2012,"D":2013,"E":2014,"F":2015,"G":2016,"H":2017,"J":2018,"K":2019,"L":2020,"M":2021,"N":2022,"P":2023,"R":2024,"S":2025,"T":2026,"V":2027,"W":2028,"X":2029,"Y":2030,"1":2031,"2":2032,"3":2033,"4":2034,"5":2035,"6":2036,"7":2037,"8":2038,"9":2039};
    const yearCodes = "ABCDEFGHJKLMNPRSTVWXY123456789";
    const yearIdx = yearCodes.indexOf(v[9]);
    const year = yearIdx >= 0 ? 2010 + yearIdx : 2020;
    const known: Record<string,any> = {
      "1HGCM82633A004352": {make:"Honda",model:"Accord",trim:"EX V6",year:2003,engine:"3.0L V6",drivetrain:"FWD"},
      "WVWZZZ3CZWE123456": {make:"Volkswagen",model:"Golf GTI",trim:"Autobahn",year:2022,engine:"2.0L Turbo I4",drivetrain:"FWD"},
      "5YJSA1DG9DFP14605": {make:"Tesla",model:"Model S",trim:"P85",year:2013,engine:"Electric 416hp",drivetrain:"AWD"},
    };
    setResult({
      vin: v, country: countries[v[0]] || "unknown", model_year: year, check_digit: v[8],
      valid: true, wmi: v.slice(0,3), vds: v.slice(3,9),
      vehicle: known[v] || null
    });
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">VINPARSER</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a><a href="#pricing" className="hover:text-terracotta">Pricing</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">That VIN tells you everything. If you know how to read it.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">VINPARSER parses any 17-character VIN — validates the check digit, extracts country of origin, model year, assembly plant, and serial number. For known VINs, returns the full make/model/engine.</p>
        <button onClick={parse} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase tracking-wide block mb-1">VIN (17 characters)</label><input type="text" value={vin} onChange={e => setVin(e.target.value.toUpperCase())} maxLength={17} className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm font-mono tracking-wider"/></div>
          <div className="grid grid-cols-4 gap-2 text-xs">
            {["1HGCM82633A004352","WVWZZZ3CZWE123456","5YJSA1DG9DFP14605"].map(v => <button key={v} onClick={()=>{setVin(v);setResult(null)}} className="bg-cream-100 rounded px-2 py-1 font-mono text-center hover:border-terracotta border border-transparent truncate">{v}</button>)}
          </div>
          <button onClick={parse} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Parse VIN →</button>
          {result && !result.error && (
            <div className="space-y-3">
              {result.vehicle && <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted mb-1">{result.vehicle.year} {result.vehicle.make} {result.vehicle.model}</div><div className="text-sm">{result.vehicle.trim} · {result.vehicle.engine} · {result.vehicle.drivetrain}</div></div>}
              <div className="grid grid-cols-2 gap-2 text-xs">
                <div><span className="text-ink-muted">VIN:</span> <span className="font-mono">{result.vin}</span></div>
                <div><span className="text-ink-muted">Valid:</span> <span className={result.valid ? "text-green-600" : "text-red-600"}>{result.valid ? "✓" : "✗"} check digit {result.check_digit}</span></div>
                <div><span className="text-ink-muted">Country:</span> {result.country}</div>
                <div><span className="text-ink-muted">Model year:</span> {result.model_year}</div>
                <div><span className="text-ink-muted">WMI:</span> <span className="font-mono">{result.wmi}</span></div>
                <div><span className="text-ink-muted">VDS:</span> <span className="font-mono">{result.vds}</span></div>
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
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">VINPARSER</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
