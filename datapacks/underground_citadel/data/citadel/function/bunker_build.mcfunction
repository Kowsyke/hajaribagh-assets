# Subterranean Citadel: Sector C Heavy Blast Door and War Room

# -------------------------------------------------------------
# Heavy Blast Door Airlock at Z: -275..-273
# Frame in Crying Obsidian and Polished Deepslate
fill 114 49 -275 120 49 -273 crying_obsidian
fill 114 55 -275 120 55 -273 crying_obsidian
fill 114 50 -275 114 54 -275 crying_obsidian
fill 120 50 -275 120 54 -275 crying_obsidian

# Blast Door Opening: 3x3 at X: 116..118, Y: 51..53
# Heavy Iron Bars and Polished Basalt Piston Seal
fill 115 50 -274 119 50 -274 polished_deepslate
fill 116 51 -274 118 53 -274 iron_bars
setblock 115 52 -275 redstone_lamp[lit=true]
setblock 119 52 -275 redstone_lamp[lit=true]
setblock 115 51 -275 lever[facing=north]
setblock 119 51 -275 lever[facing=north]

# -------------------------------------------------------------
# Sovereign Council War Room (X: 108..126, Z: -271..-259)
# Shell and Foundation
fill 107 49 -272 127 49 -258 polished_deepslate
fill 108 50 -271 126 50 -259 polished_blackstone
fill 107 58 -272 127 58 -258 deepslate_tiles

# Perimeter Walls: Deepslate Bricks and Chiseled Deepslate
fill 107 50 -272 107 57 -258 deepslate_bricks
fill 127 50 -272 127 57 -258 deepslate_bricks
fill 107 50 -272 127 57 -272 deepslate_bricks
fill 107 50 -258 127 57 -258 deepslate_bricks

# Red Carpet Runner
fill 116 50 -271 118 50 -259 red_carpet
setblock 117 49 -268 shroomlight
setblock 117 49 -265 shroomlight
setblock 117 49 -262 shroomlight

# Grand Council Conference Table (Center: X: 115..119, Z: -267..-263)
fill 115 51 -267 119 51 -263 dark_oak_slab[type=top]
fill 116 51 -266 118 51 -264 polished_blackstone_slab[type=top]
summon end_crystal 117.5 52.0 -264.5 {ShowBottom:0b}

# Sovereign Council Armchairs
# Prime Minister Chair (South end facing north)
setblock 117 51 -262 dark_oak_stairs[facing=north]
setblock 116 51 -262 dark_oak_trapdoor[facing=west,open=true]
setblock 118 51 -262 dark_oak_trapdoor[facing=east,open=true]

# Executive Chairs (East and West)
setblock 114 51 -266 dark_oak_stairs[facing=east]
setblock 114 51 -264 dark_oak_stairs[facing=east]
setblock 120 51 -266 dark_oak_stairs[facing=west]
setblock 120 51 -264 dark_oak_stairs[facing=west]

# Sovereign Strategic Map Wall (East Wall: X: 126, Z: -266..-264)
fill 126 51 -266 126 53 -264 stripped_dark_oak_wood[axis=y]
fill 126 52 -266 126 52 -264 cartography_table

# Server Constitution Lectern (West Wall: X: 108, Z: -265)
setblock 108 51 -265 lectern[facing=east]
setblock 108 52 -265 lantern[hanging=false]
fill 108 51 -267 108 53 -267 bookshelf
fill 108 51 -263 108 53 -263 bookshelf
