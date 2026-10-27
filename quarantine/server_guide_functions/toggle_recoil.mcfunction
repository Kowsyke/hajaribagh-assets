execute if score GLOBAL recoil matches 1 run scoreboard players set GLOBAL recoil 2
execute if score GLOBAL recoil matches 0 run scoreboard players set GLOBAL recoil 1
execute if score GLOBAL recoil matches 2 run scoreboard players set GLOBAL recoil 0

execute if score GLOBAL recoil matches 1 run title @s actionbar {"text":"Recoil: ON (0.1x)","color":"green","bold":true}
execute if score GLOBAL recoil matches 0 run title @s actionbar {"text":"Recoil: OFF","color":"red","bold":true}

execute if score GLOBAL recoil matches 1 run tellraw @s [{"text":"[Royal Armory] ","color":"gold","bold":true},{"text":"Firearm recoil is now ","color":"yellow"},{"text":"ENABLED (0.1x)","color":"green","bold":true}]
execute if score GLOBAL recoil matches 0 run tellraw @s [{"text":"[Royal Armory] ","color":"gold","bold":true},{"text":"Firearm recoil is now ","color":"yellow"},{"text":"DISABLED","color":"red","bold":true}]
