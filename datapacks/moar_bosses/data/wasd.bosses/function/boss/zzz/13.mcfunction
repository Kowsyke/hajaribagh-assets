#mc-build WASD content
playsound block.glass.break player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 2
summon marker ~ ~ ~ {CustomName:"an iceball",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.ice"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.ice,sort=nearest,limit=1] ~ ~ ~ ~ ~-10