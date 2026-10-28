#mc-build WASD content
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0.2
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0.4
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0.6
playsound minecraft:entity.lightning_bolt.impact player @a ~ ~ ~ 1 2
summon marker ^-0.35 ^0.4 ^0.4 {Tags:["wasd.lib_entity_tick","wasd.ability","wasd.lightning"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.lightning,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~ ~