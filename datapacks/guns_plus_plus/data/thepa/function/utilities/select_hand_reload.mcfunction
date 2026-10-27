tag @s remove gz_mainhand
tag @s remove gz_offhand

execute if data entity @s equipment.offhand.components."minecraft:custom_data".gz_data run tag @s add gz_offhand
execute if entity @s[tag=!gz_offhand] if data entity @s SelectedItem.components."minecraft:custom_data".gz_data at @s run tag @s add gz_mainhand


