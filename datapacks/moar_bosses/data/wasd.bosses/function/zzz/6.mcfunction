#mc-build WASD content
scoreboard players add @s wasd.timer 1
tp @s ~ ~ ~

execute unless score @s wasd.timer matches 200.. positioned ^ ^ ^0.2 if block ^ ^ ^0.2 #wasd.tags:nonsolid run function wasd.bosses:meteor_raytrace
