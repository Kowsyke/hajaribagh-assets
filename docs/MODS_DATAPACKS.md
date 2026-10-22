# Installed Mods, Datapacks, and Assets

This document catalogs every active modification, server datapack, and configuration installed in Project Hajaribagh.

---

## 1. Active Mods (`mods/`)

| File Name | Purpose | Side Requirement | Notes |
| :--- | :--- | :--- | :--- |
| `fabric-api-0.162.0+26.3.jar` | Core Fabric hooks | Server | Standard Fabric prerequisite |
| `lithium-fabric-0.26.2+mc26.3.jar` | Physics and chunk optimization | Server | Drastically lowers MSPT (tick time) |
| `ferritecore-9.0.0-fabric.jar` | Memory deduplication | Server | Cuts RAM usage by up to 30 percent |
| `krypton-0.3.2.jar` | Network compression | Server | Uses libdeflate for fast packet routing |
| `polymer-bundled-0.18.4+26.3.jar` | Protocol virtualization | Server | Delivers custom items to vanilla clients |
| `brewery-0.17.1+26.3.jar` | Alcoholic brewing mechanics | Server | Powered by Polymer for unmodded clients |
| `custompaintings-fabric-4.0.2+26.3.jar` | Custom painting catalog | Server | Overrides painting motives on server |

---

## 2. Server Datapacks (`datapacks/`)

### `cannabis_smoke`
* **Path**: `datapacks/cannabis_smoke/`
* **Mechanics**:
  * Custom shaped crafting: 1 Paper + 1 Dried Kelp in a crafting grid produces 3 Cannabis Joints.
  * Right-click detection increments the `cannabis.used` scoreboard objective.
  * Plays `block.campfire.crackle` audio at the player location.
  * Generates an animated column of `campfire_cosy_smoke` particles rising above the player head.
  * Awards temporary status effects: Nausea for 5 seconds, Speed II for 15 seconds, and Regeneration I for 10 seconds.
  * Supports direct command execution via `/trigger smoke`.

### `ore_xray`
* **Path**: `datapacks/ore_xray/`
* **Purpose**: Administrative utility for inspecting ore generation and underground structures.

---

## 3. Custom Paintings Asset Pack

* **Package**: `Hajaribagh-Paintings.zip`
* **Resolution**: High density quantized PNGs formatted into standard block dimensions.
* **Subjects**:
  * Sheikh Hasina (2x3 blocks)
  * President Chuppu (1x2 blocks)
  * Sarjis Alam (3x2 blocks)
  * Dhaka street scene (4x3 blocks)
  * Nahid Islam and Asif Mahmud (2x3 blocks)
  * Bengal meme artwork (2x2 blocks)
* **Client Delivery**: Delivered via the `resource-pack` directive in `server.properties`. Overrides all 46 vanilla paintings so every painting placed in the game displays custom artwork.
