scoreboard players enable @a guide
execute as @a unless score @s has_starter_kit matches 1.. at @s run function server_guide:give_starter_kit
execute as @a unless score @s has_starter_kit matches 1.. run scoreboard players set @s has_starter_kit 1
execute as @a unless score @s guide_version matches 4.. at @s run function server_guide:update_player_guide
execute as @a[scores={guide=1..}] at @s run function server_guide:give_book
scoreboard players set @a[scores={guide=1..}] guide 0
