#mc-build WASD content
execute store result score @s wasd.rng run random value 1..3
execute as @s[scores={wasd.rng=1}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370115f
execute as @s[scores={wasd.rng=2}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370116f
execute as @s[scores={wasd.rng=3}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370117f
tag @s add wasd.given_random_wand