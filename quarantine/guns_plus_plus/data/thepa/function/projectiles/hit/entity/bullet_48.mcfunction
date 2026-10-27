

#0.5
execute if entity @n[type=!#thepa:unaffected,tag=gz_headshot,distance=0] as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 10 2
execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run damage @n[type=!#thepa:unaffected,tag=gz_headshot,distance=0] .5 thepa:shot by @s

#0.125
execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run damage @n[type=!#thepa:unaffected,tag=!gz_headshot,distance=0] .1 thepa:shot by @s

execute if entity @e[type=minecraft:ender_dragon,sort=nearest,limit=1,distance=0] run damage @e[type=minecraft:ender_dragon,sort=nearest,limit=1,distance=0] 0.5 minecraft:player_explosion by @s

tag @e remove gz_headshot


data merge entity @e[type=!#thepa:unaffected,sort=nearest,limit=1,distance=0] {Fire:100s}
execute if entity @e[type=player,sort=nearest,limit=1,distance=0] as @s at @s run summon small_fireball ~ ~2.1 ~ {Motion:[0.0,-1.0,0.0]}
