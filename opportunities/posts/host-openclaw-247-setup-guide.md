# host-openclaw-247-setup-guide

**Key Takeaway:** Setting up OpenClaw 24/7 on a VPS requires PM2 for process survival, a systemd service for boot resilience, and a proper firewall — the whole stack takes about 30 minutes and costs ~€6/month on Hetzner.

---

## Twitter Hook 1

The difference between an AI agent that runs "sometimes" and one that actually works is three lines of systemd config.

Here's the 30-minute setup that makes OpenClaw truly autonomous: PM2 + systemd + firewall.

(Yes, it's that simple.) #AIagents #VPS

---

## Twitter Hook 2

PSA: if your AI agent dies when you close your laptop, it isn't autonomous — it's a script that happens to use AI.

Real 24/7 operation requires: PM2 to survive disconnects, systemd to restart on reboot, and a firewall so you don't get popped while you sleep. #OpenClaw #AIautomation

---

## LinkedIn Post

I've watched so many people set up AI agents, celebrate for a day, and then discover it died sometime during the night because they forgot one critical detail.

Here's what "running an AI agent 24/7" actually requires, in the order most people skip things:

Most tutorials show you `npm install -g openclaw && openclaw setup` and call it done. That's not an autonomous agent — that's a process running in your terminal that will die the moment your SSH session ends.

The missing pieces, in order of how often people forget them:

PM2. This keeps your agent alive after disconnects. Without it, closing your laptop kills the agent. Full stop. `pm2 start openclaw --name "agent" && pm2 save` — two commands, essential.

Systemd. PM2 survives disconnects but not server reboots. You need a systemd service file so the agent starts automatically when your VPS restarts. This is the step that turns "runs sometimes" into "runs always."

Firewall. UFW with default deny, SSH on a non-standard port, and only the ports you actually need. If you're running OpenClaw's gateway port exposed to the world without auth — fix that now.

Automatic security updates. `unattended-upgrades` exists for a reason. A compromised VPS running your AI agent is worse than a crashed one.

My own failure: I skipped firewall configuration for the first two weeks because "it's just a test server." Then I noticed random outbound connection attempts in my logs that I couldn't explain. Lesson learned.

The beautiful thing: this entire stack costs about €6/month on Hetzner's CX21 and takes 30 minutes to configure properly. Once it's done, it genuinely runs. For months.

What part of your agent setup are you most worried about failing?

---

## Reddit Post (r/selfhosted)

Wanted to share a guide I wish existed when I started with OpenClaw. The official docs are good but skip the "here's what makes this actually production-ready" parts.

The three things that make OpenClaw genuinely autonomous vs. "runs when you're watching":

**1. PM2 for process management**

```bash
npm install -g pm2
pm2 start openclaw --name "openclaw-agent"
pm2 save
pm2 startup
# Run the output command as root
```

PM2 keeps the agent alive when your SSH session disconnects. This sounds obvious but most people don't set it up before they SSH into their server from their phone and close the app.

**2. Systemd for boot resilience**

Create `/etc/systemd/system/openclaw.service`:

```
[Unit]
Description=OpenClaw Agent
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/home/your-user
ExecStart=/usr/bin/node /usr/bin/openclaw gateway start
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable openclaw
sudo systemctl start openclaw
```

This is what makes the agent survive server reboots. Without it, any kernel update requiring a reboot kills your agent until you manually restart it.

**3. Firewall with UFW**

```bash
sudo ufw default deny incoming
sudo ufw allow YOUR_SSH_PORT/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

The failure I see constantly: people run `ufw enable` while SSH'd in without first allowing their SSH port, then they can't reconnect. Always allow SSH first.

With all three in place, I've had my agent run for 4 months without manual intervention. The VPS kernel updated, the server rebooted, the agent came back up on its own. That's what autonomous actually means.

Happy to answer questions about the setup.
