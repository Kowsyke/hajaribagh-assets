#mc-build WASD content
execute store result score @s wasd.rng run random value 1..4
execute as @s[scores={wasd.rng=1}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370111f
execute as @s[scores={wasd.rng=2}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370112f
execute as @s[scores={wasd.rng=3}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370113f
execute as @s[scores={wasd.rng=4}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370114f
tag @s add wasd.given_random_wand