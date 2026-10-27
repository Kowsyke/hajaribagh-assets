scoreboard players remove @e[scores={size_time=1001..}] size_time 10
execute as @a[scores={size_time=1000}] run attribute @s scale base set 1
scoreboard players reset @e[scores={size_time=1000}]
scoreboard players add @e[scores={size_time=..999}] size_time 1
execute as @a[nbt=!{attributes:[{id:"minecraft:scale",base:1.0d}]}] unless entity @s[scores={size_time=0..}] store result score @s size_time run attribute @s minecraft:scale base get 1000

execute as @e[scores={size_time=0..}] at @s store result entity @s attributes[{id:"minecraft:scale"}].base float 0.001 run scoreboard players get @s size_time