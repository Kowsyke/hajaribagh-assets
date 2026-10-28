# Blockstate Rules and Placement Reference

This reference documents exact blockstate properties required for clean architectural geometry in Minecraft 1.21.

## Stairs

Stair facing dictates the direction of descent. Walking toward the given direction steps down.

### Standard Flight: Descending North
- Tread block: `minecraft:spruce_stairs[facing=north,half=bottom,shape=straight]`
- Walking North moves from higher elevation down to lower elevation.

### Standard Flight: Descending South
- Tread block: `minecraft:spruce_stairs[facing=south,half=bottom,shape=straight]`
- Walking South moves from higher elevation down to lower elevation.

### Standard Flight: Descending East
- Tread block: `minecraft:spruce_stairs[facing=east,half=bottom,shape=straight]`
- Walking East moves from higher elevation down to lower elevation.

### Standard Flight: Descending West
- Tread block: `minecraft:spruce_stairs[facing=west,half=bottom,shape=straight]`
- Walking West moves from higher elevation down to lower elevation.

### Inverted Ceiling Trim and Arch Cornices
- South Arch Rib: `minecraft:spruce_stairs[facing=south,half=top,shape=straight]`
- North Arch Rib: `minecraft:spruce_stairs[facing=north,half=top,shape=straight]`
- East Arch Rib: `minecraft:spruce_stairs[facing=east,half=top,shape=straight]`
- West Arch Rib: `minecraft:spruce_stairs[facing=west,half=top,shape=straight]`

### Corner Shapes
When two stair lines intersect at right angles:
- `shape=inner_left`: Turns 90 degrees to the left when ascending.
- `shape=inner_right`: Turns 90 degrees to the right when ascending.
- `shape=outer_left`: Exterior corner wrapping to the left.
- `shape=outer_right`: Exterior corner wrapping to the right.

## Storage: Chests and Barrels

### Double Chest Pairs
Double chests require precise left and right halves facing the same direction.

#### South Facing
- Left half: `minecraft:chest[facing=south,type=left]`
- Right half: `minecraft:chest[facing=south,type=right]`
- When looking North at the chest, the right block is type=right, the left block is type=left.

#### North Facing
- Left half: `minecraft:chest[facing=north,type=left]`
- Right half: `minecraft:chest[facing=north,type=right]`

#### East Facing
- Left half: `minecraft:chest[facing=east,type=left]`
- Right half: `minecraft:chest[facing=east,type=right]`

#### West Facing
- Left half: `minecraft:chest[facing=west,type=left]`
- Right half: `minecraft:chest[facing=west,type=right]`

### Single Chests and Barrels
- Single chest: `minecraft:chest[facing=south,type=single]`
- Barrel: `minecraft:barrel[facing=up,open=false]` for floor storage or `minecraft:barrel[facing=north,open=false]` for wall shelving.

## Doors and Gates

### Doors
Doors occupy two vertical blocks:
- Lower block: `minecraft:spruce_door[facing=north,half=lower,hinge=left,open=false,powered=false]`
- Upper block: `minecraft:spruce_door[facing=north,half=upper,hinge=left,open=false,powered=false]`

### Trapdoors
- Lower wall shutter: `minecraft:spruce_trapdoor[facing=north,half=bottom,open=false]`
- Raised table leaf or banister: `minecraft:spruce_trapdoor[facing=north,half=bottom,open=true]`
- Inverted ceiling hatch: `minecraft:spruce_trapdoor[facing=north,half=top,open=false]`

## Emissive Light Sources

### Lanterns
- Hanging from ceiling or chain: `minecraft:lantern[hanging=true,waterlogged=false]`
- Resting on table or pedestal: `minecraft:lantern[hanging=false,waterlogged=false]`
- Soul lantern variant: `minecraft:soul_lantern[hanging=true,waterlogged=false]`

### Copper Bulbs (Minecraft 1.21)
- Lit permanent warm light: `minecraft:copper_bulb[lit=true,powered=false]`
- Unlit state: `minecraft:copper_bulb[lit=false,powered=false]`
- Weathered states: `exposed_copper_bulb`, `weathered_copper_bulb`, `oxidized_copper_bulb`.
