execute if score @s timeRemaining matches 1.. run scoreboard players remove @s timeRemaining 1

particle minecraft:campfire_signal_smoke ~ ~1 ~ 1.5 1 1.5 0.01 100 force

execute if score @s timeRemaining matches ..0 run kill @s
