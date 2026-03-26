"use client";
import { useState } from "react";
export default function Home() {
  const [fc, setFc] = useState(1.0);
  const [cya, setCya] = useState(80);
  const [result, setResult] = useState<any>(null);
  const calc = () => {
    const lf = 1+0.25*Math.pow(Math.max(cya,1),0.57);
    const eff = fc/lf;
    const lock = ((lf-1)/lf)*100;
    setResult({fc,cya,eff:+eff.toFixed(3),lock:+lock.toFixed(1),status:lock>70?"lockup_danger":lock>50?"lockup_warning":"optimal"});
  };
  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border"><div className="font-serif text-xl font-bold tracking-tight">POOLCHEM</div></header>
      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">FCI over 150ppm and your chlorine doubles its demand overnight.</h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">POOLCHEM gives pool professionals the chemistry math — FCI chlorine lockup, CSI saturation index, chemical dose calculations — without a chemistry degree or a Taylor test kit manual from 1987.</p>
        <button onClick={calc} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">Try it →</button>
      </section>
      <section className="mb-20">
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div><label className="text-xs text-ink-muted uppercase block mb-1">Free Chlorine (ppm)</label><input type="number" step="0.1" value={fc} onChange={e=>setFc(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
            <div><label className="text-xs text-ink-muted uppercase block mb-1">CYA (ppm)</label><input type="number" value={cya} onChange={e=>setCya(Number(e.target.value))} className="w-full border border-cream-border rounded px-2 py-1.5 bg-cream-50 text-sm"/></div>
          </div>
          <button onClick={calc} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm">Calculate FCI →</button>
          {result && (
            <div className="space-y-3">
              <div className="text-center">
                <div className="text-5xl font-bold font-serif">{result.eff} <span className="text-2xl text-ink-muted">ppm</span></div>
                <div className={`text-sm px-3 py-1 rounded-full inline-block mt-2 ${result.status==="optimal"?"bg-green-100 text-green-700":result.status==="lockup_warning"?"bg-yellow-100 text-yellow-700":"bg-red-100 text-red-700"}`}>
                  {result.status==="optimal"?"Optimal":result.status==="lockup_warning"?"Warning — lockup building":"DANGER — chlorine lockup"}
                </div>
              </div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Free chlorine</div><div className="font-bold">{result.fc} ppm</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">CYA level</div><div className="font-bold">{result.cya} ppm</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Lockup %</div><div className="font-bold">{result.lock}%</div></div>
                <div className="bg-cream-50 rounded p-3"><div className="text-xs text-ink-muted">Effective FC</div><div className="font-bold">{result.eff} ppm</div></div>
              </div>
              {result.status !== "optimal" ? <div className="text-xs text-red-600">Drain recommended if CYA above 100ppm</div> : null}
            </div>
          )}
        </div>
      </section>
      <section id="pricing" className="mb-20"><h2 className="font-serif text-2xl font-bold mb-2">Pricing</h2><div className="grid grid-cols-3 gap-4">{[{tier:"Free",price:"$0",calls:"100/day"},{tier:"Dev",price:"$9",calls:"10,000/day"},{tier:"Pro",price:"$29",calls:"100,000/day"}].map(p=>(<div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5"><div className="text-xs text-ink-muted uppercase">{p.tier}</div><div className="text-2xl font-bold mt-1">{p.price}</div><div className="text-xs text-ink-muted mt-1">{p.calls}</div></div>))}</div></section>
      <footer className="border-t border-cream-border pt-8 flex justify-between text-xs text-ink-muted"><span className="font-serif font-bold text-ink">POOLCHEM</span><span>Built by KRYZL19</span></footer>
    </main>
  );
}
