# Subterranean Citadel: Atrium Shell and Architecture
# Main Floor at Y: 50
fill 104 49 -305 130 49 -277 polished_deepslate
fill 105 50 -304 129 50 -278 polished_andesite

# Ceiling Vault Shell at Y: 58
fill 104 58 -305 130 58 -277 deepslate_tiles

# Perimeter Structural Walls
fill 104 50 -305 104 58 -277 deepslate_tiles
fill 130 50 -305 130 58 -277 deepslate_tiles
fill 104 50 -305 130 58 -305 deepslate_tiles
fill 104 50 -277 130 58 -277 deepslate_tiles

# Walkway Ribbons with Dark Oak and Smooth Quartz Borders
fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -292 129 50 -290 stripped_dark_oak_wood[axis=x]

# Grand Corner Structural Pillars (Dark Oak, Basalt, Polished Blackstone)
# Pillar 1 (NW: 109, -299)
fill 109 50 -299 109 57 -299 stripped_dark_oak_log[axis=y]
setblock 109 50 -299 polished_basalt[axis=y]
setblock 109 56 -299 smooth_quartz
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

# Pillar 2 (NE: 125, -299)
fill 125 50 -299 125 57 -299 stripped_dark_oak_log[axis=y]
setblock 125 50 -299 polished_basalt[axis=y]
setblock 125 56 -299 smooth_quartz
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

# Pillar 3 (SW: 109, -283)
fill 109 50 -283 109 57 -283 stripped_dark_oak_log[axis=y]
setblock 109 50 -283 polished_basalt[axis=y]
setblock 109 56 -283 smooth_quartz
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Pillar 4 (SE: 125, -283)
fill 125 50 -283 125 57 -283 stripped_dark_oak_log[axis=y]
setblock 125 50 -283 polished_basalt[axis=y]
setblock 125 56 -283 smooth_quartz
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Sunken Bio-Aquarium Basin at X: 113..121, Z: -295..-287
# Foundation at Y: 47
fill 113 47 -295 121 47 -287 sea_lantern
fill 114 47 -294 120 47 -288 dark_prismarine
setblock 117 47 -291 sea_lantern

# Basin Walls at Y: 48..49
fill 112 48 -296 122 49 -296 polished_deepslate
fill 112 48 -286 122 49 -286 polished_deepslate
fill 112 48 -296 112 49 -286 polished_deepslate
fill 122 48 -296 122 49 -286 polished_deepslate

# Water Layer at Y: 48..49
fill 113 48 -295 121 49 -287 water

# Top Glass Walkway Layer at Y: 50
fill 113 50 -295 121 50 -287 cyan_stained_glass
# Central Crosswalk in Clear Glass
fill 116 50 -295 118 50 -287 glass
fill 113 50 -292 121 50 -290 glass

# Spawn tropical aquatic wildlife into the bio-basin
summon tropical_fish 117 48.5 -291 {PersistenceRequired:1b}
summon tropical_fish 115 48.5 -293 {PersistenceRequired:1b}
summon tropical_fish 119 48.5 -289 {PersistenceRequired:1b}
summon axolotl 117 48.5 -289 {Variant:0,PersistenceRequired:1b}
summon axolotl 115 48.5 -290 {Variant:1,PersistenceRequired:1b}
