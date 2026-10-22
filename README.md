# Project Hajaribagh: Central Agent Manifest

> **NOTICE FOR AI CODING AGENTS (CLAUDE, ANTIGRAVITY, CURSOR, CODEX)**:
> This repository houses the infrastructure, custom datapacks, configurations, and assets for Project Hajaribagh. Read this manifest and [`AGENTS.md`](./AGENTS.md) before writing code, modifying datapacks, or adding mods.

---

## 1. System Context and Narrative Concept

* **Project Name**: Project Hajaribagh
* **Lead Engineer (Node A)**: King Abir (Kowsyke, abirmia205@gmail.com, United Kingdom)
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
4. **Iron-Clad Guide Book and Repository Synchronization Rule**:
   * Whenever any new mod, command, mechanic, or player role is introduced or modified, the in-game guide book (`datapacks/server_guide`) must be updated with the changes and its version incremented.
   * All repository documentation (`README.md`, `AGENTS.md`, and `docs/MODS_DATAPACKS.md`) must be kept in sync and pushed to GitHub. No change is complete without this step.

---

## 4. Repository Structure

```
.
├── .gitattributes             # Forces LF line endings for scripts and datapack files
├── AGENTS.md                  # Comprehensive operational manual for AI agents
├── README.md                  # This manifest
├── datapacks/
│   ├── cannabis_smoke/        # Right-clickable joints, smoke animations, sound effects
│   ├── ore_xray/              # Host only spectator and night vision toggle for inspecting ore
│   └── server_guide/          # Official written guide book auto-delivered to players on login
├── configs/
│   ├── server.properties      # Production server properties with offline mode and pack delivery
│   ├── custompaintings.toml   # Custom paintings loader configuration
│   ├── ferritecore.mixin.properties # Memory optimization rules
│   ├── lithium.properties     # Physics optimization toggles
│   └── polymer/               # Polymer protocol virtualization rules
├── custompaintings/           # Source photos, metadata, and block dimensions
├── docs/
│   ├── ARCHITECTURE.md        # Cloud VM specs, systemd supervision, network topology
│   ├── FEASIBILITY_AND_LIMITS.md # Hardware limits, maximizations, and performance policy
│   ├── HOSTING_ROADMAP.md     # Production deployment history and operational runbook
│   ├── KNOWN_ISSUES.md        # Open questions, risks, and things to verify in game
│   ├── MEMBERS_ROLES.md       # Comprehensive registry of all players, developers, and locations
│   ├── MODS_DATAPACKS.md      # Detailed catalog of all installed mods and datapacks
│   └── OPERATIONS.md          # Repo to server file mapping, updating the pack and mods
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

Before your first deploy:
* King Abir (Kowsyke) must add your SSH public key to `/home/ubuntu/.ssh/authorized_keys` on the VM. The scripts cannot log in without it.
* The scripts use `~/.ssh/id_ed25519` by default. To use a different key, user, or host, set `HZ_KEY`, `HZ_USER`, or `HZ_HOST`, for example `HZ_KEY=~/.ssh/my_key ./scripts/deploy-to-cloud.sh`.
* On Windows, run the scripts from Git Bash.
* The script copies your working folder, committed or not. Run `git pull` first and deploy only what is on `main`.

### C. Reloading in Game
Most datapack changes do not require a server restart. If you have operator permissions in game, simply type:
```
/reload
```
The server will instantly compile the new functions, tags, and recipes.

### D. Viewing Live Logs and Server HUD
To open the live telemetry and log dashboard from the host machine terminal:
```bash
mserver
```
This launches the browser HUD displaying real-time SLP ping, memory, CPU, and streaming journal logs.

To monitor server logs directly inside the terminal:
```bash
./scripts/view-cloud-logs.sh
```
Or via SSH:
```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26 "sudo journalctl -u minecraft -f"
```

---

## 6. Installed Subsystems and Features

* **Server Starter Kit and Guide Book**: Auto-equips all connecting new players on first login with full leather armor (helmet, chestplate, leggings, boots), a full set of stone tools (sword, pickaxe, axe, hoe), 10 torches, 10 cooked beef steaks, an empty exploration map, and the written server guide book with base coordinates (X: 163, Z: -307). Any player can run `/trigger guide` at any time to receive a replacement book copy.
* **Custom Paintings**: Replaces the artwork of all 46 vanilla paintings with six custom images (Sheikh Hasina, President Chuppu, Sarjis Alam, a Dhaka scene, Nahid Islam and Asif Mahmud, and a Bengal meme). The images reach vanilla clients through a server resource pack that overrides the vanilla painting textures. See [`docs/MODS_DATAPACKS.md`](./docs/MODS_DATAPACKS.md) for how the pack and the `custompaintings` mod fit together.
* **Cannabis Cultivation, Curing, and Joints**: 100% server-side farming system. Players craft Cannabis Seeds (1 Wheat Seed + 1 Dried Kelp = 2 Seeds) or forage them by punching wild ferns in forests. Seeds planted on hydrated farmland grow into tall stalks that harvest into Raw Cannabis Buds and Seeds (compatible with RightClickHarvest). Raw buds cure on campfires, smokers, or furnaces into Cured Buds, which roll with paper into joints (1 Paper + 1 Cured Bud = 3 Joints). Smoking puffs smoke particles, plays audio, and grants status effects.
* **Brewery**: Patbox's Brewery mod. Cauldron cooking over a fire, barrel aging, and alcoholic drinks, delivered server-side via Polymer. Craft a Book of Brewery (1 Glass Bottle + 1 Book) to browse the recipes in game.
* **Playit Tunnel**: The original `playit.gg` route to `cairo-temptation.tun.ply.gg:47309` still runs next to the direct IP.

---

## 7. Collaboration and Vibe-Coding Protocol

Both developers (King Abir and exacyyv) collaborate on this repository using their respective AI agents:
* **Feature Branches**: Branch off `main` for new mini-games or datapack mechanics, and merge once they are checked.
* **Validation**: Verify all datapack JSON syntax and scoreboard commands prior to merging. Check `docs/KNOWN_ISSUES.md` before changing a subsystem.
* **Deploying**: `scripts/deploy-to-cloud.sh` ships your working folder straight to production, so deploy from an up to date `main`.
* **World State**: The `world/` directory lives only on the cloud VM and is intentionally decoupled from git. It has no backup yet, which is tracked in `docs/KNOWN_ISSUES.md`.
* **Secrets**: Never commit passwords, tokens, or secrets. Files in `configs/` are copies of live files, so blank any secret value before committing.
* **Operations**: Where each file in this repo belongs on the server, and how to ship a new painting pack or mod update, is in [`docs/OPERATIONS.md`](./docs/OPERATIONS.md).

---

## 8. Side Note: The Minecraft Sword

exacyyv also built a real Minecraft sword. It is a wooden toy sword with an ESP32-S3 inside that pairs with a computer over Bluetooth Low Energy as an ordinary keyboard and mouse. Swing it to attack, hold the aim button and turn it to steer the camera, and use the push buttons to walk, jump, use items and change hotbar slot. It has been tested in game with all five buttons, swing detection and camera aiming.

Because the game only sees normal keyboard and mouse input, it needs no mods and works with a vanilla client, which fits the Zero Client Mod Requirement above. Firmware, wiring and pin map: [exacyyv/Minecraft-Sword-Using-Esp32-S3-](https://github.com/exacyyv/Minecraft-Sword-Using-Esp32-S3-).
