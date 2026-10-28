#mc-build WASD content
#plains, forests, tiagas
execute if biome ~ ~ ~ minecraft:forest run function wasd.bosses:check_biome/is_earth
execute if biome ~ ~ ~ minecraft:plains unless entity @e[type=chicken,distance=..10] run function wasd.bosses:check_biome/is_earth
execute if biome ~ ~ ~ minecraft:stony_shore run function wasd.bosses:check_biome/is_earth
execute if biome ~ ~ ~ minecraft:swamp run function wasd.bosses:check_biome/is_earth
execute if biome ~ ~ ~ minecraft:taiga run function wasd.bosses:check_biome/is_earth