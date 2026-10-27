tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand
function thepa:projectiles/spawn/bullet_54 with entity @s

execute anchored eyes positioned ^ ^0.2 ^1.2 run particle minecraft:happy_villager ~ ~ ~ 0 0 0 0 1


tag @s add bfguser
execute if score GLOBAL recoil matches 1 run tag @s add gun54recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_54_recoil 1t
execute at @s run playsound guns:bfg_shoot player @a ~ ~ ~ 5 1
