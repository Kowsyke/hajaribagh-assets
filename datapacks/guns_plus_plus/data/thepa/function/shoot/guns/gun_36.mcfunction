tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

function thepa:projectiles/spawn/bullet_36 with entity @s

execute anchored eyes positioned ^ ^0.2 ^1.2 run particle campfire_cosy_smoke ~ ~ ~ 0 0 0 0 1
execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_36

execute if score GLOBAL recoil matches 1 run tag @s add gun36recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_36_recoil 1t
execute at @s run playsound guns:mini_shoot player @a ~ ~ ~ 0.3 1
