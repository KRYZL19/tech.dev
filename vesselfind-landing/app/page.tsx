"use client";
import { useState } from "react";
export default function Home() {
  const [vid, setVid] = useState("VESSEL-2024-00047");
  const [result, setResult] = useState<any>(null);
  const vessels: Record<string,any> = {
    "VESSEL-2024-00047":{name:"SEA RAY 310",owner:"J. Martinez",lien:true,lien_amount:22000,holders:"US Bank",prev_owners:2,vtype:"Motor Yacht",length:31,material:"Fiberglass",year:2019,status:"Active"},
    "VESSEL-2024-00102":{name:"YAMAHA 242X",owner:"S. Rodriguez",lien:false,lien_amount:null,holders:null,prev_owners:0,vtype:"Jet Boat",length:24,material:"Fiberglass",year:2021,status:"Active"},
    "VESSEL-2023-00888":{name:"JEANNEAU 379",owner:"K. Thompson",lien:true,lien_amount:85000,holders:"Bank of America",prev_owners:1,vtype:"Sailboat",length:37,material:"Fiberglass",year:2017,status:"Active"},
  };
  const lookup = () => setResult(vessels[vid] || {error:"Not in demo database"});
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">VESSELFIND</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">That boat has three owners and a lien against it. One API call.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">VESSELFIND gives boat dealers and marine insurance platforms USCG vessel documentation — ownership history, lien status, documentation renewal — without filing a abstract of title request.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase block mb-1">Vessel ID</label><input type="text" value={vid} onChange={e=>setVid(e.target.value)} className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm font-mono"/></div>
          <div className="grid grid-cols-3 gap-2 text-xs">{Object.keys(vessels).map(v=><button key={v} onClick={()=>{setVid(v);setResult(vessels[v])}} className="bg-cream-100 rounded px-2 py-1.5 font-mono text-center hover:border-terracotta border border-transparent">{v.slice(-5)}</button>)}</div>
          <button onClick={lookup} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Lookup →</button>
          {result && !result.error && (
            <div className="space-y-3">
              <div className="text-sm font-medium">{result.year} {result.name} · {result.length}ft {result.vtype}</div>
              <div className="grid grid-cols-2 gap-2 text-xs">
                <div><span className="text-ink-muted">Owner:</span> {result.owner}</div>
                <div><span className="text-ink-muted">Status:</span> <span className={result.status==="Active"?"text-green-600":"text-red-600"}>{result.status}</span></div>
                <div><span className="text-ink-muted">Lien:</span> <span className={result.lien?"text-red-600 font-medium":"text-green-600"}>{result.lien?"YES — $"+result.lien_amount.toLocaleString()+" — "+result.holders:"None"}</span></div>
                <div><span className="text-ink-muted">Previous owners:</span> {result.prev_owners}</div>
              </div>
              {result.lien && <div className="bg-red-50 border border-red-200 rounded p-3 text-xs text-red-700">This vessel has an active lien. Confirm lien release with {result.holders} before completing any sale.</div>}
            </div>
          )}
          {result?.error && <p className="text-sm text-red-600">{result.error}</p>}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$19",calls:"10,000/day"},{tier:"Pro",price:"$49",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">VESSELFIND</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
