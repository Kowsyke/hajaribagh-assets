#Spawn Turret
execute if entity @e[type=armor_stand,tag=spawn_turret] as @e[type=armor_stand,tag=spawn_turret] at @s run tp @s ~ ~ ~ facing entity @p
execute if entity @e[type=armor_stand,tag=spawn_turret] as @e[type=armor_stand,tag=spawn_turret] at @s run data modify entity @s Rotation[1] set value 0.0f
execute if entity @e[type=armor_stand,tag=spawn_turret] as @e[type=armor_stand,tag=spawn_turret] at @s run function thepa:turret/spawn_turret
execute if entity @e[tag=turretT] as @e[tag=turretT,scores={max_x=360..}] run scoreboard players remove @s max_x 360
execute if entity @e[tag=turretT] as @e[tag=turretT,scores={min_x=..0}] run scoreboard players add @s min_x 360
#kill Turret
execute if entity @e[tag=turretB] as @e[tag=turretB] at @s unless entity @e[tag=turretH,distance=..1.8] run kill @s
execute if entity @e[tag=turretT] as @e[tag=turretT] at @s unless entity @e[tag=turretH,distance=..1.8] run kill @s
execute if entity @e[tag=turretC] as @e[tag=turretC] at @s unless entity @e[tag=turretH,distance=..1.8] run kill @s



execute as @a at @s store result score @s rotation_x run data get entity @s Rotation[0]
execute as @a at @s if score @s rotation_x matches ..0 run scoreboard players add @s rotation_x 360