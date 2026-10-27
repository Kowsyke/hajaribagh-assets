# Subterranean Citadel: Luxury Sovereign Suites (Kowsyke, Ahsane, Jamal)

# =============================================================
# 1. KOWSYKE PRIME MINISTER SUITE (Behind Parliament Dais: X: 111..123, Z: -243..-232)
# =============================================================
fill 110 49 -244 124 57 -231 air
fill 110 48 -244 124 48 -231 gilded_blackstone
fill 111 49 -243 123 49 -232 stripped_dark_oak_wood[axis=z]
fill 110 49 -244 110 57 -231 polished_blackstone_bricks
fill 124 49 -244 124 57 -231 polished_blackstone_bricks
fill 110 49 -231 124 57 -231 polished_blackstone_bricks
fill 110 58 -244 124 58 -231 deepslate_tiles

# Private Entrance Doorway from behind Speaker Dais (Z: -244, X: 116..118)
fill 116 49 -244 118 53 -244 air
fill 116 49 -244 118 49 -244 gold_block

# Royal King Canopy Bed (Gold and Red, X: 116..118, Z: -233..-235)
fill 116 50 -233 118 50 -233 gold_block
fill 116 50 -234 118 50 -234 red_bed[facing=south,part=head]
fill 116 50 -235 118 50 -235 red_bed[facing=south,part=foot]
fill 115 50 -233 115 54 -233 stripped_dark_oak_log[axis=y]
fill 119 50 -233 119 54 -233 stripped_dark_oak_log[axis=y]
fill 115 55 -235 119 55 -233 dark_oak_slab[type=bottom]
fill 116 54 -235 118 54 -235 yellow_wool

# Private Aquarium Wall (West Wall: X: 111, Z: -240..-236)
fill 110 49 -240 110 54 -236 sea_lantern
fill 110 50 -239 110 53 -237 water
fill 111 50 -239 111 53 -237 tinted_glass
summon axolotl 110.5 50.5 -238 {Variant:4,PersistenceRequired:1b}

# Prime Minister Display Pedestal (Gold Silence Trim Netherite Armor)
setblock 121 50 -238 gold_block
summon armor_stand 121 51 -238 {ShowArms:1b,NoBasePlate:1b,Rotation:[270f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:silence"}}}]}

# Private Executive Desk and Safe
setblock 121 50 -241 dark_oak_stairs[facing=south]
setblock 121 50 -242 ender_chest[facing=south]
setblock 120 50 -242 dark_oak_slab[type=top]
setblock 120 51 -242 lantern[hanging=false]

# =============================================================
# 2. AHSANE EXECUTIVE SUITE (West Flank of Parliament: X: 93..103, Z: -268..-256)
# =============================================================
fill 92 49 -269 104 57 -255 air
fill 92 48 -269 104 48 -255 polished_deepslate
fill 93 49 -268 103 49 -256 cyan_carpet
fill 92 49 -269 92 57 -255 deepslate_bricks
fill 92 49 -269 103 57 -269 deepslate_bricks
fill 92 49 -255 103 57 -255 deepslate_bricks
fill 92 58 -269 104 58 -255 deepslate_tiles

# Entrance Doorway from Parliament West Side
fill 103 49 -263 104 53 -261 air

# Ahsane Cyan Canopy Bed
fill 94 50 -266 94 53 -266 dark_oak_fence
fill 97 50 -266 97 53 -266 dark_oak_fence
fill 94 50 -264 94 53 -264 dark_oak_fence
fill 97 50 -264 97 53 -264 dark_oak_fence
fill 94 54 -266 97 54 -264 cyan_carpet
setblock 95 50 -265 cyan_bed[facing=west,part=head]
setblock 96 50 -265 cyan_bed[facing=west,part=foot]

# Private Grand Library Alcove
fill 93 50 -258 98 53 -258 bookshelf
setblock 96 50 -260 dark_oak_stairs[facing=north]
setblock 96 50 -259 dark_oak_slab[type=top]

# Ahsane Display Pedestal (Diamond Bolt Trim Armor)
setblock 100 50 -265 diamond_block
summon armor_stand 100 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"diamond_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:diamond",pattern:"minecraft:bolt"}}}]}

# =============================================================
# 3. JAMAL EXECUTIVE SUITE (East Flank of Parliament: X: 131..141, Z: -268..-256)
# =============================================================
fill 130 49 -269 142 57 -255 air
fill 130 48 -269 142 48 -255 dark_prismarine
fill 131 49 -268 141 49 -256 purple_carpet
fill 142 49 -269 142 57 -255 deepslate_bricks
fill 131 49 -269 142 57 -269 deepslate_bricks
fill 131 49 -255 142 57 -255 deepslate_bricks
fill 130 58 -269 142 58 -255 deepslate_tiles

# Entrance Doorway from Parliament East Side
fill 130 49 -263 131 53 -261 air

# Jamal Purple Canopy Bed
fill 137 50 -266 137 53 -266 dark_oak_fence
fill 140 50 -266 140 53 -266 dark_oak_fence
fill 137 50 -264 137 53 -264 dark_oak_fence
fill 140 50 -264 140 53 -264 dark_oak_fence
fill 137 54 -266 140 54 -264 purple_carpet
setblock 139 50 -265 purple_bed[facing=east,part=head]
setblock 138 50 -265 purple_bed[facing=east,part=foot]

# Resonating Amethyst Geode Wall (East Wall)
fill 141 50 -262 141 54 -259 amethyst_block
setblock 140 51 -261 amethyst_cluster[facing=west]
setblock 140 52 -260 amethyst_cluster[facing=west]
setblock 140 50 -260 small_amethyst_bud[facing=west]

# Jamal Display Pedestal (Amethyst Ward Trim Armor)
setblock 134 50 -265 amethyst_block
summon armor_stand 134 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"bow",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:amethyst",pattern:"minecraft:ward"}}}]}
