#mc-build WASD content
summon marker ~ ~ ~ {CustomName:"a gust of wind",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.wind","wasd.wait"]}
execute as @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.wind,sort=nearest,limit=1] run data modify entity @s Rotation set from entity @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.hurricane,tag=!wasd.done,sort=nearest,limit=1] Rotation
execute store result score @s wasd.rng run random value 1..5
execute as @s[scores={wasd.rng=2}] run tp @s ~ ~ ~ ~3 ~
execute as @s[scores={wasd.rng=3}] run tp @s ~ ~ ~ ~1 ~
execute as @s[scores={wasd.rng=4}] run tp @s ~ ~ ~ ~-1 ~
execute as @s[scores={wasd.rng=5}] run tp @s ~ ~ ~ ~-3 ~
execute store result score @s wasd.rng run random value 1..5
execute as @s[scores={wasd.rng=2}] at @s run tp @s ~ ~ ~ ~ ~3
execute as @s[scores={wasd.rng=3}] at @s run tp @s ~ ~ ~ ~ ~1
execute as @s[scores={wasd.rng=4}] at @s run tp @s ~ ~ ~ ~ ~-1
execute as @s[scores={wasd.rng=5}] at @s run tp @s ~ ~ ~ ~ ~-3