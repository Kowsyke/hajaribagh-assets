
tag @s add tp_shotgun
execute unless score @s gz_id matches 7 unless score @s gz_id matches 58 unless score @s gz_id matches 47 unless score @s gz_id matches 50 run tag @s remove tp_shotgun

scoreboard players set @s gz_reload 0
scoreboard players set @s gz_reload_max 0

execute if entity @s[tag=gz_mainhand] store result score @s gz_reload_max run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time 20
execute if entity @s[tag=gz_offhand] store result score @s gz_reload_max run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.reload_time 20

execute if entity @s[tag=gz_mainhand,tag=tp_shotgun] store result score @s gz_reload_max run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time 200
execute if entity @s[tag=gz_offhand,tag=tp_shotgun] store result score @s gz_reload_max run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.reload_time 200

execute store result score @s[tag=tp_shotgun] shotgun_clicks run scoreboard players operation @s gz_capacity -= @s gz_bullets
scoreboard players operation @s gz_capacity += @s gz_bullets

scoreboard players operation @s[tag=tp_shotgun] gz_reload_max /= @s[tag=tp_shotgun] gz_capacity
scoreboard players operation @s[tag=tp_shotgun] gz_reload_max *= @s[tag=tp_shotgun] shotgun_clicks

scoreboard players operation @s[tag=tp_shotgun] gz_reload_max /= 10 10

execute unless entity @s[nbt={SelectedItem:{id:"minecraft:carrot_on_a_stick"}}] unless entity @s[nbt={equipment:{offhand:{id:"minecraft:carrot_on_a_stick"}}}] if score @s[tag=tp_shotgun] gz_reload_max matches 0 run return fail

execute as @s run function thepa:reload/timer
execute as @s[tag=!gz_reloading] at @s run function thepa:reload/sounds


execute if entity @s[tag=gz_mainhand] run tag @s add gz_reloading
execute if entity @s[tag=gz_offhand] run tag @s add gz_reloading


execute as @s[tag=gz_mainhand] store result score @s prevGun run data get entity @s SelectedItem.components."minecraft:custom_data".gz_data.id
execute as @s[tag=gz_offhand] store result score @s prevGun run data get entity @s equipment.offhand.components."minecraft:custom_data".gz_data.id

