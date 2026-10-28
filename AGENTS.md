# Agent Guidelines: Project Hajaribagh

This document is the operational context for autonomous AI coding agents (Claude, Antigravity, Argon, Codex, Cursor, etc.) working on Project Hajaribagh. Read this before modifying any file, script, or configuration.

---

## 1. Project Overview and Mission

Project Hajaribagh is a private, custom-modded Minecraft server engineered for a tight group of friends spread across the United Kingdom, Canada, and Bangladesh. 

The server blends humor, Bangladeshi cultural references, survival gameplay, and hangout mechanics. It runs 24/7 on an Oracle Cloud VM in London (direct public IP, with the original Playit tunnel kept as a fallback).

---

## 2. Team and Member Registry

### Core Developers and Operators
* **King Abir (Kowsyke, abirmia205@gmail.com)**: Prime Minister, supreme ruler, lead engineer, and host operator. Located in the United Kingdom. Must always and everywhere be introduced and addressed as King Abir across in-game copy, dialogue, guide books, and server notices.
* **exacyyv**: Minister of Public Works, co-developer, and collaborator. Has full collaborator access to vibe-code, create mods, and deploy features.
* **Dip**: Minister of Communication and server moderator. Located in Bangladesh, with collaborator access to GitHub.

### Players and Parliament
* **Ahsane (ahsane)**: Honorable President (Rashtrapati), Vice Captain, and Chief Advisor. Connects from Canada.
* **GothHunterJamal (Safwan)**: Minister of Tourism, Wildlife, and Hunting. Primary survival companion and roommate.
* **Rohit ATB (GREAT-RED-DRAGO)**: Minister of Agriculture and Tannery. Hajaribagh local living in Dhaka.
* **First Lady and Citizens**: King Abir's girlfriend and all new citizens hold equal standing beneath King Abir, who holds exclusive sovereign authority.

---

## 3. Non-Negotiable Engineering Invariants

Any agent working on this repository must enforce the following rules:

### Invariant A: Zero Client Mods (The Vanilla Handshake Rule)
Players connect using unmodded vanilla clients, standard launchers, or offline accounts. 
* Never install Fabric or Forge mods on the server that register custom client-side blocks, entities, or screens unless they are backed by Polymer.
* If a mod forces a connecting client to have a matching `.jar` file, it will break the connection for friends in Canada and Bangladesh.
* Review [`docs/SERVER_CLIENT_MATRIX.md`](./docs/SERVER_CLIENT_MATRIX.md) for the complete client and server compatibility breakdown.
* All new items, mechanics, and interactive features must be implemented via:
  1. Pure server-side Minecraft datapacks (functions, loot tables, scoreboards, triggers).
  2. Polymer-compatible mods (which translate custom server items into vanilla display packets).
  3. Server-side resource packs delivered automatically on connection.

### Invariant B: Punctuation and Writing Style
* Never use an em dash, an en dash, a double hyphen, or a single hyphen as sentence punctuation in documentation, code comments, commit messages, or dialogue copy. Use periods, commas, colons, or parentheses instead.
* Write directly, plainly, and specifically. Avoid marketing buzzwords and filler phrases.
* Bold is reserved for labels. Do not scatter bold words across paragraphs for emphasis.

### Invariant C: Performance Budget
* Maximum heap allocation is currently 8192 MB (8 GB) with ZGC on the 24 GB cloud VM (`-Xms4096M -Xmx8192M`).
* Never install heavy 3D noise generation datapacks (like Terralith) that alter terrain equations.
* Prioritize pre-baked jigsaw structures, lightweight datapacks, and memory optimization mods (Lithium, FerriteCore, Krypton).

### Invariant D: Iron-Clad Guide Book and Repository Synchronization Rule
Whenever any new mod, command, mechanic, or player role is introduced, changed, or removed on Project Hajaribagh, the working agent must:
1. Update the in-game guide book in `datapacks/server_guide/data/server_guide/function/give_book.mcfunction` with the new features, commands, or roles.
2. Increment the guide version in `give_book.mcfunction` and `tick.mcfunction` so returning players receive the new edition automatically upon logging in.
3. Update the repository documentation (`README.md`, `AGENTS.md`, and `docs/MODS_DATAPACKS.md`).
4. Deploy the updated datapack to the cloud server and run `/reload`.
5. Commit and push all changes to the GitHub repository on `main`.
No task is complete until both the in-game guide book and the GitHub repository are fully synchronized.

---

## 4. Current Technical Architecture

* **Engine**: Minecraft 26.3 running on Fabric Loader 0.19.5.
* **Java Virtual Machine**: Oracle JDK 25 LTS with Z Garbage Collector (`-XX:+UseZGC`), run by systemd as `minecraft.service`.
* **Hardware**: Oracle Cloud Always Free `VM.Standard.A1.Flex`, 4 ARM cores, 24 GB RAM, Ubuntu 24.04.
* **Networking**: Direct public IP `132.226.135.26:25565`, plus the `playit.gg` tunnel at `cairo-temptation.tun.ply.gg:47309` as a fallback.
* **Deploying**: `./scripts/deploy-to-cloud.sh` copies `datapacks/` and `configs/` to the VM. See `docs/OPERATIONS.md`.
* **Asset Pipeline**: Custom paintings pack quantized and bundled in `Hajaribagh-Paintings.zip`, which overrides the vanilla painting textures.
* **Active Datapacks**:
  * `datapacks/underground_citadel`: The Subterranean Utopia Mega Base (12 sectors: Atrium, Forge, Biosphere, Portal Nexus, Athenaeum, Banquet Hall, Transit Hub, Parliament, Suites, Conduits). See [`docs/CITADEL_UTOPIA_BLUEPRINT.md`](./docs/CITADEL_UTOPIA_BLUEPRINT.md).
  * `datapacks/great_treasury`: The Hobbit themed underground treasury and storage vault (X: 108..126, Z: -333..-301, Y: 64..72).
  * `datapacks/salman_f_rahman`: Mining tycoon system, sidebar leaderboard, and daily dividends.
  * `datapacks/cannabis_smoke`: Right-clickable joint items, smoke particle puffs, campfire audio, and status effects.
  * `datapacks/ore_xray`: Host only spectator and night vision toggle.
  * `datapacks/server_guide`: Written guide book auto-delivered to players on login and via `/trigger guide`.
  * `datapacks/moar_bosses`: Custom boss encounters and combat challenges.
  * `datapacks/more_mobs`: Additional custom mob variants.
  * `datapacks/ridedragon`: Dragon mount mechanics and flight controls.
* **Active Server Mods**:
  * `Lithium`, `FerriteCore`, `Krypton`: Performance and physics optimization.
  * `Geyser` and `Floodgate`: Bedrock cross-play translation layer.
  * `Polymer`: Protocol virtualization for client-safe server items.
  * `Bluemap`: Live isometric map viewer.
  * `LuckPerms`: Role and permission management.
* **Quarantined Mods**:
  * `quarantine/guns_plus_plus`: Removed because it disrupted the vanilla client handshake.

---

## 5. Development Workflow for Peer Agents (Claude, Argon, Codex)

When implementing features requested by either Kowsyke or exacyyv:
1. Check existing datapacks in `datapacks/` to avoid command and scoreboard objective namespace collisions.
2. Ensure all commands use silent execution where appropriate (never broadcast raw debug messages or tellraw spam to online players).
3. If creating custom items, use vanilla item bases with custom model data or NBT components.
4. Document all changes in git commits using plain descriptions without pause dashes.
5. Pull before you start (`git pull --ff-only`). Kowsyke and exacyyv both commit to this repo, and docs can go stale quickly.
6. Never commit secrets or passwords. Blank them in config copies first.
7. Test live changes using remote RCON via SSH before finishing tasks.
8. Maintain stair geometry invariants: descending stairs facing the direction of travel, wall skirting right-side up, and chairs facing their respective tables or podiums.

---

## 6. Minecraft Agent Skills and In-Game Building Guide

Agents have access to 8 curated skills in `.agents/skills/`:

* `minecraft-architect-builder`: Converts high-level architectural briefs into structured Minecraft 1.21 commands and `.mcfunction` files. Adheres to depth rules, palettes, and blockstate orientations.
* `minecraft-builder-skill`: Generates `.nbt` structures and launches Vite-based 3D previewers.
* `minecraft-commands-scripting`: Vanilla command reference, target selectors, and scoreboard logic.
* `minecraft-datapack`: Datapack format specifications and registry tags.
* `minecraft-server-admin`: Diagnostics, GC flags, and performance monitoring.
* `minecraft-worldedit-ops`: Large-scale terrain brushes and schematics.
* `minecraft-crossplay-ops`: Bedrock and Geyser bridging configuration.
* `minecraft-permissions-admin`: LuckPerms permission trees and group administration.

