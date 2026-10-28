# Project Hajaribagh: Scripts Index

This directory contains utility scripts for deploying, managing, automating, and generating content for Project Hajaribagh.

---

## 1. Cloud Deployment and Operations

* `deploy-to-cloud.sh`: The primary deployment tool. Synchronizes `datapacks/` and `configs/` to the Oracle Cloud production server via SCP. Skips `server.properties` to protect live production network and world settings.
* `view-cloud-logs.sh`: Connects to the Oracle Cloud VM over SSH and tails systemd journal logs (`journalctl -u minecraft -f`) in real time.
* `check-server.py`: Verifies server reachability, queries status via Minecraft ping protocol, tests RCON, and checks resource pack hash validity.
* `moling_rcon.py`: Production command bridge implementing the MoLing toolset (fill, setblock, clone, summon, execute, weather, time) directly over RCON.
* `start-server.sh`: JVM startup script configured for Oracle JDK 25 LTS with Z Garbage Collector (`-XX:+UseZGC`, `-Xms4096M`, `-Xmx8192M`).

---

## 2. World Generation and Architecture

* `generate_perfect_stairs_and_citadel.py`: The active master architectural generator. Produces the complete 12 sector Subterranean Utopia Citadel and Grand Descent Staircase in `datapacks/underground_citadel/data/citadel/function/`. Enforces proper Minecraft stair facings, protects the Great Treasury floor at Y: 64, and populates room interiors.
* `generate_utopian_mega_citadel.py`: Reference generator for utopian sector expansions (Athenaeum, Banquet Hall, Transit Hub, Portal Nexus).
* `generate_perfect_citadel.py`: Reference generator for early Parliament and Atrium layouts.
* `build_underground_citadel.py`: Baseline prototype generator for the original underground chambers.

---

## 3. Player Inventory and Dev Kits

* `give_dev.py`: Grants the comprehensive developer kit to a specified player via RCON.
* `give_platinum.py`: Grants the Platinum Tier supporter package via RCON.
* `give_boots.py`: Grants customized enchanted boots via RCON.
* `give_shears.py`: Grants custom shears via RCON.
* `give_shield.py`: Grants defensive custom shields via RCON.
* `give_guns.py`: Legacy gun delivery tool. Kept for historical reference. The guns mod remains quarantined.
