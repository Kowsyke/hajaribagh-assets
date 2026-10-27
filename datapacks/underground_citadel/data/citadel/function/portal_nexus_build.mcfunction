# Subterranean Citadel: The Celestial Portal Nexus
fill 106 36 -302 128 47 -280 air
fill 105 35 -303 129 35 -279 polished_deepslate
fill 106 36 -302 128 36 -280 calcite
fill 105 36 -303 105 47 -279 deepslate_bricks
fill 129 36 -303 129 47 -279 deepslate_bricks
fill 105 36 -303 129 47 -303 deepslate_bricks
fill 105 36 -279 129 47 -279 deepslate_bricks
fill 105 48 -303 129 48 -279 crying_obsidian

# Central End Portal Well (Sunken at Y: 36)
fill 115 36 -293 119 36 -289 dark_prismarine
setblock 116 36 -293 end_portal_frame[facing=south,eye=true]
setblock 117 36 -293 end_portal_frame[facing=south,eye=true]
setblock 118 36 -293 end_portal_frame[facing=south,eye=true]

setblock 116 36 -289 end_portal_frame[facing=north,eye=true]
setblock 117 36 -289 end_portal_frame[facing=north,eye=true]
setblock 118 36 -289 end_portal_frame[facing=north,eye=true]

setblock 115 36 -292 end_portal_frame[facing=east,eye=true]
setblock 115 36 -291 end_portal_frame[facing=east,eye=true]
setblock 115 36 -290 end_portal_frame[facing=east,eye=true]

setblock 119 36 -292 end_portal_frame[facing=west,eye=true]
setblock 119 36 -291 end_portal_frame[facing=west,eye=true]
setblock 119 36 -290 end_portal_frame[facing=west,eye=true]

fill 116 36 -292 118 36 -290 end_portal

# Monumental Nether Portal (North Wall: Z: -302)
fill 114 37 -302 120 44 -302 obsidian
fill 115 38 -302 119 43 -302 crying_obsidian
fill 116 39 -302 118 42 -302 nether_portal[axis=x]

# Amethyst Geode Cavity on East Wall
fill 125 36 -294 128 44 -288 amethyst_block
setblock 124 38 -292 budding_amethyst
setblock 124 39 -291 budding_amethyst
setblock 124 37 -290 budding_amethyst
setblock 123 38 -292 amethyst_cluster[facing=west]
setblock 123 39 -291 amethyst_cluster[facing=west]
setblock 123 37 -290 amethyst_cluster[facing=west]

# Ambient Lighting via Copper Bulbs and Soul Lanterns
setblock 107 41 -291 copper_bulb[lit=true]
setblock 127 41 -291 copper_bulb[lit=true]
setblock 117 41 -281 copper_bulb[lit=true]
setblock 117 46 -291 soul_lantern[hanging=true]
