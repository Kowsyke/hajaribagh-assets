#mc-build WASD content
execute if biome ~ ~ ~ minecraft:plains if entity @e[type=chicken,distance=..10] run function wasd.bosses:check_biome/is_chicken