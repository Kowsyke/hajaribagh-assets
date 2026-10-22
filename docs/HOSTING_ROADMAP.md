# Hosting Roadmap: Dual-Node and 24/7 Infrastructure

This document analyzes infrastructure strategies for Project Hajaribagh, covering dual-developer hosting, 24/7 cloud deployment, and the roles of Vercel and Neon.

---

## 1. Reality Check on Vercel and Neon

The project stack includes accounts on Vercel and Neon. Here is what they can and cannot do for a Minecraft server:

### Vercel
* **Architecture**: Serverless HTTP edge network.
* **Limitations**: Every request has a strict 10 to 60 second execution ceiling. It does not provide persistent background execution, open raw TCP sockets (port 25565), or long-lived RAM state.
* **What Vercel is great for**: Hosting a companion web application, an interactive server status dashboard, a live web map (Bluemap/Dynmap export), or an asset CDN delivering `Hajaribagh-Paintings.zip` to clients at high speed.

### Neon
* **Architecture**: Serverless PostgreSQL with branching and connection pooling.
* **Limitations**: Neon is a relational SQL database. It cannot execute Java runtime binaries or host the Minecraft game loop.
* **What Neon is great for**: Storing persistent relational data outside the game files. Examples include cross-server leaderboards, Discord linked player accounts, economy balances, chat logs, or analytics.

---

## 2. Model 1: Dual-Developer Handoff (Kowsyke Node A and exacyyv Node B)

If you and your girlfriend want to share hosting duties so either of you can spin up the server from your respective laptops:

### The Synchronization Challenge
Minecraft stores world blocks, player inventories, and ender chests in local region files inside `world/`. If Node A and Node B run simultaneously on separate copies, the worlds will diverge and create desynchronization.

### The Turn-Based Handoff Workflow
1. **Repository Synchronization**: All configs, datapacks, and scripts are synced via this GitHub repository (`Kowsyke/hajaribagh-assets`).
2. **World State Sync**: Before Node B boots the server, Node A pushes the latest `world/` folder (or compressed archive) to shared cloud storage (such as Cloudflare R2, AWS S3, or Google Drive via Rclone).
3. **Tunnel Routing**: Both nodes can share the same Playit.gg account. When Node A is offline, Node B launches the Playit tunnel using the same secret. Friends continue using `cairo-temptation.tun.ply.gg:47309` without needing a new IP address.

---

## 3. Model 2: 24/7 Always-On Cloud Hosting

To allow friends in Canada and Bangladesh to log in at any hour without keeping either laptop powered on:

### Option A: Oracle Cloud Free Tier (Recommended)
* **Specs**: 4 ARM Neoverse cores, 24 GB RAM, 200 GB SSD storage.
* **Cost**: Zero dollars permanently free.
* **Capability**: Easily handles 15 to 20 concurrent players with Lithium and FerriteCore.
* **Setup**: Launch an Ubuntu instance, install OpenJDK 25, clone this repository, copy the `world/` directory, and run the server inside a tmux session or systemd daemon.

### Option B: Budget Linux VPS
* **Providers**: Hetzner Cloud (CX22/CX32), OVH, or Linode.
* **Cost**: Approximately 4 to 6 USD per month.
* **Capability**: Dedicated static IPv4, high uptime, and low network latency.

---

## 4. Next Implementation Steps

1. Select between the Turn-Based Handoff workflow (free, using existing hardware) and Oracle Cloud 24/7 (dedicated cloud node).
2. Create automated backup scripts in `scripts/sync-world.sh` to package and transfer world saves smoothly between Node A and Node B.
3. Configure companion status endpoints if Vercel or Neon integration is desired.
