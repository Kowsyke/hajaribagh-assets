#mc-build WASD content
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
playsound item.firecharge.use player @a ~ ~ ~ 1 2
execute anchored eyes positioned ^ ^ ^0.01 run summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"a gust of wind",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.wind"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.wind,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~ ~