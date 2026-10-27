scoreboard players add @s tnt_mode 1
execute if score @s tnt_mode matches 2.. run scoreboard players set @s tnt_mode 0
execute if score @s tnt_mode matches 1 run function server_guide:tnt_mode_on
execute if score @s tnt_mode matches 0 run function server_guide:tnt_mode_off
