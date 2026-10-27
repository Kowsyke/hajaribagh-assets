
execute as @e[tag=gz_bullet_5] at @s run particle minecraft:electric_spark ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_9] at @s run particle minecraft:flame ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_27] at @s run particle minecraft:flame ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_12] at @s run particle minecraft:soul_fire_flame ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_13] at @s run particle minecraft:squid_ink ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_14] at @s run particle minecraft:smoke ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_19] at @s run playsound guns:rocket_trail master @a[distance=10..30] ~ ~ ~ 1 1
execute as @e[tag=gz_bullet_19] at @s run particle minecraft:squid_ink ~ ~1 ~ 0 0 0 0 1 force @a
execute as @e[tag=gz_bullet_48] at @s run particle minecraft:flame ~ ~ ~ 0 0 0 0 1 normal @a
execute as @e[tag=!gz_bullet_5,tag=!gz_bullet_9,tag=!gz_bullet_27,tag=!gz_bullet_12,tag=!gz_bullet_13,tag=!gz_bullet_14,tag=!gz_bullet_19,tag=!gz_bullet_54,tag=!gz_bullet_48,tag=gz_projectile] at @s run particle minecraft:smoke ~ ~ ~ 0 0 0 0 1 normal @a