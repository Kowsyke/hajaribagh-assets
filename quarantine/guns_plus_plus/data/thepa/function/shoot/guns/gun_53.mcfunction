tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand
function thepa:projectiles/spawn/bullet_53 with entity @s

execute anchored eyes positioned ^ ^1.5 ^1.5 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1

tag @s add gun53recoil
execute at @s as @s run schedule function thepa:recoil_types/recoil/gun_53_recoil 1t

execute at @s run playsound guns:aug_shoot player @a ~ ~ ~ 0.3 1


execute if entity @s[scores={gz_bullets=2..}] run tag @s add gun53bullet
execute if entity @s[scores={gz_bullets=2}] run tag @s add gun53bullet2
execute if entity @s[scores={gz_bullets=2..}] run schedule function thepa:shoot/guns/gun_53_second 2t
