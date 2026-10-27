# Subterranean Citadel: Sector A Dwarven Industrial Forge and Super Smelter
fill 82 49 -301 99 49 -281 polished_basalt[axis=y]
fill 82 50 -301 82 57 -281 polished_deepslate
fill 99 50 -301 99 57 -281 polished_deepslate
fill 82 50 -301 99 57 -301 polished_deepslate
fill 82 50 -281 99 57 -281 polished_deepslate
fill 82 58 -301 99 58 -281 deepslate_tiles

fill 99 50 -293 104 55 -289 air
fill 99 49 -292 104 49 -290 polished_basalt[axis=x]
fill 99 50 -292 104 50 -290 smooth_stone
fill 99 51 -293 104 54 -293 deepslate_tile_wall
fill 99 51 -289 104 54 -289 deepslate_tile_wall
fill 99 55 -292 104 55 -290 copper_grate
fill 99 56 -292 104 56 -290 sea_lantern

fill 83 50 -300 98 50 -282 smooth_stone
fill 85 50 -298 96 50 -284 polished_basalt[axis=y]

# 16 Furnace Super Smelter Array
setblock 89 50 -299 chest[facing=south,type=left]
setblock 90 50 -299 chest[facing=south,type=right]

fill 84 51 -300 91 51 -300 blast_furnace[facing=south,lit=true]
fill 92 51 -300 97 51 -300 furnace[facing=south,lit=true]

fill 84 50 -300 97 50 -300 hopper[facing=south]
fill 84 52 -300 97 52 -300 hopper[facing=down]
fill 84 53 -300 97 53 -300 chest[facing=south]

fill 84 54 -300 97 54 -300 redstone_lamp[lit=true]
fill 84 55 -300 97 55 -300 redstone_block

# Master Smithing & Anvil Station
fill 89 50 -293 92 50 -291 iron_block
setblock 89 51 -293 anvil[facing=south]
setblock 90 51 -293 smithing_table
setblock 91 51 -293 grindstone[facing=south,face=floor]
setblock 92 51 -293 chipped_anvil[facing=south]

summon armor_stand 88 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_pickaxe",count:1},{},{},{},{id:"netherite_helmet",count:1}]}
summon armor_stand 93 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_chestplate",count:1}]}

fill 83 50 -293 83 55 -291 lava
fill 84 50 -293 84 55 -291 tinted_glass
fill 84 50 -294 84 55 -294 copper_grate
fill 84 50 -290 84 55 -290 copper_grate

# Alchemy Lab
fill 84 50 -283 87 50 -283 soul_sand
fill 84 51 -283 87 51 -283 nether_wart[age=3]

fill 89 50 -283 93 50 -283 polished_blackstone
setblock 89 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 90 51 -283 water_cauldron[level=3]
setblock 91 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true]
setblock 92 51 -283 barrel[facing=up]
setblock 93 51 -283 water_cauldron[level=3]

fill 94 51 -283 97 51 -283 chiseled_bookshelf[facing=north]
fill 94 52 -283 97 52 -283 barrel[facing=south]
