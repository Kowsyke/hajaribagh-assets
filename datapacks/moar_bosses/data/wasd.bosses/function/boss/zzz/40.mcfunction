#mc-build WASD content
playsound block.tuff.break player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
execute anchored eyes positioned ^ ^ ^0.01 run summon marker ^-0.35 ^0.4 ^0.4 {Tags:["wasd.lib_entity_tick","wasd.ability","wasd.steel_target"]}
execute anchored eyes positioned ^ ^ ^0.01 run execute positioned ^-0.35 ^0.4 ^0.4 as @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.steel_target,sort=nearest,limit=1] run function wasd.bosses:boss/zzz/41
execute positioned ~ ~-1 ~ rotated 0 0 run function wasd.lib:detection/horizontal/rotated/9x9
execute as @e[type=marker,tag=wasd.location] at @s run function wasd.bosses:boss/zzz/42
execute store result score @s wasd.rng run random value 1..3
execute as @s[scores={wasd.rng=1}] as @e[tag=wasd.location,tag=!wasd.invalid_location,sort=random,limit=5,distance=2..] run tag @s add wasd.selected_location
execute as @s[scores={wasd.rng=2}] as @e[tag=wasd.location,tag=!wasd.invalid_location,sort=random,limit=6,distance=2..] run tag @s add wasd.selected_location
execute as @s[scores={wasd.rng=3}] as @e[tag=wasd.location,tag=!wasd.invalid_location,sort=random,limit=7,distance=2..] run tag @s add wasd.selected_location
execute as @e[tag=wasd.location,tag=wasd.selected_location] at @s run summon item_display ~ ~-2 ~ {CustomName:"a spike",Passengers:[{id:"minecraft:marker",Rotation:[0.1F,0.1F],Tags:["wasd.spike_rotation_storage"]}],item_display:"head",brightness:{sky:10,block:15},Tags:["wasd.lib_entity_tick","wasd.ability","wasd.iron_spike"],teleport_duration:50,interpolation_duration:10,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]},item:{id:"minecraft:armor_stand",count:1,components:{"minecraft:item_model":"wasd:abilities/iron_spike"}}}
kill @e[tag=wasd.location]