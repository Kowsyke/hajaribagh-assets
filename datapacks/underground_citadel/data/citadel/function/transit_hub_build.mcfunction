# Subterranean Citadel: Hyperloop Transit Hub
# Dimensions: X: 104..130, Z: -345..-325, Floor Y: 49, Ceiling Y: 58
fill 104 49 -345 130 58 -325 air

# Foundation & Concourse Quartz Floor
fill 103 48 -346 131 48 -324 polished_deepslate
fill 104 49 -345 130 49 -325 smooth_quartz
fill 103 49 -346 103 58 -324 polished_blackstone
fill 131 49 -346 131 58 -324 polished_blackstone
fill 103 49 -346 131 58 -346 polished_blackstone
fill 103 49 -324 131 58 -324 polished_blackstone
fill 103 59 -346 131 59 -324 deepslate_tiles

# Hazard Warning Stripes (Yellow and Black Concrete)
fill 109 49 -344 109 49 -328 yellow_concrete
fill 110 49 -344 110 49 -328 black_concrete
fill 124 49 -344 124 49 -328 yellow_concrete
fill 125 49 -344 125 49 -328 black_concrete

# Track Bays with Powered Rails
fill 107 49 -344 107 49 -328 polished_deepslate
fill 107 50 -344 107 50 -328 powered_rail[shape=north_south]
setblock 107 48 -336 redstone_block
setblock 107 48 -342 redstone_block

fill 127 49 -344 127 49 -328 polished_deepslate
fill 127 50 -344 127 50 -328 powered_rail[shape=north_south]
setblock 127 48 -336 redstone_block
setblock 127 48 -342 redstone_block

# Station Ticket Booth (Center: X: 115..119, Z: -340..-336)
fill 115 50 -340 119 53 -336 glass outline
setblock 117 50 -336 iron_door[facing=south,half=lower]
setblock 117 51 -336 iron_door[facing=south,half=upper]
setblock 116 50 -338 dark_oak_slab[type=top]
setblock 116 51 -338 daylight_detector

# Waiting Lounge Benches
fill 114 50 -332 114 50 -328 polished_deepslate_stairs[facing=east,half=bottom]
fill 120 50 -332 120 50 -328 polished_deepslate_stairs[facing=west,half=bottom]

# Station Illuminated Ceiling Grids
setblock 111 58 -336 sea_lantern
setblock 117 58 -336 sea_lantern
setblock 123 58 -336 sea_lantern

# Concourse Doorways to North Stairwell and Conduits
fill 116 50 -325 118 54 -325 air
