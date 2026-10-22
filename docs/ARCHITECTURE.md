# Server Architecture and Subsystems

This document describes the runtime environment, network topology, protocol translation layers, and custom subsystems powering Project Hajaribagh.

---

## 1. Runtime Environment

* **Game Version**: Minecraft 26.3
* **Mod Loader**: Fabric Loader 0.19.5
* **Java Runtime**: OpenJDK 25 (64-bit)
* **Garbage Collector**: Z Garbage Collector (`-XX:+UseZGC`)
* **Allocated Heap**: Minimum 1536 MB, Maximum 2560 MB (`-Xms1536M -Xmx2560M`)
* **Startup Command**:
  ```bash
  exec java -Xms1536M -Xmx2560M -XX:+UseZGC -jar fabric-server-launch.jar nogui
  ```

---

## 2. Core Mods and Optimization Stack

All active mods in `mods/` are purely server-side or protocol-level:

| Mod Name | Version | Function |
| :--- | :--- | :--- |
| `fabric-api` | 0.162.0+26.3 | Base hooks and event bus for Fabric |
| `lithium` | 0.26.2+mc26.3 | Physics, chunk, and AI tick optimization |
| `ferritecore` | 9.0.0 | Memory footprint reduction and data structure deduplication |
| `krypton` | 0.3.2 | Optimized network stack with Netty and libdeflate compression |
| `polymer-bundled` | 0.18.4+26.3 | Server-side model, item, and block translation into vanilla display entities |
| `brewery` | 0.17.1+26.3 | Fermentation, cauldrons, aging barrels, and alcoholic beverages |
| `custompaintings` | 4.0.2+26.3 | Dynamic painting registration and motive replacements |

---

## 3. Network and Tunnel Architecture

To allow friends in Canada and Bangladesh to connect without requiring port forwarding on home routers:
* The Minecraft server binds locally to `0.0.0.0:25565`.
* The `playit.gg` background daemon creates a TLS tunnel to nearest Anycast edge nodes.
* External endpoint: `cairo-temptation.tun.ply.gg:47309` (or direct IP alias `215.ip.gl.ply.gg:47309`).
* All external packets route over TCP through the tunnel directly into local port 25565.

---

## 4. Custom Subsystems

### A. Cannabis and Smoking (`datapacks/cannabis_smoke`)
* **Item**: Right-clickable Cannabis Joints.
* **Recipe**: 1 Paper + 1 Dried Kelp yields 3 Cannabis Joints.
* **Mechanics**:
  * Consuming or right-clicking triggers a scoreboard increment.
  * Plays a sizzling campfire audio effect (`block.campfire.crackle`).
  * Spawns a 3D animated column of camp smoke particles above the player head.
  * Applies brief status effects (Nausea, Speed, Regeneration).
  * Also supports manual triggering via `/trigger smoke`.

### B. Custom Paintings System
* Source images stored under `custompaintings/ServerPaintings/images/`.
* Includes Bengali cultural figures, political memes, and historical scenes (Hasina, Chuppu, Sarjis Alam, Dhaka scene, Nahid & Asif, Bengal meme).
* Quantized into standard square and rectangular ratios: 1x2, 2x2, 3x2, 2x3, and 4x3 blocks.
* Overrides vanilla painting motives so unmodded clients see them automatically.
