# Subterranean Citadel: Bio Dome Atrium Architecture
# Excavate bounding volume
fill 104 50 -305 130 58 -277 air

# Foundation and Primary Moss Carpet Floor
fill 103 49 -306 131 49 -276 polished_deepslate
fill 105 50 -304 129 50 -278 moss_block
fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -291 129 50 -291 stripped_dark_oak_wood[axis=x]

# Perimeter Walls and Skirting
fill 104 50 -305 104 57 -277 deepslate_tiles
fill 130 50 -305 130 57 -277 deepslate_tiles
fill 104 50 -305 130 57 -305 deepslate_tiles
fill 104 50 -277 130 57 -277 deepslate_tiles

fill 105 51 -304 105 51 -278 polished_deepslate_stairs[facing=east,half=bottom]
fill 129 51 -304 129 51 -278 polished_deepslate_stairs[facing=west,half=bottom]
fill 105 51 -304 129 51 -304 polished_deepslate_stairs[facing=south,half=bottom]
fill 105 51 -278 129 51 -278 polished_deepslate_stairs[facing=north,half=bottom]

# Clear Doorway Openings in Skirting
fill 115 51 -304 119 51 -304 air
fill 115 51 -278 119 51 -278 air
fill 105 51 -292 105 51 -290 air
fill 129 51 -292 129 51 -290 air

# Coffered Ceiling and Glass Skylight Vault
fill 104 58 -305 130 58 -277 deepslate_tiles
fill 111 58 -298 123 58 -284 glass

# Structural Granite and Basalt Pilasters
fill 109 50 -299 109 57 -299 polished_basalt[axis=y]
setblock 109 54 -299 chiseled_tuff
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 125 50 -299 125 57 -299 polished_basalt[axis=y]
setblock 125 54 -299 chiseled_tuff
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 109 50 -283 109 57 -283 polished_basalt[axis=y]
setblock 109 54 -283 chiseled_tuff
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

fill 125 50 -283 125 57 -283 polished_basalt[axis=y]
setblock 125 54 -283 chiseled_tuff
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Arched Vault Ribs
fill 110 57 -299 124 57 -299 dark_oak_stairs[facing=south,half=top]
fill 110 57 -283 124 57 -283 dark_oak_stairs[facing=north,half=top]
fill 109 57 -298 109 57 -284 dark_oak_stairs[facing=east,half=top]
fill 125 57 -298 125 57 -284 dark_oak_stairs[facing=west,half=top]

# Sunken Marine Aquarium Basin (X: 113..121, Z: -295..-287, Y: 46..49)
fill 112 45 -296 122 45 -286 sea_lantern
fill 113 46 -295 121 46 -287 dark_prismarine
fill 113 47 -295 121 49 -287 water
fill 113 50 -295 121 50 -287 air

# Aquarium Perimeter Railing and Glass Viewing Panels
fill 113 50 -295 121 50 -295 dark_oak_fence
fill 113 50 -287 121 50 -287 dark_oak_fence
fill 113 50 -294 113 50 -288 dark_oak_fence
fill 121 50 -294 121 50 -288 dark_oak_fence

fill 116 50 -295 118 50 -287 tinted_glass
fill 113 50 -292 121 50 -290 tinted_glass

# Coral Reef Flora inside Aquarium
setblock 115 47 -293 fire_coral_block
setblock 115 48 -293 fire_coral_fan[waterlogged=true]
setblock 119 47 -293 tube_coral_block
setblock 119 48 -293 tube_coral_fan[waterlogged=true]
setblock 115 47 -289 horn_coral_block
setblock 115 48 -289 horn_coral_fan[waterlogged=true]
setblock 119 47 -289 brain_coral_block
setblock 119 48 -289 brain_coral_fan[waterlogged=true]
setblock 117 47 -291 sea_pickle[pickles=4,waterlogged=true]

# Bubble Column Shafts to Sector 3 (Celestial Nexus)
fill 114 37 -291 114 50 -291 tinted_glass
setblock 114 37 -291 magma_block
fill 114 38 -291 114 50 -291 water

fill 120 37 -291 120 50 -291 tinted_glass
setblock 120 37 -291 soul_sand
fill 120 38 -291 120 50 -291 water
