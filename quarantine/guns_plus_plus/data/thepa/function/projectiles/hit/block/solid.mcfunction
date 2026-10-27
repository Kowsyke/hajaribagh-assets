
execute positioned ^ ^ ^-0.2 run particle minecraft:crit ~ ~ ~ 0 0 0 10 1 force @a
playsound minecraft:entity.dolphin.death player @a ~ ~ ~ 0.2 2
execute if entity @e[tag=gz_bullet_14] run data merge entity @e[type=fireball,sort=nearest,limit=1,tag=gz_fireball] {Motion:[0.0,-6.0,0.0]}
execute if entity @e[tag=gz_bullet_19] run summon creeper ~ ~ ~ {Fuse:1b,ignited:1b,ExplosionRadius:3}
kill @s