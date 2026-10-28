#mc-build WASD content
execute store result score @s wasd.rng run random value 1..5
execute as @s[scores={wasd.rng=1}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370105f
execute as @s[scores={wasd.rng=2}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370106f
execute as @s[scores={wasd.rng=3}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370107f
execute as @s[scores={wasd.rng=4}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370126f
execute as @s[scores={wasd.rng=5}] run data modify entity @s equipment.mainhand.components."minecraft:custom_model_data".floats[0] set value 6370127f
tag @s add wasd.given_random_wand