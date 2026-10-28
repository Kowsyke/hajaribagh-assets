# Subterranean Utopia Mega Citadel Blueprint

This document details the spatial coordinates, architectural zones, stair orientation rules, and infrastructure of the Subterranean Utopia built directly beneath the ancient tree base.

---

## 1. Spatial Coordinate Index

```
Surface Base Entrance: (X: 117, Y: 78, Z: -330)
Great Treasury Floor:  (X: 108..126, Y: 64..72, Z: -333..-301)
Descent Stairwell:     (X: 116..118, Y: 64 down to 46, Z: -322..-308)
Central Command Rotunda:(X: 111..123, Y: 46..53, Z: -307..-295)
South Sovereign Blvd:  (X: 116..118, Y: 46..53, Z: -294..-262)
King's High Parliament:(X: 105..129, Y: 46..53, Z: -261..-235)
Celestial Portal Nexus:(X: 107..127, Y: 44..53, Z: -233..-210)
Deep Tier Infrastructure:(X: 74..160, Y: 36..45, Z: -306..-235)
Hyperloop Concourse:   (X: 112..122, Y: 37..43, Z: -306..-296)
```

---

## 2. Sector Registry

### Sector Minus 1: The Great Treasury (X: 108..126, Z: -333..-301, Y: 64..72)
* Theme: Hobbit style organic underground treasury.
* Materials: Mud bricks, spruce planks, stripped spruce logs, mossy stone bricks.
* Features: 8 double chest storage alcoves, barrel racks, central carpeted aisle, royal vault chamber.
* Structural Rule: The floor at Y: 64 must remain solid from Z: -319 southwards. The stair descent opening is strictly confined to X: 116..118, Z: -322..-320.

### Sector 0: Central Bio Dome Atrium (X: 104..130, Z: -304..-278, Y: 50..58)
* Theme: Living subterranean park and aquatic sanctuary.
* Materials: Moss blocks, dark oak walkway ribbons, deepslate tile walls, glass ceiling skylights.
* Features: Sunken bio aquarium with axolotls and sea lanterns, flowering azalea gardens, spore blossoms, park benches, dual bubble column elevators to the lower nexus.

### Sector 1: Dwarven Industrial Forge (X: 82..99, Z: -301..-281, Y: 50..58)
* Theme: Heavy metallurgy, automated smelting, and master engineering.
* Materials: Smooth stone, deepslate tiles, iron bars, lava crucible.
* Features: 16 furnace super smelter battery, anvils, smithing tables, stonecutters, alchemy counter.

### Sector 2: Hydroponics Biosphere (X: 136..154, Z: -302..-280, Y: 50..61)
* Theme: Agricultural self sufficiency and apiculture.
* Materials: Farmland, irrigation water channels, glass domed apiary, cherry logs.
* Features: Terraced crop beds (wheat, carrots, potatoes, beetroot), enclosed glass bee sanctuary with active hives, cherry blossom companion tree.

### Sector 3: Celestial Portal Nexus (X: 106..128, Z: -302..-280, Y: 36..48)
* Theme: Interdimensional stargate chamber.
* Materials: Calcite floor, deepslate bricks, crying obsidian, amethyst blocks.
* Features: Active 5x7 Nether portal aperture, sunken authentic 3x3 End portal well with eyes of ender, budding amethyst geode cavity.

### Sector 4: Grand Subterranean Athenaeum (X: 80..102, Z: -330..-306, Y: 50..62)
* Theme: Arcane library and philosophical academy.
* Materials: Dark oak planks, tuff bricks, chiseled bookshelves.
* Features: Central level 30 enchanting sanctum, multi tier perimeter bookcases, mezzanine reading balcony, spiral staircase, floating study desks, alchemical stills.

### Sector 5: Sovereign Banquet and Gathering Hall (X: 132..154, Z: -330..-306, Y: 50..62)
* Theme: Ceremonial state feasts and fellowship.
* Materials: Polished blackstone bricks, red and gold ceremonial carpets, dark oak.
* Features: Long banquet tables seating 30+ players, high table dais, cakes, candles, decorated pots, dual roaring stone fireplaces with iron grates, copper chandeliers.

### Sector 6: Subterranean Hyperloop Transit Hub (X: 104..130, Z: -345..-325, Y: 49..58)
* Theme: Automated minecart rapid transit.
* Materials: Smooth quartz concourse, polished blackstone, yellow and black hazard lines.
* Features: 3 departure platforms, push button minecart dispensers, powered rail boosters, waiting benches, connected via dedicated flanking subway tunnels.

### Sector 7: Grand High Parliament of the Republic (X: 104..130, Z: -276..-244, Y: 50..58)
* Theme: Satirical democratic assembly and sovereign throne room.
* Materials: Polished blackstone, crying obsidian, green and gold carpet aisle, gilded blackstone.
* Features: Opposing 3 tier benches for 40+ members, Speaker dais, Prime Minister throne, ceremonial golden mace on blackstone plinth, voting buttons.

### Sector 8: Sovereign Residential Suites (X: 92..142, Z: -268..-231, Y: 50..58)
* Theme: Private luxury quarters for server leadership.
* King Abir Prime Minister Suite: Grand red canopy bed, executive desk, golden armor stand.
* Ahsane Executive Library Suite: Cyan canopy bed, private reading pod, lapis armor stand.
* Jamal Amethyst Sanctuary Suite: Purple canopy bed, amethyst cluster displays, ward armor stand.

### Sector 9: Vaulted Conduits and Arterial Corridors (Connecting all sectors)
* Theme: Vaulted subterranean highways and transit arteries.
* Materials: Deepslate tiles, dark oak arch ribs, polished blackstone border trim, lit copper bulbs.
* Features: Ribbed barrel vaults, clear directional sightlines, embedded copper bulb lighting grids, sealed archways into all deep sectors.

---

## 3. Minecraft Stair Orientation Mechanics

Stair orientation in Minecraft commands requires strict adherence to block states:

* Walking South and Descending: Steps must have `facing=north,half=bottom`. The high solid back faces north, and the lower step faces south, allowing players to walk smoothly down without jumping.
* Walking North and Descending: Steps must have `facing=south,half=bottom`.
* Walking East and Descending: Steps must have `facing=west,half=bottom`.
* Walking West and Descending: Steps must have `facing=east,half=bottom`.
* Chairs: Set `half=bottom`. The `facing` property defines the direction the player looks while seated. A chair facing East towards a table must have `facing=east,half=bottom`.
* Base Wall Skirting: Set `half=bottom`. The solid back rests against the wall, and the step faces into the room.
* Vault Ceiling Arches: Set `half=top`. The stair hangs from the ceiling and curves downward into the room.
