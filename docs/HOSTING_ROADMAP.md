# Hosting Roadmap and Production Operations

This document records the evolution of the hosting infrastructure for Project Hajaribagh and establishes the operational runbook for live cloud deployment.

---

## 1. Evolution and Milestones

### Phase 1: Local Single Node (Completed)
* Hosted on Kowsyke's laptop in the United Kingdom.
* Routed to players in Canada and Bangladesh using the Playit.gg reverse tunnel.
* Limitations: When the host laptop was closed or powered down, the server stopped. Memory was capped at 2.5 GB.

### Phase 2: Dedicated Cloud Migration (Completed)
* Infrastructure provisioned via OCI CLI in `uk-london-1`.
* Virtual Cloud Network, subnets, route tables, and security lists created.
* Ampere Altra ARM64 instance launched with 4 OCPUs and 24 GB RAM.
* Upgraded to Oracle JDK 25 LTS and 8 GB dedicated heap.
* Configured systemd background daemons for 24/7 autonomous uptime.
* Direct public IP `132.226.135.26` activated alongside the Playit tunnel fallback.

### Phase 3: Collaborative Agent Vibe-Coding (Active)
* Git repository configured as the central source of truth for both developers (Kowsyke and exacyyv).
* Automated synchronization scripts enabled to push datapack updates and configurations directly to the live cloud node.

---

## 2. Production Server Runbook

### Accessing the Cloud Node
To open a secure shell session on the production server:
```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26
```

### Checking Server Health and Status
```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26 "sudo systemctl status minecraft.service"
```

### Streaming Live Server Logs
To watch chat messages, player joins, and console output in real time:
```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26 "sudo journalctl -u minecraft -f"
```

### Restarting the Server Cleanly
If a configuration change or mod update requires a restart:
```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26 "sudo systemctl restart minecraft.service"
```

### Deploying Datapacks Without Restarting
To push a new datapack or function edit to the live server:
```bash
scp -i ~/.ssh/id_ed25519 -r datapacks/<pack_name> ubuntu@132.226.135.26:~/minecraft-server/world/datapacks/
```
Then run `/reload` in the game console or in game as an operator.
