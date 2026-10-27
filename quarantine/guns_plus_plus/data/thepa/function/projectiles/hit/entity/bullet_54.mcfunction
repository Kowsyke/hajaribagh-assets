
execute if entity @n[type=!#thepa:unaffected,tag=gz_headshot,distance=0] as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 10 2

summon firework_rocket ~ ~1 ~ {FireworksItem:{id:"minecraft:firework_rocket",components:{"minecraft:fireworks":{explosions:[{shape:large_ball,colors:[I;65280]},{shape:large_ball,colors:[I;65280]},{shape:large_ball,colors:[I;65280]},{shape:large_ball,colors:[I;65280]},{shape:large_ball,colors:[I;65280]}]}}}}
#40
execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run damage @n[type=!#thepa:unaffected,tag=gz_headshot,distance=0] 30 thepa:shot by @s

#22
execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run damage @n[type=!#thepa:unaffected,tag=!gz_headshot,distance=0] 19 thepa:shot by @s

execute if entity @e[type=minecraft:ender_dragon,sort=nearest,limit=1,distance=0] run damage @e[type=minecraft:ender_dragon,sort=nearest,limit=1,distance=0] 20 minecraft:player_explosion by @s
kill @n[tag=energy_ball]
tag @e remove gz_headshot

execute positioned ^ ^ ^-0.2 run particle block{block_state:"minecraft:light_gray_concrete"} ~ ~ ~ 0 0 0 0 5 normal
