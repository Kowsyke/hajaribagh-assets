execute as @e[tag=teslazap,limit=1] at @e[tag=teslazap,limit=1] run tp @s ~ ~ ~ facing entity @e[type=!#thepa:unaffected,limit=1,sort=nearest,type=!armor_stand,tag=!gz_hit,tag=!teslazapped,distance=..10]
execute as @e[tag=teslazap,limit=1] at @e[tag=teslazap,limit=1] run tp @s ^ ^ ^0.75
execute as @e[tag=teslazap] at @e[tag=teslazap] run particle minecraft:electric_spark ~ ~1 ~ 0.4 0.4 0.4 0 30 force @a

execute as @e[tag=teslazap] at @e[tag=teslazap] run scoreboard players add @e[type=!#thepa:unaffected,distance=..1] gz_teslakill 1
execute as @e[scores={gz_teslakill=10..}] at @e[scores={gz_teslakill=10..}] run kill @e[tag=teslazap,distance=..1]
execute as @e[tag=teslazap] at @e[tag=teslazap] run tag @e[distance=..1] add teslazapped

execute as @e[scores={gz_teslakill=1..}] run damage @s 6 thepa:shot
scoreboard players set @e[scores={gz_teslakill=1..}] gz_teslakill 0

execute as @e[scores={gz_teslatimer=49}] at @e[scores={gz_teslatimer=49}] if entity @e[scores={gz_teslatimer=49}] run kill @e[tag=teslazap]
execute if entity @e[scores={gz_teslatimer=49}] run tag @e[tag=teslazapped] remove teslazapped
scoreboard players set @a[scores={gz_teslatimer=50..}] gz_teslatimer 0