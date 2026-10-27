
function thepa:utilities/select_hand_shoot

execute if entity @s[tag=gz_mainhand] run function thepa:shoot/mainhand
execute if entity @s[tag=gz_offhand] run function thepa:shoot/offhand

scoreboard players set @s[scores={shootingdelay=..0}] shotcounterdelay 60
scoreboard players add @s[scores={shootingdelay=..0,gz_bullets=1..}] shotcounter 1

execute as @s[scores={shootingdelay=0}] store result score @s shootingdelay run data get entity @s SelectedItem.components."minecraft:custom_data".gz_data.shooting_delay

scoreboard players add @e[scores={gz_id=25},tag=gz_shoot] gz_teslatimer 1

tag @s remove gz_shoot
tag @s remove gz_part_reload