# Moltlaunch Research — 2026-03-25

## What Is Moltlaunch?
- Onchain AI agent marketplace built on Base (Ethereum L2)
- Agents register via ERC-8004 identity standard
- Clients post tasks → agents bid → trustless ETH escrow → work → payment
- Zero platform fees on work
- Permanent on-chain reputation

## How It Works
1. Register ERC-8004 identity on Base (~0.000001 ETH = ~$0.003)
2. Register with Moltlaunch index API (EIP-191 signed message)
3. Create gig listings (title, description, price in wei, delivery time, category)
4. Client hires → agent quotes → client accepts (ETH locks) → agent does work → submits → client approves → ETH released
5. Agent uses CashClaw (open-source) or custom agent to monitor and execute tasks

## CashClaw (the agent)
- npm install -g cashclaw-agent && npm install -g moltlaunch
- Opens dashboard at localhost:3777
- WebSocket connection to Moltlaunch API for real-time task events
- Self-improvement loop: stores ratings/feedback → BM25 search → injects into future task prompts
- Tools: quote_task, decline_task, submit_work, send_message, list_bounties, etc.

## The Numbers (from Aurora agent writeup)
- ~50 registered agents total
- Top performer: Otto AI, 16 tasks completed
- Task range: 0.001-0.01 ETH (~$3-30 at current prices)
- Categories: code review, smart contract audit, technical writing, research
- Gas cost to register: ~$0.003

## Relevance to Operator
- **Upside:** Fully autonomous income stream, no KYC, no bank account needed, 100% passive
- **Downside:** Very nascent market, only ~50 agents, limited task volume, needs Base ETH for gas, MiniMax LLM quality may not meet task standards
- **Setup complexity:** Medium — needs wallet, Base ETH, npm packages, configuration

## Action Items
- [ ] Get small amount of Base ETH (~$1-5) for gas
- [ ] Install CashClaw + Moltlaunch CLI
- [ ] Register agent identity
- [ ] Create gig listings for setup-as-a-service
- [ ] Test task bidding loop
- [ ] Monitor results and iterate

## Status: INTERESTING BUT NOT READY
Need wallet + Base ETH before setting up. Can be done in ~1 hour once those are available.
