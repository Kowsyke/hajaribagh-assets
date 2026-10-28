# Subterranean Citadel: Sovereign Residential Suites
# Dimensions: X: 92..142, Z: -268..-231, Floor Y: 50, Ceiling Y: 58
fill 92 50 -268 142 58 -231 air

# Foundation & Shell
fill 91 49 -269 143 49 -230 polished_deepslate
fill 92 50 -268 142 50 -231 spruce_planks
fill 91 50 -269 91 58 -230 stone_bricks
fill 143 50 -269 143 58 -230 stone_bricks
fill 91 50 -269 143 58 -269 stone_bricks
fill 91 50 -230 143 58 -230 stone_bricks
fill 91 59 -269 143 59 -230 deepslate_tiles

# Corridor Spine linking suites (Z: -250, X: 92..142)
fill 92 50 -251 142 50 -249 stripped_dark_oak_wood[axis=x]
fill 92 50 -250 142 50 -250 red_carpet

# King Abir Sovereign Suite (Northwest: X: 93..105, Z: -268..-252)
# Royal Canopy Bed (Red)
fill 95 50 -266 96 50 -265 red_wool
setblock 95 51 -266 red_bed[facing=south,part=head]
setblock 95 51 -265 red_bed[facing=south,part=foot]
setblock 96 51 -266 red_bed[facing=south,part=head]
setblock 96 51 -265 red_bed[facing=south,part=foot]
# Canopy Posts
setblock 94 51 -266 stripped_spruce_log[axis=y]
setblock 94 52 -266 stripped_spruce_log[axis=y]
setblock 97 51 -266 stripped_spruce_log[axis=y]
setblock 97 52 -266 stripped_spruce_log[axis=y]
setblock 94 53 -266 spruce_trapdoor[half=top,open=false]
setblock 97 53 -266 spruce_trapdoor[half=top,open=false]

# Executive Writing Desk
setblock 102 51 -266 dark_oak_slab[type=top]
setblock 102 52 -266 lectern[facing=south]
setblock 102 51 -265 dark_oak_stairs[facing=north,half=bottom]
setblock 101 52 -266 lantern[hanging=false]

# Wardrobe Armor Stand
setblock 94 51 -255 armor_stand[facing=south]
setblock 93 51 -255 chiseled_bookshelf[facing=east]

# Ahsane Executive Library Suite (Northeast: X: 129..141, Z: -268..-252)
# Cyan Canopy Bed
setblock 135 51 -266 cyan_bed[facing=south,part=head]
setblock 135 51 -265 cyan_bed[facing=south,part=foot]
setblock 136 51 -266 cyan_bed[facing=south,part=head]
setblock 136 51 -265 cyan_bed[facing=south,part=foot]

# Library Study Pod
fill 139 51 -267 141 54 -267 bookshelf
setblock 140 51 -265 dark_oak_slab[type=top]
setblock 140 52 -265 lectern[facing=south]
setblock 140 51 -264 dark_oak_stairs[facing=north,half=bottom]
setblock 139 52 -265 sea_pickle[pickles=2]

# Jamal Tourism & Hunting Suite (South: X: 111..123, Z: -248..-232)
# Purple Canopy Bed
setblock 116 51 -234 purple_bed[facing=north,part=head]
setblock 116 51 -235 purple_bed[facing=north,part=foot]
setblock 117 51 -234 purple_bed[facing=north,part=head]
setblock 117 51 -235 purple_bed[facing=north,part=foot]

# Trophy Mount & Armory Chests
setblock 120 51 -234 armor_stand[facing=north]
setblock 121 51 -234 chest[facing=north,type=left]
setblock 122 51 -234 chest[facing=north,type=right]

# Suite Lighting Fixtures
setblock 99 58 -260 iron_chain[axis=y]
setblock 99 57 -260 copper_bulb[lit=true,powered=false]
setblock 99 56 -260 lantern[hanging=true]

setblock 135 58 -260 iron_chain[axis=y]
setblock 135 57 -260 copper_bulb[lit=true,powered=false]
setblock 135 56 -260 lantern[hanging=true]

setblock 117 58 -240 iron_chain[axis=y]
setblock 117 57 -240 copper_bulb[lit=true,powered=false]
setblock 117 56 -240 lantern[hanging=true]
