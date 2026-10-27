# Subterranean Citadel: Grand High Parliament of the Republic
fill 104 50 -276 130 58 -244 air

fill 103 49 -277 131 49 -243 polished_deepslate
fill 104 50 -276 130 50 -244 polished_blackstone
fill 103 50 -277 103 58 -243 polished_blackstone_bricks
fill 131 50 -277 131 58 -243 polished_blackstone_bricks
fill 103 50 -277 131 58 -277 polished_blackstone_bricks
fill 103 50 -243 131 58 -243 polished_blackstone_bricks
fill 103 59 -277 131 59 -243 deepslate_tiles

# Chamber Pilasters
fill 104 50 -272 104 58 -272 polished_basalt[axis=y]
fill 104 50 -266 104 58 -266 polished_basalt[axis=y]
fill 104 50 -260 104 58 -260 polished_basalt[axis=y]
fill 104 50 -254 104 58 -254 polished_basalt[axis=y]
fill 104 50 -248 104 58 -248 polished_basalt[axis=y]

fill 130 50 -272 130 58 -272 polished_basalt[axis=y]
fill 130 50 -266 130 58 -266 polished_basalt[axis=y]
fill 130 50 -260 130 58 -260 polished_basalt[axis=y]
fill 130 50 -254 130 58 -254 polished_basalt[axis=y]
fill 130 50 -248 130 58 -248 polished_basalt[axis=y]

# North Portal from Atrium
fill 115 50 -277 119 55 -275 air
fill 115 49 -277 119 49 -275 polished_blackstone
fill 114 50 -276 114 55 -276 crying_obsidian
fill 120 50 -276 120 55 -276 crying_obsidian
fill 115 56 -276 119 56 -276 crying_obsidian

# Central Green Carpet Aisle
fill 116 50 -275 118 50 -252 green_carpet
fill 117 50 -275 117 50 -252 yellow_carpet

# Under floor ambient lights along aisle
setblock 117 48 -272 shroomlight
setblock 117 48 -266 shroomlight
setblock 117 48 -260 shroomlight
setblock 117 48 -254 shroomlight

# Cabinet Benches (West side: Members sit facing EAST towards aisle)
fill 114 50 -272 114 50 -254 dark_oak_planks
fill 114 51 -272 114 51 -254 dark_oak_slab[type=top]
fill 113 50 -272 113 50 -254 dark_oak_stairs[facing=east,half=bottom]
fill 113 51 -272 113 51 -254 green_carpet

fill 111 50 -272 112 50 -254 polished_blackstone
fill 112 51 -272 112 51 -254 dark_oak_slab[type=top]
fill 111 51 -272 111 51 -254 dark_oak_stairs[facing=east,half=bottom]
fill 111 52 -272 111 52 -254 green_carpet

fill 109 50 -272 110 51 -254 polished_blackstone
fill 110 52 -272 110 52 -254 dark_oak_slab[type=top]
fill 109 52 -272 109 52 -254 dark_oak_stairs[facing=east,half=bottom]
fill 109 53 -272 109 53 -254 green_carpet

setblock 114 52 -270 end_rod
setblock 114 52 -269 stone_button[face=floor,facing=north]
setblock 114 52 -266 end_rod
setblock 114 52 -265 stone_button[face=floor,facing=north]
setblock 114 52 -262 end_rod
setblock 114 52 -261 stone_button[face=floor,facing=north]
setblock 114 52 -258 end_rod
setblock 114 52 -257 stone_button[face=floor,facing=north]

# Assembly Benches (East side: Members sit facing WEST towards aisle)
fill 120 50 -272 120 50 -254 dark_oak_planks
fill 120 51 -272 120 51 -254 dark_oak_slab[type=top]
fill 121 50 -272 121 50 -254 dark_oak_stairs[facing=west,half=bottom]
fill 121 51 -272 121 51 -254 green_carpet

fill 122 50 -272 123 50 -254 polished_blackstone
fill 122 51 -272 122 51 -254 dark_oak_slab[type=top]
fill 123 51 -272 123 51 -254 dark_oak_stairs[facing=west,half=bottom]
fill 123 52 -272 123 52 -254 green_carpet

fill 124 50 -272 125 51 -254 polished_blackstone
fill 124 52 -272 124 52 -254 dark_oak_slab[type=top]
fill 125 52 -272 125 52 -254 dark_oak_stairs[facing=west,half=bottom]
fill 125 53 -272 125 53 -254 green_carpet

setblock 120 52 -270 end_rod
setblock 120 52 -269 stone_button[face=floor,facing=north]
setblock 120 52 -266 end_rod
setblock 120 52 -265 stone_button[face=floor,facing=north]
setblock 120 52 -262 end_rod
setblock 120 52 -261 stone_button[face=floor,facing=north]
setblock 120 52 -258 end_rod
setblock 120 52 -257 stone_button[face=floor,facing=north]

# Dais and Speaker Throne (South end: Steps face NORTH so players step UP to the south)
fill 113 50 -251 121 50 -245 smooth_quartz
fill 114 51 -251 120 51 -245 smooth_quartz
fill 114 51 -251 120 51 -251 smooth_quartz_stairs[facing=north,half=bottom]

fill 115 52 -249 119 52 -245 gold_block
fill 115 52 -249 119 52 -249 smooth_quartz_stairs[facing=north,half=bottom]

setblock 116 51 -251 dark_oak_slab[type=top]
setblock 117 51 -251 dark_oak_slab[type=top]
setblock 118 51 -251 dark_oak_slab[type=top]

# Ceremonial Mace on Blackstone Plinth
setblock 117 52 -251 polished_blackstone_brick_slab[type=bottom]
setblock 117 53 -251 lightning_rod[facing=up]

# Clerk Desks
setblock 119 52 -250 dark_oak_slab[type=top]
setblock 119 53 -250 green_candle[lit=true]
setblock 115 52 -250 dark_oak_slab[type=top]
setblock 115 53 -250 red_candle[lit=true]

setblock 117 53 -247 gilded_blackstone
setblock 117 54 -247 dark_oak_stairs[facing=north,half=bottom]
setblock 116 54 -247 dark_oak_trapdoor[facing=west,open=true]
setblock 118 54 -247 dark_oak_trapdoor[facing=east,open=true]

# Heraldic Wall of State behind Dais
fill 114 50 -244 120 57 -244 crying_obsidian
fill 116 54 -244 118 56 -244 gold_block
setblock 117 55 -244 bell[facing=north]

# Vaulted Chandeliers
setblock 117 58 -269 iron_chain[axis=y]
setblock 117 57 -269 iron_chain[axis=y]
setblock 117 56 -269 shroomlight
setblock 116 56 -269 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -269 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -269 soul_lantern[hanging=true]

setblock 117 58 -261 iron_chain[axis=y]
setblock 117 57 -261 iron_chain[axis=y]
setblock 117 56 -261 shroomlight
setblock 116 56 -261 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -261 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -261 soul_lantern[hanging=true]

setblock 117 58 -250 iron_chain[axis=y]
setblock 117 57 -250 iron_chain[axis=y]
setblock 117 56 -250 shroomlight
setblock 116 56 -250 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -250 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -250 soul_lantern[hanging=true]
