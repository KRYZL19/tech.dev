"use client";
import { useState } from "react";
export default function Home() {
  const [cik, setCik] = useState("0001318605");
  const [result, setResult] = useState<any>(null);
  const filings = [
    {cik:"0001318605",company:"NVIDIA Corp",form:"4",insider:"Jensen Huang",title:"CEO",transaction:"purchase",amount:2200000,price:875.30,filed:"2024-03-13"},
    {cik:"0000320193",company:"Apple Inc",form:"4",insider:"Tim Cook",title:"CEO",transaction:"purchase",amount:1200000,price:178.50,filed:"2024-03-15"},
    {cik:"0000789019",company:"Microsoft Corp",form:"4",insider:"Satya Nadella",title:"CEO",transaction:"sale",amount:850000,price:415.20,filed:"2024-03-14"},
    {cik:"0001045810",company:"Meta Platforms",form:"8-K",insider:null,title:null,transaction:null,amount:null,price:null,filed:"2024-03-12"},
  ];
  const companies: Record<string,string> = {"0001318605":"NVIDIA Corp","0000320193":"Apple Inc","0000789019":"Microsoft Corp","0001045810":"Meta Platforms"};
  const lookup = () => { const f = filings.filter(x=>x.cik===cik&&x.insider); setResult({cik,company:companies[cik]||cik,filings:f}); };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">SECFILER</div><nav className="flex gap-6 text-sm text-ink-muted"><a href="#docs" className="hover:text-terracotta">Docs</a></nav></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">Alert me when NVDA's CFO buys $1M in options. Within 24 hours.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">SECFILER gives investors and financial platforms SEC EDGAR Form 4 insider trade alerts and filing search — without building a scraper or maintaining a 10-year filing database.</p>
        <button onClick={lookup} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">"By the time a Form 4 shows up on the SEC website, the trade is 24 hours old. That's not a bug — it's how EDGAR works."</p>
          <footer className="text-sm text-ink-muted mt-3">— Every quant trader who's tried to build real-time alerts</footer>
        </blockquote>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div><label className="text-xs text-ink-muted uppercase block mb-1">Company CIK</label>
            <select value={cik} onChange={e=>{setCik(e.target.value);setResult(null)}} className="w-full border border-cream-border rounded px-3 py-2 bg-cream-50 text-sm">
              {Object.entries(companies).map(([k,v])=><option key={k} value={k}>{v} ({k})</option>)}
            </select>
          </div>
          <button onClick={lookup} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Search filings →</button>
          {result && (
            <div className="space-y-3">
              <div className="text-sm font-medium mb-2">{result.company} — {result.filings.length} Form 4 filings</div>
              {result.filings.map((f:any,i:number)=>(
                <div key={i} className="bg-cream-50 rounded p-3 text-xs">
                  <div className="flex justify-between"><span className="font-medium">{f.insider} ({f.title})</span><span className="text-ink-muted">{f.filed}</span></div>
                  <div className="text-ink-muted">{f.form} · {f.transaction} · ${(f.amount/1000).toFixed(0)}K @ ${f.price}</div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2>
        <div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$49",calls:"10,000/day"},{tier:"Pro",price:"$149",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div>
      </section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">SECFILER</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
