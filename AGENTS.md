# Agent Guidelines: Project Hajaribagh

This document is the operational context for autonomous AI coding agents (Claude, Antigravity, Codex, Cursor, etc.) working on Project Hajaribagh. Read this before modifying any file, script, or configuration.

---

## 1. Project Overview and Mission

Project Hajaribagh is a private, custom-modded Minecraft server engineered for a tight group of friends spread across the United Kingdom, Canada, and Bangladesh. 

The server blends humor, Bangladeshi cultural references, survival gameplay, and hangout mechanics. It runs 24/7 on an Oracle Cloud VM in London (direct public IP, with the original Playit tunnel kept as a fallback).

---

## 2. Team and Member Registry

### Core Developers and Operators
* **Kowsyke (abirmia205@gmail.com)**: Lead engineer and server operator. Located in the United Kingdom.
* **exacyyv**: Co-developer and collaborator. Has full collaborator access to vibe-code, create mods, and deploy features. Also built the Minecraft sword controller described in the README.

### Players and Community
* **GothHunterJamal**: Primary survival companion and roommate. Connects through the direct public IP.
* **ahsane**: Remote player connecting from Canada.
* **Dip**: Remote player connecting from Bangladesh.

---

## 3. Non-Negotiable Engineering Invariants

Any agent working on this repository must enforce the following rules:

### Invariant A: Zero Client Mods (The Vanilla Handshake Rule)
Players connect using unmodded vanilla clients, standard launchers, or offline accounts. 
* Never install Fabric or Forge mods on the server that register custom client-side blocks, entities, or screens unless they are backed by Polymer.
* If a mod forces a connecting client to have a matching `.jar` file, it will break the connection for friends in Canada and Bangladesh.
* All new items, mechanics, and interactive features must be implemented via:
  1. Pure server-side Minecraft datapacks (functions, loot tables, scoreboards, triggers).
  2. Polymer-compatible mods (which translate custom server items into vanilla display packets).
  3. Server-side resource packs delivered automatically on connection.

### Invariant B: Punctuation and Writing Style
* Never use an em dash, an en dash, a double hyphen, or a single hyphen as sentence punctuation in documentation, code comments, commit messages, or dialogue copy. Use periods, commas, colons, or parentheses instead.
* Write directly, plainly, and specifically. Avoid marketing buzzwords and filler phrases.

### Invariant C: Performance Budget
* Maximum heap allocation is currently 8192 MB (8 GB) with ZGC on the 24 GB cloud VM (`-Xms4096M -Xmx8192M`).
* Never install heavy 3D noise generation datapacks (like Terralith) that alter terrain equations.
* Prioritize pre-baked jigsaw structures, lightweight datapacks, and memory optimization mods (Lithium, FerriteCore, Krypton).

---

## 4. Current Technical Architecture

* **Engine**: Minecraft 26.3 running on Fabric Loader 0.19.5.
* **Java Virtual Machine**: Oracle JDK 25 LTS with Z Garbage Collector (`-XX:+UseZGC`), run by systemd as `minecraft.service`.
* **Hardware**: Oracle Cloud Always Free `VM.Standard.A1.Flex`, 4 ARM cores, 24 GB RAM, Ubuntu 24.04.
* **Networking**: Direct public IP `132.226.135.26:25565`, plus the `playit.gg` tunnel at `cairo-temptation.tun.ply.gg:47309` as a fallback.
* **Deploying**: `scripts/deploy-to-cloud.sh` copies `datapacks/` and `configs/` to the VM. See `docs/OPERATIONS.md`.
* **Asset Pipeline**: Custom paintings pack quantized and bundled in `Hajaribagh-Paintings.zip`, which overrides the vanilla painting textures.
* **Subsystems**:
  * `datapacks/cannabis_smoke`: Right-clickable joint items, smoke particle puffs, campfire audio, and status effects.
  * `datapacks/ore_xray`: Host only spectator and night vision toggle.
  * `configs/polymer`: Protocol translation layer for vanilla clients.
  * `custompaintings`: Painting pack mod. Its Modrinth page lists it as required on the client, so check `docs/KNOWN_ISSUES.md` before relying on it.

---

## 5. Development Workflow for Peer Agents

When implementing features requested by either Kowsyke or exacyyv:
1. Check existing datapacks in `datapacks/` to avoid command and scoreboard objective namespace collisions.
2. Ensure all commands use silent execution where appropriate (do not flood public chat with system notifications).
3. If creating custom items, use vanilla item bases with custom model data or NBT tags.
4. Document all changes in git commits using plain descriptions without pause dashes.
5. Pull before you start (`git pull --ff-only`). Kowsyke and exacyyv both commit to this repo, and docs can go stale quickly.
6. Never commit secrets or passwords. Blank them in config copies first.
7. Do not edit `Hajaribagh-Paintings.zip` without updating `resource-pack-sha1` in `configs/server.properties`. The steps are in `docs/OPERATIONS.md`.

---

## 6. Mandatory Feasibility and Latency Assessment Policy

Before proposing or introducing any mod, datapack, or configuration update, every agent must provide an explicit feasibility evaluation. 

Review [`docs/FEASIBILITY_AND_LIMITS.md`](./docs/FEASIBILITY_AND_LIMITS.md) for the full hardware envelope:
* If a feature introduces heavy single thread tick overhead (such as 3D terrain density calculations), reject it.
* If a mod requires client side `.jar` installations, reject it.
* Always communicate performance tradeoffs transparently with the developers before writing code.

