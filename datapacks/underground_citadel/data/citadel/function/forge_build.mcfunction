# Subterranean Citadel: Dwarven Industrial Forge
fill 82 50 -301 99 58 -281 air
fill 81 49 -302 100 49 -280 polished_deepslate
fill 82 50 -301 99 50 -281 smooth_stone
fill 81 50 -302 81 58 -280 deepslate_tiles
fill 100 50 -302 100 58 -280 deepslate_tiles
fill 81 50 -302 100 58 -302 deepslate_tiles
fill 81 50 -280 100 58 -280 deepslate_tiles
fill 81 59 -302 100 59 -280 deepslate_tiles

# Central Magma Core & Crucible
fill 89 50 -293 93 50 -289 lava
fill 89 51 -293 93 53 -289 tinted_glass
fill 89 50 -293 93 54 -289 iron_bars replace tinted_glass
setblock 91 50 -291 lava

# 16-Furnace Super Smelter Battery (West Wall)
fill 82 51 -299 82 51 -292 blast_furnace[facing=east,lit=true]
fill 82 52 -299 82 52 -292 hopper[facing=down]
fill 82 53 -299 82 53 -292 chest[facing=east,type=single]

fill 82 51 -290 82 51 -283 furnace[facing=east,lit=true]
fill 82 52 -290 82 52 -283 hopper[facing=down]
fill 82 53 -290 82 53 -283 chest[facing=east,type=single]

# Smithing & Engineering Benches
setblock 86 51 -298 smithing_table
setblock 87 51 -298 anvil[facing=north]
setblock 88 51 -298 grindstone[facing=north,face=floor]
setblock 89 51 -298 crafting_table

setblock 86 51 -284 smithing_table
setblock 87 51 -284 chipped_anvil[facing=south]
setblock 88 51 -284 stonecutter[facing=south]
setblock 89 51 -284 crafting_table

# Alchemy & Brewing Counter
fill 95 51 -299 98 51 -299 polished_blackstone
setblock 95 52 -299 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 96 52 -299 cauldron
setblock 97 52 -299 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 98 52 -299 cauldron

# Archway connecting to Bio-Atrium (East Wall)
fill 100 50 -293 104 55 -289 air
fill 100 49 -293 104 49 -289 polished_deepslate
fill 100 50 -291 104 50 -291 stripped_dark_oak_wood[axis=x]
