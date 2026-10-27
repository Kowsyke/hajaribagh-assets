

scoreboard players reset @s gz_damage
scoreboard players set @s[scores={gz_bullets=..0}] gz_bullets 0
execute unless entity @s[scores={gz_bullets=..0}] run function thepa:utilities/calc_damage
execute unless entity @s[scores={gz_bullets=..0}] if score @s gz_id matches 61 run function thepa:utilities/calc_cooldown
execute unless entity @s[scores={gz_bullets=..0}] if score @s gz_id matches 63 run function thepa:utilities/calc_cooldown

execute store result score @s gz_reload_time run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time 1
execute store result storage gz:temp capacity int 1 run scoreboard players get @s gz_capacity
execute store result storage gz:temp bullets int 1 run scoreboard players get @s gz_bullets
execute store result storage gz:temp debuff double 0.1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.debuff 10

function thepa:utilities/calculate_delay {"slot":"SelectedItem"}

execute store result storage gz:temp shooting_delay double 0.0001 run scoreboard players get @s delay_calculator


#set the bullet data and carrot to warped_fungus_on_a_stick
execute if score GLOBAL legacyControls matches 1 run item modify entity @s[scores={gz_bullets=1..}] weapon.mainhand thepa:crossbow_update_legacy
execute if score GLOBAL legacyControls matches 0 run item modify entity @s[scores={gz_bullets=1..}] weapon.mainhand thepa:crossbow_update
item modify entity @s[scores={gz_id=19,gz_bullets=1..}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/rpgloaded"}}

execute as @s[scores={gz_id=19,gz_bullets=1..}] if score GLOBAL legacyControls matches 0 run function thepa:utilities/single_ammo_model with entity @s SelectedItem.components."minecraft:custom_data".gz_data

#set the gun to a carrot on stick item
execute if score GLOBAL legacyControls matches 1 run item modify entity @s[scores={gz_bullets=..0}] weapon.mainhand thepa:item_update_legacy
execute if score GLOBAL legacyControls matches 0 run item modify entity @s[scores={gz_bullets=..0}] weapon.mainhand thepa:item_update
execute if entity @s[scores={gz_bullets=..0,gz_id=61}] run function thepa:reload/start
execute if entity @s[scores={gz_bullets=..0,gz_id=63}] run function thepa:reload/start
item modify entity @s[scores={gz_id=19,gz_bullets=..0}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/rpg"}}

execute as @s[scores={gz_id=19,gz_bullets=..0}] if score GLOBAL legacyControls matches 0 run function thepa:utilities/single_ammo_model {id:19,path:'from entity @s SelectedItem.components."minecraft:item_model"'} 

execute as @s[scores={gz_id=61,gz_bullets=..0}] if score GLOBAL legacyControls matches 0 run function thepa:utilities/single_ammo_model {id:61,path:'value "minecraft:guns/poweruprifle"'}


execute if score GLOBAL legacyControls matches 1 run function thepa:utilities/update_handler/legacy_scopes_mh
execute if entity @s[scores={gz_bullets=..0}] at @s as @s run function thepa:utilities/apply_item_modifiers