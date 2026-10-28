#mc-build WASD content
#nether biomes but not warped forest
execute unless biome ~ ~ ~ minecraft:warped_forest run function wasd.bosses:check_biome/is_fire