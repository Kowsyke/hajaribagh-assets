# Subterranean Citadel: Sector B Automated Hydroponics and Tree Conservatory
fill 136 49 -302 154 49 -280 stripped_cherry_wood[axis=y]
fill 136 50 -302 136 60 -280 smooth_quartz
fill 154 50 -302 154 60 -280 smooth_quartz
fill 136 50 -302 154 60 -302 smooth_quartz
fill 136 50 -280 154 60 -280 smooth_quartz
fill 136 61 -302 154 61 -280 deepslate_tiles

fill 130 50 -293 136 55 -289 air
fill 130 49 -292 136 49 -290 stripped_cherry_wood[axis=x]
fill 130 50 -292 136 50 -290 bamboo_mosaic
fill 130 51 -293 136 54 -293 smooth_quartz_stairs[facing=south]
fill 130 51 -289 136 54 -289 smooth_quartz_stairs[facing=north]
fill 130 55 -292 136 55 -290 sea_lantern

fill 137 50 -301 153 50 -281 bamboo_mosaic
fill 142 50 -297 148 50 -285 mud

# 1. Automated Sugarcane & Bamboo Harvester
fill 138 49 -300 151 49 -300 water
setblock 137 49 -300 hopper[facing=west]
setblock 136 49 -300 barrel[facing=up]

fill 138 50 -301 144 50 -301 sand
fill 145 50 -301 151 50 -301 mud

fill 138 51 -301 144 51 -301 sugar_cane
fill 145 51 -301 151 51 -301 bamboo[age=1,leaves=large,stage=0]

fill 138 52 -301 151 52 -301 piston[facing=south]
fill 138 53 -301 151 53 -301 observer[facing=south]

fill 138 52 -302 151 52 -302 smooth_stone
fill 138 53 -302 151 53 -302 redstone_wire

fill 138 51 -299 151 54 -299 glass
fill 138 55 -301 151 55 -299 sea_lantern

# 2. Indoor Tree Conservatory
fill 143 50 -295 147 50 -287 rooted_dirt
fill 144 50 -294 146 50 -288 mud

fill 145 51 -293 145 56 -293 stripped_cherry_log[axis=y]
fill 143 56 -295 147 58 -291 cherry_leaves
fill 144 59 -294 146 59 -292 cherry_leaves

fill 145 51 -288 145 55 -288 stripped_dark_oak_log[axis=y]
fill 143 55 -290 147 57 -286 dark_oak_leaves

setblock 142 51 -291 dispenser[facing=east]
setblock 142 52 -291 stone_button[facing=east]

# 3. Apiary Bee Sanctuary
fill 138 50 -284 151 50 -284 packed_mud
fill 140 49 -283 148 49 -283 campfire[lit=true]
fill 140 50 -283 148 50 -283 moss_carpet

setblock 141 51 -283 beehive[facing=north,honey_level=5]
setblock 143 51 -283 bee_nest[facing=north,honey_level=5]
setblock 145 51 -283 beehive[facing=north,honey_level=5]
setblock 147 51 -283 bee_nest[facing=north,honey_level=5]

setblock 141 51 -284 flowering_azalea
setblock 143 51 -284 rose_bush[half=lower]
setblock 143 52 -284 rose_bush[half=upper]
setblock 145 51 -284 flowering_azalea
setblock 147 51 -284 peony[half=lower]
setblock 147 52 -284 peony[half=upper]

fill 139 51 -285 149 54 -285 tinted_glass
fill 139 55 -285 149 55 -283 sea_lantern

summon bee 144 52 -284 {CannotEnterHiveTicks:0,TicksInHive:0}
summon bee 146 52 -284 {CannotEnterHiveTicks:0,TicksInHive:0}
