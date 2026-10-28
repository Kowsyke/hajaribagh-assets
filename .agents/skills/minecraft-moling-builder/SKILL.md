---
name: minecraft-moling-builder
description: Conversational Minecraft building and game control assistant based on MoLing architecture. Interprets natural language building requests, breaks complex architectural structures into sequential command steps, manages block replacement modes, and executes live building operations via RCON socket or compiled function packs.
---

# Minecraft MoLing Builder

## Overview

This skill incorporates and enhances the MoLing AI building model. It enables natural language architectural construction, game environment control, and sequential build execution directly on the Minecraft server.

## Building Methodology

### 1. Request Decomposition

When given a building brief (such as a radio tower, bridge, fortification, or pavilion), decompose construction into distinct operational phases:

1. Ground Clearing and Foundation:
   - Level terrain or excavate underground footprint using `/fill <x1> <y1> <z1> <x2> <y2> <z2> air replace <blocks>`.
   - Lay perimeter footings with masonry blocks (stone bricks, tuff bricks, or polished deepslate).
2. Structural Core and Framing:
   - Erect vertical pillars, support trusses, and primary columns at regular intervals.
   - Hollow out interior volumes using `hollow` or `outline` modes to avoid solid block waste.
3. Floors, Walls, and Ceilings:
   - Fill floor levels using alternating planks or polished stone.
   - Form wall insets recessed by 1 block behind structural pillars.
   - Construct vaulted ceilings or domes using catenary and parabolic curves.
4. Architectural Relief and Detailing:
   - Install stairs, slabs, and trapdoors with strict blockstate orientation tags.
   - Place windows, archways, and structural buttresses.
5. Functional Furnishings and Lighting:
   - Place workstations, storage chests, and seating arrangements.
   - Add illumination using lanterns, chains, and lit copper bulbs.
6. Environmental Integration:
   - Blend surrounding terrain with grass, moss, foliage, and paths.

### 2. Block Handling Modes

Choose the appropriate `/fill` mode for each phase:

- `replace`: Overwrites target blocks. When specifying a filter block (e.g. `/fill ... air replace stone`), it clears only unwanted stone without damaging adjacent structures.
- `hollow`: Fills the bounding box with the specified block on the exterior shell and replaces all interior blocks with air. Best for rapid room excavation and tower shafts.
- `outline`: Fills only the exterior shell with the target block, leaving interior blocks unchanged. Ideal for creating protective vaults around pre-existing machinery.
- `keep`: Places blocks only in coordinates currently occupied by air. Preserves existing terrain while infilling voids.
- `destroy`: Replaces all blocks in the region and drops destroyed blocks as player pickup items. Use with caution to avoid server entity lag.

### 3. Server Lag Prevention

- Maximum Fill Limit: Minecraft caps standard `/fill` operations at 32,768 blocks per command. For volumes exceeding this threshold, split the volume into smaller coordinate slices.
- Entity Dropping: Never use `destroy` over volumes larger than 100 blocks, as hundreds of dropped item entities can cause severe client FPS drops and server tick spikes.
- Packet Throttling: When streaming commands over RCON, send in batches of 50 commands with a 0.05 second yield between batches to maintain a steady 20 TPS.

## RCON Tool Bridge

Use the included helper script `scripts/moling_rcon.py` for direct command execution:

```bash
# Set a single block with explicit blockstate
./scripts/moling_rcon.py setblock 120 50 -310 "minecraft:copper_bulb[lit=true]"

# Fill a hollow room shell
./scripts/moling_rcon.py fill 110 50 -320 120 58 -310 "minecraft:tuff_bricks" --mode hollow

# Clone a repeated structural arch
./scripts/moling_rcon.py clone 110 50 -320 115 56 -320 116 50 -320

# Run execute chain
./scripts/moling_rcon.py execute "at @a run setblock ~ ~-1 ~ minecraft:gold_block"

# Send raw server command
./scripts/moling_rcon.py raw "time set day"
```

## Large Scale Compilation

For structures exceeding 200 blocks, write the complete command sequence to a dedicated `.mcfunction` file inside `datapacks/underground_citadel` or a custom datapack. Then execute:

```bash
./scripts/moling_rcon.py raw "reload"
./scripts/moling_rcon.py raw "function pack_name:function_name"
```

This compiles the entire build into a single server tick execution without network packet overhead.
