# Server vs Client Architectural Matrix

This document defines the strict boundary between server-side operations and client-side requirements for Project Hajaribagh. Read this before proposing, downloading, or configuring any mod, plugin, or datapack.

---

## 1. Core Principle: The Zero Client Mod Invariant

The server serves players across three countries: the United Kingdom, Canada, and Bangladesh. Several players use standard vanilla launchers or offline clients.

Under no circumstances may the server require a client-side mod jar to join. If a player connects with a completely unmodified, vanilla Minecraft client, the connection must succeed instantly without disconnect errors or handshake rejections.

---

## 2. Component Distribution Matrix

| Component | Execution Location | Client Requirement | Virtualization Method | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Minecraft Core | Server (Oracle Cloud VM) | Vanilla 1.21.1 / 26.3 | Standard TCP handshake | Fabric Loader 0.19.5 on Oracle JDK 25 |
| Lithium | Server | None | Internal game physics optimization | Reduces tick lag, zero client awareness |
| FerriteCore | Server | None | Memory data structure compaction | Saves RAM on server heap |
| Krypton | Server | None | Optimized network stack | Reduces CPU time in packet serializing |
| Polymer Bundled | Server | None | Protocol packet translation | Virtualizes custom blocks and entities |
| Geyser + Floodgate | Server | Bedrock Client (Optional) | Bedrock to Java protocol translation | Allows friends on mobile/console to join |
| LuckPerms | Server | None | Permission system | Governs roles and commands |
| Bluemap | Server | Web Browser | Dynamic web map server | Live map at port 8100 |
| Datapacks (Citadel, Guide, Tycoon) | Server | None | Vanilla mcfunction engine | Completely server driven |
| Custom Paintings Pack | Server + Client Delivery | Vanilla Resource Pack prompt | Server resource pack URL | Hash verified via `server.properties` |
| Quarantined Mods (Guns++) | Quarantined | Excluded | None | Removed to protect client handshake |

---

## 3. How New Features Must Be Implemented

When adding gameplay mechanics, decorative elements, or items:

### Method 1: Pure Server Datapacks (Preferred)
* Implement logic using Minecraft mcfunction scripts, scoreboards, triggers, and loot tables.
* Examples: `underground_citadel`, `great_treasury`, `server_guide`, `salman_f_rahman`, `cannabis_smoke`.
* Advantage: 100% native compatibility with all Java and Bedrock clients.

### Method 2: Polymer Virtualization
* If a Fabric mod adds custom items or entities, it must be registered with Polymer.
* Polymer automatically converts custom blocks into vanilla blocks with custom block states or display entities for connecting clients.

### Method 3: Server Resource Packs
* Visual enhancements (such as paintings, textures, audio) are packaged into zip files and referenced in `server.properties`.
* Clients download them automatically upon login without manual file installation.
