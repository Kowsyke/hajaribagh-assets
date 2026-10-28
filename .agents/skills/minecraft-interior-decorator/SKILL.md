---
name: minecraft-interior-decorator
description: Professional interior design and decoration skill for Minecraft 1.21. Specializes in furniture construction, lighting fixtures, object logic, workstation clusters, functional living spaces, ceremonial halls, and cozy atmospheric detailing using pure vanilla blocks.
---

# Minecraft Interior Decorator

## Overview

This skill guides the interior furnishing, object logic, and decorative styling of Minecraft spaces. It covers furniture design, warm lighting techniques, functional workstation integration, and immersive room styling for subterranean and aboveground builds.

## Lighting Fixtures and Atmospheric Illumination

Lighting must be integrated naturally into structural geometry rather than placed randomly on floors.

### 1. Ceiling Chandeliers and Lantern Drops
- Chain Drop Lantern: `minecraft:chain[axis=y]` suspended from beams, ending with `minecraft:lantern[hanging=true]` or `minecraft:soul_lantern[hanging=true]`.
- Vaulted Copper Chandelier: Central chain connected to a ring of 4 dark oak fences or copper grates, each holding a lit copper bulb (`minecraft:copper_bulb[lit=true,powered=false]`).
- Shrouded Shroomlight: `minecraft:shroomlight` suspended from a chain, surrounded on all 4 vertical faces by closed trapdoors (`minecraft:spruce_trapdoor[half=top,open=false]`), with a hanging lantern beneath.

### 2. Sconce Wall Fixtures
- Tripwire Sconce: Place `minecraft:tripwire_hook[facing=north]` on the wall, with a hanging lantern on an iron chain beneath it.
- Inverted Stair Sconce: Inset an upside down stair (`half=top`) into the wall, place a sea lantern or glowstone behind a copper grate or iron trapdoor.
- Candle Pedestal: Place a smooth stone slab or dark oak fence on the wall, topped with 1 to 4 lit candles (`minecraft:candle[lit=true,candles=3]`).

### 3. Recessed Floor and Up-Lighting
- Concealed Floor Radiance: Recess sea lanterns or shroomlights into the floor layer, concealed beneath green moss carpet, dark oak trapdoors, or tinted glass.
- Baseboard Glow: Place lit copper bulbs along the lower skirting corners behind upside down stairs or iron bars.

## Furniture and Object Logic

Every piece of furniture must respect scale, player movement ergonomics, and directional orientation.

### 1. Seating and Benches
- Armchair: Place a stair block (`half=bottom,shape=straight`), flanked on both sides by blank signs (`spruce_wall_sign`) or closed trapdoors (`spruce_trapdoor[half=bottom,open=false]`).
- Council High Back Throne: Place a polished deepslate stair as the seat, backed by 2 vertical polished deepslate walls, with a banner hanging down the back and dark oak trapdoors as armrests.
- Banquet Bench: Continuous rows of stairs facing inward towards the dining table. Ensure outer ends use corner stairs (`shape=outer_left` or `shape=outer_right`).

### 2. Dining and Feast Tables
- Table Construction: Alternating spruce slabs or dark oak trapdoors elevated on fence posts or stripped log pilasters.
- Table Settings:
  * Place mats: Brown, red, or white carpets.
  * Dinner plates: Heavy weighted pressure plates (`minecraft:heavy_weighted_pressure_plate`).
  * Steins and Goblets: Flower pots with sea pickles or dried kelp (`minecraft:potted_cactus` or `flower_pot`).
  * Centerpieces: Decorated pots with ferns, lit candle clusters, or whole cakes (`minecraft:cake[bites=0]`).

### 3. Sleeping Quarters and Beds
- Royal Canopy Bed: Place two colored beds head to head. Enclose the four corners with stripped spruce pillars rising 3 blocks, bridged across the top with spruce trapdoors and draped with hanging wool or banners.
- Nightstand: A barrel or chiseled bookshelf facing outward, topped with a flower pot holding an azalea bush or a single warm candle.
- Wardrobe Closet: 2 blocks wide, 2 blocks high. Inset armor stands equipped with iron, diamond, or netherite armor, enclosed behind functioning spruce doors.

### 4. Workstations and Laboratories
- Smithing and Smelting Battery: Group anvils, smithing tables, and grindstones together. Place blast furnaces beneath hoppers and chimneys. Add a water cauldron for quenching metal.
- Alchemical Brewing Station: Water cauldron in center, flanked by brewing stands on polished basalt pedestals, with potion chests and ingredient barrels above.
- Scholar Desks: Lectern holding a written book, flanked by chiseled bookshelves filled with enchanted tomes, illuminated by a table lantern.

### 5. Fireplaces and Hearths
- Hearth Foundation: Netherrack or campfires over hay bales for tall smoke plumes.
- Fire Safety: Surround fire source with nonflammable stone, deepslate, or copper. Never expose bare wood planks within 3 blocks of open fire.
- Flue and Mantle: Mantle of polished blackstone stairs with an iron bar safety gate, venting into a vertical brick chimney.
