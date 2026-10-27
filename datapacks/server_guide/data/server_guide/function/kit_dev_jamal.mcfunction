# Kit Dev: Safwan and GothHunterJamal
# Minister of Tourism, Wildlife and Hunting
# Mystic Amethyst Ward and Rib Armor Trims

# Clear starter citizen junk if present
clear @s stone_sword[custom_name='{"text":"✦ Citizen Blade ✦","color":"white","bold":true,"italic":false}']
clear @s stone_pickaxe[custom_name='{"text":"✦ Citizen Pickaxe ✦","color":"white","bold":true,"italic":false}']
clear @s stone_axe[custom_name='{"text":"✦ Citizen Hatchet ✦","color":"white","bold":true,"italic":false}']
clear @s stone_hoe[custom_name='{"text":"✦ Citizen Hoe ✦","color":"white","bold":true,"italic":false}']
clear @s leather_helmet[custom_name='{"text":"✦ Citizen Cap ✦","color":"green","bold":true,"italic":false}']
clear @s leather_chestplate[custom_name='{"text":"✦ Citizen Tunic ✦","color":"green","bold":true,"italic":false}']
clear @s leather_leggings[custom_name='{"text":"✦ Citizen Pants ✦","color":"green","bold":true,"italic":false}']
clear @s leather_boots[custom_name='{"text":"✦ Citizen Boots ✦","color":"green","bold":true,"italic":false}']

# Equip Mystic Amethyst Trimmed God Netherite Armor
item replace entity @s armor.head with netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:respiration":3,"minecraft:aqua_affinity":1,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:amethyst",pattern:"minecraft:ward"},custom_name='{"text":"✦ Mask of the Deep Hunter ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Amethyst ward trimmed helm of the Explorer","color":"dark_purple","italic":false}']]
item replace entity @s armor.chest with netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:amethyst",pattern:"minecraft:ward"},custom_name='{"text":"✦ Carapace of the Deep Hunter ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Amethyst ward trimmed cuirass shielding against deep darkness","color":"dark_purple","italic":false}']]
item replace entity @s armor.legs with netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:swift_sneak":3,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:amethyst",pattern:"minecraft:rib"},custom_name='{"text":"✦ Stalkers of the Deep Hunter ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Rib trimmed swift greaves for prowling ancient cities","color":"dark_purple","italic":false}']]
item replace entity @s armor.feet with netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4,"minecraft:depth_strider":3,"minecraft:soul_speed":3,"minecraft:frost_walker":2,"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:thorns":3},trim={material:"minecraft:amethyst",pattern:"minecraft:ward"},custom_name='{"text":"✦ Silent Treads of the Hunter ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Muffled footsteps that produce zero acoustic vibrations","color":"dark_purple","italic":false}']]
item replace entity @s weapon.offhand with totem_of_undying[custom_name='{"text":"✦ Hunter Totem of Immortality ✦","color":"light_purple","bold":true,"italic":false}']

# Dev Weapons and Tools
give @s netherite_sword[enchantments={"minecraft:sharpness":5,"minecraft:fire_aspect":2,"minecraft:sweeping_edge":3,"minecraft:looting":3,"minecraft:knockback":2,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Edge of the Deep Hunter ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Blade forged to hunt deep dark abominations","color":"dark_purple","italic":false}']] 1
give @s mace[enchantments={"minecraft:density":5,"minecraft:breach":4,"minecraft:wind_burst":3,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Storm Hammer ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Crushes heavy armor and bosses with wind burst impact","color":"aqua","italic":false}']] 1
give @s netherite_axe[enchantments={"minecraft:efficiency":5,"minecraft:sharpness":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Netherite War Axe ✦","color":"yellow","bold":true,"italic":false}',lore=['{"text":"Fells entire trees and cleaves through armor","color":"gold","italic":false}']] 1
give @s netherite_pickaxe[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Silk Touch Pickaxe ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Safely harvests Sculk Shriekers and catalysts intact","color":"gray","italic":false}']] 1
give @s netherite_pickaxe[enchantments={"minecraft:efficiency":5,"minecraft:fortune":3,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Fortune III Pickaxe ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Multiplies rare ores and gems from the earth","color":"yellow","italic":false}']] 1
give @s netherite_shovel[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Royal Excavator ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Effortlessly carves through earth and gravel","color":"gray","italic":false}']] 1
give @s netherite_hoe[enchantments={"minecraft:efficiency":5,"minecraft:fortune":3,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Harvester of Hajaribagh ✦","color":"green","bold":true,"italic":false}',lore=['{"text":"Instantly clears and harvests sculk veins and catalysts","color":"dark_green","italic":false}']] 1
give @s bow[enchantments={"minecraft:power":5,"minecraft:flame":1,"minecraft:punch":2,"minecraft:infinity":1,"minecraft:unbreaking":3},custom_name='{"text":"✦ Royal Longbow ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Strikes with flaming infinite precision","color":"yellow","italic":false}']] 1
give @s crossbow[enchantments={"minecraft:quick_charge":3,"minecraft:multishot":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Royal Ballista ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Fires rapid multishot volleys in combat","color":"gray","italic":false}']] 1
give @s elytra[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Wings of the Realm ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Sovereign wings blessed with eternal flight","color":"gray","italic":false}']] 1
give @s shield[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Aegis of the Hunter ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Impenetrable shield of the Minister of Hunting","color":"gray","italic":false}']] 1
give @s shears[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Shears of Hajaribagh ✦","color":"yellow","bold":true,"italic":false}',lore=['{"text":"Harvests delicate leaves and wool intact","color":"gray","italic":false}']] 1
give @s flint_and_steel[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Eternal Spark ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Ignites everlasting flames on command","color":"red","italic":false}']] 1

# Anti-Warden Combat and Survival Supplies
give @s totem_of_undying[max_stack_size=64,custom_name='{"text":"✦ Hunter Totem of Immortality ✦","color":"light_purple","bold":true,"italic":false}'] 16
give @s enchanted_golden_apple 64
give @s white_wool 64
give @s snowball 64
give @s wind_charge 64
give @s potion[potion_contents={potion:"minecraft:long_night_vision"},max_stack_size=16] 8
give @s potion[potion_contents={potion:"minecraft:strong_swiftness"},max_stack_size=16] 8
give @s potion[potion_contents={potion:"minecraft:strong_strength"},max_stack_size=16] 8
give @s potion[potion_contents={potion:"minecraft:strong_regeneration"},max_stack_size=16] 8
give @s firework_rocket[fireworks={flight_duration:3},custom_name='{"text":"✦ Sovereign Flight Rocket ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Duration 3 high velocity flight propulsion","color":"gray","italic":false}']] 64
give @s arrow[custom_name='{"text":"✦ Hunter Sovereign Arrow ✦","color":"white","bold":true,"italic":false}',lore=['{"text":"Precision ammunition for the Royal Longbow","color":"gray","italic":false}']] 64

# Firearms Arsenal
function thepa:give/awp
function thepa:give/combat_shotgun
function thepa:give/ak_47
function thepa:give/rpg
function thepa:give/suppressor
function thepa:give/lasersight
give @s minecraft:clock[minecraft:item_model="minecraft:ammo/sniper_ammo",minecraft:custom_data={"gz_data":{"bullet_type":11b}},minecraft:item_name={"translate":"thepa.item.name.bullet_11","color":"white","italic":false},minecraft:custom_name={"text":"Heavy Rounds (AWP)","color":"gold","italic":false}] 64
give @s minecraft:clock[minecraft:item_model="minecraft:ammo/shotgun_shells",minecraft:custom_data={"gz_data":{"bullet_type":2b}},minecraft:item_name={"translate":"thepa.item.name.bullet_2","color":"white","italic":false},minecraft:custom_name={"text":"Shells (Combat Shotgun)","color":"gold","italic":false}] 64
give @s minecraft:clock[minecraft:item_model="minecraft:ammo/medium_ammo",minecraft:custom_data={"gz_data":{"bullet_type":6b}},minecraft:item_name={"translate":"thepa.item.name.bullet_6","color":"white","italic":false},minecraft:custom_name={"text":"Medium Rounds (AK-47)","color":"gold","italic":false}] 64
give @s minecraft:clock[minecraft:item_model="minecraft:ammo/rocket_ammo",minecraft:custom_data={"gz_data":{"bullet_type":31b}},minecraft:item_name={"translate":"thepa.item.name.bullet_31","color":"white","italic":false},minecraft:custom_name={"text":"Rockets (RPG)","color":"gold","italic":false}] 32
tag @s add inf_reload

# Confirmation
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @s [{"text":"[Hunter Dev Kit] ","color":"light_purple","bold":true},{"text":"Equipped Amethyst-Trimmed Netherite God Armor, Anti-Warden supplies, and Heavy Firearms.","color":"green"}]
