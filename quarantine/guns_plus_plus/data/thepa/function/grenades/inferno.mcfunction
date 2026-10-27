summon minecraft:marker ~ ~ ~ {Tags:["inferno","infSpawn"]}
scoreboard players add @e[tag=inferno,tag=infSpawn,type=minecraft:marker] timeRemaining 200
fill ~4 ~4 ~4 ~-4 ~-4 ~-4 fire replace air
tag @e[type=marker] remove infSpawn