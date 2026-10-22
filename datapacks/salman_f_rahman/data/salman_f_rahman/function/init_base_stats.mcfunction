# Initialize base gold mined stats for existing players from world statistics.
# Runs once using a marker score.

scoreboard players add #init_gold sfr_base 0
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set GothHunterJamal sfr_base 63
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set Kowsyke sfr_base 46
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set ahsane sfr_base 33
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set DL_7_7 sfr_base 13
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set Dip sfr_base 0
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set GREAT-RED-DRAGO sfr_base 0
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set Exacyyv sfr_base 0
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set InhabiToRs74978 sfr_base 0
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set 808pinik sfr_base 0

execute unless score #init_gold sfr_base matches 1.. run scoreboard players set GothHunterJamal sfr_score 63
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set Kowsyke sfr_score 46
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set ahsane sfr_score 33
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set DL_7_7 sfr_score 13
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set Dip sfr_score 0
execute unless score #init_gold sfr_base matches 1.. run scoreboard players set GREAT-RED-DRAGO sfr_score 0

execute unless score #init_gold sfr_base matches 1.. run scoreboard players set #init_gold sfr_base 1

execute as @a unless score @s sfr_base matches 0.. run scoreboard players set @s sfr_base 0
