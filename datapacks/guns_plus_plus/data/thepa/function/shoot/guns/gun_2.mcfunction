tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand
function thepa:projectiles/spawn/bullet_2 with entity @s

execute anchored eyes positioned ^ ^0.2 ^1.2 run particle campfire_cosy_smoke ~ ~ ~ 0 0 0 0 1
execute anchored eyes positioned ^ ^1.5 ^1.5 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1

execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_2



execute if score GLOBAL recoil matches 1 run tag @s add gun2recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_2_recoil 1t

execute at @s run playsound guns:musket_shoot player @a ~ ~ ~ 0.2 1