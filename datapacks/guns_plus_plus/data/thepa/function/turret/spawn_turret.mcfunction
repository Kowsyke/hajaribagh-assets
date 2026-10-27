summon minecraft:mule ~ ~ ~ {CustomName:'Turret',ChestedHorse:1b,active_effects:[{duration:-1,show_particles:0b,id:"minecraft:invisibility"}],NoAI:1b,attributes:[{id:"minecraft:max_health",base:100b},{id:"minecraft:movement_speed",base:0b}],Tame:1b,Tags:["turretH"]}


summon armor_stand ^ ^ ^-2 {Tags:["dummyRot"]}

tp @e[tag=turretH,distance=..3,limit=1,sort=nearest] ~ ~-1 ~ facing entity @e[tag=dummyRot,limit=1,sort=nearest]

summon minecraft:item_display ^ ^ ^ {item:{id:"minecraft:carrot_on_a_stick",count:1,components:{"minecraft:item_model":"minecraft:guns/turret/turret_base"}},item_display:head,Tags:["turretB"]}
summon minecraft:item_display ^ ^ ^ {item:{id:"minecraft:carrot_on_a_stick",count:1,components:{"minecraft:item_model":"minecraft:guns/turret/turret_base"}},item_display:head,Tags:["turretC"]}
summon minecraft:item_display ^ ^ ^ {item:{id:"minecraft:carrot_on_a_stick",count:1,components:{"minecraft:item_model":"minecraft:guns/turret/turret_top"}},item_display:head,Tags:["turretT"]}

execute as @e[tag=turretB,distance=..3,limit=1,sort=nearest] at @s run tp @s ~ ~ ~ facing entity @e[tag=dummyRot,limit=1,sort=nearest]
execute as @e[tag=turretC,distance=..3,limit=1,sort=nearest] at @s run tp @s ~ ~ ~ facing entity @e[tag=dummyRot,limit=1,sort=nearest]
execute as @e[tag=turretT,distance=..3,limit=1,sort=nearest] at @s run tp @s ~ ~ ~ facing entity @e[tag=dummyRot,limit=1,sort=nearest]

execute as @e[tag=turretB,distance=..3,limit=1,sort=nearest] at @s run tp @s ^ ^ ^1.4
execute as @e[tag=turretC,distance=..3,limit=1,sort=nearest] at @s run tp @s ^ ^-0.6 ^
execute as @e[tag=turretT,distance=..3,limit=1,sort=nearest] at @s run tp @s ^ ^ ^1.4
tp @e[tag=turretH,distance=..3,limit=1,sort=nearest] ~ ~-0.8 ~ facing entity @e[tag=dummyRot,limit=1,sort=nearest]

execute as @e[tag=turretT] at @s store result score @s turretRotsp run data get entity @s Rotation[0]

execute as @e[tag=turretT] at @s if score @s turretRotsp matches ..0 run scoreboard players add @s turretRotsp 360

execute as @e[tag=turretT] at @s store result score @s min_x run scoreboard players get @s turretRotsp
execute as @e[tag=turretT] at @s store result score @s max_x run scoreboard players get @s turretRotsp

execute as @e[tag=turretT] at @s run scoreboard players add @s max_x 65
execute as @e[tag=turretT] at @s run scoreboard players remove @s min_x 65

kill @e[tag=dummyRot,limit=1,sort=nearest]
kill @s