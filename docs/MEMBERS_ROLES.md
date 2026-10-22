# Member Registry and Roles

This file details all participants, their access levels, network locations, and responsibilities in Project Hajaribagh.

---

## Developers and Node Hosts

### 1. Kowsyke
* **GitHub**: `Kowsyke` (abirmia205@gmail.com)
* **In-Game Username**: `Kowsyke`
* **Role**: Lead Administrator, Host Operator (Node A)
* **Location**: United Kingdom
* **Host Environment**: Linux x86_64, OpenJDK 25, Playit Tunnel daemon
* **Responsibilities**: Infrastructure maintenance, memory profiling, core network routing, primary daemon supervisor.

### 2. exacyyv
* **GitHub**: `exacyyv`
* **Role**: Co-Developer, Feature Architect, Host Operator (Node B candidate)
* **Access**: Collaborator with full read and write access to `Kowsyke/hajaribagh-assets`
* **Responsibilities**: Vibe-coding, creating fun gameplay mechanics, customizing items, designing mini-games, potential dual-node host.

---

## Players and Companions

### 1. GothHunterJamal
* **In-Game Username**: `GothHunterJamal`
* **Role**: Primary Survival Partner
* **Location**: United Kingdom (Local Area Network / Roommate)
* **Connection**: Directly via LAN or tunnel endpoint

### 2. ahsane
* **In-Game Username**: `ahsane`
* **Role**: Explorer and Builder
* **Location**: Canada
* **Connection**: Reverse tunnel (`cairo-temptation.tun.ply.gg:47309`)

### 3. Dip
* **In-Game Username**: `Dip`
* **Role**: Community Member
* **Location**: Bangladesh
* **Connection**: Reverse tunnel (`cairo-temptation.tun.ply.gg:47309`)

---

## Operational Directives for Member Interactions

* **Server Auth**: The server runs with `online-mode=false` in `server.properties` to ensure all members can join regardless of launcher authentication states.
* **Privacy Controls**: In-game mode changes (survival, creative, spectator) should be executed silently so notifications do not disrupt member immersion.
* **Loot Balance**: Custom mechanics must remain accessible and fair for members across high-latency links (Canada and Bangladesh).
