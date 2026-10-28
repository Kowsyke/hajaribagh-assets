#mc-build WASD content
execute as @e[tag=wasd.boss] at @s run function wasd.bosses:as_bosses
execute if score bosses w.bosses_setting matches 1.. run function wasd.bosses:zzz/1