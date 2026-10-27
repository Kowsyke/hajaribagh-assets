tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

execute as @a[tag=gun15bullet] at @s run function thepa:projectiles/spawn/bullet_15 with entity @s

execute as @a[tag=gun15bullet] at @s anchored eyes positioned ^ ^1 ^1.2 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1

execute as @a[tag=gun15bullet] run tag @s add gun15recoil
execute as @a[tag=gun15bullet] at @s as @s run schedule function thepa:recoil_types/recoil/gun_15_recoil 1t
