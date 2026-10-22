scoreboard players enable @a guide
execute as @a unless score @s has_guide matches 1.. at @s run function server_guide:give_book
execute as @a unless score @s has_guide matches 1.. run scoreboard players set @s has_guide 1
execute as @a[scores={guide=1..}] at @s run function server_guide:give_book
scoreboard players set @a[scores={guide=1..}] guide 0
