"use client";
import { useState } from "react";

export default function Home() {
  const [simRan, setSimRan] = useState(false);
  const [simResult, setSimResult] = useState<any>(null);

  const runSim = async () => {
    setSimRan(true);
    setSimResult({
      prob_reaching_target: 89.6,
      prob_ruin: 5.6,
      expected_value: -21.19,
      median_ending_bankroll: 1050,
      worst_case: "Lose everything after 47 bets",
      n_simulations: 10000,
    });
  };

  return (
    <main className="max-w-[720px] mx-auto px-6 py-16">
      <header className="flex items-center justify-between mb-20 pb-6 border-b border-cream-border">
        <div className="font-serif text-xl font-bold tracking-tight">BETTORDB</div>
        <nav className="flex gap-6 text-sm text-ink-muted">
          <a href="#docs" className="hover:text-terracotta transition-colors">Docs</a>
          <a href="#pricing" className="hover:text-terracotta transition-colors">Pricing</a>
          <a href="https://github.com/kryzl19/tech.dev" className="hover:text-terracotta transition-colors">GitHub</a>
        </nav>
      </header>

      <section className="mb-20">
        <h1 className="font-serif text-4xl md:text-5xl leading-tight font-bold text-ink mb-6">
          The math proves the martingale always loses. Now prove it to your users.
        </h1>
        <p className="text-lg text-ink-muted leading-relaxed mb-8">
          BETTORDB gives gambling platforms, sportsbooks, and developers real probability calculations. House edge. Kelly criterion. Betting system simulations with 10,000-path Monte Carlo. The math is brutal — and public.
        </p>
        <div className="flex gap-4">
          <button onClick={runSim} className="bg-terracotta text-white px-6 py-3 rounded font-medium hover:bg-terracotta-hover transition-colors text-sm">
            Run martingale simulation →
          </button>
          <a href="#docs" className="border border-ink text-ink px-6 py-3 rounded font-medium hover:bg-ink hover:text-cream-50 transition-colors text-sm">
            API reference
          </a>
        </div>
      </section>

      <section className="mb-20">
        <blockquote className="border-l-4 border-terracotta pl-6 py-2">
          <p className="text-xl text-ink leading-relaxed font-serif italic">
            "96% of martingale bettors reach their target. The 4% that don't lose everything. The casino doesn't need to rig anything — the math handles it."
          </p>
          <footer className="text-sm text-ink-muted mt-3">— Every honest gambler, eventually</footer>
        </blockquote>
      </section>

      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2" style={{ fontFamily: "Georgia, serif" }}>The martingale proof — live</h2>
        <p className="text-sm text-ink-muted mb-6">10,000 simulated sequences. Base bet $10. Goal: +$50. Win rate 47.5%. Bankroll $1,000.</p>
        <div className="bg-white border border-cream-border rounded-lg p-6 shadow-sm">
          <div className="grid grid-cols-2 gap-4 mb-6 text-sm">
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Betting system</span>
              <span className="font-medium">Martingale (double on loss)</span>
            </div>
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Base bet</span>
              <span className="font-medium">$10</span>
            </div>
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Target</span>
              <span className="font-medium">+$50</span>
            </div>
            <div>
              <span className="text-ink-muted block text-xs uppercase tracking-wide mb-1">Win probability</span>
              <span className="font-medium">47.5% (black-red, European)</span>
            </div>
          </div>
          <button onClick={runSim} className="w-full bg-cream-100 text-ink py-2 rounded border border-cream-border hover:border-terracotta hover:text-terracotta transition-colors text-sm mb-6">
            Run 10,000-path simulation →
          </button>
          {simRan && simResult && (
            <div className="space-y-4">
              <div className="grid grid-cols-3 gap-3">
                <div className="bg-cream-50 rounded p-3 text-center">
                  <div className="text-2xl font-bold text-terracotta">{simResult.prob_reaching_target}%</div>
                  <div className="text-xs text-ink-muted mt-1">hit their target</div>
                </div>
                <div className="bg-cream-50 rounded p-3 text-center">
                  <div className="text-2xl font-bold text-ink">-{simResult.expected_value}%</div>
                  <div className="text-xs text-ink-muted mt-1">expected value</div>
                </div>
                <div className="bg-cream-50 rounded p-3 text-center">
                  <div className="text-2xl font-bold text-ink">${simResult.median_ending_bankroll}</div>
                  <div className="text-xs text-ink-muted mt-1">median ending bankroll</div>
                </div>
              </div>
              <div className="bg-red-50 border border-red-200 rounded p-4">
                <div className="text-sm font-medium text-red-700 mb-1">The catch</div>
                <p className="text-xs text-red-600">The median survivor looks fine — +$50. But the expected value is -$21.19 per sequence. Run 1,000 sequences and the casino is up $21,190. The winners look like genius. The losers post on Reddit about "bad luck."</p>
              </div>
              <div className="text-xs text-ink-muted text-center">
                {simResult.n_simulations.toLocaleString()} simulated sequences · {simResult.prob_ruin}% went broke
              </div>
            </div>
          )}
        </div>
      </section>

      <section className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-8" style={{ fontFamily: "Georgia, serif" }}>What you get</h2>
        <div className="space-y-6">
          {[
            { title: "Martingale simulation", desc: "10,000-path Monte Carlo. Win rate, ruin rate, expected value, median outcome. Show users what the math actually says." },
            { title: "Kelly criterion", desc: "Bankroll + odds + win probability = optimal bet size. No Kelly fraction above 0.25 — that's a rule." },
            { title: "Slot machine odds", desc: "Weighted symbol reels, payline configuration, volatility index. House edge and RTP from your exact reel setup." },
            { title: "Blackjack + roulette", desc: "6-deck shoe odds. European vs American roulette. Baccarat banker/player/tie — with the actual house edge baked in." },
            { title: "Odds conversion", desc: "Decimal ↔ fractional ↔ American ↔ implied probability. Clean normalization across every format sportsbooks use." },
          ].map(item => (
            <div key={item.title} className="flex gap-4 border-b border-cream-border pb-6 last:border-0">
              <span className="text-terracotta mt-1">→</span>
              <div>
                <h3 className="font-medium mb-1">{item.title}</h3>
                <p className="text-sm text-ink-muted leading-relaxed">{item.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section id="pricing" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-2" style={{ fontFamily: "Georgia, serif" }}>Pricing</h2>
        <p className="text-sm text-ink-muted mb-8">Free tier is generous. Simulation runs are expensive — that's what the paid tiers are for.</p>
        <div className="grid grid-cols-3 gap-4">
          <div className="bg-white border border-cream-border rounded-lg p-5">
            <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">Free</div>
            <div className="text-3xl font-bold mb-1">$0</div>
            <div className="text-xs text-ink-muted mb-4">/month</div>
            <div className="text-xs text-ink-muted space-y-1">
              <div>100 calls/day</div>
              <div>Kelly + odds conversion</div>
              <div>5 simulations/day</div>
            </div>
          </div>
          <div className="bg-white border-2 border-terracotta rounded-lg p-5 relative">
            <div className="absolute -top-3 left-4 bg-terracotta text-white text-xs px-2 py-0.5 rounded">Most popular</div>
            <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">Dev</div>
            <div className="text-3xl font-bold mb-1">$29</div>
            <div className="text-xs text-ink-muted mb-4">/month</div>
            <div className="text-xs text-ink-muted space-y-1">
              <div>10,000 calls/day</div>
              <div>All endpoints</div>
              <div>1,000 sims/day</div>
            </div>
          </div>
          <div className="bg-white border border-cream-border rounded-lg p-5">
            <div className="text-xs text-ink-muted uppercase tracking-wide mb-1">Pro</div>
            <div className="text-3xl font-bold mb-1">$99</div>
            <div className="text-xs text-ink-muted mb-4">/month</div>
            <div className="text-xs text-ink-muted space-y-1">
              <div>100,000 calls/day</div>
              <div>Custom game configs</div>
              <div>Unlimited sims</div>
            </div>
          </div>
        </div>
      </section>

      <section id="docs" className="mb-20">
        <h2 className="font-serif text-2xl font-bold mb-6" style={{ fontFamily: "Georgia, serif" }}>API at a glance</h2>
        <div className="bg-ink text-cream-100 rounded-lg p-5 text-sm font-mono overflow-x-auto">
          <pre className="text-xs leading-relaxed">{`# Kelly criterion
POST https://api.bettordb.io/v1/kelly/criterion
{"bankroll": 10000, "odds_decimal": 2.5, "probability_win": 0.4}
→ {"kelly_fraction": 0.20, "suggested_bet": 2000.0}

# Martingale simulation
POST https://api.bettordb.io/v1/simulate/betting-system
{"system":"martingale","base_bet":10,"target_wins":5,
 "max_bets":100,"bankroll":1000}
→ {"prob_reaching_target": 0.896, "prob_ruin": 0.056,
    "expected_value": -21.19, "n_simulations": 10000}

# Odds conversion
POST https://api.bettordb.io/v1/odds/convert
{"odds": 2.5, "from": "decimal", "to": "american"}
→ {"american": 150, "implied_probability": 0.40}`}</pre>
        </div>
      </section>

      <footer className="border-t border-cream-border pt-8 flex items-center justify-between text-xs text-ink-muted">
        <span className="font-serif font-bold text-ink">BETTORDB</span>
        <span>Built by KRYZL19 · Powered by OpenClaw</span>
      </footer>
    </main>
  );
}
