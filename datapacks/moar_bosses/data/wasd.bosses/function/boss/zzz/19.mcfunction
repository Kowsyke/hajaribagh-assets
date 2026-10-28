#mc-build WASD content
tag @s add wasd.checking_los
execute anchored eyes positioned ^ ^ ^1.5 facing entity @p eyes run function wasd.bosses:boss/zzz/20
scoreboard players reset @s wasd.timer
execute store result score @s wasd.rng run random value 1..3
execute as @s[tag=wasd.has_los] run tp @s ~ ~ ~ facing entity @p[gamemode=!creative,gamemode=!spectator,distance=..25] eyes
execute as @s[tag=wasd.has_los] anchored eyes positioned ^ ^ ^0.1 facing entity @p feet run function wasd.bosses:boss/zzz/22
execute store result score @s wasd.rng run random value 1..100
scoreboard players operation @s wasd.timer = @s wasd.rng
tag @s remove wasd.checking_los
tag @s remove wasd.has_los