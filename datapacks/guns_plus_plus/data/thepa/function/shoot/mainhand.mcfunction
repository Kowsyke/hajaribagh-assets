
execute store result score @s gz_id run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute store result score @s gz_capacity run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.capacity
execute store result score @s gz_bullets run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.bullets
execute store result score @s[tag=!tp_shotgun] gz_reload_max run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time 20

execute unless entity @s[tag=gz_part_reload] if entity @s[scores={shootingdelay=0,gz_bullets=20}] if score @s gz_id matches 54 run scoreboard players remove @s gz_bullets 20


execute unless entity @s[tag=gz_part_reload] if entity @s[scores={shootingdelay=0}] unless score @s gz_id matches 54 run scoreboard players remove @s gz_bullets 1
execute unless entity @s[tag=gz_part_reload] if score @s[tag=inf_reload] gz_id matches 62 run scoreboard players add @s gz_bullets 1


execute unless entity @s[tag=gz_part_reload] if entity @s[scores={shootingdelay=0}] if score @s gz_id matches 53 run scoreboard players remove @s gz_bullets 2

function thepa:utilities/update_mainhand
