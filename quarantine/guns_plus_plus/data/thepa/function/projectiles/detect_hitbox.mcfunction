

execute at @n[type=area_effect_cloud,tag=gz_projectile] if entity @s[dz=0,dx=0,dy=0,type=!player] run tag @n[type=area_effect_cloud,tag=gz_projectile] add gz_hit
execute at @n[type=area_effect_cloud,tag=gz_projectile] if entity @s[dz=0,dx=0,dy=0,type=player,gamemode=!spectator] run tag @n[type=area_effect_cloud,tag=gz_projectile] add gz_hit


execute at @s[type=#thepa:animal] positioned ^ ^0.5 ^0.5 if entity @n[type=area_effect_cloud,tag=gz_projectile,tag=gz_hit,distance=..0.65] run tag @s add gz_headshot

execute at @s[type=#thepa:humanoid,type=!player] positioned ~ ~1.8 ~ if entity @n[type=area_effect_cloud,tag=gz_projectile,tag=gz_hit,distance=..0.73] run tag @s add gz_headshot

execute at @s[type=player,gamemode=!spectator] positioned ~ ~1.8 ~ if entity @n[type=area_effect_cloud,tag=gz_projectile,tag=gz_hit,distance=..0.73] run tag @s add gz_headshot

execute as @s[type=#thepa:big] at @s positioned ~ ~2.8 ~ if entity @n[type=area_effect_cloud,tag=gz_projectile,tag=gz_hit,distance=..0.73] run tag @s add gz_headshot




#execute as @e[type=!area_effect_cloud,type=!armor_stand,type=!area_effect_cloud] at @s if entity @e[type=area_effect_cloud,distance=1.5..50.1,tag=gz_projectile,tag=gz_hit] run tag @s[type=!#thepa:animal,type=!#thepa:big,type=!#thepa:humanoid,type=!#thepa:small] add gz_headshot
