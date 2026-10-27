# Subterranean Citadel: The Grand Subterranean Athenaeum
# Dimensions: X: 80..102, Z: -330..-306, Floor Y: 50, Ceiling Y: 62
fill 80 50 -330 102 62 -306 air

# Shell & Foundation
fill 79 49 -331 103 49 -305 polished_deepslate
fill 80 50 -330 102 50 -306 dark_oak_planks
fill 79 50 -331 79 62 -305 tuff_bricks
fill 103 50 -331 103 62 -305 tuff_bricks
fill 79 50 -331 103 62 -331 tuff_bricks
fill 79 50 -305 103 62 -305 tuff_bricks
fill 79 63 -331 103 63 -305 deepslate_tiles

# Central Level 30 Enchanting Sanctum (X: 89..93, Z: -320..-316)
fill 89 50 -320 93 50 -316 smooth_quartz
setblock 91 51 -318 enchanting_table
fill 89 51 -320 93 52 -320 bookshelf
fill 89 51 -316 93 52 -316 bookshelf
fill 89 51 -319 89 52 -317 bookshelf
fill 93 51 -319 93 52 -317 chiseled_bookshelf[facing=west]

# Perimeter Multi Tier Bookshelves (North & West Walls)
fill 80 51 -329 80 58 -307 chiseled_bookshelf[facing=east]
fill 81 51 -330 101 58 -330 chiseled_bookshelf[facing=south]

# Mezzanine Reading Balcony at Y: 55
fill 81 55 -328 83 55 -308 dark_oak_slab[type=top]
fill 84 55 -329 101 55 -327 dark_oak_slab[type=top]
fill 84 56 -326 101 56 -326 dark_oak_fence

# Spiral Access Stairs to Mezzanine (X: 100..101, Z: -310..-308)
setblock 100 50 -310 polished_deepslate
setblock 100 51 -310 dark_oak_stairs[facing=south,half=bottom]
setblock 101 51 -310 polished_deepslate
setblock 101 52 -310 dark_oak_stairs[facing=west,half=bottom]
setblock 101 52 -309 polished_deepslate
setblock 101 53 -309 dark_oak_stairs[facing=north,half=bottom]
setblock 100 53 -309 polished_deepslate
setblock 100 54 -309 dark_oak_stairs[facing=east,half=bottom]
setblock 100 54 -308 dark_oak_slab[type=top]

# Floating Lecterns & Study Tables
setblock 87 51 -314 dark_oak_slab[type=top]
setblock 87 52 -314 lectern[facing=south]
setblock 87 51 -313 dark_oak_stairs[facing=north,half=bottom]

setblock 95 51 -314 dark_oak_slab[type=top]
setblock 95 52 -314 lectern[facing=south]
setblock 95 51 -313 dark_oak_stairs[facing=north,half=bottom]

# Alchemical Distillation Corner (East Wall of Library: X: 101..102, Z: -316..-312)
fill 101 51 -316 102 51 -312 polished_blackstone
setblock 101 52 -315 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 101 52 -313 cauldron
fill 102 52 -316 102 54 -312 barrel[facing=west]

# Chandeliers and Lanterns
setblock 91 62 -318 iron_chain[axis=y]
setblock 91 61 -318 iron_chain[axis=y]
setblock 91 60 -318 copper_bulb[lit=true]
setblock 91 59 -318 lantern[hanging=true]

# Doorway connecting to Crossroads Corridor at X=103
fill 103 50 -307 103 54 -305 air
