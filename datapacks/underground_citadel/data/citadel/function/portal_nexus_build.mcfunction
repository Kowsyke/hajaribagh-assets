# Subterranean Citadel: Celestial Portal Nexus
# Dimensions: X: 106..128, Z: -302..-280, Floor Y: 36, Ceiling Y: 48
fill 106 36 -302 128 48 -280 air

# Foundation & Calcite Concentric Floor
fill 105 35 -303 129 35 -279 polished_deepslate
fill 106 36 -302 128 36 -280 polished_deepslate_bricks
fill 112 36 -296 122 36 -286 calcite
fill 115 36 -293 119 36 -289 crying_obsidian
fill 105 36 -303 105 48 -279 deepslate_tiles
fill 129 36 -303 129 48 -279 deepslate_tiles
fill 105 36 -303 129 48 -303 deepslate_tiles
fill 105 36 -279 129 48 -279 deepslate_tiles
fill 105 49 -303 129 49 -279 deepslate_tiles

# Active 5x7 Nether Portal Aperture (North Wall: Z: -302)
fill 115 37 -302 119 43 -302 obsidian
fill 116 38 -302 118 42 -302 nether_portal[axis=x]
fill 114 37 -302 114 43 -302 gilded_blackstone
fill 120 37 -302 120 43 -302 gilded_blackstone
setblock 113 37 -301 soul_fire
setblock 121 37 -301 soul_fire

# Sunken Authentic End Portal Well (South: Z: -284)
fill 115 35 -286 119 35 -282 end_stone_bricks
setblock 116 36 -286 end_portal_frame[facing=south,eye=true]
setblock 117 36 -286 end_portal_frame[facing=south,eye=true]
setblock 118 36 -286 end_portal_frame[facing=south,eye=true]
setblock 116 36 -282 end_portal_frame[facing=north,eye=true]
setblock 117 36 -282 end_portal_frame[facing=north,eye=true]
setblock 118 36 -282 end_portal_frame[facing=north,eye=true]
setblock 115 36 -285 end_portal_frame[facing=east,eye=true]
setblock 115 36 -284 end_portal_frame[facing=east,eye=true]
setblock 115 36 -283 end_portal_frame[facing=east,eye=true]
setblock 119 36 -285 end_portal_frame[facing=west,eye=true]
setblock 119 36 -284 end_portal_frame[facing=west,eye=true]
setblock 119 36 -283 end_portal_frame[facing=west,eye=true]
fill 116 36 -285 118 36 -283 end_portal

# Crystal Amethyst Geode Cavity (East Wall: X: 125..128)
fill 125 36 -293 128 42 -289 amethyst_block
fill 126 37 -292 127 41 -290 air
setblock 126 37 -291 budding_amethyst
setblock 127 37 -291 amethyst_cluster[facing=up]
setblock 126 41 -291 amethyst_cluster[facing=down]

# Celestial Chandelier
setblock 117 48 -291 iron_chain[axis=y]
setblock 117 47 -291 iron_chain[axis=y]
setblock 117 46 -291 copper_bulb[lit=true,powered=false]
setblock 117 45 -291 soul_lantern[hanging=true]
setblock 116 45 -291 end_rod
setblock 118 45 -291 end_rod
