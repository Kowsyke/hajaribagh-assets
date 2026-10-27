# The Great Treasury: Royal Sovereign Sanctuary
# Dais elevation at Y: 65 (Z = -307 to -301, X = 111 to 123)
fill 111 65 -307 123 65 -301 mud_bricks replace air
fill 113 65 -306 121 65 -302 polished_blackstone_brick_slab[type=bottom]
fill 114 65 -307 120 65 -307 mud_brick_stairs[facing=north,half=bottom]

# Royal Pedestal with Ender Chest at center (117, 66, -303)
setblock 117 65 -303 gold_block
setblock 117 66 -303 ender_chest[facing=north]
setblock 116 66 -303 gold_block
setblock 118 66 -303 gold_block
setblock 116 67 -303 lantern[hanging=false]
setblock 118 67 -303 lantern[hanging=false]

# West Workstation Alcove (X = 112..114, Z = -305..-303)
setblock 113 66 -303 anvil[facing=east]
setblock 113 66 -304 smithing_table
setblock 113 66 -305 grindstone[facing=east,face=floor]
setblock 113 66 -306 cartography_table
fill 112 66 -306 112 68 -303 chiseled_bookshelf

# East Enchanting Sanctuary (X = 120..122, Z = -305..-303)
setblock 121 66 -304 enchanting_table
fill 120 66 -306 122 67 -306 chiseled_bookshelf
fill 122 66 -305 122 67 -303 chiseled_bookshelf
setblock 120 66 -303 lapis_block
setblock 120 67 -303 soul_lantern[hanging=false]

# Grand Cozy Fireplace Hearth at South Wall (117, 65..71, -301)
fill 115 65 -302 119 69 -301 mud_bricks
fill 116 66 -302 118 67 -302 air
setblock 117 65 -302 campfire[lit=true]
setblock 117 66 -302 iron_bars
setblock 116 66 -302 mud_brick_stairs[facing=east]
setblock 118 66 -302 mud_brick_stairs[facing=west]
fill 116 68 -302 118 68 -302 mud_brick_slab[type=bottom]
setblock 117 69 -302 potted_fern
