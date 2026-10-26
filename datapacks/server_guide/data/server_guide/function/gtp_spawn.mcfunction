# Start GTA Transit to World Spawn
tag @s add gtp_to_spawn
tag @s remove gtp_to_base
scoreboard players set @s gtp_timer 1
effect give @s minecraft:resistance 6 255 true
effect give @s minecraft:blindness 2 1 true
effect give @s minecraft:levitation 1 45 true
playsound minecraft:gta.switch player @s ~ ~ ~ 2 1
playsound minecraft:entity.breeze.wind_burst player @s ~ ~ ~ 2 0.8
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1.5 1.5
particle minecraft:cloud ~ ~1 ~ 1 0.8 1 0.1 60 force
particle minecraft:gust_emitter_large ~ ~ ~ 1 1 1 0 1 force
title @s times 5 15 5
title @s subtitle {"text":"Ascending into clouds...","color":"gray"}
title @s title {"text":"✦ TRANSIT LAUNCH ✦","color":"yellow","bold":true}
