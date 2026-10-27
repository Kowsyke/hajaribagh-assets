# Subterranean Citadel: Atrium Shell and Architecture
fill 104 50 -304 130 57 -278 air
fill 112 47 -296 122 49 -286 air
fill 104 49 -305 130 49 -277 polished_deepslate
fill 105 50 -304 129 50 -278 polished_andesite
fill 104 58 -305 130 58 -277 deepslate_tiles

# Perimeter Walls with 3D Layered Pilasters & Moldings
fill 104 50 -305 104 57 -277 deepslate_tiles
fill 130 50 -305 130 57 -277 deepslate_tiles
fill 104 50 -305 130 57 -305 deepslate_tiles
fill 104 50 -277 130 57 -277 deepslate_tiles

fill 105 51 -304 105 51 -278 polished_deepslate_stairs[facing=east,half=bottom]
fill 129 51 -304 129 51 -278 polished_deepslate_stairs[facing=west,half=bottom]
fill 105 51 -304 129 51 -304 polished_deepslate_stairs[facing=south,half=bottom]
fill 105 51 -278 129 51 -278 polished_deepslate_stairs[facing=north,half=bottom]

# Clear portals in skirting
fill 115 51 -304 119 51 -304 air
fill 115 51 -278 119 51 -278 air
fill 105 51 -293 105 51 -289 air
fill 129 51 -293 129 51 -289 air

# Upper Mezzanine Catwalk at Y: 54
fill 105 54 -304 107 54 -278 dark_oak_planks
fill 127 54 -304 129 54 -278 dark_oak_planks
fill 105 54 -304 129 54 -302 dark_oak_planks
fill 105 54 -280 129 54 -278 dark_oak_planks

fill 108 55 -301 108 55 -281 dark_oak_fence
fill 126 55 -301 126 55 -281 dark_oak_fence
fill 108 55 -301 126 55 -301 dark_oak_fence
fill 108 55 -281 126 55 -281 dark_oak_fence

fill 115 54 -304 119 56 -301 air
fill 115 54 -281 119 56 -278 air
fill 104 54 -293 107 56 -289 air
fill 127 54 -293 130 56 -289 air

fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -292 129 50 -290 stripped_dark_oak_wood[axis=x]

# Grand Corner Pillars
fill 109 50 -299 109 57 -299 stripped_dark_oak_log[axis=y]
setblock 109 50 -299 polished_basalt[axis=y]
setblock 109 54 -299 smooth_quartz
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 125 50 -299 125 57 -299 stripped_dark_oak_log[axis=y]
setblock 125 50 -299 polished_basalt[axis=y]
setblock 125 54 -299 smooth_quartz
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 109 50 -283 109 57 -283 stripped_dark_oak_log[axis=y]
setblock 109 50 -283 polished_basalt[axis=y]
setblock 109 54 -283 smooth_quartz
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

fill 125 50 -283 125 57 -283 stripped_dark_oak_log[axis=y]
setblock 125 50 -283 polished_basalt[axis=y]
setblock 125 54 -283 smooth_quartz
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Sunken Bio-Aquarium Basin (X: 113..121, Z: -295..-287)
fill 113 47 -295 121 47 -287 sea_lantern
fill 114 47 -294 120 47 -288 dark_prismarine
setblock 117 47 -291 sea_lantern

fill 112 48 -296 122 49 -296 polished_deepslate
fill 112 48 -286 122 49 -286 polished_deepslate
fill 112 48 -296 112 49 -286 polished_deepslate
fill 122 48 -296 122 49 -286 polished_deepslate

fill 113 48 -295 121 49 -287 water
fill 113 50 -295 121 50 -287 cyan_stained_glass
fill 116 50 -295 118 50 -287 glass
fill 113 50 -292 121 50 -290 glass

# Downward & Upward Glass Bubble Column Elevators to Celestial Portal Nexus
# Downward Elevator (Magma Block at Y: 37)
fill 114 37 -291 114 50 -291 glass
setblock 114 37 -291 magma_block
fill 114 38 -291 114 50 -291 water

# Upward Elevator (Soul Sand at Y: 37)
fill 120 37 -291 120 50 -291 glass
setblock 120 37 -291 soul_sand
fill 120 38 -291 120 50 -291 water

summon tropical_fish 117 48.5 -291 {PersistenceRequired:1b}
summon tropical_fish 115 48.5 -293 {PersistenceRequired:1b}
summon axolotl 117 48.5 -289 {Variant:0,PersistenceRequired:1b}
