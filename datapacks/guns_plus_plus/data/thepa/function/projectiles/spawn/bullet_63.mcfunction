
$execute as @s anchored eyes positioned ^ ^-.2 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_63","gz_spawn"],CustomName:"a Blaster Pistol",WaitTime:-1}
execute as @s run data modify entity @e[type=area_effect_cloud, tag=gz_spawn, limit=1] Rotation set from entity @s Rotation

execute if score GLOBAL bloom matches 1 run function thepa:recoil_types/bloom/bullet_53
execute if score GLOBAL spray matches 1 run function thepa:recoil_types/sprays/bullet_53
execute if score GLOBAL spray matches 1 if entity @s[tag=gz_mainhand] run function thepa:recoil_types/bloom/bullet_53

execute as @e[type=area_effect_cloud, tag=gz_spawn, limit=1] run scoreboard players set @s gz_capacity 12
execute as @e[type=area_effect_cloud, tag=gz_spawn] run tag @s remove gz_spawn