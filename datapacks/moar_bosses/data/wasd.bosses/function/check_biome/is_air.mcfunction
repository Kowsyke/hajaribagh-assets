#mc-build WASD content
execute store result score @s wasd.rng run random value 1..3
execute as @s[scores={wasd.rng=1}] run function wasd.bosses:summon/wind/zombie
execute as @s[scores={wasd.rng=2}] run function wasd.bosses:summon/wind/skeleton
execute as @s[scores={wasd.rng=3}] run function wasd.bosses:summon/wind/piglin
tp @s[type=!player] ~ -1000 ~