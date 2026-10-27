# Kit Dev: King Abir and Prime Minister Kowsyke
# Royal Imperial Edition with Gold Silence and Spire Armor Trims

# Clear starter citizen junk if present
clear @s stone_sword[custom_name='{"text":"✦ Citizen Blade ✦","color":"white","bold":true,"italic":false}']
clear @s stone_pickaxe[custom_name='{"text":"✦ Citizen Pickaxe ✦","color":"white","bold":true,"italic":false}']
clear @s stone_axe[custom_name='{"text":"✦ Citizen Hatchet ✦","color":"white","bold":true,"italic":false}']
clear @s stone_hoe[custom_name='{"text":"✦ Citizen Hoe ✦","color":"white","bold":true,"italic":false}']
clear @s leather_helmet[custom_name='{"text":"✦ Citizen Cap ✦","color":"green","bold":true,"italic":false}']
clear @s leather_chestplate[custom_name='{"text":"✦ Citizen Tunic ✦","color":"green","bold":true,"italic":false}']
clear @s leather_leggings[custom_name='{"text":"✦ Citizen Pants ✦","color":"green","bold":true,"italic":false}']
clear @s leather_boots[custom_name='{"text":"✦ Citizen Boots ✦","color":"green","bold":true,"italic":false}']

# Equip Imperial Trimmed God Netherite Armor
item replace entity @s armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:respiration":3,"minecraft:aqua_affinity":1,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:gold",pattern:"minecraft:silence"},custom_name='{"text":"✦ Crown of Hajaribagh ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Imperial gold trimmed crown of the Prime Minister","color":"yellow","italic":false}']]
item replace entity @s armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:gold",pattern:"minecraft:spire"},custom_name='{"text":"✦ Cuirass of Hajaribagh ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Imperial gold trimmed chestplate of the Sovereign","color":"yellow","italic":false}']]
item replace entity @s armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:swift_sneak":3,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:gold",pattern:"minecraft:silence"},custom_name='{"text":"✦ Greaves of Hajaribagh ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Shadow forged swift royal greaves for silent stalking","color":"yellow","italic":false}']]
item replace entity @s armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4,"minecraft:depth_strider":3,"minecraft:soul_speed":3,"minecraft:frost_walker":2,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:gold",pattern:"minecraft:spire"},custom_name='{"text":"✦ Striders of Hajaribagh ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Treads softly across any terrain or liquid","color":"yellow","italic":false}']]
item replace entity @s weapon.offhand with totem_of_undying[custom_name='{"text":"✦ Royal Totem of Immortality ✦","color":"gold","bold":true,"italic":false}']

# Dev Weapons and Tools
give @s netherite_sword[enchantments={"minecraft:sharpness":5,"minecraft:fire_aspect":2,"minecraft:sweeping_edge":3,"minecraft:looting":3,"minecraft:knockback":2,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Excalibur of Hajaribagh ✦","color":"red","bold":true,"italic":false}',lore=['{"text":"Blade of supreme authority and swift judgment","color":"gold","italic":false}']] 1
give @s mace[enchantments={"minecraft:density":5,"minecraft:breach":4,"minecraft:wind_burst":3,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Storm Hammer ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Crushes heavy armor and bosses with wind burst impact","color":"aqua","italic":false}']] 1
give @s netherite_axe[enchantments={"minecraft:efficiency":5,"minecraft:sharpness":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Netherite War Axe ✦","color":"yellow","bold":true,"italic":false}',lore=['{"text":"Fells entire trees and cleaves through armor","color":"gold","italic":false}']] 1
give @s netherite_pickaxe[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Silk Touch Pickaxe ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Safely harvests Sculk Shriekers and catalysts intact","color":"gray","italic":false}']] 1
give @s netherite_pickaxe[enchantments={"minecraft:efficiency":5,"minecraft:fortune":3,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Fortune III Pickaxe ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Multiplies rare ores and gems from the earth","color":"yellow","italic":false}']] 1
give @s netherite_shovel[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Royal Excavator ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Effortlessly carves through earth and gravel","color":"gray","italic":false}']] 1
give @s netherite_hoe[enchantments={"minecraft:efficiency":5,"minecraft:fortune":3,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Harvester of Hajaribagh ✦","color":"green","bold":true,"italic":false}',lore=['{"text":"Instantly clears and harvests sculk veins and catalysts","color":"dark_green","italic":false}']] 1
give @s bow[enchantments={"minecraft:power":5,"minecraft:flame":1,"minecraft:punch":2,"minecraft:infinity":1,"minecraft:unbreaking":3},custom_name='{"text":"✦ Royal Longbow ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Strikes with flaming infinite precision","color":"yellow","italic":false}']] 1
give @s crossbow[enchantments={"minecraft:quick_charge":3,"minecraft:multishot":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Royal Ballista ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Fires rapid multishot volleys in combat","color":"gray","italic":false}']] 1
give @s elytra[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Wings of the Realm ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Sovereign wings blessed with eternal flight","color":"gray","italic":false}']] 1
give @s shield[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Aegis of Hajaribagh ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Impenetrable shield of the Realm","color":"gray","italic":false}']] 1
give @s shears[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Shears of Hajaribagh ✦","color":"yellow","bold":true,"italic":false}',lore=['{"text":"Harvests delicate leaves and wool intact","color":"gray","italic":false}']] 1
give @s flint_and_steel[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Eternal Spark ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Ignites everlasting flames on command","color":"red","italic":false}']] 1

# Anti-Warden Combat and Survival Supplies
give @s totem_of_undying[max_stack_size=64,custom_name='{"text":"✦ Royal Totem of Immortality ✦","color":"gold","bold":true,"italic":false}'] 16
give @s enchanted_golden_apple 64
give @s white_wool 64
give @s snowball 64
give @s wind_charge 64
give @s potion[potion_contents={potion:"minecraft:long_night_vision"},max_stack_size=16] 8
give @s potion[potion_contents={potion:"minecraft:strong_swiftness"},max_stack_size=16] 8
give @s potion[potion_contents={potion:"minecraft:strong_strength"},max_stack_size=16] 8
give @s potion[potion_contents={potion:"minecraft:strong_regeneration"},max_stack_size=16] 8
give @s firework_rocket[fireworks={flight_duration:3},custom_name='{"text":"✦ Sovereign Flight Rocket ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Duration 3 high velocity flight propulsion","color":"gray","italic":false}']] 64
give @s arrow[custom_name='{"text":"✦ Royal Sovereign Arrow ✦","color":"white","bold":true,"italic":false}',lore=['{"text":"Precision ammunition for the Royal Longbow","color":"gray","italic":false}']] 64

# Confirmation
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @s [{"text":"[Royal Dev Kit] ","color":"gold","bold":true},{"text":"Equipped Gold-Trimmed Netherite God Armor and Anti-Warden supplies.","color":"green"}]
