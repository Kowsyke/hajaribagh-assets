
function thepa:utilities/select_hand_shoot

execute if entity @s[tag=gz_mainhand] store result score @s gz_id run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute if entity @s[tag=gz_offhand] store result score @s gz_id run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.id

execute if entity @s[scores={gz_sneak=1..}] run tag @s add gz_part_reload
execute if entity @s[scores={gz_sneak=1..}] run function thepa:reload/start
execute as @s[scores={gz_sneak=..0,gz_bullets=1..}] at @s positioned as @s run function thepa:shoot/guns/select
execute if score GLOBAL legacyControls matches 0 if score @s scope_timer matches 1.. run function thepa:shoot/minigun/fire
execute if score GLOBAL legacyControls matches 1 run function thepa:shoot/minigun/fire


tag @s add gz_shoot