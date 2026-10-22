# Member Registry and Roles

This file details all participants, their access levels, network locations, and responsibilities in Project Hajaribagh.

---

## Developers and Node Hosts

### 1. King Abir (Kowsyke)
* **Title & Persona**: King Abir (always and everywhere introduced as King Abir across the server, in-game copy, books, and announcements)
* **GitHub**: `Kowsyke` (abirmia205@gmail.com)
* **In-Game Username**: `Kowsyke`
* **Role**: Supreme Server Ruler, Lead Administrator, Host Operator (Node A)
* **Location**: United Kingdom
* **Host Environment**: Oracle Cloud Always Free VM (Ubuntu 24.04 aarch64, Oracle JDK 25), supervised by systemd, with the Playit tunnel kept as a fallback route.
* **Responsibilities**: Sovereign leadership, infrastructure maintenance, memory profiling, core network routing, primary daemon supervisor.

### 2. exacyyv
* **GitHub**: `exacyyv`
* **Role**: Co-Developer, Feature Architect
* **Access**: Collaborator with full read and write access to `Kowsyke/hajaribagh-assets`. Deploying to the cloud VM also needs Kowsyke to add an SSH public key for exacyyv on the VM.
* **Responsibilities**: Vibe-coding, creating fun gameplay mechanics, customizing items, designing mini-games.
* **Side project**: Built a physical Minecraft sword controller (wooden toy sword, ESP32-S3, Bluetooth keyboard and mouse). See the README and [exacyyv/Minecraft-Sword-Using-Esp32-S3-](https://github.com/exacyyv/Minecraft-Sword-Using-Esp32-S3-).

---

## Players and Companions

### 1. GothHunterJamal
* **In-Game Username**: `GothHunterJamal`
* **Role**: Primary Survival Partner
* **Location**: United Kingdom (Roommate)
* **Connection**: Direct public IP `132.226.135.26:25565`

### 2. ahsane
* **In-Game Username**: `ahsane`
* **Title & Role**: Vice Captain, Advisor
* **Instagram**: `@sanerar`
* **Status**: Single, heterosexual, looking for a girlfriend
* **Advisory**: Designated contact for community questions, political strategy, and financial guidance
* **Location**: Canada
* **Connection**: Direct public IP `132.226.135.26:25565` (the Playit tunnel `cairo-temptation.tun.ply.gg:47309` still works as a fallback)

### 3. Dip
* **In-Game Username**: `Dip`
* **Role**: Community Member
* **Location**: Bangladesh
* **Connection**: Direct public IP `132.226.135.26:25565` (the Playit tunnel `cairo-temptation.tun.ply.gg:47309` still works as a fallback)

---

## Operational Directives for Member Interactions

* **Server Auth**: The server runs with `online-mode=false` in `server.properties` to ensure all members can join regardless of launcher authentication states.
* **Privacy Controls**: In-game mode changes (survival, creative, spectator) should be executed silently so notifications do not disrupt member immersion.
* **Loot Balance**: Custom mechanics must remain accessible and fair for members across high-latency links (Canada and Bangladesh).
