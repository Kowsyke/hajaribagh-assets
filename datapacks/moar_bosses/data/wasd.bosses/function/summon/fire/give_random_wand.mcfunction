#mc-build WASD content
execute store result score @s wasd.rng run random value 1..4
execute as @s[scores={wasd.rng=1}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370101f
execute as @s[scores={wasd.rng=2}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370102f
execute as @s[scores={wasd.rng=3}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370103f
execute as @s[scores={wasd.rng=4}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370104f
tag @s add wasd.given_random_wand