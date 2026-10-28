# MoLing Building Patterns and Task Decompositions

This reference demonstrates how to decompose complex natural language building prompts into sequential Minecraft command batches.

## Case Study 1: Futuristic Radio and Observation Tower

**Prompt**: "Build a futuristic radio tower at (40, 87, 125), approximately 60 blocks tall. The structure should use smooth metal and glass, topped with a spherical observation dome and illuminated with warm lights."

### Phase 1: Foundation Plaza (Radius 12)
- Coordinate bounds: `(X: 28..52, Y: 86, Z: 113..137)`
- Base circle excavation: Clear surface foliage.
- Pavement: Concentric rings of polished andesite and smooth stone slabs.
- Command template:
  * `/fill 28 86 113 52 86 137 minecraft:polished_andesite`

### Phase 2: Central Tower Core (Height: 40 blocks)
- Central coordinates: `(X: 38..42, Y: 87..127, Z: 123..127)`
- Hollow shaft for elevator and service ladders:
  * `/fill 38 87 123 42 127 127 minecraft:iron_block outline`
  * `/fill 39 87 124 41 127 126 minecraft:air replace`
- Corner buttress struts at base tapering inward every 10 vertical blocks.

### Phase 3: Spherical Observation Deck (Diameter 15 blocks)
- Center: `(40, 132, 125)`, Radius 7.
- Floor deck: Smooth quartz blocks at `Y: 128` with circular perimeter.
- Panoramic glass shell:
  * Inverted quartz stairs for lower support ring.
  * Tinted glass ring around viewing level `(Y: 129..134)`.
  * Hemispherical quartz dome for upper roof `(Y: 135..138)`.

### Phase 4: Antenna Spire and Beacon (Height: 15 blocks)
- Center: `(40, 139..154, 125)`.
- Base: Netherite block with lightning rod apex.
- Spire shaft: Iron bars and end rods stacked vertically.
- Lighting: Copper bulbs (`lit=true`) placed at navigation warning nodes.

---

## Case Study 2: Subterranean Arched Aqueduct Bridge

**Prompt**: "Construct an ancient stone aqueduct bridge crossing a chasm from (110, 50, -320) to (110, 50, -290), 5 blocks wide, with water flowing across the top deck."

### Phase 1: Pillar Piers
- Two central support piers rising from ravine floor `Y: 30` to `Y: 48`.
- Pier dimensions: 3 blocks wide by 3 blocks deep.
- Material: Stone bricks with cobblestone foundation skirting.

### Phase 2: Parabolic Vault Arches
- Vault span between piers using inverted stone brick stairs (`half=top`).
- Central keystones using chiseled stone bricks.

### Phase 3: Deck and Flume Channel
- Width: 5 blocks `(X: 108..112)`.
- Channel walls: Stone brick walls (`minecraft:stone_brick_wall`) along edges `X: 108` and `X: 112`.
- Flume bed: Stone slabs (`minecraft:smooth_stone_slab[type=bottom]`) along center `X: 109..111`.
- Water stream placed at the northern end flowing south.
