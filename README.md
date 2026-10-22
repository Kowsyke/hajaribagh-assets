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

## 2. Invariants for AI Agents (Do Not Violate)

1. **Zero Client Mod Requirement (Strict)**:
   * Friends connect using unmodified vanilla clients and offline launchers.
   * Never add server mods that require client-side `.jar` installations.
   * All mechanics must be achieved via Polymer virtualization, server-side datapacks, or resource packs delivered automatically over the network.
2. **Punctuation and Syntax Constraints**:
   * Never use em dashes, en dashes, double hyphens, or single hyphens as sentence punctuation in code comments, commit messages, or markdown documents. Use periods, commas, colons, or parentheses instead.
3. **Performance Envelope**:
   * Hardware memory ceiling is 2560 MB (2.5 GB) with Z Garbage Collector.
   * Do not introduce 3D terrain noise generators that cause chunk generation lag. Keep world generation lightweight and structure-based.

---

## 3. Repository Structure

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
│   ├── ARCHITECTURE.md        # Deep dive into JVM, Fabric, and Playit network tunnels
│   ├── HOSTING_ROADMAP.md     # Dual-node handoff, 24/7 VPS deployment, Vercel/Neon guide
│   ├── MEMBERS_ROLES.md       # Comprehensive registry of all players, developers, and locations
│   └── MODS_DATAPACKS.md      # Detailed catalog of all installed mods and datapacks
├── scripts/
│   └── start-server.sh        # Optimized server startup script with ZGC flags
└── Hajaribagh-Paintings.zip   # Quantized server-side custom paintings resource pack
```

---

## 4. Installed Subsystems and Features

* **Custom Paintings**: Replaces vanilla paintings with custom artwork featuring Sheikh Hasina, President Chuppu, Sarjis Alam, historic Dhaka scenes, Nahid Islam, and Asif Mahmud.
* **Cannabis and Joints**: Craftable right-clickable joints (1 Paper + 1 Dried Kelp = 3 Joints). Emits 3D camp smoke columns, campfire crackle sounds, and status buffs.
* **Brewery**: Cauldron fermenting, barrel aging, and custom alcoholic drinks delivered server-side via Polymer.
* **Reverse Tunnel**: Public routing provided by `playit.gg` to `cairo-temptation.tun.ply.gg:47309` (internal port 25565).

---

## 5. Collaboration and Vibe-Coding Protocol

Both developers (Kowsyke and exacyyv) collaborate on this repository using their respective AI agents:
* **Feature Branches**: Branch off `main` for new mini-games or datapack mechanics.
* **Validation**: Verify all datapack JSON syntax and scoreboard commands prior to merging.
* **World State**: The `world/` directory is intentionally decoupled from git. Refer to [`docs/HOSTING_ROADMAP.md`](./docs/HOSTING_ROADMAP.md) for world state synchronization procedures between Node A and Node B.
