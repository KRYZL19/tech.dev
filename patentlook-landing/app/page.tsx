"use client";
import { useState } from "react";
export default function Home() {
  const [q, setQ] = useState("neural network");
  const [result, setResult] = useState<any>(null);
  const patents = [
    {num:"US10123456B2",title:"Neural network training with dynamic learning rate scheduling",assignee:"OpenAI",cpc:"G06N3/08",filed:"2021-03-15",granted:"2023-09-12"},
    {num:"US9876543A1",title:"Lattice-based cryptographic key encapsulation mechanism",assignee:"Cloudflare",cpc:"H04L9/30",filed:"2020-07-22",granted:"2022-02-08"},
    {num:"US11234567C1",title:"Autonomous vehicle path planning using reinforcement learning",assignee:"Waymo",cpc:"B60W60/00",filed:"2019-11-30",granted:"2021-06-15"},
    {num:"US9981234D1",title:"Attention mechanism with linear complexity for long sequences",assignee:"Carnegie Mellon",cpc:"G06N3/02",filed:"2022-01-10",granted:null},
  ];
  const search = () => { const r=patents.filter(p=>p.title.toLowerCase().includes(q.toLowerCase())); setResult(r); };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">PATENTLOOK</div></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Find all patents for 'neural network training.' CPC code included.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">PATENTLOOK gives researchers and investors patent search without a $5,000/year subscription or spending an afternoon on Google Patents.</p>
        <button onClick={search} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase block mb-1">Search patents</label><input type="text" value={q} onChange={e=>setQ(e.target.value)} onKeyDown={e=>e.key==="Enter"&&search()} placeholder="e.g. neural network, cryptographic, reinforcement learning" className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm"/></div>
          <button onClick={search} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Search →</button>
          {result && (
            <div className="space-y-3">
              <div className="text-sm text-ink-muted">{result.length} results for "{q}"</div>
              {result.map((p:any,i:number)=>(
                <div key={i} className="border border-cream-border rounded p-3 text-xs">
                  <div className="font-medium text-sm mb-1">{p.title}</div>
                  <div className="text-ink-muted grid grid-cols-2 gap-x-4 gap-y-1">
                    <span>US Patent: <span className="font-mono">{p.num}</span></span>
                    <span>Assignee: {p.assignee}</span>
                    <span>CPC: <span className="font-mono">{p.cpc}</span></span>
                    <span>Filed: {p.filed}{p.granted ? ` · Granted ${p.granted}` : " (pending)"}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20"><h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2><div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"50/day"},{tier:"Dev",price:"$29",calls:"10,000/day"},{tier:"Pro",price:"$99",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div></section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">PATENTLOOK</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
