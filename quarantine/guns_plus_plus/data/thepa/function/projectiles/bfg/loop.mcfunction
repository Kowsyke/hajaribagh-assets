scoreboard players add @a[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{id:54b}},"minecraft:custom_data":{gz_data:{bullets:20}}}}}] bfg_idle 1
scoreboard players reset @a[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{id:54b}},"minecraft:custom_data":{gz_data:{bullets:0}}}}}] bfg_idle
execute as @a[nbt={equipment:{offhand:{components:{"minecraft:custom_data":{gz_data:{id:54b}}}}}}] unless entity @a[nbt={equipment:{offhand:{components:{"minecraft:custom_data":{gz_data:{id:54b}}}}}}] run stopsound @s player guns:bfg_idle
scoreboard players add @a[nbt={equipment:{offhand:{components:{"minecraft:custom_data":{gz_data:{id:54b}},"minecraft:custom_data":{gz_data:{bullets:20}}}}}}] bfg_idle 1
scoreboard players reset @a[nbt={equipment:{offhand:{components:{"minecraft:custom_data":{gz_data:{id:54b}},"minecraft:custom_data":{gz_data:{bullets:0}}}}}}] bfg_idle

execute as @a unless score @s bfg_idle matches 0.. run stopsound @s player guns:bfg_idle
scoreboard players reset @a[scores={bfg_idle=55..}] bfg_idle

execute as @e[tag=energy_ball] at @s unless entity @n[tag=gz_bullet_54,distance=..3] run kill @s
execute if entity @e[tag=bfgtarget] run function thepa:projectiles/bfg/tracers
execute if entity @e[tag=energy_ball] run function thepa:projectiles/bfg/rotate
execute if entity @e[tag=energy_ball] run function thepa:projectiles/bfg/bfgtags