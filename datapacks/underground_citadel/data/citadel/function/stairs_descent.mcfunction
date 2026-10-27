# Subterranean Citadel: Grand Staircase Descent
# Extends from Treasury stairs at X: 116..118, Z: -318, Y: 60 down to Atrium landing at Y: 50, Z: -305

# Clear stair corridor
fill 114 49 -318 120 65 -305 air

# Enclosure walls and vaulting
fill 114 49 -318 114 65 -305 deepslate_tiles
fill 120 49 -318 120 65 -305 deepslate_tiles

# Stair steps descending south facing south
# Z=-317: Y=59
fill 114 49 -317 120 58 -317 polished_deepslate
fill 116 59 -317 118 59 -317 spruce_stairs[facing=south]
setblock 115 59 -317 stripped_dark_oak_log[axis=y]
setblock 119 59 -317 stripped_dark_oak_log[axis=y]
fill 115 60 -317 115 64 -317 deepslate_tile_wall
fill 119 60 -317 119 64 -317 deepslate_tile_wall

# Z=-316: Y=58
fill 114 49 -316 120 57 -316 polished_deepslate
fill 116 58 -316 118 58 -316 spruce_stairs[facing=south]

# Z=-315: Y=57
fill 114 49 -315 120 56 -315 polished_deepslate
fill 116 57 -315 118 57 -315 spruce_stairs[facing=south]
setblock 115 58 -315 stripped_dark_oak_log[axis=y]
setblock 119 58 -315 stripped_dark_oak_log[axis=y]
setblock 115 59 -315 lantern[hanging=false]
setblock 119 59 -315 lantern[hanging=false]

# Z=-314: Y=56
fill 114 49 -314 120 55 -314 polished_deepslate
fill 116 56 -314 118 56 -314 spruce_stairs[facing=south]

# Z=-313: Y=55
fill 114 49 -313 120 54 -313 polished_deepslate
fill 116 55 -313 118 55 -313 spruce_stairs[facing=south]

# Z=-312: Y=54
fill 114 49 -312 120 53 -312 polished_deepslate
fill 116 54 -312 118 54 -312 spruce_stairs[facing=south]
setblock 115 55 -312 stripped_dark_oak_log[axis=y]
setblock 119 55 -312 stripped_dark_oak_log[axis=y]
setblock 115 56 -312 lantern[hanging=false]
setblock 119 56 -312 lantern[hanging=false]

# Z=-311: Y=53
fill 114 49 -311 120 52 -311 polished_deepslate
fill 116 53 -311 118 53 -311 spruce_stairs[facing=south]

# Z=-310: Y=52
fill 114 49 -310 120 51 -310 polished_deepslate
fill 116 52 -310 118 52 -310 spruce_stairs[facing=south]

# Z=-309: Y=51
fill 114 49 -309 120 50 -309 polished_deepslate
fill 116 51 -309 118 51 -309 spruce_stairs[facing=south]
setblock 115 52 -309 stripped_dark_oak_log[axis=y]
setblock 119 52 -309 stripped_dark_oak_log[axis=y]
setblock 115 53 -309 lantern[hanging=false]
setblock 119 53 -309 lantern[hanging=false]

# Z=-308: Y=50 (Final landing step)
fill 114 49 -308 120 49 -308 polished_deepslate
fill 116 50 -308 118 50 -308 spruce_stairs[facing=south]

# Transition Vestibule at Z: -307..-305 with floor Y=50
fill 114 49 -307 120 49 -305 polished_deepslate
fill 116 50 -307 118 50 -305 stripped_spruce_wood[axis=z]
fill 115 50 -307 115 50 -305 mud_bricks
fill 119 50 -307 119 50 -305 mud_bricks

# Under-floor ambient lights in vestibule
setblock 117 49 -306 shroomlight
setblock 117 50 -306 moss_carpet
setblock 116 50 -306 moss_block
setblock 118 50 -306 moss_block

# Archway pillars entering Atrium
fill 115 51 -305 115 54 -305 stripped_dark_oak_log[axis=y]
fill 119 51 -305 119 54 -305 stripped_dark_oak_log[axis=y]
setblock 116 55 -305 dark_oak_stairs[facing=east,half=top]
setblock 118 55 -305 dark_oak_stairs[facing=west,half=top]
setblock 117 55 -305 polished_deepslate_slab[type=top]
