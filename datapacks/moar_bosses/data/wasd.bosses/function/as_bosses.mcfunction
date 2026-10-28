#mc-build WASD content
execute as @s[tag=wasd.fire_boss] run function wasd.bosses:boss/fire
execute as @s[tag=wasd.water_boss] run function wasd.bosses:boss/water
execute as @s[tag=wasd.lightning_boss] run function wasd.bosses:boss/lightning
execute as @s[tag=wasd.earth_boss] run function wasd.bosses:boss/earth
execute as @s[tag=wasd.metal_boss] run function wasd.bosses:boss/metal
execute as @s[tag=wasd.wind_boss] run function wasd.bosses:boss/wind
execute as @s[tag=wasd.chicken_boss] run function wasd.bosses:boss/chicken
execute unless entity @a[distance=..32] run scoreboard players add @s wasd.variables 1
execute as @s[scores={wasd.variables=48000..}] run function wasd.bosses:zzz/2