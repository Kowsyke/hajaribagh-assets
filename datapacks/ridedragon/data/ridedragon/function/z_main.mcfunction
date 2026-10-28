execute as @a[scores={rd_summon=1..}] at @s run function ridedragon:z_summon_trigger
execute as @a[scores={rd_vanish=1..}] at @s run function ridedragon:z_vanish_trigger
execute as @a[scores={rd_silence=1..}] at @s run function ridedragon:z_silence_trigger
execute as @a[scores={rd_help=1..}] at @s run function ridedragon:z_help_trigger

execute as @e[type=ender_dragon,tag=dragonvisible] at @s run function ridedragon:z_dragon_motion


