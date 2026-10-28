# Executed as dragonhelper, no position

execute as @s at @s if block ~ ~-1.2 ~ air run tp @s ~ ~-0.1 ~
execute as @s at @s unless block ~ ~-1.2 ~ air run tp @s ~ ~0.1 ~

execute as @s at @s run tp @e[type=horse,distance=..7,tag=dragonseat_selected,limit=1] ~ ~ ~ ~ ~

execute as @e[distance=..7,tag=dragonseat_selected,limit=1] at @s rotated ~ 0 positioned ^ ^ ^-3.5 rotated as @s run tp @e[tag=dragonvisible_selected,limit=1,distance=..7] ~ ~-1.0 ~ ~-180 ~
