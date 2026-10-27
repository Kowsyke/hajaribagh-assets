# Subterranean Citadel: The Subterranean Hyperloop Transit Hub
# Dimensions: X: 104..130, Z: -345..-325, Floor Y: 49..50, Ceiling Y: 58
fill 104 49 -345 130 58 -325 air

# Foundation & Concourse
fill 103 48 -346 131 48 -324 polished_deepslate
fill 104 50 -345 130 50 -325 smooth_quartz
fill 103 50 -346 103 58 -324 polished_blackstone
fill 131 50 -346 131 58 -324 polished_blackstone
fill 103 50 -346 131 58 -346 polished_blackstone
fill 103 59 -346 131 59 -324 deepslate_tiles

# Concourse Stairs connecting from Treasury area (Z: -325)
fill 115 50 -325 119 54 -325 air

# Track Trough 1 (West Line: Surface Express, X: 108..109, Y: 49)
fill 108 49 -345 109 49 -327 polished_blackstone
fill 108 50 -345 108 50 -327 yellow_concrete
fill 109 50 -345 109 50 -327 powered_rail[powered=true,shape=north_south]

# Track Trough 2 (Center Line: Bedrock Mining Express, X: 117..118, Y: 49)
fill 117 49 -345 118 49 -327 polished_blackstone
fill 116 50 -345 116 50 -327 yellow_concrete
fill 117 50 -345 117 50 -327 powered_rail[powered=true,shape=north_south]

# Track Trough 3 (East Line: City Base Express, X: 125..126, Y: 49)
fill 125 49 -345 126 49 -327 polished_blackstone
fill 124 50 -345 124 50 -327 yellow_concrete
fill 125 50 -345 125 50 -327 powered_rail[powered=true,shape=north_south]

# Push-Button Minecart Dispensers at Boarding Gates (Z: -328)
setblock 109 51 -328 dispenser[facing=north]
setblock 109 52 -328 stone_button[face=floor,facing=north]

setblock 117 51 -328 dispenser[facing=north]
setblock 117 52 -328 stone_button[face=floor,facing=north]

setblock 125 51 -328 dispenser[facing=north]
setblock 125 52 -328 stone_button[face=floor,facing=north]

# Hazard Warning Stripes along Platform Edges
fill 110 50 -345 110 50 -327 black_concrete
fill 115 50 -345 115 50 -327 black_concrete
fill 118 50 -345 118 50 -327 black_concrete
fill 123 50 -345 123 50 -327 black_concrete

# Lighting via Inset Sea Lanterns and Copper Bulbs
fill 112 50 -340 114 50 -340 sea_lantern
fill 120 50 -340 122 50 -340 sea_lantern
setblock 109 55 -335 copper_bulb[lit=true]
setblock 117 55 -335 copper_bulb[lit=true]
setblock 125 55 -335 copper_bulb[lit=true]
