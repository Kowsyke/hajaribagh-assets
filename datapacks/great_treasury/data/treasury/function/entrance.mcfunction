# The Great Treasury: Organic Tree Root Entrance Stairwell
# Connecting Y: 80 down to Y: 65 along corridor Z = -333 to -328
fill 115 65 -333 119 75 -329 air
fill 114 64 -333 120 64 -329 spruce_planks
fill 114 65 -333 114 74 -329 mud_bricks
fill 120 65 -333 120 74 -329 mud_bricks

# Gentle Steps descending from tree base
fill 116 79 -330 118 79 -330 spruce_stairs[facing=south,half=bottom]
fill 116 78 -331 118 78 -331 spruce_planks
fill 116 77 -331 118 77 -331 spruce_stairs[facing=south,half=bottom]
fill 116 76 -332 118 76 -332 spruce_planks
fill 116 75 -332 118 75 -332 spruce_stairs[facing=south,half=bottom]
fill 116 74 -333 118 74 -333 spruce_planks
fill 116 73 -333 118 73 -333 spruce_stairs[facing=south,half=bottom]
fill 116 72 -334 118 72 -334 spruce_planks
fill 116 71 -334 118 71 -334 spruce_stairs[facing=south,half=bottom]
fill 116 70 -334 118 70 -334 spruce_planks
fill 116 69 -333 118 69 -333 spruce_stairs[facing=north,half=bottom]
fill 116 68 -332 118 68 -332 spruce_planks
fill 116 67 -331 118 67 -331 spruce_stairs[facing=south,half=bottom]
fill 116 66 -330 118 66 -330 spruce_planks
fill 116 65 -329 118 65 -329 spruce_stairs[facing=south,half=bottom]
fill 115 64 -328 119 64 -327 spruce_planks

# Grand Circular Hobbit Portal Doorway at Z = -328
# Circular ring of Stripped Dark Oak Wood
setblock 115 65 -328 stripped_dark_oak_wood
setblock 119 65 -328 stripped_dark_oak_wood
setblock 114 66 -328 stripped_dark_oak_wood
setblock 120 66 -328 stripped_dark_oak_wood
setblock 114 67 -328 stripped_dark_oak_wood
setblock 120 67 -328 stripped_dark_oak_wood
setblock 115 68 -328 stripped_dark_oak_wood
setblock 119 68 -328 stripped_dark_oak_wood
fill 116 69 -328 118 69 -328 stripped_dark_oak_wood
setblock 117 68 -328 lantern[hanging=true]

# Tree Roots Entangled in Stone Walls
setblock 115 66 -329 stripped_oak_wood[axis=y]
setblock 115 67 -330 stripped_oak_wood[axis=y]
setblock 119 66 -329 stripped_oak_wood[axis=y]
setblock 119 67 -330 stripped_oak_wood[axis=y]
setblock 115 65 -330 rooted_dirt
setblock 119 65 -330 rooted_dirt
