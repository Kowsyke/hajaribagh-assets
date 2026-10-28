#mc-build WASD content
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0.2
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0.4
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0.6
summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"electricity",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.electric"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.electric,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~ ~