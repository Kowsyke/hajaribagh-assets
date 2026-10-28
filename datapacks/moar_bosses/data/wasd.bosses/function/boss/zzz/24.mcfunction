#mc-build WASD content
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0.6
playsound minecraft:entity.lightning_bolt.thunder player @a ~ ~ ~ 1 2
effect give @s resistance 1 255 true
summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"thunder",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.thunder"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.thunder,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~ ~