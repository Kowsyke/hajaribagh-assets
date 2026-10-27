

$execute store result score @s delay_calculator run data get entity @s $(slot).components."minecraft:custom_data".gz_data.shooting_delay
scoreboard players operation 50000 50000 /= @s delay_calculator
execute store result score @s delay_calculator run scoreboard players get 50000 50000
scoreboard players set 50000 50000 50000
scoreboard players operation @s delay_calculator -= 10000 10000
