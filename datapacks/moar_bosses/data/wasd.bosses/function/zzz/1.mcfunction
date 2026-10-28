#mc-build WASD content
execute as @e[type=enderman,tag=!wasd.checked_spawn] at @s run function wasd.bosses:spawning
execute as @e[type=witch,tag=!wasd.checked_spawn] at @s run function wasd.bosses:spawning