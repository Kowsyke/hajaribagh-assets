# Subterranean Citadel: Luxury Sovereign Suites (Kowsyke, Ahsane, Jamal)

# =============================================================
# 1. KOWSYKE PRIME MINISTER SUITE (South: X: 111..123, Z: -258..-246)
# =============================================================
fill 110 49 -258 124 49 -245 gilded_blackstone
fill 111 50 -257 123 50 -246 stripped_dark_oak_wood[axis=z]
fill 110 50 -258 110 57 -245 polished_blackstone_bricks
fill 124 50 -258 124 57 -245 polished_blackstone_bricks
fill 110 50 -245 124 57 -245 polished_blackstone_bricks
fill 110 58 -258 124 58 -245 deepslate_tiles

# Royal King Canopy Bed (Gold and Red, X: 116..118, Z: -247..-249)
fill 116 51 -247 118 51 -247 gold_block
fill 116 51 -248 118 51 -248 red_bed[facing=south,part=head]
fill 116 51 -249 118 51 -249 red_bed[facing=south,part=foot]
fill 115 51 -247 115 54 -247 stripped_dark_oak_log[axis=y]
fill 119 51 -247 119 54 -247 stripped_dark_oak_log[axis=y]
fill 115 55 -249 119 55 -247 dark_oak_slab[type=bottom]
fill 116 54 -249 118 54 -249 yellow_wool

# Private Aquarium Wall (West Wall: X: 111, Z: -254..-250)
fill 110 50 -254 110 54 -250 sea_lantern
fill 110 51 -253 110 53 -251 water
fill 111 51 -253 111 53 -251 tinted_glass
summon axolotl 110.5 51.5 -252 {Variant:4,PersistenceRequired:1b}

# Prime Minister Display Pedestal (Gold Silence Trim Netherite Armor)
setblock 121 51 -252 gold_block
summon armor_stand 121 52 -252 {ShowArms:1b,NoBasePlate:1b,Rotation:[270f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:silence"}}}]}

# Private Executive Desk and Safe
setblock 121 51 -255 dark_oak_stairs[facing=south]
setblock 121 51 -256 ender_chest[facing=south]
setblock 120 51 -256 dark_oak_slab[type=top]
setblock 120 52 -256 lantern[hanging=false]

# =============================================================
# 2. AHSANE EXECUTIVE SUITE (West: X: 98..107, Z: -271..-259)
# =============================================================
fill 97 49 -272 108 49 -258 polished_deepslate
fill 98 50 -271 107 50 -259 cyan_carpet
fill 97 50 -272 97 56 -258 deepslate_bricks
fill 97 50 -272 107 56 -272 deepslate_bricks
fill 97 50 -258 107 56 -258 deepslate_bricks
fill 97 57 -272 108 57 -258 deepslate_tiles

# Ahsane Cyan Canopy Bed
fill 98 51 -269 98 54 -269 dark_oak_fence
fill 101 51 -269 101 54 -269 dark_oak_fence
fill 98 51 -267 98 54 -267 dark_oak_fence
fill 101 51 -267 101 54 -267 dark_oak_fence
fill 98 55 -269 101 55 -267 cyan_carpet
setblock 99 51 -268 cyan_bed[facing=west,part=head]
setblock 100 51 -268 cyan_bed[facing=west,part=foot]

# Private Grand Library Alcove
fill 98 51 -261 103 53 -261 bookshelf
setblock 101 51 -263 dark_oak_stairs[facing=north]
setblock 101 51 -262 dark_oak_slab[type=top]

# Ahsane Display Pedestal (Diamond Bolt Trim Armor)
setblock 105 51 -268 diamond_block
summon armor_stand 105 52 -268 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"diamond_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:diamond",pattern:"minecraft:bolt"}}}]}

# =============================================================
# 3. JAMAL EXECUTIVE SUITE (East: X: 127..136, Z: -271..-259)
# =============================================================
fill 126 49 -272 137 49 -258 dark_prismarine
fill 127 50 -271 136 50 -259 purple_carpet
fill 137 50 -272 137 56 -258 deepslate_bricks
fill 127 50 -272 137 56 -272 deepslate_bricks
fill 127 50 -258 137 56 -258 deepslate_bricks
fill 126 57 -272 137 57 -258 deepslate_tiles

# Jamal Purple Canopy Bed
fill 133 51 -269 133 54 -269 dark_oak_fence
fill 136 51 -269 136 54 -269 dark_oak_fence
fill 133 51 -267 133 54 -267 dark_oak_fence
fill 136 51 -267 136 54 -267 dark_oak_fence
fill 133 55 -269 136 55 -267 purple_carpet
setblock 135 51 -268 purple_bed[facing=east,part=head]
setblock 134 51 -268 purple_bed[facing=east,part=foot]

# Resonating Amethyst Geode Wall (East Wall)
fill 136 51 -265 136 54 -262 amethyst_block
setblock 135 52 -264 amethyst_cluster[facing=west]
setblock 135 53 -263 amethyst_cluster[facing=west]
setblock 135 51 -263 small_amethyst_bud[facing=west]

# Jamal Display Pedestal (Amethyst Ward Trim Armor)
setblock 129 51 -268 amethyst_block
summon armor_stand 129 52 -268 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"bow",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:amethyst",pattern:"minecraft:ward"}}}]}
