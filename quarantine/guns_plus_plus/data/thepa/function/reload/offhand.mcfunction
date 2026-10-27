
title @s actionbar [{"text":""}]
execute store result score @s gz_id run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.id
execute store result score @s gz_capacity run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.capacity
execute store result score @s gz_bullets run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.bullets


scoreboard players set @s shotcounter 0
execute unless score @s gz_bullets >= @s gz_capacity run function thepa:reload/bullets/select
function thepa:utilities/update_offhand

tag @s remove gz_reloading

