execute if entity @s[tag=inf_reload] run tag @s add temp_remove_inf
execute unless entity @s[tag=inf_reload] run tag @s add inf_reload
execute if entity @s[tag=temp_remove_inf] run tag @s remove inf_reload
tag @s remove temp_remove_inf

execute if entity @s[tag=inf_reload] run title @s actionbar {"text":"Infinite Ammo: ENABLED","color":"green","bold":true}
execute unless entity @s[tag=inf_reload] run title @s actionbar {"text":"Infinite Ammo: DISABLED","color":"red","bold":true}

execute if entity @s[tag=inf_reload] run tellraw @s [{"text":"[Royal Armory] ","color":"gold","bold":true},{"text":"Infinite ammo is now ","color":"yellow"},{"text":"ENABLED","color":"green","bold":true}]
execute unless entity @s[tag=inf_reload] run tellraw @s [{"text":"[Royal Armory] ","color":"gold","bold":true},{"text":"Infinite ammo is now ","color":"yellow"},{"text":"DISABLED (Consumes Ammo)","color":"red","bold":true}]
