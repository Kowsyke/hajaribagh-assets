#mc-build WASD content
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0
playsound item.firecharge.use player @a ~ ~ ~ 1 0
summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"a flamethrower",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.flamethrower","one"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.flamethrower,tag=one,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~ ~
summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"a flamethrower",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.flamethrower","two"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.flamethrower,tag=two,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~15 ~
summon marker ^-0.35 ^0.4 ^0.4 {CustomName:"a flamethrower",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.flamethrower","three"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.flamethrower,tag=three,sort=nearest,limit=1] ^-0.35 ^0.4 ^0.4 ~-15 ~