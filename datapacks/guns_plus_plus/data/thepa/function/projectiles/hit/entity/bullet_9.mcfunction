
execute if entity @e[type=!#thepa:unaffected,sort=nearest,limit=1,distance=0] run summon small_fireball ~ ~4 ~ {Motion:[0.0,-5.0,0.0]}

execute if entity @e[type=end_crystal,sort=nearest,limit=1,distance=0] run damage @e[type=end_crystal,sort=nearest,limit=1,distance=0] 1 arrow

execute positioned ^ ^ ^-0.2 run particle block{block_state:"minecraft:light_gray_concrete"} ~ ~ ~ 0 0 0 0 5 normal
