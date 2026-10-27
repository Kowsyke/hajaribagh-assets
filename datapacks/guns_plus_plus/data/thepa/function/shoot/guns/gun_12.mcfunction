tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

function thepa:projectiles/spawn/bullet_12 with entity @s

execute anchored eyes positioned ^ ^1.5 ^1.5 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1
execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_12

execute if score GLOBAL recoil matches 1 run tag @s add gun12recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_12_recoil 1t

execute at @s run playsound guns:ray_shoot player @a ~ ~ ~ 0.3 1