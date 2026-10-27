
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet1"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet2"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet3"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet4"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet5"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet6"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet7"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet8"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet9"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet10"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet11"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet12"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet13"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet14"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet15"],CustomName:"a Ranger Shotgun"}
$execute as @s anchored eyes positioned ^ ^-0.1 ^-0.2 run summon area_effect_cloud ~ ~ ~ {Radius:0f,Particle:{type:"dust",color:[0.000,0.000,0.000],scale:0.01},WaitTime:-1,Age:0,Owner:$(UUID),Duration:40,Tags:["gz_projectile","gz_bullet_55","gz_spawn","bullet16"],CustomName:"a Ranger Shotgun"}
execute as @s run data modify entity @e[type=area_effect_cloud, tag=gz_spawn,tag=gz_bullet_55, limit=1] Rotation set from entity @s Rotation

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet8, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~0.5 ~-0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet8, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~1.5 ~-1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet15, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~ ~-0.25
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet15, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~ ~-0.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet1, limit=1] ^ ^-0.1 ^-0.2 ~0.5 ~
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet1, limit=1] ^ ^-0.1 ^-0.2 ~1.5 ~

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet10, limit=1] ^ ^-0.1 ^-0.2 ~0.25 ~
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet10, limit=1] ^ ^-0.1 ^-0.2 ~0.5 ~

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet9, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.5 ~0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet9, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-1.5 ~1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet13, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.25 ~
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet13, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.5 ~

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet5, limit=1] ^ ^-0.1 ^-0.2 ~-0.25 ~0.25
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet5, limit=1] ^ ^-0.1 ^-0.2 ~-0.5 ~0.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet14, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.25 ~-0.25
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet14, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.5 ~-0.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet12, limit=1] ^ ^-0.1 ^-0.2 ~ ~0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet12, limit=1] ^ ^-0.1 ^-0.2 ~ ~0.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet11, limit=1] ^ ^-0.1 ^-0.2 ~0.25 ~0.25
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet11, limit=1] ^ ^-0.1 ^-0.2 ~0.5 ~0.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet7, limit=1] ^ ^-0.1 ^-0.2 ~ ~-0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet7, limit=1] ^ ^-0.1 ^-0.2 ~ ~-1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet6, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.5 ~-0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet6, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-1.5 ~-1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet7, limit=1] ^ ^-0.1 ^-0.2 ~ ~-0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet7, limit=1] ^ ^-0.1 ^-0.2 ~ ~-1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet4, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-0.5 ~
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=bullet4, tag=gz_spawn, limit=1] ^ ^-0.1 ^-0.2 ~-1.5 ~

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet3, limit=1] ^ ^-0.1 ^-0.2 ~ ~0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet3, limit=1] ^ ^-0.1 ^-0.2 ~ ~1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet2, limit=1] ^ ^-0.1 ^-0.2 ~0.5 ~0.5
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet2, limit=1] ^ ^-0.1 ^-0.2 ~1.5 ~1.5

execute as @s[tag=gz_offhand] at @s[tag=gz_offhand  ] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet16, limit=1] ^ ^-0.1 ^-0.2 ~0.25 ~-0.25
execute as @s[tag=!gz_offhand] at @s[tag=!gz_offhand] anchored eyes run tp @e[type=area_effect_cloud, tag=gz_spawn, tag=bullet16, limit=1] ^ ^-0.1 ^-0.2 ~0.5 ~-0.5

execute as @e[type=area_effect_cloud, tag=gz_spawn] run scoreboard players set @s gz_capacity 9
execute as @e[type=area_effect_cloud, tag=gz_spawn] run tag @s remove gz_spawn