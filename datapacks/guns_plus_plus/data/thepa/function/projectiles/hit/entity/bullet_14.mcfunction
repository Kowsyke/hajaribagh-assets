
execute if entity @e[tag=gz_bullet_14] run data merge entity @e[type=fireball,sort=nearest,limit=1,tag=gz_fireball] {Motion:[0.0,-6.0,0.0]}

execute positioned ^ ^ ^-0.2 run particle block{block_state:"minecraft:light_gray_concrete"} ~ ~ ~ 0 0 0 0 5 normal
