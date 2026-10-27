# Subterranean Citadel: Sovereign Residential Suites
fill 92 50 -268 142 58 -231 air
fill 91 49 -269 143 49 -230 polished_deepslate
fill 91 50 -269 143 58 -230 polished_deepslate
fill 91 59 -269 143 59 -230 deepslate_tiles

# Central Corridor (Y=50, Z: -268..-232, X: 115..119)
fill 115 50 -268 119 55 -232 air
fill 116 50 -268 118 50 -232 red_carpet
fill 115 50 -268 115 50 -232 polished_deepslate
fill 119 50 -268 119 50 -232 polished_deepslate
setblock 117 54 -260 lantern[hanging=true]
setblock 117 54 -250 lantern[hanging=true]
setblock 117 54 -240 lantern[hanging=true]

# Suite 1: King Abir Prime Minister Stateroom (South End: Z: -242..-232, X: 110..124)
fill 110 50 -242 124 57 -232 air
fill 110 50 -242 124 50 -232 dark_oak_planks
fill 114 50 -240 120 50 -234 yellow_carpet

# King Abir Grand Canopy Bed (X: 116..118, Z: -234..-232)
fill 116 50 -234 116 53 -234 stripped_dark_oak_log[axis=y]
fill 118 50 -234 118 53 -234 stripped_dark_oak_log[axis=y]
fill 116 50 -232 116 53 -232 stripped_dark_oak_log[axis=y]
fill 118 50 -232 118 53 -232 stripped_dark_oak_log[axis=y]
fill 116 54 -234 118 54 -232 red_carpet
setblock 117 50 -233 red_bed[facing=south,part=head]
setblock 117 50 -234 red_bed[facing=south,part=foot]

setblock 113 50 -234 ender_chest[facing=east]
setblock 121 50 -234 crafting_table

# Executive Writing Desk & Prime Minister Chair
setblock 116 51 -240 dark_oak_slab[type=top]
setblock 117 51 -240 dark_oak_slab[type=top]
setblock 118 51 -240 dark_oak_slab[type=top]
setblock 117 52 -240 lectern[facing=south]
setblock 117 51 -239 dark_oak_stairs[facing=north,half=bottom]

# Prime Minister Custom Trimmed Armor Stand
setblock 112 50 -238 gold_block
summon armor_stand 112 51 -238 {ShowArms:1b,NoBasePlate:1b,Rotation:[90f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:spire"}}}]}

# Suite 2: Ahsane Executive Library Suite (West Wing: X: 93..113, Z: -267..-255)
fill 93 50 -267 113 57 -255 air
fill 93 50 -267 113 50 -255 spruce_planks
fill 98 50 -264 108 50 -258 cyan_carpet

# Ahsane Canopy Bed (X: 95..98, Z: -266..-264)
fill 95 50 -266 95 53 -266 spruce_fence
fill 98 50 -266 98 53 -266 spruce_fence
fill 95 50 -264 95 53 -264 spruce_fence
fill 98 50 -264 98 53 -264 spruce_fence
fill 95 54 -266 98 54 -264 cyan_carpet
setblock 96 50 -265 cyan_bed[facing=west,part=head]
setblock 97 50 -265 cyan_bed[facing=west,part=foot]

# Ahsane Reading Pod with Bookshelves
fill 93 51 -260 93 55 -256 chiseled_bookshelf[facing=east]
setblock 96 51 -258 lectern[facing=west]
setblock 97 51 -258 spruce_stairs[facing=east,half=bottom]

setblock 101 50 -265 lapis_block
summon armor_stand 101 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"trident",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:lapis",pattern:"minecraft:tide"}}}]}

# Suite 3: Jamal Amethyst Sanctuary Suite (East Wing: X: 121..141, Z: -267..-255)
fill 121 50 -267 141 57 -255 air
fill 121 50 -267 141 50 -255 dark_oak_planks
fill 126 50 -264 136 50 -258 purple_carpet

# Jamal Canopy Bed (X: 137..140, Z: -266..-264)
fill 137 50 -266 137 53 -266 dark_oak_fence
fill 140 50 -266 140 53 -266 dark_oak_fence
fill 137 50 -264 137 53 -264 dark_oak_fence
fill 140 50 -264 140 53 -264 dark_oak_fence
fill 137 54 -266 140 54 -264 purple_carpet
setblock 139 50 -265 purple_bed[facing=east,part=head]
setblock 138 50 -265 purple_bed[facing=east,part=foot]

fill 141 50 -262 141 54 -259 amethyst_block
setblock 140 51 -261 amethyst_cluster[facing=west]
setblock 140 52 -260 amethyst_cluster[facing=west]
setblock 140 50 -260 small_amethyst_bud[facing=west]

setblock 134 50 -265 amethyst_block
summon armor_stand 134 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"bow",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:amethyst",pattern:"minecraft:ward"}}}]}
