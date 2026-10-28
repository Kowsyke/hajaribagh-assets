#mc-build WASD content
#deserts and such
execute if biome ~ ~ ~ minecraft:badlands run function wasd.bosses:check_biome/is_electric
execute if biome ~ ~ ~ minecraft:desert run function wasd.bosses:check_biome/is_electric
execute if biome ~ ~ ~ minecraft:eroded_badlands run function wasd.bosses:check_biome/is_electric
execute if biome ~ ~ ~ minecraft:savanna run function wasd.bosses:check_biome/is_electric
execute if biome ~ ~ ~ minecraft:savanna_plateau run function wasd.bosses:check_biome/is_electric