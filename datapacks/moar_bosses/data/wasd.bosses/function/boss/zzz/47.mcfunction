#mc-build WASD content
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 0
execute at @s positioned as @s align y run summon marker ~ ~ ~ {CustomName:"a blast of air",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.air"]}
execute at @s positioned as @s facing entity @p feet run tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.air,sort=nearest,limit=1] ~ ~ ~ ~ 0