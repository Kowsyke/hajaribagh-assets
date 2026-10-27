tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

function thepa:projectiles/spawn/bullet_5 with entity @s
execute at @s run playsound guns:mini_shoot player @a ~ ~ ~ 5 1
execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_5


execute if score GLOBAL recoil matches 1 run tag @s add gun5recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_5_recoil 1t