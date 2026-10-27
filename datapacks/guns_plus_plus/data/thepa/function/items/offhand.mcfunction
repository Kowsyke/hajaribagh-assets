
execute store result score @s gz_id run data get entity @s equipment.offhand.components.minecraft:custom_data.gz_data.id

execute if entity @s[scores={gz_sneak=1..}] at @s run function thepa:reload/start
execute if entity @s[scores={gz_sneak=..0}] at @s run playsound minecraft:block.iron_trapdoor.open player @s ~ ~ ~ 1.0 2