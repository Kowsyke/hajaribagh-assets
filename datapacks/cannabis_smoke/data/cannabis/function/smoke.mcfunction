scoreboard players set @s smoke 0
scoreboard players set @s use_joint 0
scoreboard players set @s smoke_timer 60
playsound minecraft:block.campfire.crackle player @a ~ ~ ~ 1.0 1.0
playsound minecraft:entity.generic.drink player @s ~ ~ ~ 0.8 1.0
title @s actionbar {"text":"*Takes a deep puff of cannabis* Feeling chilled...","color":"green","bold":true}
effect give @s minecraft:regeneration 15 1 true
effect give @s minecraft:resistance 20 1 true
effect give @s minecraft:slow_falling 10 0 true
effect give @s minecraft:saturation 2 0 true
effect give @s minecraft:nausea 6 0 true
