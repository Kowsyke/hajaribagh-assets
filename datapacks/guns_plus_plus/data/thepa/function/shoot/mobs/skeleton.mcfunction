

execute as @s at @s positioned ~ ~1 ~ if entity @e[type=minecraft:arrow,distance=..0.8] store result score @s gz_id run data get entity @s equipment.mainhand.components."minecraft:custom_data".gz_data.id 1

execute as @s at @s positioned ~ ~1 ~ if entity @e[type=minecraft:arrow,distance=..0.8] run stopsound @a[distance=..10] * minecraft:entity.skeleton.shoot

execute as @s at @s positioned ~ ~1 ~ if entity @e[type=minecraft:arrow,distance=..0.8] store result score @s shootingdelay run data get entity @s equipment.mainhand.components."minecraft:custom_data".gz_data.shooting_delay

execute as @s at @s positioned ~ ~1 ~ if entity @e[type=minecraft:arrow,distance=..0.8] positioned ^ ^-1 ^1 run function thepa:shoot/guns/select


execute as @s at @s positioned ~ ~1 ~ if entity @e[type=minecraft:arrow,distance=..0.8] run kill @n[type=minecraft:arrow,distance=..0.8]