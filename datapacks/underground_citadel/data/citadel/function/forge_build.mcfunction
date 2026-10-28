# Subterranean Citadel: Dwarven Metallurgy Forge
# Dimensions: X: 82..99, Z: -301..-281, Floor Y: 50, Ceiling Y: 58
fill 82 50 -301 99 58 -281 air

# Shell and Heavy Masonry Foundation
fill 81 49 -302 100 49 -280 polished_deepslate
fill 82 50 -301 99 50 -281 polished_basalt[axis=y]
fill 81 50 -302 81 58 -280 deepslate_tiles
fill 100 50 -302 100 58 -280 deepslate_tiles
fill 81 50 -302 100 58 -302 deepslate_tiles
fill 81 50 -280 100 58 -280 deepslate_tiles
fill 81 59 -302 100 59 -280 smooth_stone

# 16 Furnace Super Smelter Battery (West Wall)
fill 82 51 -298 82 52 -284 blast_furnace[facing=east]
fill 82 53 -298 82 53 -284 hopper[facing=down]
fill 82 54 -298 82 54 -284 chest[facing=east,type=single]
fill 82 55 -298 82 57 -284 iron_bars

# Molten Lava Crucible (Center: X: 89..92, Z: -293..-289)
fill 88 50 -294 93 50 -288 polished_blackstone
fill 89 51 -293 92 51 -289 polished_blackstone_bricks
setblock 90 51 -291 lava
setblock 91 51 -291 lava
fill 89 52 -293 92 53 -289 iron_bars
fill 89 54 -293 92 55 -289 brick_stairs[facing=south,half=top]

# Master Smith Workstation (East side)
setblock 96 51 -295 polished_granite
setblock 96 52 -295 anvil[facing=north]

setblock 96 51 -293 smithing_table
setblock 96 51 -291 stonecutter[facing=west]

# Quenching Trough with Water
setblock 96 51 -289 cauldron
setblock 96 52 -289 tripwire_hook[facing=east]

# Hanging Grindstone
setblock 94 54 -291 iron_chain[axis=y]
setblock 94 53 -291 grindstone[facing=west,face=ceiling]

# Storage and Ingot Racks (North Wall)
fill 85 51 -301 88 53 -301 barrel[facing=south]
fill 93 51 -301 95 51 -301 raw_iron_block
fill 93 52 -301 95 52 -301 raw_copper_block
fill 93 53 -301 95 53 -301 coal_block

# Industrial Copper Bulb and Chain Lighting
setblock 86 58 -291 iron_chain[axis=y]
setblock 86 57 -291 copper_bulb[lit=true,powered=false]
setblock 86 56 -291 lantern[hanging=true]

setblock 96 58 -291 iron_chain[axis=y]
setblock 96 57 -291 copper_bulb[lit=true,powered=false]
setblock 96 56 -291 lantern[hanging=true]

# Doorway to Atrium at X=100
fill 100 50 -292 100 54 -290 air
