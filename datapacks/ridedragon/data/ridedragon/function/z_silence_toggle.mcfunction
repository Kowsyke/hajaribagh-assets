
execute store success score #rd_success rd_help run data modify entity @s Silent set value 1b
execute unless score #rd_success rd_help matches 1 run data modify entity @s Silent set value 0b

execute if score #rd_success rd_help matches 1 run tellraw @p [{"text":"The dragon has been ","color":"aqua"},{"text":"silenced","color":"yellow"}]
execute unless score #rd_success rd_help matches 1 run tellraw @p [{"text":"The dragon has been ","color":"aqua"},{"text":"granted its voice back","color":"yellow"}]
