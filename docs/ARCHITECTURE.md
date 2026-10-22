# Server Architecture and Cloud Infrastructure

This document details the live production architecture, cloud network topology, process supervisors, and custom subsystems powering Project Hajaribagh.

---

## 1. Production Compute Infrastructure

* **Host Provider**: Oracle Cloud Infrastructure (OCI, Always Free Tier)
* **Compute Shape**: `VM.Standard.A1.Flex`
* **CPU Architecture**: 3.0 GHz Ampere Altra ARM64 (4 OCPUs / 4 vCPUs)
* **Total System Memory**: 24 GB RAM
* **Operating System**: Canonical Ubuntu 24.04 LTS aarch64 (Linux kernel 6.17)
* **Public IPv4 Address**: `132.226.135.26`
* **Private Subnet Address**: `10.0.0.7`

---

## 2. Java Runtime and Performance Configuration

* **Runtime**: Oracle JDK 25 LTS (build 25.0.5.0.2+1-LTS-2)
* **Bytecode Target**: Class file version 69.0 (native Minecraft 26.3 requirement)
* **Garbage Collector**: Z Garbage Collector (`-XX:+UseZGC`)
* **Allocated Heap**: Minimum 4096 MB, Maximum 8192 MB (`-Xms4096M -Xmx8192M`)
* **Execution Wrapper**:
  ```bash
  /opt/jdk-25/bin/java -Xms4096M -Xmx8192M -XX:+UseZGC -jar fabric-server-launch.jar nogui
  ```

---

## 3. Cloud Network and Security Architecture

The server operates within a dedicated Virtual Cloud Network configured via the OCI CLI:

1. **Virtual Cloud Network (VCN)**: `hajaribagh-vcn` (`10.0.0.0/16`)
2. **Internet Gateway**: `hajaribagh-igw` enabling bi-directional external traffic
3. **Route Table**: `hajaribagh-public-rt` routing destination `0.0.0.0/0` to the gateway
4. **Public Subnet**: `hajaribagh-subnet` (`10.0.0.0/24`)
5. **Security List Rules (`hajaribagh-sec-list`)**:
   * Port 22 (SSH): Open to `0.0.0.0/0`
   * Port 25565 (TCP, Minecraft): Open to `0.0.0.0/0`
   * Port 25565 (UDP, Minecraft): Open to `0.0.0.0/0`
6. **Host Firewall (iptables)**: Port 25565 is explicitly allowed before the default drop rule.

---

## 4. Dual Routing Paths

Players can connect through two distinct paths:

1. **Direct Public IP (Recommended, lowest latency)**:
   * Endpoint: `132.226.135.26:25565`
   * Direct connection to cloud VM network interface with zero tunnel overhead.
2. **Reverse Tunnel (Legacy domain)**:
   * Endpoint: `cairo-temptation.tun.ply.gg:47309`
   * Provided by the `playit` daemon for players who prefer domain-based routing.

---

## 5. Systemd Supervision

Both critical services are supervised by systemd on the cloud node:

### `minecraft.service`
* Working Directory: `/home/ubuntu/minecraft-server`
* Command: `/bin/bash /home/ubuntu/minecraft-server/start-server.sh`
* Policy: Automatically starts on boot, restarts after 10 seconds on failure.
* Log Access: `sudo journalctl -u minecraft -f`

### `playit.service`
* Working Directory: `/run/playit`
* Policy: Automatically connects to the tunnel network on boot.
* Log Access: `sudo journalctl -u playit -f`

---

## 6. Active Mods

Mods live in `mods/` on the VM and are not stored in this repo (`*.jar` is gitignored). Six of the seven are server-side or optional on the client. The exception is `custompaintings`, which its author lists as required on both sides. See [`MODS_DATAPACKS.md`](./MODS_DATAPACKS.md) for sources and details.

| Mod Name | Version | Function | Client needs it? |
| :--- | :--- | :--- | :--- |
| `fabric-api` | 0.162.0+26.3 | Base hooks and event bus for Fabric | No |
| `lithium` | 0.26.2+mc26.3 | Chunk and entity tick performance optimization | No |
| `ferritecore` | 9.0.0 | Memory deduplication and footprint reduction | No |
| `krypton` | 0.3.2 | Libdeflate network compression | No |
| `polymer-bundled` | 0.18.4+26.3 | Server-side model, item, and block translation into vanilla display entities | No |
| `brewery` | 0.17.1+26.3 | Patbox's Brewery: cauldrons, aging barrels, and alcoholic beverages, built on Polymer | No |
| `custompaintings` | 4.0.2+26.3 | Roundaround's Custom Paintings: painting packs, picker menu, custom sizes | Yes, per its Modrinth page (see `KNOWN_ISSUES.md`) |

---

## 7. Custom Subsystems

### A. Cannabis and Smoking (`datapacks/cannabis_smoke`)
* **Item**: `minecraft:warped_fungus_on_a_stick` with a custom name and lore. Using that item increments the `use_joint` scoreboard objective (criterion `minecraft.used:minecraft.warped_fungus_on_a_stick`), which is how right-click is detected without a client mod.
* **Recipe**: 1 Paper + 1 Dried Kelp yields 3 Cannabis Joints.
* **Mechanics** (all in `datapacks/cannabis_smoke/data/cannabis/function/`):
  * `tick.mcfunction` runs every tick. If a player has `use_joint` or `smoke` at 1 or more, it runs `smoke.mcfunction` as that player.
  * `smoke.mcfunction` resets both scores, sets `smoke_timer` to 60 ticks, plays `block.campfire.crackle` to nearby players and `entity.generic.drink` to the smoker, shows an action bar message, and applies Regeneration II (15 s), Resistance II (20 s), Slow Falling (10 s), Saturation (2 s) and Nausea (6 s).
  * While `smoke_timer` is above 0, `puff_particles.mcfunction` spawns `campfire_cosy_smoke` and `smoke` particles about 1.6 blocks up and 0.5 blocks in front of the player, so smoke appears at face height for 3 seconds.
  * `/trigger smoke` runs the same effects without needing a joint.

### B. Custom Paintings System
Two separate layers exist, and only the first one is known to work for vanilla clients.

1. **Resource pack texture override** (`Hajaribagh-Paintings.zip`): six images are copied over all 46 vanilla painting textures in `assets/minecraft/textures/painting/`, grouped by aspect ratio. The server sends the zip to connecting clients through `resource-pack` and `resource-pack-sha1` in `server.properties`. Players see custom art on any painting they place, with no client mod. The URL must be downloadable without a login (see `KNOWN_ISSUES.md`).
2. **Custom Paintings mod** (`custompaintings` jar plus `custompaintings/ServerPaintings/`): a painting pack with source images and a `custompaintings.json` manifest that defines six paintings with their own names and block sizes. The mod page lists the mod as required on both client and server, so players without it should not be relied on to see these entries.

Images: Hasina (2x3), Chuppu (1x2), Sarjis Alam (3x2), Dhaka scene (4x3), Nahid and Asif (2x3), Bengal meme (2x2). The zip build step is not in this repo yet. See [`OPERATIONS.md`](./OPERATIONS.md).

### C. Ore Inspection Toggle (`datapacks/ore_xray`)
* `/trigger xray` is enabled only for the player named `Kowsyke`. Other players' `xray` score is reset to 0 every tick.
* First use puts the player in spectator mode with infinite night vision, so they can pass through terrain and look at ore and caves.
* Second use clears night vision and returns the player to survival mode, whatever mode they were in before.
