
scoreboard players add @s gz_bullets 1

tp @s ^ ^ ^0.4


execute if entity @s[tag=gz_bullet_14] as @s at @s run tp @e[tag=gz_fireball,limit=1,sort=nearest] @s
execute if entity @s[tag=gz_fireball] as @s at @s unless entity @e[tag=gz_bullet_14,limit=1,sort=nearest,distance=..5] run kill @s

execute if entity @s[tag=gz_bullet_9] as @s at @s run fill ~ ~ ~ ~ ~ ~ fire replace air
execute if entity @s[tag=gz_bullet_27] as @s at @s run fill ~-0.5 ~-0.5 ~-0.5 ~0.5 ~ ~0.5 fire replace air

execute if entity @s[tag=gz_bullet_54] as @s at @s run tp @n[tag=energy_ball,type=item_display] ~ ~ ~
execute if entity @s[tag=gz_bullet_54] run kill @e[tag=gz_bullet_54,nbt={Age:50}]


execute if block ~ ~ ~ target run summon arrow ^ ^ ^-0.5 {Motion:[5.0,-5.0,5.0],Tags:["targetScore"]}
execute if entity @e[tag=targetScore,type=marker] if block ~ ~ ~ target positioned 0 0 0 run summon minecraft:marker ^ ^ ^5 {Tags:["arrowRot"]}
execute if entity @e[tag=targetScore,type=marker] run data modify entity @n[type=minecraft:arrow,tag=targetScore] Motion set from entity @n[type=minecraft:marker,limit=1,tag=arrowRot] Pos


execute if entity @e[type=!#thepa:unaffected,distance=..3] unless score @s killCredit = @n[type=!#thepa:unaffected,dx=0,dy=0,dz=0] killCredit as @e[type=player,dx=0,dy=0,dz=0,tag=!gz_shoot,gamemode=!spectator] at @s run function thepa:projectiles/detect_hitbox
execute if entity @e[type=!#thepa:unaffected,distance=..3] unless score @s killCredit = @n[type=!#thepa:unaffected,dx=0,dy=0,dz=0,type=!player] killCredit as @e[type=!#thepa:unaffected,dx=0,dy=0,dz=0,tag=!gz_shoot] at @s run function thepa:projectiles/detect_hitbox

execute unless block ~ ~ ~ #thepa:non_solid run function thepa:projectiles/hit/block/select
execute if entity @s[tag=gz_hit] at @s run function thepa:projectiles/hit/entity/select

execute unless entity @s[tag=gz_hit] if score @s gz_bullets < @s gz_capacity at @s as @s run function thepa:projectiles/move
