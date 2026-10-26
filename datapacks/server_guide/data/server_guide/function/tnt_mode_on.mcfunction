scoreboard players set @s tnt_mode 1
playsound minecraft:entity.tnt.primed player @s ~ ~ ~ 1 1.2
title @s actionbar {"text":"✦ TNT Arrows: ENABLED (Explodes on Contact)","color":"red","bold":true}
tellraw @s [{"text":"[Hajaribagh] ","color":"gold","bold":true},{"text":"TNT Arrow Mode: ","color":"yellow"},{"text":"ENABLED","color":"green","bold":true},{"text":". Your arrows now explode like TNT on contact. Type /trigger tnt_arrow to toggle off.","color":"gold"}]
