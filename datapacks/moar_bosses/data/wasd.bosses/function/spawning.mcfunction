#mc-build WASD content
tag @s add wasd.checked_spawn
execute store result score @s wasd.rng run random value 1..100
execute if score @s wasd.rng <= spawn_chance w.bosses_setting unless dimension minecraft:the_end run function wasd.bosses:zzz/3