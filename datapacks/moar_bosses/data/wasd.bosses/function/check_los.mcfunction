#mc-build WASD content
scoreboard players add @s wasd.timer 1
tp @s ~ ~ ~
execute unless score @s wasd.timer matches 200.. positioned ^ ^ ^0.2 if block ^ ^ ^0.2 #wasd.tags:nonsolid positioned ~ ~1 ~ unless entity @a[distance=..1] positioned ~ ~-1 ~ unless entity @a[distance=..1] positioned ~ ~-1 ~ unless entity @a[distance=..1] positioned ~ ~1 ~ run function wasd.bosses:check_los
execute positioned ^ ^ ^0.2 positioned ~ ~1 ~ if entity @a[distance=..1] run tag @e[tag=wasd.boss,tag=wasd.checking_los,sort=nearest,limit=1] add wasd.has_los
execute positioned ^ ^ ^0.2 positioned ~ ~0 ~ if entity @a[distance=..1] run tag @e[tag=wasd.boss,tag=wasd.checking_los,sort=nearest,limit=1] add wasd.has_los
execute positioned ^ ^ ^0.2 positioned ~ ~-1 ~ if entity @a[distance=..1] run tag @e[tag=wasd.boss,tag=wasd.checking_los,sort=nearest,limit=1] add wasd.has_los