# Agent Guidelines: Project Hajaribagh

This document is the operational context for autonomous AI coding agents (Claude, Antigravity, Codex, Cursor, etc.) working on Project Hajaribagh. Read this before modifying any file, script, or configuration.

---

## 1. Project Overview and Mission

Project Hajaribagh is a private, custom-modded Minecraft server engineered for a tight group of friends spread across the United Kingdom, Canada, and Bangladesh. 

The server blends humor, Bangladeshi cultural references, survival gameplay, and hangout mechanics. It runs on a local node in the United Kingdom with public routing via an encrypted reverse tunnel.

---

## 2. Team and Member Registry

### Core Developers and Operators
* **Kowsyke (abirmia205@gmail.com)**: Lead engineer and Node A host. Located in the United Kingdom.
* **exacyyv**: Co-developer and collaborator. Has full collaborator access to vibe-code, create mods, and deploy features.

### Players and Community
* **GothHunterJamal**: Primary survival companion and roommate. Connects via local area network (LAN) and tunnel.
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
* Maximum heap allocation is currently 2560 MB (2.5 GB) with ZGC.
* Never install heavy 3D noise generation datapacks (like Terralith) that alter terrain equations.
* Prioritize pre-baked jigsaw structures, lightweight datapacks, and memory optimization mods (Lithium, FerriteCore, Krypton).

---

## 4. Current Technical Architecture

* **Engine**: Minecraft 26.3 running on Fabric Loader 0.19.5.
* **Java Virtual Machine**: OpenJDK 25 with Z Garbage Collector (`-XX:+UseZGC`).
* **Networking**: Routed through `playit.gg` reverse tunnel to `cairo-temptation.tun.ply.gg:47309` (internal port 25565).
* **Asset Pipeline**: Custom paintings pack quantized and bundled in `Hajaribagh-Paintings.zip`.
* **Subsystems**:
  * `datapacks/cannabis_smoke`: Right-clickable joint items, 3D animated particle plumes, campfire audio, and status effects.
  * `configs/polymer`: Protocol translation layer for vanilla clients.
  * `custompaintings`: Server-side painting catalog replacing vanilla painting motives.

---

## 5. Development Workflow for Peer Agents

When implementing features requested by either Kowsyke or exacyyv:
1. Check existing datapacks in `datapacks/` to avoid command and scoreboard objective namespace collisions.
2. Ensure all commands use silent execution where appropriate (do not flood public chat with system notifications).
3. If creating custom items, use vanilla item bases with custom model data or NBT tags.
4. Document all changes in git commits using plain descriptions without pause dashes.
