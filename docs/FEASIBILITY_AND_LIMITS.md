# Server Hardware Feasibility and Performance Envelope

This document is the non-negotiable standard for performance governance on Project Hajaribagh. Any feature, mod, or datapack considered for this server must be evaluated against these exact benchmarks before implementation.

---

## 1. Production Hardware Specifications

* **Cloud Node**: Oracle Cloud Infrastructure (Always Free Tier)
* **Processor**: 4x 3.0 GHz Ampere Altra Neoverse-N1 cores (ARM64 architecture)
* **System Memory**: 24 GB RAM total
* **Minecraft Dedicated Allocation**: 8 GB RAM with Z Garbage Collector (`-Xms4096M -Xmx8192M -XX:+UseZGC`)
* **Storage**: NVMe SSD (High IOPS block volume)
* **Target Tick Rate**: 20.0 TPS (Ticks Per Second) with MSPT below 35.0 milliseconds

---

## 2. Mandatory Agent Rule: Pre-Implementation Feasibility Audit

From this point forward, whenever any developer or AI agent (Antigravity, Claude, Codex, etc.) proposes adding or altering a feature, they must provide an explicit feasibility evaluation covering:

1. **Single-Threaded Tick Impact**: Will this logic stall the main Minecraft game loop?
2. **Heap Footprint**: Will this add persistent memory overhead to the 8 GB heap?
3. **The Vanilla Handshake Test**: Will this require client `.jar` installations or kick unmodded friends?
4. **Network Bandwidth**: Will this overburden the 4 Gbps interface or increase packet drops for players in Bangladesh and Canada?

If a proposed mod fails any of these four criteria, it must be rejected immediately without compromise.

---

## 3. Hard Limitations (What Will Cause Lag or Break the Server)

### A. 3D Mathematical Terrain Noise Generators (Strictly Infeasible)
* **Examples**: Terralith, William Wythers Overhauled Overworld, custom density function datapacks.
* **Why it fails**: In Minecraft, world generation noise is processed on a single core. Computing complex 3D noise equations takes 2x to 3x longer per chunk. When multiple players travel on horses, boats, or fly into unexplored territory simultaneously, MSPT spikes above 50 ms, causing severe rubber-banding and server stalls.

### B. Client-Enforced Fabric or Forge Mods (Strictly Infeasible)
* **Examples**: Create, Twilight Forest, Alex's Mobs, Tech mods.
* **Why it fails**: They register custom blocks and entity IDs on the client side. Unmodded vanilla launchers and offline accounts will be rejected at the login handshake.

### C. Excessive View Distances (Strictly Infeasible)
* **Limits**: Server view distance must never exceed 10 chunks.
* **Why it fails**: Chunks scale quadratically. A view distance of 16 loads 1,089 chunks around each player, whereas a distance of 10 loads only 441 chunks. Let players use Sodium on their clients for extended visual distance.

### D. Unbounded Entity Counts and Hopper Clocks
* **Limits**: Maximum 300 to 400 active entities in loaded chunks.
* **Why it fails**: Entity ticking and pathfinding consume the majority of main thread CPU time during passive gameplay.

---

## 4. Maximizations (What the Server Can Safely Handle at Peak Performance)

### A. Pre-Baked Jigsaw Structure Packs (Fully Feasible)
* **Examples**: Dungeons and Taverns, Towns and Towers.
* **Why it succeeds**: These packs use pre-compiled structure templates made of vanilla blocks. The server pastes them into chunks during generation with zero mathematical noise overhead. Once pasted, they are static blocks with zero ongoing CPU load.

### B. World Pregeneration via Chunky (Recommended Maximization)
* **Workflow**: Pre-generating a 3,000 to 5,000 block radius around spawn writes all chunk data directly to the NVMe disk before players log in.
* **Benefit**: When players explore the world, the server reads blocks from SSD cache in less than 2 milliseconds instead of computing chunk generation on the CPU. Live exploration lag is reduced to zero.

### C. Server-Side Datapacks and Scoreboards (Fully Feasible)
* **Examples**: Mini-games, custom recipes, casino machines, custom weapons with CustomModelData, custom bosses, quests, and economy systems.
* **Why it succeeds**: Vanilla command logic is lightweight and runs natively inside the optimized Fabric environment.

### D. Polymer Virtual Entities (Fully Feasible)
* **Examples**: Custom drinks, plushies, custom backpacks, and decorative furniture.
* **Why it succeeds**: Polymer intercepts modded entities on the server and translates them into vanilla display entities before sending packets to players.
