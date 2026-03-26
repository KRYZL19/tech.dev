"use client";
import { useState } from "react";
export default function Home() {
  const [nnum, setNnum] = useState("N284CT");
  const [result, setResult] = useState<any>(null);
  const aircraft: Record<string,any> = {
    N284CT:{n_num:"N284CT",make:"CESSNA",model:"208B CARAVAN",year:2021,hp:675,useful_load:3025,gross:8830,status:"Current",airworthy:"Yes",fuel:335,cruise:186},
    N315LD:{n_num:"N315LD",make:"CESSNA",model:"172S SKYHAWK",year:2019,hp:180,useful_load:1080,gross:2550,status:"Current",airworthy:"Yes",fuel:56,cruise:122},
    N450MK:{n_num:"N450MK",make:"ICON",model:"A-5",year:2023,hp:180,useful_load:950,gross:2400,status:"Current",airworthy:"Yes",fuel:51,cruise:140},
    N920X:{n_num:"N920X",make:"VAN'S",model:"RV-6A",year:2018,hp:160,useful_load:690,gross:1800,status:"Current",airworthy:"Yes",fuel:40,cruise:165},
  };
  const lookup = () => setResult(aircraft[nnum.toUpperCase()] || {error:"Not in demo database"});
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">AIRCRAFTDB</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">N-number lookup before you buy. Airworthiness status. Useful load.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">AIRCRAFTDB gives aircraft buyers, FBOs, and insurance platforms instant access to FAA registration data — without navigating the AFSS weather briefing system just to look up a tail number.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase block mb-1">N-number</label>
            <input type="text" value={nnum} onChange={e=>setNnum(e.target.value.toUpperCase())} placeholder="N284CT" className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm font-mono"/></div>
          <div className="grid grid-cols-4 gap-2 text-xs">
            {Object.keys(aircraft).map(n=><button key={n} onClick={()=>{setNnum(n);setResult(aircraft[n])}} className="bg-cream-100 rounded px-2 py-1.5 text-center font-mono hover:border-terracotta border border-transparent">{n}</button>)}
          </div>
          <button onClick={lookup} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Lookup →</button>
          {result && !result.error && (
            <div className="space-y-3">
              <div className="text-sm font-medium">{result.year} {result.make} {result.model}</div>
              <div className="grid grid-cols-2 gap-2 text-xs">
                <div><span className="text-ink-muted">N-number:</span> <span className="font-mono font-bold">{result.n_num}</span></div>
                <div><span className="text-ink-muted">Status:</span> <span className={result.status === "Current" ? "text-green-600" : "text-red-600"}>{result.status}</span></div>
                <div><span className="text-ink-muted">Airworthy:</span> {result.airworthy}</div>
                <div><span className="text-ink-muted">Useful load:</span> {result.useful_load.toLocaleString()} lbs</div>
                <div><span className="text-ink-muted">Gross weight:</span> {result.gross.toLocaleString()} lbs</div>
                <div><span className="text-ink-muted">Fuel:</span> {result.fuel} gal</div>
                <div><span className="text-ink-muted">Cruise:</span> {result.cruise} kts</div>
                <div><span className="text-ink-muted">Engine:</span> {result.hp} hp</div>
              </div>
            </div>
          )}
          {result?.error && <p className="text-sm text-red-600">{result.error}</p>}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$19",calls:"10,000/day"},{tier:"Pro",price:"$49",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">AIRCRAFTDB</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
