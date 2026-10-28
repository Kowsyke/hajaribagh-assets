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
* `scripts/`: Operational tools, remote log viewers, RCON helpers, and the active builder generator `build_full_veteran_bunker.py`.
* `scripts/generators/`: Procedural architectural generator library with 50+ modules for roofs, windows, timber frames, domes, trees, plazas, and interior partitions.
* `references/architectural-styles/`: Curated JSON architectural style templates for medieval, gothic, modern, elven, and oriental builds.
* `references/blueprints/`: Veteran subterranean bunker schematics and room layout specifications.
* `.agents/skills/`: Verified Minecraft agent skills suite for building, commands, datapacks, and server administration.
* `docs/`: Comprehensive guides:
  * `SERVER_CLIENT_MATRIX.md`: Client vs server compatibility rules.
  * `CITADEL_UTOPIA_BLUEPRINT.md`: Subterranean Mega Base coordinates and sector breakdown.
  * `OPERATIONS.md`: Server deployment and sync runbook.
  * `MEMBERS_ROLES.md`: Player titles and locations.
  * `MODS_DATAPACKS.md`: Complete mod and datapack catalog.
* `quarantine/`: Quarantined mods and discontinued functions.

---

## 4. Subterranean Hivemind Bunker Landmarks

* Ancient Tree Surface Entrance: `(117, 78, -330)`.
* Sector Minus 1: The Great Treasury: `(X: 108..126, Z: -333..-301, Y: 64..72)`.
* Central Descent Staircase: `(X: 116..118, Z: -322..-308, Y: 64 down to 50)`.
* Sector 0: Central Command Rotunda: `(X: 111..123, Z: -307..-295, Y: 46..53)`.
* Sector 1: Tool & Equipment Armory: `(X: 74..94, Z: -307..-295, Y: 46..53)`.
* Sector 2: Blacksmith & Smelting Workshop: `(X: 74..94, Z: -291..-275, Y: 46..53)`.
* Sector 3: Grand Arcane Library: `(X: 140..160, Z: -307..-295, Y: 46..53)`.
* Sector 4: Brewing & Alchemy Laboratory: `(X: 140..160, Z: -291..-275, Y: 46..53)`.
* Sector 5: Underground Farm & Botany Pod: `(X: 96..114, Z: -291..-265, Y: 46..53)`.
* Sector 6: Modern Subterranean Housing: `(X: 120..138, Z: -291..-265, Y: 46..53)`.
* Sector 7: King's Council & High Parliament: `(X: 105..129, Z: -261..-235, Y: 46..53)`.
* Sector 8: The Celestial Portal Nexus: `(X: 107..127, Z: -233..-210, Y: 44..53)`.
* Sector 9: The Sovereign Banquet & Feasting Hall: `(X: 105..129, Z: -261..-235, Y: 36..45)`.
* Sector 10: The Royal Geothermal Spa & Bathhouse: `(X: 120..138, Z: -291..-265, Y: 36..45)`.
* Sector 11: The Subterranean Hyperloop Transit Hub: `(X: 112..122, Z: -306..-296, Y: 37..43)`.
* Deep Infrastructure Tier 3 Facilities:
  * Central Beacon Well and Bubble Elevators: `(X: 111..120, Z: -304..-296, Y: 36..45)`.
  * Heavy Ore Processing Refinery: `(X: 78..90, Z: -289..-277, Y: 38..45)`.
  * Forbidden Apocrypha Archive: `(X: 144..156, Z: -305..-297, Y: 38..45)`.
  * Subterranean Aquaponics Grotto: `(X: 98..112, Z: -289..-267, Y: 36..45)`.

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
9. `minecraft-moling-builder`: Conversational building assistant based on MoLing architecture. Decomposes prompts into sequential commands, manages block replacement modes, and interfaces directly with the server via `scripts/moling_rcon.py`.
10. `minecraft-interior-decorator`: Professional interior design and decoration skill for Minecraft 1.21. Specializes in furniture construction, lighting fixtures, object logic, workstation clusters, functional living spaces, ceremonial halls, and cozy atmospheric detailing.
11. `minecraft-nature-terraformer`: Subterranean landscaping and biome terraforming skill for Minecraft 1.21. Designs organic subterranean gardens, hanging foliage, aquascaping, crystal geode caverns, stepped irrigation terraces, and custom organic vegetation.


