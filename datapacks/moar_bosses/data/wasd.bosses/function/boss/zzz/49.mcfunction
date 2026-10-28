#mc-build WASD content
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
playsound item.elytra.flying player @a ~ ~ ~ 1 1.7
execute positioned ~ ~2 ~ rotated ~ 0 run function wasd.lib:detection/vertical/9x9
execute positioned ~ ~2 ~ as @e[tag=wasd.location,distance=..1] at @s run tag @s add wasd.invalid_location
summon marker ~ ~2 ~ {Tags:["wasd.lib_entity_tick","wasd.ability","wasd.hurricane"]}
execute at @s positioned ~ ~2 ~ run tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.hurricane,sort=nearest,limit=1] ~ ~ ~ ~ ~10
execute as @e[tag=wasd.location] at @s unless block ~ ~ ~ #wasd.tags:nonsolid run tag @s add wasd.invalid_location
execute as @e[tag=wasd.location,sort=random,limit=15,tag=!wasd.invalid_location] at @s run function wasd.bosses:boss/zzz/50
kill @e[tag=wasd.location]
tag @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.hurricane,sort=nearest,limit=1] add wasd.done