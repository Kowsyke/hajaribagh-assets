execute if score @s bouncyCount matches 3.. run data merge entity @s {fuse:0s}

execute unless score @s bouncyCount matches 1.. run scoreboard players set @s SCOREBOARD1 -50
execute store result entity @s Motion[1] double -0.01 run scoreboard players get @s SCOREBOARD1
scoreboard players add @s bouncyCount 1
