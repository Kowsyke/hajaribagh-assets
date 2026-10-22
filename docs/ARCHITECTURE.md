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

## 6. Active Mods and Subsystems

* `fabric-api`: Standard Fabric hooks.
* `lithium`: Chunk and entity tick performance optimization.
* `ferritecore`: Memory deduplication and footprint reduction.
* `krypton`: Libdeflate network compression.
* `polymer-bundled`: Server-side model, item, and block translation into vanilla display entities.
* `brewery`: Cauldron fermenting, barrel aging, and drinks.
* `custompaintings`: Server-side painting motive replacements.
* `cannabis_smoke` datapack: Craftable joints, 3D animated smoke particles, sound effects, and status buffs.
