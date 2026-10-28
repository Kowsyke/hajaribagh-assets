#mc-build WASD content
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 1
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 2
playsound entity.firework_rocket.large_blast player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.large_blast player @a ~ ~ ~ 1 2
summon marker ^-0.35 ^0.4 ^0.4 {Tags:["wasd.lib_entity_tick","wasd.ability","wasd.meteor"]}
execute positioned ^-0.35 ^0.4 ^0.4 as @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.meteor,sort=nearest,limit=1] run function wasd.bosses:boss/zzz/6