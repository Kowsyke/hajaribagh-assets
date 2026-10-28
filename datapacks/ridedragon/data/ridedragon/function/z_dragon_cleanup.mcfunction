execute as @e[type=ender_dragon,tag=dragonvisible] at @s run function ridedragon:z_dragon_cleanup_visible

execute as @e[type=horse,tag=dragonseat] at @s unless entity @e[tag=dragonvisible,distance=..7,limit=1] run kill @s
execute as @e[type=marker,tag=dragonhelper] at @s unless entity @e[tag=dragonvisible,distance=..7,limit=1] run kill @s

schedule function ridedragon:z_dragon_cleanup 23t
