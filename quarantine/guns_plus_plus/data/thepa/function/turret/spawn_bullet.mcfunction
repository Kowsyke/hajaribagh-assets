
$execute as @s anchored feet positioned ^ ^1 ^1 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.1},Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_99","gz_spawn"],CustomName:"an M2 Browning",WaitTime:-1}

execute as @s run data modify entity @e[type=area_effect_cloud, tag=gz_spawn, limit=1] Rotation set from entity @s Rotation

execute as @e[type=area_effect_cloud, tag=gz_spawn, limit=1] run scoreboard players set @s gz_capacity 12
execute as @e[type=area_effect_cloud, tag=gz_spawn] run tag @s remove gz_spawn

playsound guns:lmg_shoot master @a[distance=..5] ~ ~ ~ 2 1