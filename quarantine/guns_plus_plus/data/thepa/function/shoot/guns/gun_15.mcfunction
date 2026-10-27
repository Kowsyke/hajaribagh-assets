tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand


function thepa:projectiles/spawn/bullet_15 with entity @s

execute anchored eyes positioned ^ ^1.5 ^1.5 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1

execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_15

execute if score GLOBAL recoil matches 1 run tag @s add gun15recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_15_recoil 1t

execute if entity @s run playsound guns:dualies_shoot player @a ~ ~ ~ 0.3 1


execute if entity @s[scores={gz_bullets=1..}] run tag @s add gun15bullet
execute if entity @s[scores={gz_bullets=1..}] run schedule function thepa:shoot/guns/gun_15_second 2t