scoreboard players set @s tnt_mode 0
playsound minecraft:block.fire.extinguish player @s ~ ~ ~ 1 1
title @s actionbar {"text":"✦ TNT Arrows: DISABLED (Normal)","color":"gray"}
tellraw @s [{"text":"[Hajaribagh] ","color":"gold","bold":true},{"text":"TNT Arrow Mode: ","color":"yellow"},{"text":"DISABLED","color":"red","bold":true},{"text":". Your arrows are back to normal. Type /trigger tnt_arrow to re-enable.","color":"gray"}]
