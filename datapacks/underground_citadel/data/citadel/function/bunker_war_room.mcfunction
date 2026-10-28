# Sector 13: Subterranean War Room & Strategic Cartography Command (X: 111..123, Z: -320..-308, Y: 46..53)
kill @e[tag=war_vanguard_nw]
kill @e[tag=war_vanguard_ne]
kill @e[tag=war_vanguard_sw]
kill @e[tag=war_vanguard_se]
kill @e[tag=war_room_entity]
fill 111 46 -320 123 52 -308 air
fill 111 46 -320 123 46 -308 polished_deepslate
fill 113 46 -318 121 46 -310 deepslate_tiles
fill 111 53 -320 123 53 -308 deepslate_tiles
fill 111 46 -320 123 52 -320 deepslate_bricks
fill 111 46 -308 123 52 -308 deepslate_bricks
fill 111 46 -320 111 52 -308 deepslate_bricks
fill 123 46 -320 123 52 -308 deepslate_bricks
fill 111 46 -320 111 52 -320 chiseled_deepslate
fill 123 46 -320 123 52 -320 chiseled_deepslate
fill 111 46 -308 111 52 -308 chiseled_deepslate
fill 123 46 -308 123 52 -308 chiseled_deepslate
fill 116 47 -320 118 51 -320 air
fill 116 47 -308 118 51 -308 air
fill 115 46 -316 119 46 -312 sea_lantern replace
fill 115 47 -316 119 47 -316 dark_oak_stairs[facing=south,half=bottom] replace
fill 115 47 -312 119 47 -312 dark_oak_stairs[facing=north,half=bottom] replace
fill 115 47 -315 115 47 -313 dark_oak_stairs[facing=east,half=bottom] replace
fill 119 47 -315 119 47 -313 dark_oak_stairs[facing=west,half=bottom] replace
setblock 115 47 -316 dark_oak_planks replace
setblock 119 47 -316 dark_oak_planks replace
setblock 115 47 -312 dark_oak_planks replace
setblock 119 47 -312 dark_oak_planks replace
setblock 116 47 -315 lime_stained_glass replace
setblock 117 47 -315 yellow_stained_glass replace
setblock 118 47 -315 lime_stained_glass replace
setblock 116 47 -314 light_blue_stained_glass replace
setblock 117 47 -314 yellow_stained_glass replace
setblock 118 47 -314 light_blue_stained_glass replace
setblock 116 47 -313 lime_stained_glass replace
setblock 117 47 -313 yellow_stained_glass replace
setblock 118 47 -313 lime_stained_glass replace
setblock 121 46 -317 chiseled_polished_blackstone replace
setblock 121 47 -317 waxed_copper_grate replace
setblock 121 48 -317 lightning_rod[facing=up] replace
setblock 121 49 -317 iron_bars replace
setblock 121 50 -317 iron_bars replace
setblock 121 51 -317 lightning_rod[facing=down] replace
setblock 121 52 -317 end_rod[facing=up] replace
setblock 121 53 -317 tinted_glass replace
setblock 114 46 -317 gilded_blackstone replace
summon armor_stand 114.5 47.0 -316.5 {Tags:["citadel_decor","war_vanguard_nw"],ShowArms:1b,NoBasePlate:1b,Rotation:[135.0f,0.0f]}
item replace entity @e[tag=war_vanguard_nw,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_nw,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_nw,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_nw,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]
item replace entity @e[tag=war_vanguard_nw,limit=1] weapon.mainhand with netherite_sword[enchantments={"minecraft:sharpness":5}]
item replace entity @e[tag=war_vanguard_nw,limit=1] weapon.offhand with spyglass
setblock 120 46 -317 gilded_blackstone replace
summon armor_stand 119.5 47.0 -316.5 {Tags:["citadel_decor","war_room_entity","war_vanguard_ne"],ShowArms:1b,NoBasePlate:1b,Rotation:[225.0f,0.0f]}
item replace entity @e[tag=war_vanguard_ne,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_ne,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_ne,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_ne,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]
item replace entity @e[tag=war_vanguard_ne,limit=1] weapon.mainhand with netherite_sword[enchantments={"minecraft:sharpness":5}]
item replace entity @e[tag=war_vanguard_ne,limit=1] weapon.offhand with shield
setblock 114 46 -311 gilded_blackstone replace
summon armor_stand 114.5 47.0 -311.5 {Tags:["citadel_decor","war_room_entity","war_vanguard_sw"],ShowArms:1b,NoBasePlate:1b,Rotation:[45.0f,0.0f]}
item replace entity @e[tag=war_vanguard_sw,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_sw,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_sw,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_sw,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]
item replace entity @e[tag=war_vanguard_sw,limit=1] weapon.mainhand with netherite_sword[enchantments={"minecraft:sharpness":5}]
item replace entity @e[tag=war_vanguard_sw,limit=1] weapon.offhand with shield
setblock 120 46 -311 gilded_blackstone replace
summon armor_stand 119.5 47.0 -311.5 {Tags:["citadel_decor","war_room_entity","war_vanguard_se"],ShowArms:1b,NoBasePlate:1b,Rotation:[315.0f,0.0f]}
item replace entity @e[tag=war_vanguard_se,limit=1] armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_se,limit=1] armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_se,limit=1] armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]
item replace entity @e[tag=war_vanguard_se,limit=1] armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]
item replace entity @e[tag=war_vanguard_se,limit=1] weapon.mainhand with netherite_sword[enchantments={"minecraft:sharpness":5}]
item replace entity @e[tag=war_vanguard_se,limit=1] weapon.offhand with shield
setblock 113 47 -314 lectern[facing=east,has_book=true] replace
data modify block 113 47 -314 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Royal War Directives",pages:["Official military orders of King Abir."]}}}
setblock 121 47 -314 lectern[facing=west,has_book=true] replace
data modify block 121 47 -314 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Citadel Defense Plan",pages:["Official military orders of King Abir."]}}}
setblock 114 47 -318 lectern[facing=south,has_book=true] replace
data modify block 114 47 -318 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Frontier Cartography",pages:["Official military orders of King Abir."]}}}
setblock 120 47 -310 lectern[facing=north,has_book=true] replace
data modify block 120 47 -310 Book set value {id:"minecraft:written_book",count:1,components:{"minecraft:written_book_content":{author:"King Abir",title:"Bunker Perimeter Alert",pages:["Official military orders of King Abir."]}}}
setblock 112 47 -315 chiseled_polished_blackstone replace
setblock 112 48 -315 calibrated_sculk_sensor replace
setblock 112 47 -314 polished_blackstone replace
setblock 112 48 -314 comparator[facing=east] replace
setblock 112 47 -313 chiseled_polished_blackstone replace
setblock 112 48 -313 redstone_lamp replace
setblock 113 47 -316 chest[facing=east] replace
item replace block 113 47 -316 container.0 with recovery_compass 1
item replace block 113 47 -316 container.1 with clock 1
item replace block 113 47 -316 container.2 with compass 1
item replace block 113 47 -316 container.3 with spyglass 1
item replace block 113 47 -316 container.4 with filled_map 1
setblock 112 49 -318 red_wall_banner[facing=east] replace
setblock 112 49 -310 red_wall_banner[facing=east] replace
setblock 122 49 -318 red_wall_banner[facing=west] replace
setblock 122 49 -310 red_wall_banner[facing=west] replace
fill 112 52 -318 122 52 -318 chiseled_deepslate replace
fill 112 52 -314 122 52 -314 chiseled_deepslate replace
fill 112 52 -310 122 52 -310 chiseled_deepslate replace
setblock 117 52 -314 copper_chain[axis=y] replace
setblock 117 51 -314 soul_lantern[hanging=true] replace
setblock 115 52 -316 copper_chain[axis=y] replace
setblock 115 51 -316 soul_lantern[hanging=true] replace
setblock 119 52 -316 copper_chain[axis=y] replace
setblock 119 51 -316 soul_lantern[hanging=true] replace
setblock 115 52 -312 copper_chain[axis=y] replace
setblock 115 51 -312 soul_lantern[hanging=true] replace
setblock 119 52 -312 copper_chain[axis=y] replace
setblock 119 51 -312 soul_lantern[hanging=true] replace
setblock 117 53 -318 waxed_copper_bulb[lit=true,powered=false] replace
setblock 117 53 -314 waxed_copper_bulb[lit=true,powered=false] replace
setblock 117 53 -310 waxed_copper_bulb[lit=true,powered=false] replace
setblock 113 53 -314 waxed_copper_bulb[lit=true,powered=false] replace
setblock 121 53 -314 waxed_copper_bulb[lit=true,powered=false] replace
