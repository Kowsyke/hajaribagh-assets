# Subterranean Citadel: Sector A Dwarven Industrial Forge and Super Smelter

# Enclosure Shell
fill 82 49 -301 99 49 -281 polished_basalt[axis=y]
fill 82 50 -301 82 57 -281 polished_deepslate
fill 99 50 -301 99 57 -281 polished_deepslate
fill 82 50 -301 99 57 -301 polished_deepslate
fill 82 50 -281 99 57 -281 polished_deepslate
fill 82 58 -301 99 58 -281 deepslate_tiles

# Corridor to Atrium
fill 99 49 -292 104 49 -290 polished_basalt[axis=x]
fill 99 50 -292 104 50 -290 smooth_stone
fill 99 51 -293 104 54 -293 deepslate_tile_wall
fill 99 51 -289 104 54 -289 deepslate_tile_wall
fill 99 55 -292 104 55 -290 polished_deepslate_stairs[facing=south,half=top]

# Forge Floor (Industrial Grate Pattern: Smooth Stone and Basalt)
fill 83 50 -300 98 50 -282 smooth_stone
fill 85 50 -298 96 50 -284 polished_basalt[axis=y]

# -------------------------------------------------------------
# 16-Furnace Super Smelter Battery (North Wall, Z: -300)
# Output Double Chest at (89, 50, -299) and (90, 50, -299)
setblock 89 50 -299 chest[facing=south,type=left]
setblock 90 50 -299 chest[facing=south,type=right]

# Smelter Line: 8 Blast Furnaces (X: 84..91) and 8 Furnaces (X: 92..97)
fill 84 51 -300 91 51 -300 blast_furnace[facing=south,lit=true]
fill 92 51 -300 97 51 -300 furnace[facing=south,lit=true]

# Bottom collection hoppers below furnaces feeding output
fill 84 50 -300 97 50 -300 hopper[facing=south]

# Top Item-Input Hoppers at Y: 52 feeding down into furnaces
fill 84 52 -300 97 52 -300 hopper[facing=down]

# Top Input Chests at Y: 53
fill 84 53 -300 97 53 -300 chest[facing=south]

# Smelter Status Lighting (Redstone Lamps above)
fill 84 54 -300 97 54 -300 redstone_lamp[lit=true]
fill 84 55 -300 97 55 -300 redstone_block

# -------------------------------------------------------------
# Heavy Anvil and Master Smithing Bay (Center: X: 89..92, Z: -291..-293)
fill 89 50 -293 92 50 -291 iron_block
setblock 89 51 -293 anvil[facing=south]
setblock 90 51 -293 smithing_table
setblock 91 51 -293 grindstone[facing=south,face=floor]
setblock 92 51 -293 chipped_anvil[facing=south]

# Tool and Armor Displays
summon armor_stand 88 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_pickaxe",count:1},{},{},{},{id:"netherite_helmet",count:1}]}
summon armor_stand 93 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_chestplate",count:1}]}

# Lava Observation Core in Tinted Glass (West Wall: X: 83, Z: -291..-293)
fill 83 50 -293 83 55 -291 lava
fill 84 50 -293 84 55 -291 tinted_glass
fill 84 50 -294 84 55 -294 copper_grate
fill 84 50 -290 84 55 -290 copper_grate

# -------------------------------------------------------------
# Potion Alchemy Laboratory (South Wall, Z: -282)
# Soul Sand Nether Wart Nursery
fill 84 50 -283 87 50 -283 soul_sand
fill 84 51 -283 87 51 -283 nether_wart[age=3]

# Brewing Station Counter
fill 89 50 -283 93 50 -283 polished_blackstone
setblock 89 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 90 51 -283 water_cauldron[level=3]
setblock 91 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true]
setblock 92 51 -283 barrel[facing=up]
setblock 93 51 -283 water_cauldron[level=3]

# Alchemy Supply Chests and Shelving
fill 94 51 -283 97 51 -283 chiseled_bookshelf[facing=north]
fill 94 52 -283 97 52 -283 barrel[facing=south]
