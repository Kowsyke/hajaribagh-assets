#mc-build WASD content
playsound block.basalt.break player @a ~ ~ ~ 1 1
playsound block.basalt.break player @a ~ ~ ~ 1 1
playsound block.basalt.break player @a ~ ~ ~ 1 1
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
execute align y run summon marker ~ ~ ~ {Tags:["wasd.lib_entity_tick","wasd.ability","wasd.earth"]}
execute facing entity @p feet run tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.earth,sort=nearest,limit=1] ~ ~ ~ ~ 0