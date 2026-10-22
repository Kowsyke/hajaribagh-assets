scoreboard players set @s xray 0
scoreboard players enable @s xray
execute if entity @s[gamemode=spectator] run tag @s add was_spectator
execute if entity @s[tag=was_spectator] run function ore_xray:turn_off
execute unless entity @s[tag=was_spectator] run function ore_xray:turn_on
tag @s remove was_spectator
