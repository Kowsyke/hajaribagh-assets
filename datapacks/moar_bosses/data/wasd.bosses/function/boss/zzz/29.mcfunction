#mc-build WASD content
summon area_effect_cloud ~ ~ ~ {custom_particle:{type:"block",block_state:"minecraft:air"},Duration:1,Tags:["wasd.earth_rotation"]}
tp @e[tag=wasd.earth_rotation,sort=nearest,limit=1] ~ ~ ~ ~-5 ~10
execute as @s[scores={wasd.rng=1}] run function wasd.bosses:boss/zzz/30
execute as @s[scores={wasd.rng=2}] run function wasd.bosses:boss/zzz/32
execute as @s[scores={wasd.rng=3}] run function wasd.bosses:boss/zzz/34