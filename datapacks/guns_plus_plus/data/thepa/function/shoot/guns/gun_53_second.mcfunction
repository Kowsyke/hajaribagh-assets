tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

execute as @a[tag=gun53bullet,scores={augCount=..1}] at @s run function thepa:projectiles/spawn/bullet_53 with entity @s
scoreboard players add @a[tag=gun53bullet] augCount 1

execute as @a[tag=gun53bullet,scores={augCount=..1}] at @s anchored eyes positioned ^ ^1 ^1.2 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1



execute as @a[tag=gun53bullet,scores={augCount=..2}] run tag @s add gun53recoil
execute as @a[tag=gun53bullet,scores={augCount=..2}] at @s as @s run schedule function thepa:recoil_types/recoil/gun_53_recoil 1t

execute as @a[tag=gun53bullet] if entity @s[tag=gun53bullet2] run return run tag @s remove gun53bullet2

schedule function thepa:shoot/guns/gun_53_second 2t
execute if entity @a[scores={augCount=2..}] run schedule clear thepa:shoot/guns/gun_53_second
execute as @a[tag=gun53bullet,scores={augCount=2..}] run tag @s remove gun53bullet
scoreboard players reset @a[scores={augCount=2..}] augCount
