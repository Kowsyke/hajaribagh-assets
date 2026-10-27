
$execute as @s anchored eyes positioned ^ ^-.2 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:100,Tags:["gz_projectile","gz_bullet_14","gz_spawn"],CustomName:"a Dragon Breath Shotgun"}
execute as @s run data modify entity @e[type=area_effect_cloud, tag=gz_spawn, limit=1] Rotation set from entity @s Rotation
execute as @s anchored eyes positioned ^ ^-.2 ^ run summon fireball ~ ~ ~ {ExplosionPower:2,Tags:["gz_fireball"]}

execute as @e[type=area_effect_cloud, tag=gz_spawn, limit=1] run scoreboard players set @s gz_capacity 12
execute as @e[type=area_effect_cloud, tag=gz_spawn] run tag @s remove gz_spawn