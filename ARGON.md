# Argon Operational Manifest: Project Hajaribagh

Welcome Argon. This document is your primary entry point for Project Hajaribagh. Read this alongside [`AGENTS.md`](./AGENTS.md), [`docs/SERVER_CLIENT_MATRIX.md`](./docs/SERVER_CLIENT_MATRIX.md), and [`docs/CITADEL_UTOPIA_BLUEPRINT.md`](./docs/CITADEL_UTOPIA_BLUEPRINT.md).

---

## 1. Quick Reference & Endpoints

* Production Server: Oracle Cloud Infrastructure, Ubuntu 24.04 (Ampere A1 ARM64, 4 OCPUs, 24 GB RAM).
* Public IP: `132.226.135.26:25565` (Direct connect for Java and Bedrock via Geyser).
* SSH Access: `ssh -i ~/.ssh/id_ed25519 ubuntu@132.226.135.26`.
* Server Path on VM: `/home/ubuntu/minecraft-server`.
* Service Unit: `minecraft.service` (managed via systemctl).
* Deploy Command: `./scripts/deploy-to-cloud.sh` from the repository root.

---

## 2. Invariants You Must Never Violate

1. Zero Client Mods (The Vanilla Handshake Rule):
   Connecting players from the UK, Canada, and Bangladesh use standard unmodded vanilla clients. Never add mods that force client jar downloads. All mechanics must use pure server datapacks or Polymer virtualization.
2. Punctuation Rule (Strict):
   Never use an em dash, an en dash, a double hyphen, or a single hyphen as sentence punctuation in documentation, code comments, commit messages, or dialogue copy. Use periods, commas, colons, or parentheses instead.
3. Writing Style:
   Plain, specific, and human. Avoid marketing filler ("seamless", "robust", "cutting edge", "elevate", "unlock"). Bold is for labels only.
4. Silent Execution:
   Do not broadcast `tellraw @a` spam to active players during automated builds or scripts.
5. Guide Book Sync:
   Whenever mechanics or commands change, update `datapacks/server_guide`, increment the version, and push to GitHub.

---

## 3. Directory Layout and Architecture

* `datapacks/`: Active server datapacks (`underground_citadel`, `great_treasury`, `salman_f_rahman`, `server_guide`, `cannabis_smoke`, `ore_xray`, `moar_bosses`, `more_mobs`, `ridedragon`).
* `configs/`: Live configuration templates (`server.properties`, `polymer/`, `lithium.properties`, `ferritecore.mixin.properties`, `Geyser-Fabric/`, `luckperms/`).
* `scripts/`: Operational tools, remote log viewers, RCON helpers, and the active builder generator `generate_perfect_stairs_and_citadel.py`.
* `.agents/skills/`: Verified Minecraft agent skills suite for building, commands, datapacks, and server administration.
* `docs/`: Comprehensive guides:
  * `SERVER_CLIENT_MATRIX.md`: Client vs server compatibility rules.
  * `CITADEL_UTOPIA_BLUEPRINT.md`: Subterranean Mega Base coordinates and sector breakdown.
  * `OPERATIONS.md`: Server deployment and sync runbook.
  * `MEMBERS_ROLES.md`: Player titles and locations.
  * `MODS_DATAPACKS.md`: Complete mod and datapack catalog.
* `quarantine/`: Quarantined mods and discontinued functions.

---

## 4. Subterranean Utopia Landmarks

* Ancient Tree Surface Entrance: `(117, 78, -330)`.
* Sector -1: The Great Treasury: `(X: 108..126, Z: -333..-301, Y: 64..72)`.
* Central Descent Staircase: `(X: 116..118, Z: -322..-308, Y: 64 down to 50)`.
* Central Crossroads Landing: `(X: 114..120, Y: 50, Z: -307..-305)`.
* Sector 0: Bio Dome Atrium and Aquarium: `(X: 104..130, Z: -304..-278, Y: 50..58)`.
* Sector 1: Dwarven Forge and Super Smelter: `(X: 82..99, Z: -301..-281, Y: 50..58)`.
* Sector 2: Hydroponics Biosphere and Apiary: `(X: 136..154, Z: -302..-280, Y: 50..61)`.
* Sector 3: Celestial Portal Nexus: `(X: 106..128, Z: -302..-280, Y: 36..48)`.
* Sector 4: Grand Athenaeum Library: `(X: 80..102, Z: -330..-306, Y: 50..62)`.
* Sector 5: Sovereign Banquet Hall: `(X: 132..154, Z: -330..-306, Y: 50..62)`.
* Sector 6: Hyperloop Transit Hub: `(X: 104..130, Z: -345..-325, Y: 49..58)`.
* Sector 7: Grand High Parliament: `(X: 104..130, Z: -276..-244, Y: 50..58)`.
* Sector 8: Sovereign Residential Suites: `(X: 92..142, Z: -268..-231, Y: 50..58)`.

---

## 5. Agent Skills Toolkit

The repository is equipped with curated, verified Minecraft skills located in `.agents/skills/`:

1. `minecraft-architect-builder`: Master architectural builder for Minecraft 1.21. Generates block palettes, depth layers, mathematical geometry (ellipses, catenary vaults, domes, spiral stairs), and correct blockstate orientations from natural language prompts.
2. `minecraft-builder-skill`: Programmatic NBT structure generation using Lodestone and Three.js 3D web previewing.
3. `minecraft-commands-scripting`: Vanilla 1.21 commands, target selectors, execute chains, scoreboards, and NBT path manipulation.
4. `minecraft-datapack`: Datapack structure, tick/load functions, tags, recipes, and loot table management.
5. `minecraft-server-admin`: Fabric server operations, GC tuning, crash diagnosis, and lag prevention.
6. `minecraft-worldedit-ops`: Fast asynchronous terrain modification, brushes, and schematics.
7. `minecraft-crossplay-ops`: Geyser and Floodgate configuration and Bedrock optimization.
8. `minecraft-permissions-admin`: LuckPerms permission hierarchy and group configuration.

