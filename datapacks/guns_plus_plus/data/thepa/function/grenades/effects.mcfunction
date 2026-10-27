
#Grenade
execute as @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:weaving"}]}}] at @s run function thepa:grenades/smoke
execute as @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:infested"}]}}] at @s run function thepa:grenades/frag
execute as @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:oozing"}]}}] at @s run function thepa:grenades/inferno
execute as @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:luck"}]}}] at @s run function thepa:grenades/spawn_flash
 
kill @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:oozing"}]}}]
kill @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:infested"}]}}]
kill @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:weaving"}]}}]
kill @e[type=minecraft:area_effect_cloud,nbt={potion_contents:{custom_effects:[{id:"minecraft:luck"}]}}]

tag ThePatriotsFanXS remove flashed
tag Alex remove flashed


execute if entity @e[tag=flashbang] as @a[tag=!flashed] at @s positioned ^ ^ ^1 facing entity @e[tag=flashbang,distance=..50] eyes positioned ^ ^ ^-0.5 if entity @s[distance=..0.9] run function thepa:grenades/flashbang
execute if entity @e[tag=flashbang] as @a[tag=!flashed] at @s if entity @e[tag=flashbang,distance=..1.9] run function thepa:grenades/flashbang

execute if entity @e[tag=flashbang] as @a if entity @e[tag=flashbang,distance=..25] run playsound guns:flashbang_ring master @s ~ ~ ~ 10 1 1


execute if entity @e[tag=flashbang] as @e[type=!player] at @s positioned ^ ^ ^1 facing entity @e[tag=flashbang,distance=..20] eyes positioned ^ ^ ^-0.5 if entity @s[distance=..1] run effect give @s minecraft:slowness 10 3 true


tag @a[tag=flashed,scores={timeRemaining=..0}] remove flashed

execute as @e[tag=inferno,type=minecraft:marker] if score @s timeRemaining matches 1.. run scoreboard players remove @s timeRemaining 1

execute as @e[tag=flashbang,type=minecraft:marker] if score @s timeRemaining matches 1.. run scoreboard players remove @s timeRemaining 1


execute if entity @e[tag=smoke,type=minecraft:marker] as @e[tag=smoke,type=minecraft:marker] at @s run function thepa:grenades/smoke_persist

execute as @e[tag=inferno,type=minecraft:marker] at @s if score @s timeRemaining matches ..0 run fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air replace fire

execute as @e[tag=inferno,type=minecraft:marker] if score @s timeRemaining matches ..0 run kill @s
execute as @e[tag=flashbang,type=minecraft:marker] if score @s timeRemaining matches ..0 run kill @s