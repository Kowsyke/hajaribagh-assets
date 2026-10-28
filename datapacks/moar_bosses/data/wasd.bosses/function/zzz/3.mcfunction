#mc-build WASD content
execute store result score @s wasd.temp if entity @e[tag=wasd.boss]
execute if score @s wasd.temp < max_bosses w.bosses_setting run function wasd.bosses:zzz/4