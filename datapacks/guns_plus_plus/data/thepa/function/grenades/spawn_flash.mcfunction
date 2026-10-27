
summon minecraft:marker ~ ~1 ~ {Tags:["flashbang","spawnflash"]}
scoreboard players add @e[tag=flashbang,tag=spawnflash,type=minecraft:marker] timeRemaining 1
execute as @a if entity @e[tag=flashbang,distance=..5] run playsound guns:flashbang_ring master @s ~ ~ ~ 10 1 1

tag @e[tag=spawnflash,type=minecraft:marker] remove spawnflash