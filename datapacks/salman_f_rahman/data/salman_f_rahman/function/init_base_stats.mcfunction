# Initialize base mined stats for existing players from world statistics.
# Runs once using a marker score.

scoreboard players add #init sfr_base 0
execute unless score #init sfr_base matches 1.. run scoreboard players set GothHunterJamal sfr_base 6421
execute unless score #init sfr_base matches 1.. run scoreboard players set ahsane sfr_base 1945
execute unless score #init sfr_base matches 1.. run scoreboard players set Kowsyke sfr_base 1698
execute unless score #init sfr_base matches 1.. run scoreboard players set Dip sfr_base 743
execute unless score #init sfr_base matches 1.. run scoreboard players set DL_7_7 sfr_base 293
execute unless score #init sfr_base matches 1.. run scoreboard players set GREAT-RED-DRAGO sfr_base 134
execute unless score #init sfr_base matches 1.. run scoreboard players set Exacyyv sfr_base 0
execute unless score #init sfr_base matches 1.. run scoreboard players set InhabiToRs74978 sfr_base 0
execute unless score #init sfr_base matches 1.. run scoreboard players set 808pinik sfr_base 0

execute unless score #init sfr_base matches 1.. run scoreboard players set GothHunterJamal sfr_score 6421
execute unless score #init sfr_base matches 1.. run scoreboard players set ahsane sfr_score 1945
execute unless score #init sfr_base matches 1.. run scoreboard players set Kowsyke sfr_score 1698
execute unless score #init sfr_base matches 1.. run scoreboard players set Dip sfr_score 743
execute unless score #init sfr_base matches 1.. run scoreboard players set DL_7_7 sfr_score 293
execute unless score #init sfr_base matches 1.. run scoreboard players set GREAT-RED-DRAGO sfr_score 134

execute unless score #init sfr_base matches 1.. run scoreboard players set #init sfr_base 1

execute as @a unless score @s sfr_base matches 0.. run scoreboard players set @s sfr_base 0
