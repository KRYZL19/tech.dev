"use client";
import { useState } from "react";

export default function Home() {
  const [caliber, setCaliber] = useState("556_nato_62gr");
  const [result, setResult] = useState<any>(null);

  const data: Record<string, any> = {
    "556_nato_62gr": { name: "5.56x45mm NATO (62gr FMJ)", type: "rifle", velocity_fps: 3100, energy_ftlbs: 1324, pressure_nato: "58,000 PSI", penetration: 12, expansion: 8, notes: "Standard NATO ball. 3100fps from 14.5\" barrel." },
    "308_win_168gr": { name: ".308 Winchester (168gr BTHP)", type: "rifle", velocity_fps: 2650, energy_ftlbs: 2620, pressure_nato: "62,000 PSI", penetration: 22, expansion: 10, notes: "Match-grade. 175gr has slightly more recoil, slightly more energy." },
    "9mm_luger_124gr": { name: "9mm Luger (124gr JHP)", type: "pistol", velocity_fps: 1100, energy_ftlbs: 333, pressure_nato: "36,500 PSI", penetration: 12, expansion: 13, notes: "JHP expands reliably above 1000fps. Below that, acts like FMJ." },
    "762x39": { name: "7.62x39mm (123gr FMJ)", type: "rifle", velocity_fps: 2300, energy_ftlbs: 1527, pressure_nato: "45,300 PSI", penetration: 16, expansion: 10, notes: "Soviet intermediate. More recoil than 5.56 in a comparable platform." },
  };

  const run = () => setResult(data[caliber]);

  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">AMMODEX</div>
        <nav className="flex gap-6 text-sm text-ink-muted">
          <a href="#docs" className="hover:text-terracotta transition-colors">Docs</a>
          <a href="#pricing" className="hover:text-terracotta transition-colors">Pricing</a>
        </nav>
      </header>

      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">
          Your ammunition spec sheet is wrong. This one isn't.
        </h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">
          Every manufacturer prints different numbers for the same caliber. AMMODEX gives you NIST-standard ballistic data — real muzzle velocities, gel test penetration depths, and pressure readings — for 14 calibers. One API call.
        </p>
        <div className="flex gap-4">
          <button onClick={run} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">
            Try the demo →
          </button>
          <a href="#docs" className="border border-ink text-ink px-6 py-3 rounded font-medium hover:bg-ink hover:text-cream-50 transition-colors text-sm">
            API reference
          </a>
        </div>
      </section>

      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">
            "Hornady says 5.56 NATO travels at 3240fps. Federal says 3100fps. They're both measuring from different barrel lengths. Nobody tells you which one to believe."
          </p>
          <footer className="text-sm text-ink-muted mt-3">— Every competitive shooter, at 2am</footer>
        </blockquote>
      </section>

      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6" style={{ fontFamily: "Georgia, serif" }}>Ballistic data — live</h2>
        <p className="text-sm text-ink-muted mb-4">Select a caliber and see real ballistic figures.</p>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm">
          <select
            value={caliber}
            onChange={e => { setCaliber(e.target.value); setResult(null); }}
            className="w-full border border-cream-border rounded px-3 py-2 text-sm mb-4 bg-cream-50"
          >
            <option value="556_nato_62gr">5.56x45mm NATO (62gr FMJ)</option>
            <option value="308_win_168gr">.308 Winchester (168gr BTHP)</option>
            <option value="9mm_luger_124gr">9mm Luger (124gr JHP)</option>
            <option value="762x39">7.62x39mm (123gr FMJ Soviet)</option>
          </select>
          <button onClick={run} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm mb-6">
            Get ballistic data →
          </button>
          {result && (
            <div className="space-y-3">
              <div className="text-xs uppercase tracking-wide text-ink-muted mb-3">{result.name}</div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="bg-cream-50 rounded p-3">
                  <div className="text-xs text-ink-muted">Muzzle velocity</div>
                  <div className="font-bold text-lg">{result.velocity_fps.toLocaleString()} fps</div>
                </div>
                <div className="bg-cream-50 rounded p-3">
                  <div className="text-xs text-ink-muted">Muzzle energy</div>
                  <div className="font-bold text-lg">{result.energy_ftlbs.toLocaleString()} ft·lbs</div>
                </div>
                <div className="bg-cream-50 rounded p-3">
                  <div className="text-xs text-ink-muted">NATO pressure</div>
                  <div className="font-bold">{result.pressure_nato}</div>
                </div>
                <div className="bg-cream-50 rounded p-3">
                  <div className="text-xs text-ink-muted">Gel penetration</div>
                  <div className="font-bold">{result.penetration}mm · {result.expansion}mm expansion</div>
                </div>
              </div>
              <p className="text-xs text-ink-muted italic border-t border-cream-border pt-3">{result.notes}</p>
            </div>
          )}
        </div>
      </section>

      <section id="docs" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6" style={{ fontFamily: "Georgia, serif" }}>API</h2>
        <div className="bg-ink text-cream-100 rounded-lg p-5 text-sm font-mono overflow-x-auto">
          <pre className="text-xs leading-relaxed">{`# Get ballistic data
curl https://api.ammodex.io/v1/ammo/556_nato_62gr

# Custom velocity calc
curl "https://api.ammodex.io/v1/energy-calc?caliber_id=308_win_168gr&velocity_fps=2700"

# Gel test simulation
curl -X POST https://api.ammodex.io/v1/ballistics/gel-test \\
  -H "Content-Type: application/json" \\
  -d '{"caliber_id":"223_rem_55gr","velocity_fps":3100}'

# Response
{
  "name": "5.56x45mm NATO (62gr FMJ)",
  "muzzle_velocity_fps": 3100,
  "muzzle_energy_ftlbs": 1324,
  "penetration_in_gel": 12,
  "expansion_mm": 8,
  "pressure_nato_psi": 58000
}`}</pre>
        </div>
      </section>

      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2" style={{ fontFamily: "Georgia, serif" }}>Pricing</h2>
        <p className="text-sm text-ink-muted mb-8">Ballistic data is public. What you're paying for is the structured API.</p>
        <div className="grid grid-cols-3 gap-4">
          {[
            { tier: "Free", price: "$0", calls: "100/day", features: ["14 calibers", "Basic energy calc", "Gel test sim"] },
            { tier: "Dev", price: "$19", calls: "10,000/day", features: ["All endpoints", "Custom velocity input", "NATO pressure data"] },
            { tier: "Pro", price: "$79", calls: "100,000/day", features: ["Custom caliber upload", "Reload planning", "Priority support"] },
          ].map(p => (
            <div key={p.tier} className="bg-white border border-cream-border rounded-lg p-5">
              <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">{p.tier}</div>
              <div className="text-3xl font-bold mb-1">{p.price}</div>
              <div className="text-xs text-ink-muted mb-4">{p.calls}</div>
              {p.features.map(f => <div key={f} className="text-xs text-ink-muted">• {f}</div>)}
            </div>
          ))}
        </div>
      </section>

      <footer className="border-t border-cream-border pt-8 flex items-center justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">AMMODEX</span>
        <span>Built by KRYZL19</span>
      </footer>
    </main>
  );
}
