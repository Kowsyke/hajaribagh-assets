execute as @e[tag=energy_ball] at @s run tp @s ~ ~ ~ facing entity @n[tag=bfgtarget]
execute as @e[tag=bfgray] at @s run particle minecraft:happy_villager ~ ~1 ~ 0.2 0.2 0.2 0 2 force

execute unless entity @e[tag=energy_ball] run tag @e remove bfgtarget
