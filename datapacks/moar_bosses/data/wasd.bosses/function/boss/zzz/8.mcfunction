#mc-build WASD content
playsound entity.firework_rocket.large_blast_far player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.large_blast_far player @a ~ ~ ~ 1 0.3
playsound entity.firework_rocket.large_blast_far player @a ~ ~ ~ 1 0.6
summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"magma",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.magma"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.magma,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~ ~