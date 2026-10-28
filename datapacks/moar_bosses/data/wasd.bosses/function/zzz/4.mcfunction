#mc-build WASD content
execute if score fire w.bosses_setting matches 1.. unless entity @s[y=-64,dy=64] unless entity @s[y=130,dy=200] if dimension minecraft:the_nether run function wasd.bosses:check_biome/fire
execute if score water w.bosses_setting matches 1.. unless entity @s[y=-64,dy=64] unless entity @s[y=130,dy=200] run function wasd.bosses:check_biome/water
execute if score electric w.bosses_setting matches 1.. unless entity @s[y=-64,dy=64] unless entity @s[y=130,dy=200] run function wasd.bosses:check_biome/electric
execute if score earth w.bosses_setting matches 1.. unless entity @s[y=-64,dy=64] unless entity @s[y=130,dy=200] run function wasd.bosses:check_biome/earth
execute if score metal w.bosses_setting matches 1.. if entity @s[y=-64,dy=64] unless entity @s[y=130,dy=200] run function wasd.bosses:check_biome/metal
execute if score air w.bosses_setting matches 1.. unless entity @s[y=-64,dy=64] if entity @s[y=130,dy=200] run function wasd.bosses:check_biome/air
execute if score chicken w.bosses_setting matches 1.. unless entity @s[y=-64,dy=64] unless entity @s[y=130,dy=200] run function wasd.bosses:check_biome/chicken