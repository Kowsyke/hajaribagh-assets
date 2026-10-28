#mc-build WASD content
playsound block.glass.break player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 2
execute at @s positioned as @s align y run summon marker ~ ~ ~ {CustomName:"frost",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.frost"]}
execute at @s positioned as @s facing entity @p feet run tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.frost,sort=nearest,limit=1] ~ ~ ~ ~ 0