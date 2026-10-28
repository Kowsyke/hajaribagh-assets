# Cleanup prior decorative entities
kill @e[tag=citadel_decor]
# Sector 0: Central Command Rotunda Detailing
setblock 117 47 -300 dark_oak_stairs[facing=south,half=bottom] replace
setblock 117 47 -302 dark_oak_stairs[facing=north,half=bottom] replace
setblock 116 47 -301 dark_oak_stairs[facing=west,half=bottom] replace
setblock 118 47 -301 dark_oak_stairs[facing=east,half=bottom] replace
setblock 117 47 -301 air replace
setblock 112 47 -302 barrel[facing=east] replace
item replace block 112 47 -302 container.0 with recovery_compass 1
item replace block 112 47 -302 container.1 with clock 1
setblock 112 47 -301 chiseled_polished_blackstone
setblock 112 48 -301 calibrated_sculk_sensor
setblock 122 47 -301 chiseled_polished_blackstone
setblock 122 48 -301 comparator[facing=west]
setblock 111 49 -306 red_wall_banner[facing=south]
setblock 123 49 -306 red_wall_banner[facing=south]
setblock 111 49 -296 red_wall_banner[facing=north]
setblock 123 49 -296 red_wall_banner[facing=north]
setblock 112 47 -305 potted_flowering_azalea_bush replace
setblock 122 47 -305 potted_flowering_azalea_bush replace
# Sector 1: Tool & Equipment Armory Detailing
setblock 75 47 -306 smooth_stone_slab[type=bottom]
setblock 75 48 -306 air
setblock 75 49 -306 air
setblock 75 50 -306 iron_trapdoor[half=bottom]
setblock 75 51 -306 sea_lantern
setblock 75 47 -304 smooth_stone_slab[type=bottom]
setblock 75 48 -304 air
setblock 75 49 -304 air
setblock 75 50 -304 iron_trapdoor[half=bottom]
setblock 75 51 -304 sea_lantern
setblock 75 47 -302 smooth_stone_slab[type=bottom]
setblock 75 48 -302 air
setblock 75 49 -302 air
setblock 75 50 -302 iron_trapdoor[half=bottom]
setblock 75 51 -302 sea_lantern
setblock 75 47 -300 smooth_stone_slab[type=bottom]
setblock 75 48 -300 air
setblock 75 49 -300 air
setblock 75 50 -300 iron_trapdoor[half=bottom]
setblock 75 51 -300 sea_lantern
setblock 75 47 -298 smooth_stone_slab[type=bottom]
setblock 75 48 -298 air
setblock 75 49 -298 air
setblock 75 50 -298 iron_trapdoor[half=bottom]
setblock 75 51 -298 sea_lantern
setblock 75 47 -296 smooth_stone_slab[type=bottom]
setblock 75 48 -296 air
setblock 75 49 -296 air
setblock 75 50 -296 iron_trapdoor[half=bottom]
setblock 75 51 -296 sea_lantern
summon armor_stand 75.5 47.0 -305.5 {Tags:["citadel_decor","armory_stand_1"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}
item replace entity @e[tag=armory_stand_1,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=armory_stand_1,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=armory_stand_1,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=armory_stand_1,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]
item replace entity @e[tag=armory_stand_1,limit=1] weapon.mainhand with netherite_sword[enchantments={"minecraft:sharpness":5,"minecraft:unbreaking":3}]
item replace entity @e[tag=armory_stand_1,limit=1] weapon.offhand with shield
summon armor_stand 75.5 47.0 -303.5 {Tags:["citadel_decor","armory_stand_2"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}
item replace entity @e[tag=armory_stand_2,limit=1] armor.head with diamond_helmet[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=armory_stand_2,limit=1] armor.chest with diamond_chestplate[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=armory_stand_2,limit=1] armor.legs with diamond_leggings[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=armory_stand_2,limit=1] armor.feet with diamond_boots[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=armory_stand_2,limit=1] weapon.mainhand with diamond_axe[enchantments={"minecraft:efficiency":5}]
item replace entity @e[tag=armory_stand_2,limit=1] weapon.offhand with shield
summon armor_stand 75.5 47.0 -301.5 {Tags:["citadel_decor","armory_stand_3"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}
item replace entity @e[tag=armory_stand_3,limit=1] armor.head with golden_helmet[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_3,limit=1] armor.chest with golden_chestplate[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_3,limit=1] armor.legs with golden_leggings[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_3,limit=1] armor.feet with golden_boots[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_3,limit=1] weapon.mainhand with trident[enchantments={"minecraft:loyalty":3}]
item replace entity @e[tag=armory_stand_3,limit=1] weapon.offhand with totem_of_undying
summon armor_stand 75.5 47.0 -299.5 {Tags:["citadel_decor","armory_stand_4"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}
item replace entity @e[tag=armory_stand_4,limit=1] armor.head with iron_helmet[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_4,limit=1] armor.chest with iron_chestplate[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_4,limit=1] armor.legs with iron_leggings[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_4,limit=1] armor.feet with iron_boots[enchantments={"minecraft:protection":3}]
item replace entity @e[tag=armory_stand_4,limit=1] weapon.mainhand with crossbow[enchantments={"minecraft:quick_charge":3}]
item replace entity @e[tag=armory_stand_4,limit=1] weapon.offhand with shield
summon armor_stand 75.5 47.0 -297.5 {Tags:["citadel_decor","armory_stand_5"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}
item replace entity @e[tag=armory_stand_5,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:blast_protection":4}]
item replace entity @e[tag=armory_stand_5,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:blast_protection":4}]
item replace entity @e[tag=armory_stand_5,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:blast_protection":4}]
item replace entity @e[tag=armory_stand_5,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:feather_falling":4}]
item replace entity @e[tag=armory_stand_5,limit=1] weapon.mainhand with mace[enchantments={"minecraft:density":5}]
item replace entity @e[tag=armory_stand_5,limit=1] weapon.offhand with shield
summon armor_stand 75.5 47.0 -295.5 {Tags:["citadel_decor","armory_stand_6"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}
item replace entity @e[tag=armory_stand_6,limit=1] armor.head with diamond_helmet[enchantments={"minecraft:projectile_protection":4}]
item replace entity @e[tag=armory_stand_6,limit=1] armor.chest with diamond_chestplate[enchantments={"minecraft:projectile_protection":4}]
item replace entity @e[tag=armory_stand_6,limit=1] armor.legs with diamond_leggings[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=armory_stand_6,limit=1] armor.feet with diamond_boots[enchantments={"minecraft:depth_strider":3}]
item replace entity @e[tag=armory_stand_6,limit=1] weapon.mainhand with bow[enchantments={"minecraft:power":5,"minecraft:flame":1}]
item replace entity @e[tag=armory_stand_6,limit=1] weapon.offhand with spectral_arrow
setblock 86 47 -306 chest[facing=south,type=right] replace
setblock 87 47 -306 chest[facing=south,type=left] replace
setblock 88 47 -306 chest[facing=south,type=right] replace
setblock 89 47 -306 chest[facing=south,type=left] replace
setblock 90 47 -306 chest[facing=south,type=right] replace
setblock 91 47 -306 chest[facing=south,type=left] replace
setblock 92 47 -306 deepslate_brick_wall replace
setblock 86 48 -306 chest[facing=south,type=right] replace
setblock 87 48 -306 chest[facing=south,type=left] replace
setblock 88 48 -306 chest[facing=south,type=right] replace
setblock 89 48 -306 chest[facing=south,type=left] replace
setblock 90 48 -306 chest[facing=south,type=right] replace
setblock 91 48 -306 chest[facing=south,type=left] replace
setblock 92 48 -306 deepslate_brick_wall replace
item replace block 86 48 -306 container.0 with netherite_pickaxe 1
item replace block 86 48 -306 container.1 with netherite_axe 1
item replace block 86 48 -306 container.2 with netherite_shovel 1
item replace block 88 48 -306 container.0 with diamond_sword 1
item replace block 88 48 -306 container.1 with trident 1
item replace block 88 48 -306 container.2 with mace 1
item replace block 86 47 -306 container.0 with bow 1
item replace block 86 47 -306 container.1 with crossbow 1
item replace block 86 47 -306 container.2 with shield 1
item replace block 88 47 -306 container.0 with elytra 1
item replace block 88 47 -306 container.1 with spyglass 1
item replace block 88 47 -306 container.2 with clock 1
setblock 85 47 -306 chest[facing=south] replace
item replace block 85 47 -306 container.0 with netherite_upgrade_smithing_template 2
item replace block 85 47 -306 container.1 with netherite_ingot 8
item replace block 85 47 -306 container.2 with diamond 16
item replace block 85 47 -306 container.3 with iron_ingot 32
item replace block 85 47 -306 container.4 with ender_eye 12
# Sector 2: Blacksmith & Smelting Workshop Detailing
setblock 89 46 -283 campfire[lit=true] replace
setblock 89 47 -283 water_cauldron[level=3] replace
setblock 89 46 -281 campfire[lit=true] replace
setblock 89 47 -281 water_cauldron[level=3] replace
fill 82 46 -285 86 46 -281 chiseled_polished_blackstone
setblock 84 46 -283 lava
setblock 84 47 -283 lava
setblock 84 48 -283 lava
fill 83 47 -284 85 48 -282 tinted_glass
fill 82 47 -285 86 48 -285 iron_bars
fill 82 47 -281 86 48 -281 iron_bars
fill 82 47 -285 82 48 -281 iron_bars
fill 86 47 -285 86 48 -281 iron_bars
fill 83 49 -284 85 49 -282 iron_bars
setblock 92 47 -288 raw_iron_block replace
setblock 92 48 -288 raw_iron_block replace
setblock 92 47 -287 iron_block replace
setblock 92 47 -286 raw_gold_block replace
setblock 92 47 -285 gold_block replace
setblock 92 47 -284 raw_copper_block replace
setblock 91 47 -288 barrel[facing=west] replace
item replace block 91 47 -288 container.0 with iron_ingot 64
item replace block 91 47 -288 container.1 with raw_iron 64
item replace block 91 47 -288 container.2 with gold_ingot 64
item replace block 91 47 -288 container.3 with raw_gold 64
item replace block 91 47 -288 container.4 with copper_ingot 64
item replace block 91 47 -288 container.5 with netherite_ingot 4
item replace block 91 47 -288 container.6 with heavy_core 1
# Sector 3: Grand Arcane Library Detailing
setblock 144 47 -304 end_rod[facing=up] replace
setblock 144 48 -304 lectern[facing=east,has_book=true] replace
data modify block 144 48 -304 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Hivemind Citadel Genesis",pages:["Registered in the royal archives of the Citadel."]}}}
setblock 144 47 -298 end_rod[facing=up] replace
setblock 144 48 -298 lectern[facing=east,has_book=true] replace
data modify block 144 48 -298 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Citadel Vault Protocols",pages:["Registered in the royal archives of the Citadel."]}}}
setblock 156 47 -304 end_rod[facing=up] replace
setblock 156 48 -304 lectern[facing=west,has_book=true] replace
data modify block 156 48 -304 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Redstone Engineering Lexicon",pages:["Registered in the royal archives of the Citadel."]}}}
setblock 156 47 -298 end_rod[facing=up] replace
setblock 156 48 -298 lectern[facing=west,has_book=true] replace
data modify block 156 48 -298 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Ancient Glyphs & Arcane Enigmas",pages:["Registered in the royal archives of the Citadel."]}}}
setblock 144 47 -301 dark_oak_stairs[facing=east,half=bottom] replace
setblock 145 47 -301 dark_oak_slab[type=bottom] replace
setblock 156 47 -301 dark_oak_stairs[facing=west,half=bottom] replace
setblock 155 47 -301 dark_oak_slab[type=bottom] replace
setblock 145 48 -301 candle[candles=3,lit=true] replace
setblock 155 48 -301 purple_candle[candles=3,lit=true] replace
setblock 142 48 -305 candle[candles=4,lit=true] replace
setblock 158 48 -305 purple_candle[candles=4,lit=true] replace
setblock 142 48 -297 candle[candles=4,lit=true] replace
setblock 158 48 -297 purple_candle[candles=4,lit=true] replace
setblock 147 47 -301 chiseled_bookshelf[facing=south] replace
item replace block 147 47 -301 container.0 with enchanted_book[stored_enchantments={"minecraft:mending":1}]
item replace block 147 47 -301 container.1 with enchanted_book[stored_enchantments={"minecraft:unbreaking":3}]
item replace block 147 47 -301 container.2 with enchanted_book[stored_enchantments={"minecraft:fortune":3}]
item replace block 147 47 -301 container.3 with enchanted_book[stored_enchantments={"minecraft:silk_touch":1}]
item replace block 147 47 -301 container.4 with enchanted_book[stored_enchantments={"minecraft:efficiency":5}]
item replace block 147 47 -301 container.5 with enchanted_book[stored_enchantments={"minecraft:infinity":1}]
# Sector 4: Brewing & Alchemy Laboratory Detailing
setblock 159 47 -283 water_cauldron[level=3] replace
setblock 158 47 -283 water_cauldron[level=3] replace
setblock 159 48 -285 brewing_stand replace
setblock 159 48 -284 brewing_stand replace
setblock 159 48 -282 brewing_stand replace
setblock 159 48 -281 brewing_stand replace
item replace block 159 48 -285 container.4 with blaze_powder 64
item replace block 159 48 -284 container.4 with blaze_powder 64
setblock 158 47 -285 barrel[facing=west] replace
item replace block 158 47 -285 container.0 with nether_wart 64
item replace block 158 47 -285 container.1 with blaze_powder 64
item replace block 158 47 -285 container.2 with ghast_tear 16
item replace block 158 47 -285 container.3 with glistering_melon_slice 64
item replace block 158 47 -285 container.4 with fermented_spider_eye 64
# Sector 5: Underground Farm & Botany Pod Detailing
setblock 99 46 -273 campfire[lit=true] replace
setblock 99 48 -273 bee_nest[facing=east,honey_level=5] replace
setblock 103 46 -273 campfire[lit=true] replace
setblock 103 48 -273 bee_nest[facing=west,honey_level=5] replace
setblock 112 47 -268 chest[facing=west,type=right] replace
setblock 112 47 -267 chest[facing=west,type=left] replace
item replace block 112 47 -268 container.0 with golden_carrot 64
item replace block 112 47 -268 container.1 with wheat 64
item replace block 112 47 -268 container.2 with diamond_hoe[unbreakable={}]
# Sector 6: Modern Subterranean Housing Detailing
setblock 136 47 -289 red_bed[facing=north,part=head] replace
setblock 136 47 -288 red_bed[facing=north,part=foot] replace
setblock 135 47 -289 red_bed[facing=north,part=head] replace
setblock 135 47 -288 red_bed[facing=north,part=foot] replace
setblock 134 47 -289 stripped_spruce_log replace
setblock 134 48 -289 potted_fern replace
setblock 137 47 -289 stripped_spruce_log replace
setblock 137 48 -289 potted_flowering_azalea_bush replace
setblock 131 46 -290 smooth_quartz replace
setblock 132 46 -290 smooth_quartz replace
setblock 133 46 -290 smooth_quartz replace
setblock 131 47 -290 smooth_quartz replace
setblock 132 47 -290 barrel[facing=south] replace
setblock 133 47 -290 smooth_quartz replace
setblock 131 48 -290 air replace
setblock 132 48 -290 barrel[facing=south] replace
setblock 133 48 -290 air replace
setblock 131 49 -290 smooth_quartz_slab[type=bottom] replace
setblock 132 49 -290 smooth_quartz_slab[type=bottom] replace
setblock 133 49 -290 smooth_quartz_slab[type=bottom] replace
setblock 131 47 -289 spruce_trapdoor[facing=south,half=bottom,open=true] replace
setblock 133 47 -289 spruce_trapdoor[facing=south,half=bottom,open=true] replace
summon armor_stand 131.5 48.0 -289.8 {Tags:["citadel_decor","housing_wardrobe_1"],ShowArms:1b,NoBasePlate:1b,Rotation:[0.0f,0.0f]}
item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.head with golden_helmet
item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.chest with diamond_chestplate
item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.legs with golden_leggings
item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.feet with netherite_boots
summon armor_stand 133.5 48.0 -289.8 {Tags:["citadel_decor","housing_wardrobe_2"],ShowArms:1b,NoBasePlate:1b,Rotation:[0.0f,0.0f]}
item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.head with turtle_helmet
item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.chest with netherite_chestplate
item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.legs with diamond_leggings
item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.feet with diamond_boots
fill 135 47 -274 137 49 -274 bricks replace
setblock 136 47 -274 netherrack replace
setblock 136 48 -274 fire replace
fill 135 48 -273 137 48 -273 iron_bars replace
fill 136 49 -274 136 53 -274 bricks replace
fill 131 47 -275 131 47 -271 smooth_quartz_stairs[facing=east,half=bottom] replace
setblock 131 47 -276 smooth_quartz_stairs[facing=south,half=bottom] replace
setblock 131 47 -270 smooth_quartz_stairs[facing=north,half=bottom] replace
setblock 133 47 -273 smooth_stone_slab[type=bottom] replace
setblock 133 47 -272 smooth_stone_slab[type=bottom] replace
setblock 133 48 -273 potted_fern replace
setblock 133 48 -272 candle[candles=2,lit=true] replace
summon painting 125 48 -281 {Tags:["citadel_decor","housing_art"],facing:3b,variant:"minecraft:plant"}
summon painting 137 48 -277 {Tags:["citadel_decor","housing_art"],facing:4b,variant:"minecraft:wasteland"}
setblock 121 47 -275 smoker[facing=east] replace
setblock 121 48 -275 hopper[facing=down] replace
fill 121 49 -275 121 52 -275 polished_deepslate_wall replace
setblock 121 53 -275 deepslate_tiles replace
setblock 121 47 -274 water_cauldron[level=3] replace
setblock 121 48 -274 tripwire_hook[facing=east] replace
setblock 121 47 -273 barrel[facing=east] replace
setblock 121 47 -272 barrel[facing=east] replace
setblock 121 47 -271 brewing_stand replace
fill 123 47 -274 123 47 -270 smooth_quartz replace
setblock 123 48 -274 heavy_weighted_pressure_plate replace
setblock 123 48 -273 flower_pot replace
setblock 123 48 -272 cake[bites=0] replace
setblock 123 48 -271 flower_pot replace
setblock 123 48 -270 heavy_weighted_pressure_plate replace
setblock 125 47 -274 smooth_quartz_stairs[facing=west,half=bottom] replace
setblock 125 47 -272 smooth_quartz_stairs[facing=west,half=bottom] replace
setblock 125 47 -270 smooth_quartz_stairs[facing=west,half=bottom] replace
setblock 122 47 -289 cyan_bed[facing=north,part=head] replace
setblock 122 47 -288 cyan_bed[facing=north,part=foot] replace
setblock 124 47 -289 purple_bed[facing=north,part=head] replace
setblock 124 47 -288 purple_bed[facing=north,part=foot] replace
setblock 123 47 -289 stripped_spruce_log replace
setblock 123 48 -289 potted_fern replace
# Sector 7: King's Council & High Parliament Detailing
setblock 112 47 -256 dark_oak_stairs[facing=east,half=bottom] replace
setblock 111 48 -256 dark_oak_stairs[facing=east,half=bottom] replace
setblock 112 47 -254 dark_oak_stairs[facing=east,half=bottom] replace
setblock 111 48 -254 dark_oak_stairs[facing=east,half=bottom] replace
setblock 112 47 -252 dark_oak_stairs[facing=east,half=bottom] replace
setblock 111 48 -252 dark_oak_stairs[facing=east,half=bottom] replace
setblock 112 47 -250 dark_oak_stairs[facing=east,half=bottom] replace
setblock 111 48 -250 dark_oak_stairs[facing=east,half=bottom] replace
setblock 112 47 -248 dark_oak_stairs[facing=east,half=bottom] replace
setblock 111 48 -248 dark_oak_stairs[facing=east,half=bottom] replace
setblock 112 47 -246 dark_oak_stairs[facing=east,half=bottom] replace
setblock 111 48 -246 dark_oak_stairs[facing=east,half=bottom] replace
fill 113 47 -256 113 47 -246 dark_oak_slab[type=top] replace
setblock 113 48 -256 polished_blackstone_button[face=floor] replace
setblock 113 48 -254 polished_blackstone_button[face=floor] replace
setblock 113 48 -252 polished_blackstone_button[face=floor] replace
setblock 113 48 -250 polished_blackstone_button[face=floor] replace
setblock 113 48 -248 polished_blackstone_button[face=floor] replace
setblock 113 48 -246 polished_blackstone_button[face=floor] replace
setblock 122 47 -256 dark_oak_stairs[facing=west,half=bottom] replace
setblock 123 48 -256 dark_oak_stairs[facing=west,half=bottom] replace
setblock 122 47 -254 dark_oak_stairs[facing=west,half=bottom] replace
setblock 123 48 -254 dark_oak_stairs[facing=west,half=bottom] replace
setblock 122 47 -252 dark_oak_stairs[facing=west,half=bottom] replace
setblock 123 48 -252 dark_oak_stairs[facing=west,half=bottom] replace
setblock 122 47 -250 dark_oak_stairs[facing=west,half=bottom] replace
setblock 123 48 -250 dark_oak_stairs[facing=west,half=bottom] replace
setblock 122 47 -248 dark_oak_stairs[facing=west,half=bottom] replace
setblock 123 48 -248 dark_oak_stairs[facing=west,half=bottom] replace
setblock 122 47 -246 dark_oak_stairs[facing=west,half=bottom] replace
setblock 123 48 -246 dark_oak_stairs[facing=west,half=bottom] replace
fill 121 47 -256 121 47 -246 dark_oak_slab[type=top] replace
setblock 121 48 -256 polished_blackstone_button[face=floor] replace
setblock 121 48 -254 polished_blackstone_button[face=floor] replace
setblock 121 48 -252 polished_blackstone_button[face=floor] replace
setblock 121 48 -250 polished_blackstone_button[face=floor] replace
setblock 121 48 -248 polished_blackstone_button[face=floor] replace
setblock 121 48 -246 polished_blackstone_button[face=floor] replace
fill 116 47 -243 118 47 -243 dark_oak_slab[type=top] replace
setblock 117 47 -242 lectern[facing=north,has_book=true] replace
data modify block 117 47 -242 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Parliament Standing Orders",pages:["Decrees and rules of debate for the High Parliament."]}}}
setblock 116 48 -243 chest[facing=north] replace
data modify block 116 48 -243 custom_name set value '{"text":"Government Dispatch Box","color":"gold"}'
setblock 118 48 -243 chest[facing=north] replace
data modify block 118 48 -243 custom_name set value '{"text":"Opposition Dispatch Box","color":"gold"}'
setblock 107 46 -259 gilded_blackstone replace
summon armor_stand 107.5 47.0 -259.5 {Tags:["citadel_decor","parliament_guard_nw"],ShowArms:1b,NoBasePlate:1b,Rotation:[135.0f,0.0f]}
item replace entity @e[tag=parliament_guard_nw,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_nw,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_nw,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_nw,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_nw,limit=1] weapon.mainhand with trident[enchantments={"minecraft:loyalty":3}]
item replace entity @e[tag=parliament_guard_nw,limit=1] weapon.offhand with shield
setblock 126 46 -259 gilded_blackstone replace
summon armor_stand 126.5 47.0 -259.5 {Tags:["citadel_decor","parliament_guard_ne"],ShowArms:1b,NoBasePlate:1b,Rotation:[225.0f,0.0f]}
item replace entity @e[tag=parliament_guard_ne,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_ne,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_ne,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_ne,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_ne,limit=1] weapon.mainhand with trident[enchantments={"minecraft:loyalty":3}]
item replace entity @e[tag=parliament_guard_ne,limit=1] weapon.offhand with shield
setblock 107 46 -238 gilded_blackstone replace
summon armor_stand 107.5 47.0 -238.5 {Tags:["citadel_decor","parliament_guard_sw"],ShowArms:1b,NoBasePlate:1b,Rotation:[45.0f,0.0f]}
item replace entity @e[tag=parliament_guard_sw,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_sw,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_sw,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_sw,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_sw,limit=1] weapon.mainhand with trident[enchantments={"minecraft:loyalty":3}]
item replace entity @e[tag=parliament_guard_sw,limit=1] weapon.offhand with shield
setblock 126 46 -238 gilded_blackstone replace
summon armor_stand 126.5 47.0 -238.5 {Tags:["citadel_decor","parliament_guard_se"],ShowArms:1b,NoBasePlate:1b,Rotation:[315.0f,0.0f]}
item replace entity @e[tag=parliament_guard_se,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_se,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_se,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_se,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4}]
item replace entity @e[tag=parliament_guard_se,limit=1] weapon.mainhand with trident[enchantments={"minecraft:loyalty":3}]
item replace entity @e[tag=parliament_guard_se,limit=1] weapon.offhand with shield
fill 108 51 -260 115 51 -260 red_wall_banner[facing=south] replace
fill 119 51 -260 126 51 -260 red_wall_banner[facing=south] replace
fill 108 51 -236 126 51 -236 red_wall_banner[facing=north] replace
fill 106 51 -258 106 51 -238 red_wall_banner[facing=east] replace
fill 128 51 -258 128 51 -238 red_wall_banner[facing=west] replace
