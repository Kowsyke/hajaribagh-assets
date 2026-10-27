
execute if score @s scope_timer matches 10 unless score @s minigun_sounds matches 4.. run scoreboard players set @s minigun_sounds 12
execute if score @s scope_timer matches 0..9 unless score @s minigun_sounds matches 4.. run scoreboard players set @s minigun_sounds 11

execute at @s[scores={minigun_sounds=11}] run playsound guns:mini_idle master @s ~ ~ ~ 1
execute at @s[scores={minigun_sounds=12}] run playsound guns:mini_spin master @s ~ ~ ~ 1

