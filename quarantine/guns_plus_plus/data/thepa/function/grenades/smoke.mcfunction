fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air replace fire
summon minecraft:marker ~ ~ ~ {Tags:["smoke","smoSpawn"]}
scoreboard players add @e[tag=smoke,tag=smoSpawn ,type=minecraft:marker] timeRemaining 50

tag @e[type=marker] remove smoSpawn