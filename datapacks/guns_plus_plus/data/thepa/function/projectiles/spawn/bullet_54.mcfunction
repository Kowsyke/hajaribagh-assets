
$execute as @s anchored eyes positioned ^ ^-.2 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},Age:0,Owner:$(UUID),Duration:100,Tags:["gz_projectile","gz_bullet_54","gz_spawn"],CustomName:"a BFG 9000",WaitTime:-1}
execute as @s run data modify entity @e[type=area_effect_cloud, tag=gz_spawn, limit=1] Rotation set from entity @s Rotation


execute as @e[type=area_effect_cloud, tag=gz_spawn, limit=1] run scoreboard players set @s gz_capacity 1

execute as @s anchored eyes positioned ^ ^-.2 ^ run summon item_display ~ ~ ~ {Tags:[energy_ball],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[3f,3f,3f]},item:{id:"minecraft:clock",count:1,components:{"minecraft:item_model":"minecraft:misc/energy_projectile"}}}

execute as @e[type=area_effect_cloud, tag=gz_spawn] run tag @s remove gz_spawn