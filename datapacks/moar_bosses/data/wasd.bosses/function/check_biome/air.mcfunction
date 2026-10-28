#mc-build WASD content
#mountains high up
execute if biome ~ ~ ~ minecraft:frozen_peaks run function wasd.bosses:check_biome/is_air
execute if biome ~ ~ ~ minecraft:jagged_peaks run function wasd.bosses:check_biome/is_air
execute if biome ~ ~ ~ minecraft:meadow run function wasd.bosses:check_biome/is_air
execute if biome ~ ~ ~ minecraft:snowy_slopes run function wasd.bosses:check_biome/is_air
execute if biome ~ ~ ~ minecraft:stony_peaks run function wasd.bosses:check_biome/is_air
execute if biome ~ ~ ~ minecraft:grove run function wasd.bosses:check_biome/is_air