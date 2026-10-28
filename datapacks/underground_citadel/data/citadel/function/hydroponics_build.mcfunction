# Subterranean Citadel: Hydroponics Biosphere and Apiary
# Dimensions: X: 136..154, Z: -302..-280, Floor Y: 50, Ceiling Y: 61
fill 136 50 -302 154 61 -280 air

# Foundation & Outer Shell
fill 135 49 -303 155 49 -279 polished_deepslate
fill 135 50 -303 135 61 -279 stone_bricks
fill 155 50 -303 155 61 -279 stone_bricks
fill 135 50 -303 155 61 -303 stone_bricks
fill 135 50 -279 155 61 -279 stone_bricks
fill 135 62 -303 155 62 -279 deepslate_tiles

# Terraced Hydrated Farmland (South wing: Z: -290..-281)
fill 137 50 -290 144 50 -281 farmland[moisture=7]
fill 137 51 -290 144 51 -288 wheat[age=7]
fill 137 51 -287 144 51 -285 carrots[age=7]
fill 137 51 -284 144 51 -282 potatoes[age=7]
fill 137 51 -281 144 51 -281 beetroots[age=3]

# Stepped Irrigation Canal
fill 141 50 -291 141 50 -281 water
setblock 141 49 -286 sea_pickle[pickles=3,waterlogged=true]

# Enclosed Glass Apiary Sanctuary (North wing: Z: -301..-293)
fill 137 50 -301 144 50 -293 grass_block
fill 136 51 -302 145 56 -292 glass outline
fill 137 51 -301 144 55 -293 air

# 4 Active Beehives with Campfire Smoke Dampers
setblock 139 49 -298 campfire[lit=true]
setblock 139 50 -298 oak_trapdoor[half=top,open=false]
setblock 139 51 -298 beehive[facing=south,honey_level=5]

setblock 142 49 -298 campfire[lit=true]
setblock 142 50 -298 oak_trapdoor[half=top,open=false]
setblock 142 51 -298 beehive[facing=south,honey_level=5]

# Bee Flora
setblock 138 51 -295 rose_bush[half=lower]
setblock 138 52 -295 rose_bush[half=upper]
setblock 143 51 -295 sunflower[half=lower]
setblock 143 52 -295 sunflower[half=upper]
setblock 140 51 -295 dandelion
setblock 141 51 -295 poppy

# Subterranean Cherry Blossom Tree (East side: X: 149, Z: -291)
fill 149 50 -291 149 54 -291 stripped_cherry_log[axis=y]
fill 147 55 -293 151 56 -289 cherry_leaves
setblock 149 57 -291 cherry_leaves
setblock 149 54 -292 cave_vines[berries=true]

# Composter & Tool Storage
setblock 152 50 -283 composter[level=6]
setblock 153 50 -283 composter[level=7]
fill 152 50 -281 153 52 -281 barrel[facing=south]

# Warm Amber Lantern Lighting
setblock 145 58 -291 iron_chain[axis=y]
setblock 145 57 -291 copper_bulb[lit=true,powered=false]
setblock 145 56 -291 lantern[hanging=true]

# Doorway to Atrium at X=135
fill 135 50 -292 135 54 -290 air
