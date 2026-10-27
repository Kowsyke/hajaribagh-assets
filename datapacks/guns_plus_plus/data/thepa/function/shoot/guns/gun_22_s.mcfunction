tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

function thepa:projectiles/spawn/bullet_22_s with entity @s

execute anchored eyes positioned ^ ^1.5 ^1.5 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1
execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_22_s


execute if score GLOBAL recoil matches 1 run tag @s add gun22srecoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_22_s_recoil 1t
execute at @s run playsound guns:sggfire_s player @a[distance=..10] ~ ~ ~ 0.3 2


