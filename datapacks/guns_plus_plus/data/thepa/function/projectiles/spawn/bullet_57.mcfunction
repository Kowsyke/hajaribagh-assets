$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet1"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet2"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet3"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet4"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet5"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet6"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet7"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet8"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet9"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet10"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet11"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet12"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet13"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet14"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet15"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet16"],CustomName:"a Sawed-Off Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^ run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:10,Tags:["gz_projectile","gz_bullet_57","gz_spawn","bullet17"],CustomName:"a Sawed-Off Shotgun"}

execute as @e[type=area_effect_cloud, tag=gz_spawn,tag=gz_bullet_57] run data modify entity @s Rotation set from entity @a[sort=nearest,limit=1] Rotation

execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet1, limit=1] ^ ^-0.1 ^ ~ ~
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet2, limit=1] ^ ^-0.1 ^ ~-31.0 ~-17.3
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet3, limit=1] ^ ^-0.1 ^ ~0.0 ~-17.3
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet4, limit=1] ^ ^-0.1 ^ ~31.0 ~-17.3
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet5, limit=1] ^ ^-0.1 ^ ~31.0 ~0.0
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet6, limit=1] ^ ^-0.1 ^ ~31.0 ~17.3
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet7, limit=1] ^ ^-0.1 ^ ~0.0 ~17.3
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet8, limit=1] ^ ^-0.1 ^ ~-31.0 ~17.3
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet9, limit=1] ^ ^-0.1 ^ ~-31.0 ~0.0
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet10, limit=1] ^ ^-0.1 ^ ~-19.9 ~-9.8
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet11, limit=1] ^ ^-0.1 ^ ~0.0 ~-9.8
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet12, limit=1] ^ ^-0.1 ^ ~19.9 ~-9.8
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet13, limit=1] ^ ^-0.1 ^ ~19.9 ~0.0
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet14, limit=1] ^ ^-0.1 ^ ~19.9 ~9.8
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet15, limit=1] ^ ^-0.1 ^ ~0.0 ~9.8
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet16, limit=1] ^ ^-0.1 ^ ~-19.9 ~9.8
execute as @s[tag=gz_mainhand] at @s[tag=gz_mainhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet17, limit=1] ^ ^-0.1 ^ ~-19.9 ~0.0


execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet1, limit=1] ^ ^-0.1 ^ ~ ~
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet2, limit=1] ^ ^-0.1 ^ ~-15.5 ~-8.6
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet3, limit=1] ^ ^-0.1 ^ ~0.0 ~-8.6
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet4, limit=1] ^ ^-0.1 ^ ~15.5 ~-8.6
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet5, limit=1] ^ ^-0.1 ^ ~15.5 ~0.0
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet6, limit=1] ^ ^-0.1 ^ ~15.5 ~8.6
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet7, limit=1] ^ ^-0.1 ^ ~0.0 ~8.6
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet8, limit=1] ^ ^-0.1 ^ ~-15.5 ~8.6
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet9, limit=1] ^ ^-0.1 ^ ~-15.5 ~0.0
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet10, limit=1] ^ ^-0.1 ^ ~-9.9 ~-4.9
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet11, limit=1] ^ ^-0.1 ^ ~0.0 ~-4.9
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet12, limit=1] ^ ^-0.1 ^ ~9.9 ~-4.9
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet13, limit=1] ^ ^-0.1 ^ ~9.9 ~0.0
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet14, limit=1] ^ ^-0.1 ^ ~9.9 ~4.9
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet15, limit=1] ^ ^-0.1 ^ ~0.0 ~4.9
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet16, limit=1] ^ ^-0.1 ^ ~-9.9 ~4.9
execute as @s[tag=gz_offhand] at @s[tag=gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet17, limit=1] ^ ^-0.1 ^ ~-9.9 ~0.0


execute as @e[type=area_effect_cloud, tag=gz_spawn] run scoreboard players set @s gz_capacity 5
execute as @e[type=area_effect_cloud, tag=gz_spawn] run tag @s remove gz_spawn