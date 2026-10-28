#mc-build WASD content
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
playsound item.bucket.empty player @a ~ ~ ~ 1 1
execute anchored eyes positioned ^ ^ ^0.01 run summon marker ~ ~ ~ {CustomName:"water",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.water"]}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.water,sort=nearest,limit=1] ~ ~ ~ ~ ~-10