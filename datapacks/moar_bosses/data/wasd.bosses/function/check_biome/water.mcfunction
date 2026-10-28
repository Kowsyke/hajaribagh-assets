#mc-build WASD content
#oceans
execute if biome ~ ~ ~ minecraft:river run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:beach run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:ice_spikes run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:snowy_plains run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:snowy_taiga run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:warm_ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:lukewarm_ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:deep_ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:deep_lukewarm_ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:deep_frozen_ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:deep_cold_ocean run function wasd.bosses:check_biome/is_water
execute if biome ~ ~ ~ minecraft:cold_ocean run function wasd.bosses:check_biome/is_water