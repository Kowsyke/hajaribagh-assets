---
name: minecraft-architect-builder
description: Professional architectural design and building system for Minecraft 1.21. Generates structures, rooms, halls, and landscape modifications from natural language prompts. Covers color palettes, gradients, depth layers, mathematical geometry, blockstate orientations, interior furniture, and automated construction via RCON or mcfunction datapacks.
---

# Minecraft Architect Builder

## Overview

This skill guides the design and construction of Minecraft structures with professional architectural standards. It handles prompt interpretation, structural planning, block palette selection, mathematical geometry generation, blockstate orientation, and in-game deployment.

## Architectural Principles

### 1. Depth and Layering

Never construct flat exterior or interior walls. Every wall must have at least three functional layers:

1. Structural Frame: Outer pillars, columns, buttresses, or ceiling beams placed at regular intervals (typically every 3, 5, or 7 blocks). Use heavier, darker blocks such as polished deepslate, logs, or stone brick pillars.
2. Wall Inset: Recessed by 1 block behind the frame. Use the primary wall material such as spruce planks, tuff bricks, or mud bricks.
3. Relief and Trim: Slabs, upside-down stairs, trapdoors, and wall blocks that bridge the frame and wall inset. These create shadow lines, cornices, and windowsill details.
4. Accent Layer: Wall-mounted lanterns, chains, vines, leaf clusters, or banner hangings.

### 2. Proportions and Dimensions

- Odd Number Rule: Rooms, halls, archways, and doorways should prefer odd-numbered spans (3, 5, 7, 9, 11). Odd spans provide a clear central block for doors, ridge beams, chandeliers, and vaulted apexes.
- Height Proportions: Ceiling height must feel proportional to floor area.
  * Corridors: Width 3, Height 3 to 4.
  * Living quarters and workshops: Width 7 to 9, Height 4 to 5.
  * Great halls and council chambers: Width 13 to 21, Height 7 to 12.
- Foundation Skirting: The lowest 1 to 2 block layers of a wall should transition into heavier stone or masonry to ground the structure visually.

### 3. Block Palette Design

Every build requires an intentional palette of four roles:

1. Primary Structural Block: Constitutes 50 to 60 percent of the build. Establishes the core atmosphere. Examples: Stone bricks, tuff bricks, deepslate tiles, spruce planks.
2. Secondary Contrast Block: Constitutes 20 to 30 percent. Accents columns, arch lintels, or floor patterns. Examples: Dark oak logs, polished andesite, stripped spruce wood.
3. Accent and Detail Block: Constitutes 10 to 15 percent. Used for trims, stairs, slabs, and furniture. Examples: Spruce stairs, copper grates, chiseled tuff.
4. Highlight and Emissive Block: Constitutes 2 to 5 percent. Provides warm illumination and focal points. Examples: Sea lanterns, shroomlights hidden under carpets, soul lanterns, copper bulbs.

### 4. Texture Mixing and Gradients

Avoid monoblock surfaces. Mix blocks with similar values to create visual texture:

- Aged Stone: Stone bricks (60%), cracked stone bricks (20%), mossy stone bricks (10%), andesite (10%).
- Deep Masonry: Deepslate tiles (50%), polished deepslate (30%), cobbled deepslate (20%).
- Subterranean Earth: Tuff (40%), tuff bricks (40%), polished tuff (20%).
- Hobbit Warmth: Spruce planks (60%), stripped spruce wood (25%), dark oak accents (15%).

## Blockstate Rules and Orientation

Incorrect blockstates ruin otherwise good builds. Always apply explicit blockstate tags.

### Stairs

Stair facing indicates the direction a player walks when descending the stair:

- Walking North to descend: `facing=north,half=bottom,shape=straight`
- Walking South to descend: `facing=south,half=bottom,shape=straight`
- Walking East to descend: `facing=east,half=bottom,shape=straight`
- Walking West to descend: `facing=west,half=bottom,shape=straight`
- Ceiling Arch / Cornice Trim: Use `half=top` with the same facing logic.
- Corner Stairs: Use `shape=inner_left`, `shape=inner_right`, `shape=outer_left`, or `shape=outer_right` when adjoining stairs intersect.

### Chests

Double chests require paired blockstates:

- Facing South:
  * Left side: `minecraft:chest[facing=south,type=left]`
  * Right side: `minecraft:chest[facing=south,type=right]`
- Facing North:
  * Left side: `minecraft:chest[facing=north,type=left]`
  * Right side: `minecraft:chest[facing=north,type=right]`

### Lighting Fixtures

- Ceiling Lantern: `minecraft:lantern[hanging=true]` attached to `minecraft:chain` or fence posts.
- Floor / Shelf Lantern: `minecraft:lantern[hanging=false]`.
- Copper Bulb: `minecraft:copper_bulb[lit=true,powered=false]` for warm amber lighting.

### Slabs and Trapdoors

- Slabs: Specify `type=bottom`, `type=top`, or `type=double`.
- Trapdoors: Specify `facing=(north|south|east|west)`, `half=(top|bottom)`, and `open=(true|false)`.

## Mathematical Geometry Reference

### Bresenham Circles and Ellipses

For an ellipse with radius X (`rx`) and radius Z (`rz`) centered at (`cx`, `cz`):

A block at (`x`, `z`) is inside the ellipse if:
`((x - cx) / (rx + 0.5))^2 + ((z - cz) / (rz + 0.5))^2 <= 1.0`

For hollow walls, check if distance is between `r_inner` and `r_outer`.

### Catenary and Parabolic Vaults

For an arch spanning from `x = -w` to `x = +w` with peak height `h`:
`y = h * (1.0 - (x / w)^2)`

Use this parabolic formula for vaulted ceilings, bridges, and subterranean tunnels. It creates organic transitions superior to semicircles.

### Spiral Staircases

For a spiral stair around central column (`cx`, `cz`):
- Step angle increment: `theta = step_index * (pi / 2)` (4 steps per revolution) or `(pi / 4)` (8 steps per revolution).
- Coordinates: `x = cx + round(r * cos(theta))`, `z = cz + round(r * sin(theta))`, `y = cy + step_index`.
- Orientation: Rotate stair facing tangentially to the circle.

## Prompt to Build Workflow

When the user asks to build a room, structure, or sector:

1. Interpret and Clarify:
   - Identify function, architectural theme, dimensions, and center coordinates.
   - If coordinates are not given, query player position via RCON or refer to known landmark bounds.
2. Verify Bounding Box:
   - Check that the proposed volume does not intersect or overwrite existing structures.
   - Read coordinates from blueprint documentation before generating blocks.
3. Select Block Palette:
   - Match the room purpose to the master theme.
   - Define primary, secondary, accent, and lighting blocks.
4. Generate Construction Commands:
   - Excavate or frame the volume using `/fill`.
   - Apply floor layers, skirting, and ceiling vaults.
   - Construct pilasters, arches, and doorways.
   - Furnish functional items (tables, workstations, double chests, shelves).
   - Place lighting and vegetative accents.
5. Execution Method:
   - Large builds (over 200 blocks): Write to a `.mcfunction` file in a datapack and run `/reload` followed by `/function pack:file`.
   - Small targeted edits: Execute directly through RCON socket in batches of 50 commands.
6. In-Game Verification:
   - Check blockstates at key coordinates (stair facing, chest pairs, light levels).
   - Verify zero player disconnection or server lag spikes.
