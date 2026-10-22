# Project Hajaribagh: Central Agent Manifest

> **NOTICE FOR AI CODING AGENTS (CLAUDE, ANTIGRAVITY, CURSOR, CODEX)**:
> This repository houses the infrastructure, custom datapacks, configurations, and assets for Project Hajaribagh. Read this manifest and [`AGENTS.md`](./AGENTS.md) before writing code, modifying datapacks, or adding mods.

---

## 1. System Context and Narrative Concept

* **Project Name**: Project Hajaribagh
* **Lead Engineer (Node A)**: Kowsyke (abirmia205@gmail.com, United Kingdom)
* **Co-Developer (Node B)**: exacyyv (Collaborator, Vibe-coding partner)
* **Target Audience**: A private, cross-continental group of close friends in the UK, Canada, and Bangladesh.
* **Core Philosophy**: A humorous, culturally resonant Bangladeshi survival multiplayer server. It blends inside jokes, political satire, hangout mechanics (cannabis smoking and brewing), and vanilla survival.

---

## 2. Live 24/7 Production Deployment

The server has been migrated from local laptop hosting to a dedicated cloud node running 24/7:

* **Host Provider**: Oracle Cloud Infrastructure (Always Free Tier)
* **Architecture**: Ampere Altra ARM64 (4 OCPUs, 24 GB RAM)
* **Java Runtime**: Oracle JDK 25 LTS (build 25.0.5.0.2)
* **Memory Allocation**: 8 GB Dedicated Heap with Z Garbage Collector (`-Xms4096M -Xmx8192M -XX:+UseZGC`)
* **Process Supervisor**: Managed via `systemd` (`minecraft.service` and `playit.service`)
* **Direct Public Endpoint**: `132.226.135.26:25565` (or simply `132.226.135.26`)
* **Legacy Tunnel Endpoint**: `cairo-temptation.tun.ply.gg:47309`

---

## 3. Invariants for AI Agents (Do Not Violate)

1. **Zero Client Mod Requirement (Strict)**:
   * Friends connect using unmodified vanilla clients and offline launchers.
   * Never add server mods that require client-side `.jar` installations.
   * All mechanics must be achieved via Polymer virtualization, server-side datapacks, or resource packs delivered automatically over the network.
2. **Punctuation and Syntax Constraints**:
   * Never use em dashes, en dashes, double hyphens, or single hyphens as sentence punctuation in code comments, commit messages, or markdown documents. Use periods, commas, colons, or parentheses instead.
3. **Performance Envelope**:
   * Hardware memory ceiling on the cloud node is 8 GB for Minecraft.
   * Do not introduce 3D terrain noise generators that cause chunk generation lag. Keep world generation lightweight and structure-based.

---

## 4. Repository Structure

```
.
├── AGENTS.md                  # Comprehensive operational manual for AI agents
├── README.md                  # This manifest
├── datapacks/
│   ├── cannabis_smoke/        # Right-clickable joints, smoke animations, sound effects
│   └── ore_xray/              # Administrative inspection tools
├── configs/
│   ├── server.properties      # Production server properties with offline mode and pack delivery
│   ├── custompaintings.toml   # Custom paintings loader configuration
│   ├── ferritecore.mixin.properties # Memory optimization rules
│   ├── lithium.properties     # Physics optimization toggles
│   └── polymer/               # Polymer protocol virtualization rules
├── custompaintings/           # Source photos, metadata, and block dimensions
├── docs/
│   ├── ARCHITECTURE.md        # Cloud VM specs, systemd supervision, network topology
│   ├── HOSTING_ROADMAP.md     # Production deployment history and operational runbook
│   ├── MEMBERS_ROLES.md       # Comprehensive registry of all players, developers, and locations
│   └── MODS_DATAPACKS.md      # Detailed catalog of all installed mods and datapacks
├── scripts/
│   ├── start-server.sh        # Production startup script with 8GB ZGC flags
│   ├── deploy-to-cloud.sh     # Synchronization script to deploy local changes to cloud
│   └── view-cloud-logs.sh     # Real-time remote log stream utility
└── Hajaribagh-Paintings.zip   # Quantized server-side custom paintings resource pack
```

---

## 5. Developer Guide: How exacyyv and Her Agent Can Work

Any collaborator with access to this repository can write code, create new features, and deploy them to the live 24/7 server:

### A. Developing Features
1. Clone this repository locally.
2. Build new mechanics inside `datapacks/` (such as custom recipes, mini-games, or interactive items using vanilla triggers and loot tables).
3. Test syntax and verify that no client-side mods are introduced.

### B. Deploying to the Production Cloud Server
To push changes to the live 24/7 server:
```bash
./scripts/deploy-to-cloud.sh
```
Or manually via SSH:
```bash
scp -i ~/.ssh/id_ed25519 -r datapacks/* ubuntu@132.226.135.26:~/minecraft-server/world/datapacks/
```

### C. Reloading in Game
Most datapack changes do not require a server restart. If you have operator permissions in game, simply type:
```
/reload
```
The server will instantly compile the new functions, tags, and recipes.

### D. Viewing Live Logs
To monitor server activity, player connections, or debugging output in real time:
```bash
./scripts/view-cloud-logs.sh
```
Or via SSH:
```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26 "sudo journalctl -u minecraft -f"
```
