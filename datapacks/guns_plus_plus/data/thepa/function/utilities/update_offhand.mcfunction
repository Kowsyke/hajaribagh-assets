scoreboard players reset @s gz_damage
scoreboard players set @s[scores={gz_bullets=..0}] gz_bullets 0

execute unless entity @s[scores={gz_bullets=..0}] run function thepa:utilities/calc_damage

execute store result score @s gz_reload_time run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.reload_time 1


execute store result storage gz:temp capacity int 1 run scoreboard players get @s gz_capacity
execute store result storage gz:temp bullets int 1 run scoreboard players get @s gz_bullets
execute store result storage gz:temp debuff double 0.1 run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.debuff 10

function thepa:utilities/calculate_delay {"slot":"equipment.offhand"}
execute store result storage gz:temp shooting_delay double 0.0001 run scoreboard players get @s delay_calculator
scoreboard players reset @s delay_calculator


execute if score GLOBAL legacyControls matches 1 run item modify entity @s[scores={gz_bullets=1..}] weapon.offhand thepa:crossbow_update_legacy
execute if score GLOBAL legacyControls matches 0 run item modify entity @s[scores={gz_bullets=1..}] weapon.offhand thepa:crossbow_update
item modify entity @s[scores={gz_id=19,gz_bullets=1..}] weapon.offhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/rpgloaded"}}


#Scopes
item modify entity @s[scores={gz_id=19,gz_bullets=1..}] weapon.offhand {"type":"minecraft:set_components","components":{"minecraft:equippable":{"camera_overlay":"scopes/rpgscope","slot":"offhand"}}}


#set the gun to a carrot on stick item
execute if score GLOBAL legacyControls matches 1 run item modify entity @s[scores={gz_bullets=..0}] weapon.offhand thepa:item_update_legacy
execute if score GLOBAL legacyControls matches 0 run item modify entity @s[scores={gz_bullets=..0}] weapon.offhand thepa:item_update
item modify entity @s[scores={gz_id=19,gz_bullets=..0}] weapon.offhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/rpg"}}




execute if score GLOBAL legacyControls matches 1 run function thepa:utilities/update_handler/legacy_scopes_oh

execute if entity @s[scores={gz_bullets=..0}] at @s as @s run function thepa:utilities/apply_item_modifiers