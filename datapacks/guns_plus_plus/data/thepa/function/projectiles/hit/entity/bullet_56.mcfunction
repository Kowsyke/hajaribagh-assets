#Summons Little Sticky Creeper

summon creeper ~ ~0.9 ~ {HasVisualFire:1b,Invulnerable:1b,NoAI:1b,ExplosionRadius:1b,Fuse:20,ignited:1b,CustomName:"a Sticky Bomb",attributes:[{id:"minecraft:scale",base:0.2}],Tags:["stickyBomb"]}
#4
execute if entity @n[type=!#thepa:unaffected,tag=gz_headshot,distance=0] as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 10 2
execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run damage @n[type=!#thepa:unaffected,tag=gz_headshot,distance=0] 4 thepa:shot by @s

#2
execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run damage @n[type=!#thepa:unaffected,tag=!gz_headshot,distance=0] 2 thepa:shot by @s

execute as @e[type=!area_effect_cloud] if score @s killCredit = @n[type=area_effect_cloud,tag=gz_projectile,distance=..5] killCredit run tag @n[type=!#thepa:unaffected,distance=0] add stickyBombTarget

execute if entity @e[type=minecraft:ender_dragon,sort=nearest,limit=1,distance=0] run damage @e[type=minecraft:ender_dragon,sort=nearest,limit=1,distance=0] 0.6 minecraft:player_explosion by @s

tag @e remove gz_headshot

execute positioned ^ ^ ^-0.2 run particle block{block_state:"minecraft:light_gray_concrete"} ~ ~ ~ 0 0 0 0 5 normal




